"""Migração única (titular, 17/10/2026): RESTAURA as certidões do Cartório descartadas sem rastro na absorção de 16/10.
A versão boa (16/10 19:20, 2.423 certidões) está em certidoes_2026_10_16_1920.json.gz. Para cada certidão que falta:
ligada a um livro (identificador ou índice) → volta, somada às atuais; sem livro → o título passa pelo caminho normal
(portão, triagem, índice): liga ou cria o livro, e a certidão entra nele; barrada → registrada como descarte.
Idempotente: só acrescenta o que falta."""
import gzip, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from src import livro_arquivo as LA, pesquisa_externa as P
from src.indice_livros import Indice, entrada
from src.banco_livros import registrar_achados, _triagem

A = json.load(gzip.open(Path(__file__).with_name("certidoes_2026_10_16_1920.json.gz"), "rt", encoding="utf-8"))["certidoes"]
p = LA.ROOT / "estado/cartorio/certidoes.json"
doc = LA.ler_arquivo(p, {}) or {}; H = doc.setdefault("certidoes", {})
falt = {k: v for k, v in A.items() if k not in H}
if not falt or any((v or {}).get("restaurada_de") == "2164a0a37^ (16/10 19:20)" for v in H.values()):   # aplicada uma vez
    print(json.dumps({"migracao": "já aplicada"})); sys.exit(0)
L = json.load(open(ROOT / "biblioteca_alexandria/fontes/motores.json"))["motores"]; mapa = P._mapa_livros(L)
ind = Indice([entrada(x) for x in L if x.get("id")]); sem = {}
marca = {"restaurada_em": "2026-10-17", "restaurada_de": "2164a0a37^ (16/10 19:20)"}
for k, c in falt.items():
    oid = k.split(":", 1)[-1]
    lid = mapa.get(oid) or ind.encontrar({"titulo": c.get("titulo") or "", "url": c.get("link_oficial"), "link_oficial": c.get("link_oficial")})[0]
    if lid:
        H[k] = {**c, "livro": lid, **marca}
    else:
        sem[k] = c
ops = [{"id": k.split(":", 1)[-1], "titulo": c.get("titulo") or "", "url": c.get("link_oficial"), "link_oficial": c.get("link_oficial"),
        "fim": c.get("fim"), "sensor": "cartorio-restauracao"} for k, c in sem.items()]
reg = registrar_achados(ops, motor="cartorio-restauracao") if ops else {}
mapa = P._mapa_livros(json.load(open(ROOT / "biblioteca_alexandria/fontes/motores.json"))["motores"]); desc = []
for k, c in sem.items():
    lid = mapa.get(k.split(":", 1)[-1])
    if lid:
        H[k] = {**c, "livro": lid, **marca}
    else:
        desc.append({"arquivo": "estado/cartorio/certidoes.json", "chave": k, "registro": c,
                     "motivo": _triagem({"titulo": c.get("titulo") or "", "url": c.get("link_oficial"), "fim": c.get("fim")}) or "sem livro"})
LA.guardar_lote([(p, doc)])
if desc:
    LA.registrar_descartes(desc, "restauração das certidões (barradas pelo portão)")
print(json.dumps({"faltavam": len(falt), "registro": reg, "descartes": len(desc),
                  "certidoes_agora": len((LA.ler_arquivo(p, {}) or {}).get("certidoes") or {})}, ensure_ascii=False))
