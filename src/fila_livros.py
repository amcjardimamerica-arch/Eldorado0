"""FILA DE LIVROS (titular, 18/10/2026).

Depois que os motores encontram as oportunidades e a regra dos livros é aplicada (um banco só), cada livro entra numa
fila e é verificado UM A UM, com todas as ferramentas à disposição dele — inclusive o Interceptador.
REGRA: no máximo 3 TENTATIVAS de cada ferramenta para cada livro, com INTERVALO ESTUDADO entre elas:
  1ª imediata · 2ª depois de 6 h (bloqueio temporário, site fora do ar) · 3ª depois de 24 h (ciclo diário de publicação)
Depois da 3ª sem resolver, o livro está ESGOTADO para aquela ferramenta e segue para a verificação externa.
Estado (controle, sem dado de oportunidade): estado/fila_livros.json.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARQ = ROOT / "estado/fila_livros.json"
MAX_TENTATIVAS = 3
INTERVALO_H = (0, 6, 24)              # antes da 1ª, 2ª e 3ª tentativa


def _agora() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def _ler() -> dict:
    try:
        return json.loads(ARQ.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {"livros": {}}


def _gravar(d: dict) -> None:
    d["em"] = _agora().isoformat(); ARQ.parent.mkdir(parents=True, exist_ok=True)
    ARQ.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def montar(necessidades: dict[str, set]) -> dict:
    """Atualiza a fila com as necessidades de cada oportunidade aberta ({id: {ferramentas}}); a que saiu das abertas sai."""
    d = _ler(); L = d.setdefault("livros", {})
    for oid in [k for k in L if k not in necessidades]:
        L.pop(oid)
    for oid, nec in necessidades.items():
        e = L.setdefault(oid, {"entrou_em": _agora().isoformat(), "tentativas": {}})
        e["precisa"] = sorted(nec)
    _gravar(d)
    return resumo(d)


def pode(oid: str, ferramenta: str, d: dict | None = None) -> bool:
    t = ((((d or _ler()).get("livros") or {}).get(str(oid)) or {}).get("tentativas") or {}).get(ferramenta) or {}
    n = int(t.get("n") or 0)
    if t.get("resolvido") or n >= MAX_TENTATIVAS:
        return False
    if n == 0 or not t.get("ultima"):
        return True
    return _agora() >= datetime.fromisoformat(t["ultima"]) + timedelta(hours=INTERVALO_H[n])


def tentativa(oid: str, ferramenta: str, resolvido: bool = False, d: dict | None = None, gravar: bool = True) -> dict:
    d = d or _ler()
    e = d.setdefault("livros", {}).setdefault(str(oid), {"entrou_em": _agora().isoformat(), "tentativas": {}})
    t = e.setdefault("tentativas", {}).setdefault(ferramenta, {"n": 0})
    t["n"] = int(t.get("n") or 0) + 1; t["ultima"] = _agora().isoformat()
    if resolvido:
        t["resolvido"] = True
    if gravar:
        _gravar(d)
    return t


def resumo(d: dict | None = None) -> dict:
    d = d or _ler(); L = d.get("livros") or {}
    esg = {oid for oid, e in L.items() for f, t in (e.get("tentativas") or {}).items()
           if not t.get("resolvido") and int(t.get("n") or 0) >= MAX_TENTATIVAS}
    agora = {oid for oid, e in L.items() if any(pode(oid, f, d) for f in e.get("precisa") or [])}
    return {"na_fila": len(L), "prontos_agora": len(agora), "aguardando_intervalo": len(L) - len(agora) - len(esg - agora),
            "esgotados_em_alguma_ferramenta": len(esg), "max_tentativas": MAX_TENTATIVAS, "intervalos_h": list(INTERVALO_H)}
