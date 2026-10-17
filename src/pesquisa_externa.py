"""PESQUISA EXTERNA NOS LIVROS (titular, 17/10/2026).

Toda consulta externa (Claude no Chrome) é gravada DIRETAMENTE no livro da oportunidade, somando ao que o livro já tem:
  livro["pesquisa_externa"]  veredito, parecer, site oficial, documento, prazo, itens (com "como_encontrou"), dispensas
  livro["aprendizados"]      o aprendizado da busca, INDIVIDUAL por livro (onde estava, tipo de documento, busca que
                             funcionou, bloqueio, sugestão para o motor, skill necessária) — é com ele que os motores melhoram
A oportunidade que nunca teve livro (ruído descartado) fica no LIVRO ESPECIAL "Pesquisa externa". O arquivo coletivo de
vereditos e o relatório de aprendizado passam a ser VISTAS regeradas a partir dos livros. A trava dos livros protege tudo
(nada apagado nem sobrescrito).
"""
from __future__ import annotations

import collections
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "biblioteca_alexandria/fontes/motores.json"
REP = ROOT / "biblioteca_alexandria/livros/_vistas/repositorio_unico.json"
ESPECIAL = ROOT / "biblioteca_alexandria/livros/especiais/pesquisa_externa"
SEM_LIVRO = ESPECIAL / "livro.json"
VEREDITOS = ROOT / "biblioteca_alexandria/livros/_acervo/editais/vereditos_revisao.json"
APRENDIZADO = ROOT / "docs/dados/aprendizado_chrome.json"
CAMPOS = ("veredito", "parecer", "site_oficial", "link_documento", "prazo", "itens", "dispensas")


def _agora() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _j(p: Path, padrao):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return padrao


def _mapa_livros(L: list[dict]) -> dict:
    """id de oportunidade → id do livro (repositório; coleta, histórico e id do próprio livro)."""
    m: dict = {}
    for lv in L:
        lid = lv.get("id")
        m.setdefault(str(lid), lid)
        for k, a in (lv.get("coleta") or {}).items():
            m.setdefault(str(k), lid)
            if isinstance(a, dict) and a.get("id"):
                m.setdefault(str(a["id"]), lid)
        for h in lv.get("historico") or []:
            if isinstance(h, dict) and h.get("id"):
                m.setdefault(str(h["id"]), lid)
    for r in (_j(REP, {}) or {}).get("registros") or []:
        if r.get("livro"):
            for i in [r.get("id"), *(r.get("ids_origem") or [])]:
                if i:
                    m[str(i)] = r["livro"]
    return m


def gravar(registros: list[dict], origem: str, gravar_: bool = True) -> dict:
    """Grava cada resultado no LIVRO da oportunidade (ou no livro especial, se ela nunca teve livro)."""
    cat = _j(CAT, {"motores": []}); L = cat.setdefault("motores", [])
    por_id = {x.get("id"): x for x in L}
    mapa = _mapa_livros(L)
    esp = _j(SEM_LIVRO, {}) or {"id": "pesquisa-externa", "tipo": "livro_especial",
                                 "regra": "resultados da pesquisa externa de oportunidades que nunca tiveram livro",
                                 "resultados": {}}
    st = collections.Counter()
    for x in registros:
        oid = str(x.get("id") or "")
        if not oid:
            continue
        ent = {"id": oid, "origem": origem, "em": x.get("em") or _agora(),
               **{k: x.get(k) for k in CAMPOS if x.get(k) not in (None, "", [], {})},
               "definitivo": x.get("veredito") not in (None, "pendente")}
        ap = x.get("aprendizado") if isinstance(x.get("aprendizado"), dict) else None
        lv = por_id.get(mapa.get(oid))
        if lv is None:
            chave = f"{oid}|{origem}"
            if chave not in esp["resultados"]:
                esp["resultados"][chave] = {**ent, **({"aprendizado": ap} if ap else {})}
                st["no_livro_especial"] += 1
            continue
        pe = lv.setdefault("pesquisa_externa", [])
        if not any(p.get("id") == oid and p.get("origem") == origem for p in pe):
            pe.append(ent); st["gravados_no_livro"] += 1
        if ap:
            aps = lv.setdefault("aprendizados", [])
            if not any(a.get("id") == oid and a.get("origem") == origem for a in aps):
                aps.append({"id": oid, "origem": origem, "em": ent["em"], "veredito": x.get("veredito"), **ap})
                st["aprendizados_no_livro"] += 1
    if gravar_:
        CAT.write_text(json.dumps(cat, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        ESPECIAL.mkdir(parents=True, exist_ok=True)
        SEM_LIVRO.write_text(json.dumps(esp, ensure_ascii=False, indent=1), encoding="utf-8")
    return dict(st)


def migrar(gravar_: bool = True) -> dict:
    """Os vereditos e aprendizados que estavam FORA dos livros (arquivo coletivo, certidões) vão para os livros."""
    V = (_j(VEREDITOS, {}) or {}).get("vereditos") or {}
    regs = [{"id": i, "veredito": v.get("veredito"), "parecer": v.get("motivo"), "em": v.get("em"),
             **({"aprendizado": v["aprendizado"]} if isinstance(v.get("aprendizado"), dict) else {})}
            for i, v in V.items() if isinstance(v, dict)]
    por_origem = collections.defaultdict(list)
    for (i, v), r in zip(V.items(), regs):
        por_origem[str((v or {}).get("origem") or "revisao")].append(r)
    st = collections.Counter()
    for o, rr in por_origem.items():
        st.update(gravar(rr, o, gravar_))
    return {"vereditos": len(regs), **st}


def vista_vereditos(gravar_: bool = True) -> dict:
    """O arquivo coletivo de vereditos passa a ser VISTA: regerado a partir dos livros (o mais recente de cada oportunidade).
    Nada se perde: o que já estava no arquivo e ainda não está em livro continua (até migrar)."""
    atual = _j(VEREDITOS, {}) or {}
    V = dict(atual.get("vereditos") or {})
    fontes = [(p, lv.get("id")) for lv in (_j(CAT, {}) or {}).get("motores") or [] for p in lv.get("pesquisa_externa") or []]
    fontes += [(p, None) for p in ((_j(SEM_LIVRO, {}) or {}).get("resultados") or {}).values()]
    for p, lid in sorted(fontes, key=lambda t: str(t[0].get("em") or "")):
        if p.get("veredito"):
            V[p["id"]] = {**(V.get(p["id"]) or {}), "veredito": p["veredito"], "motivo": str(p.get("parecer") or "")[:300],
                          "origem": p.get("origem"), "em": p.get("em"), **({"livro": lid} if lid else {})}
    atual["vereditos"] = V
    atual["origem_dos_dados"] = "VISTA regerada a partir dos livros (src.pesquisa_externa) — o dado está no livro"
    if gravar_:
        VEREDITOS.write_text(json.dumps(atual, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"vereditos_na_vista": len(V)}


def vista_aprendizado(gravar_: bool = True) -> dict:
    """O relatório de aprendizado, regerado a partir dos aprendizados de CADA LIVRO (e do livro especial)."""
    itens = [(lv.get("id"), a) for lv in (_j(CAT, {}) or {}).get("motores") or [] for a in lv.get("aprendizados") or []]
    itens += [(None, {**(p.get("aprendizado") or {}), "veredito": p.get("veredito")})
              for p in ((_j(SEM_LIVRO, {}) or {}).get("resultados") or {}).values() if p.get("aprendizado")]
    def cont(c):
        return collections.Counter(str(a.get(c)).strip()[:120] for _l, a in itens if a.get(c)).most_common(25)
    out = {"em": _agora(), "livros_com_aprendizado": len({l for l, _a in itens if l}), "aprendizados": len(itens),
           "onde_estava": cont("onde_estava"), "tipo_de_documento": cont("tipo_de_documento"),
           "busca_que_funcionou": cont("busca_que_funcionou"), "bloqueios": cont("bloqueio"),
           "sugestao_para_o_motor": cont("sugestao_para_o_motor"), "skill_necessaria": cont("skill_necessaria"),
           "por_veredito": cont("veredito"),
           "regra": "VISTA: os aprendizados estão em cada livro (livro['aprendizados']); este é o resumo para os motores"}
    if gravar_:
        APRENDIZADO.parent.mkdir(parents=True, exist_ok=True)
        APRENDIZADO.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return {k: out[k] for k in ("livros_com_aprendizado", "aprendizados")}
