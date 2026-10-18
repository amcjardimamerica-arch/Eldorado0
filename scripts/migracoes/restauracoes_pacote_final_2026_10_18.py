"""Migração única (pacote final do chat de testes, 18/10/2026): restaura dados perdidos por defeitos já corrigidos.
1. Fontes 260: 'nivel' e 'nota' (a sincronização regravava o nivel com a esfera do livro e perdia a nota).
2. Revisão humana: os motivos apagados pela vista dos vereditos (só onde o motivo está vazio e o veredito é o mesmo); o
   motivo vai também para o livro (parecer da pesquisa externa, quando vazio).
3. Pilotos: radar e radar de captação no livro especial de Empresas — JUNÇÃO (só acrescenta o que falta).
Idempotente: só preenche o que falta."""
import gzip, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
D = Path(__file__).with_name("pacote_final_2026_10_18")
ld = lambda n: json.load(gzip.open(D / n, "rt", encoding="utf-8"))  # noqa: E731
st = {}
# 1. fontes 260
cfgp = ROOT / "config/fontes_captacao_260.json"; cfg = json.loads(cfgp.read_text(encoding="utf-8"))
boa = {f.get("id"): f for f in ld("fontes_captacao_260.json.gz").get("fontes") or []}
n = 0
for f in cfg.get("fontes") or []:
    b = boa.get(f.get("id")) or {}
    for k in ("nivel", "nota"):
        if b.get(k) not in (None, "") and f.get(k) != b[k]:
            f[k] = b[k]; n += 1
cfgp.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8"); st["fontes_campos_restaurados"] = n
# os livros das fontes guardam a nota (o livro é o dono)
catp = ROOT / "biblioteca_alexandria/fontes/motores.json"; cat = json.loads(catp.read_text(encoding="utf-8"))
for lv in cat.get("motores") or []:
    b = boa.get(lv.get("id"))
    if b and b.get("nota") and isinstance(lv.get("fonte_260"), dict) and not lv["fonte_260"].get("nota"):
        lv["fonte_260"]["nota"] = b["nota"]; lv["fonte_260"].setdefault("nivel", b.get("nivel"))
# 2. motivos da revisão humana
vp = ROOT / "biblioteca_alexandria/livros/_acervo/editais/vereditos_revisao.json"; V = json.loads(vp.read_text(encoding="utf-8"))
boaV = ld("vereditos_revisao.json.gz").get("vereditos") or {}
mot = {}
for i, v in (V.get("vereditos") or {}).items():
    b = boaV.get(i) or {}
    if not (v or {}).get("motivo") and b.get("motivo") and b.get("veredito") == (v or {}).get("veredito"):
        v["motivo"] = b["motivo"]; mot[i] = b["motivo"]
vp.write_text(json.dumps(V, ensure_ascii=False, indent=1), encoding="utf-8"); st["motivos_restaurados"] = len(mot)
nl = 0
for lv in cat.get("motores") or []:
    for p in lv.get("pesquisa_externa") or []:
        if p.get("id") in mot and not p.get("parecer"):
            p["parecer"] = mot[p["id"]]; nl += 1
catp.write_text(json.dumps(cat, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"); st["motivos_nos_livros"] = nl
# 3. radar dos pilotos (junção)
def juntar(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        for k, v in b.items():
            a[k] = juntar(a[k], v) if k in a else v
        return a
    if isinstance(a, list) and isinstance(b, list):
        ch = {json.dumps(x, sort_keys=True, ensure_ascii=False) for x in a}
        return a + [x for x in b if json.dumps(x, sort_keys=True, ensure_ascii=False) not in ch]
    return a if a not in (None, "", [], {}) else b
for nome, rel in (("radar_piloto.json.gz", "biblioteca_alexandria/livros/especiais/empresas/dados/radar_piloto.json"),
                  ("radar_captacao.json.gz", "biblioteca_alexandria/livros/especiais/empresas/radar_captacao.json")):
    p = ROOT / rel; atual = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    antes = len(json.dumps(atual)); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(juntar(atual, ld(nome)), ensure_ascii=False, indent=1), encoding="utf-8")
    st[nome.split(".")[0]] = f"{antes} → {p.stat().st_size} bytes"
print(json.dumps(st, ensure_ascii=False))
