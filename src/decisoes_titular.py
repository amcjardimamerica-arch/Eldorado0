"""DECISÕES DA TITULAR NO PAINEL → LIVRO (12/10/2026) — docs/prompts/PROMPT-FICHA-DA-OPORTUNIDADE-2026-10-12.md

Entrada: estado/decisoes_editais.json, exportado pelo painel (janela da oportunidade: «Inscrição realizada» e
«Descartar»). Nada é apagado:
  descartado → o livro da oportunidade recebe `revisao_exclusao` (pedido em, por, oportunidade, título, motivo,
               situação "aguardando análise do Claude") e entra na fila docs/dados/fila_revisao_exclusao.json; o
               Claude decide se exclui ou não
  inscrito   → o livro recebe `inscricao_realizada` (em, oportunidade)
Se a titular recuperar a oportunidade (a decisão sai do arquivo), a sinalização feita pelo painel é retirada.
O repositório único lê as mesmas decisões: a oportunidade decidida sai das abertas (marca "arquivada").
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISOES = ROOT / "estado/decisoes_editais.json"
REP = ROOT / "biblioteca_alexandria/livros/_vistas/repositorio_unico.json"
CATALOGO = ROOT / "biblioteca_alexandria/fontes/motores.json"
FILA = ROOT / "docs/dados/fila_revisao_exclusao.json"
POR = "titular (painel)"


def _j(p: Path, padrao=None):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return padrao if padrao is not None else {}


def decisoes() -> dict:
    d = _j(DECISOES, {}) or {}
    return d.get("decisoes") if isinstance(d.get("decisoes"), dict) else {k: v for k, v in d.items() if isinstance(v, dict) and v.get("estado")}


def marca_no_repositorio(ids: list[str], dec: dict | None = None) -> str | None:
    """Usado pelo repositório único: a oportunidade decidida no painel sai das abertas."""
    dec = decisoes() if dec is None else dec
    for i in ids:
        v = dec.get(i) or {}
        if v.get("estado") == "descartado":
            return f"descartada pela titular em {str(v.get('em') or '')[:10]} — aguardando análise do Claude (o livro fica)"
        if v.get("estado") == "inscrito":
            return f"inscrição realizada em {str(v.get('em') or '')[:10]}"
    return None


def run() -> dict:
    dec = decisoes()
    R = (_j(REP, {}).get("registros") or [])
    por_id = {}
    for r in R:
        for i in [r["id"], *(r.get("ids_origem") or [])]:
            por_id[i] = r
    C = _j(CATALOGO, {}) or {}
    livros = {m.get("id"): m for m in (C.get("motores") or [])}
    sinalizados, inscritos, retirados, mudou = [], 0, 0, False
    ativos = set()
    for oid, v in dec.items():
        r = por_id.get(oid); L = livros.get((r or {}).get("livro"))
        if not L:
            continue
        if v.get("estado") == "descartado":
            ativos.add(L["id"])
            if not L.get("revisao_exclusao") or (L["revisao_exclusao"].get("por") == POR and L["revisao_exclusao"].get("oportunidade") != oid):
                L["revisao_exclusao"] = {"pedido_em": v.get("em") or datetime.now(timezone.utc).isoformat(), "por": POR, "oportunidade": oid,
                                         "titulo": v.get("titulo") or (r or {}).get("titulo"), "motivo": v.get("motivo") or "descartada no painel",
                                         "situacao": "aguardando análise do Claude"}
                mudou = True
            sinalizados.append({"livro": L["id"], **L["revisao_exclusao"]})
        elif v.get("estado") == "inscrito" and not L.get("inscricao_realizada"):
            L["inscricao_realizada"] = {"em": v.get("em"), "oportunidade": oid}; inscritos += 1; mudou = True
    for L in livros.values():                      # recuperada no painel: retira a sinalização feita pelo painel
        rx = L.get("revisao_exclusao")
        if rx and rx.get("por") == POR and rx.get("situacao") == "aguardando análise do Claude" and L["id"] not in ativos:
            L.pop("revisao_exclusao"); retirados += 1; mudou = True
    if mudou:
        CATALOGO.write_text(json.dumps(C, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")   # formato único (compacto)
    FILA.write_text(json.dumps({"em": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                                "regra": "descartar no painel não apaga o livro: sinaliza para o Claude analisar a exclusão",
                                "pendentes": sinalizados}, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"decisoes": len(dec), "livros_sinalizados": len(sinalizados), "inscricoes_registradas": inscritos, "sinalizacoes_retiradas": retirados}


def definir(oid: str, estado: str, titulo: str = "") -> dict:
    """12/10: a decisão chega do painel pelo fluxo 33 (sem exportar arquivo). estado: inscrito · descartado · em_andamento
    (em_andamento = recuperar: a decisão sai do arquivo)."""
    d = _j(DECISOES, {}) or {}
    dec = decisoes()
    if estado == "em_andamento":
        dec.pop(oid, None)
    else:
        dec[oid] = {"estado": estado, "em": datetime.now(timezone.utc).replace(microsecond=0).isoformat(), "titulo": titulo[:200],
                    "acao": {"inscrito": "inscrição realizada", "descartado": "descartado"}.get(estado, estado), "por": POR}
    DECISOES.parent.mkdir(parents=True, exist_ok=True)
    DECISOES.write_text(json.dumps({**({k: v for k, v in d.items() if k != "decisoes"} if "decisoes" in d else {}),
                                    "atualizado_em": datetime.now(timezone.utc).replace(microsecond=0).isoformat(), "decisoes": dec},
                                   ensure_ascii=False, indent=1), encoding="utf-8")
    return {"oportunidade": oid, "estado": estado, "decisoes": len(dec)}


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4 and sys.argv[1] == "definir":
        print(json.dumps(definir(sys.argv[2], sys.argv[3], " ".join(sys.argv[4:])), ensure_ascii=False))
    print(json.dumps(run(), ensure_ascii=False))


# ── 18/10/2026: decisões do titular sobre vereditos da pesquisa externa ─────────────────────────────────────────────
_RESTRICAO_LOCAL = re.compile(r"(?i)resid|domic|com sede|sede (?:no|na|em)|sediad|restrit[oa]s? (?:a|ao|às|aos)|"
                              r"apenas (?:do|de|a) munic|local(?:is)? do munic")
_EMENDA = re.compile(r"(?i)\bemenda(?:s)? parlamentar|^emenda-")


def _de_goias(r: dict, motivo: str = "") -> bool:
    t = f"{r.get('titulo') or ''} {r.get('orgao') or ''} {motivo}"
    if str(r.get("uf") or "").upper() == "GO" or re.search(r"(?i)\bgoi[áa]s\b|/go\b|\(go\)|-go\b", t):
        return True
    try:
        from .repositorio_unico import _municipio_goiano
        if _municipio_goiano(t):
            return True
    except Exception:  # noqa: BLE001
        pass
    # o NOME de um município que só existe em Goiás (lista do IBGE) — homônimos de outros estados não decidem
    import unicodedata as _ud
    sem = lambda x: _ud.normalize("NFKD", str(x).lower()).encode("ascii", "ignore").decode()  # noqa: E731
    if not _SO_GOIAS:
        try:
            m = json.loads((Path(__file__).resolve().parents[1] / "config/municipios_brasil.json").read_text(encoding="utf-8")).get("municipios") or {}
            _SO_GOIAS.extend(sorted({sem(n) for n, ufs in m.items() if list(ufs) == ["GO"] and len(n) >= 4}, key=len, reverse=True))
        except Exception:  # noqa: BLE001
            _SO_GOIAS.append("-")
    tt = sem(t)
    return any(re.search(rf"\b{re.escape(n)}\b", tt) for n in _SO_GOIAS)


_SO_GOIAS: list = []


def veredito_efetivo(ver: dict | None, r: dict) -> tuple[str | None, str | None]:
    """O veredito da pesquisa externa depois das DECISÕES DO TITULAR (o veredito original fica guardado no livro).
    1. (18/10) Edital de GOIÁS restrito a residentes ou a OSC com sede no município É DO PERFIL — o Eldorado é de Goiás e
       deve obtê-lo: 'fora_perfil' por essa restrição não elimina.
    2. (18/10) EMENDA PARLAMENTAR NÃO É RUÍDO — federal, estadual e municipal constam conforme programado."""
    v = (ver or {}).get("veredito")
    motivo = str((ver or {}).get("motivo") or "")
    if v == "fora_perfil" and _RESTRICAO_LOCAL.search(motivo) and _de_goias(r, motivo):
        return None, "decisão do titular (18/10): edital de Goiás restrito a residentes/sede no município é do perfil"
    if v in ("ruido", "fora_perfil", "encerrada", "duplicata") and \
            (_EMENDA.search(str(r.get("id") or "")) or _EMENDA.search(str(r.get("titulo") or ""))) and v != "duplicata":
        return None, "decisão do titular (18/10): emenda parlamentar não é ruído — consta conforme programado"
    return v, None
