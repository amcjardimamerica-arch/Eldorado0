#!/usr/bin/env python3
"""GRAVAR SOMENTE O QUE ESTE FLUXO ALTEROU (titular, 15/10/2026 — análise do sistema, ciclo 5).

Defeito medido: a análise das 14:43 reaplicou a ÁRVORE INTEIRA que tinha copiado às 14:03 e apagou a coleta que o
comando único gravou às 14:37 (docs/dados/maestro.json e comando.json voltaram às 12:46). O mesmo mecanismo existia no
fluxo 22. Regra nova: cada fluxo grava só os arquivos que ELE mudou, sempre por cima do main MAIS RECENTE.

    python scripts/gravar_somente_alterados.py salvar              # ao fim do trabalho: guarda os arquivos alterados
    python scripts/gravar_somente_alterados.py aplicar "mensagem"   # parte do main atual e grava só esses arquivos
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUARDA = Path("/tmp/alterados_pelo_fluxo")
AREAS = ["biblioteca_alexandria", "dados", "estado", "docs/dados", "docs/dashboard-dados.js", "docs/dashboard-dados.json", "docs/relatorios"]


# 17/10/2026: arquivos-ÍNDICE que vários fluxos gravam ao mesmo tempo. Copiar a versão do fluxo por cima do main apagava
# o que os outros fluxos tinham acrescentado enquanto este rodava (o índice dos livros caiu de 8.412 para 1 e depois
# ficou em 263 entradas). Para eles, a gravação JUNTA: tudo o que está no main fica; o que este fluxo gravou prevalece.
INDICES_JUNTADOS = {"biblioteca_alexandria/livros/_origens.json"}


# 17/10/2026 (chat de testes, item 6): ARQUIVOS DE CONTROLE COM VÁRIOS GRAVADORES. A cópia do fluxo por cima do main
# apagava o que outro fluxo tinha gravado durante a execução. Para estes, a gravação é uma JUNÇÃO EM 3 VIAS: a versão de
# onde o fluxo PARTIU (base, guardada no "salvar") diz o que ele mudou; só isso vai por cima do main — o resto do main
# fica. Registro .jsonl (só acréscimo): as linhas novas do fluxo entram no fim do main.
#   estado/livros_monitoramento.json (ex-estado/opressores.json, 10 gravadores) e o seu índice (3 gravadores);
#   estado/auditoria.jsonl (10 gravadores, registro só de acréscimo).
# biblioteca_alexandria/fontes/motores.json (30 gravadores) NÃO entra aqui: o aplicar roda a trava dos livros depois da
# cópia, contra o main atual (HEAD), e ela já junta — livro que sumiu volta, campo que sumiu volta, valor mudado guarda o
# anterior. estado/quarentena.jsonl (12) e estado/ia_uso.jsonl (5) não são versionados: cada execução grava o seu.
JUNTADOS_3_VIAS = {"estado/livros_monitoramento.json", "estado/livros_monitoramento_indice.json", "estado/auditoria.jsonl"}


def juntar_indice(no_main: dict, do_fluxo: dict) -> dict:
    """União sem perda: chaves só do main ficam; chaves do fluxo prevalecem."""
    return {**(no_main or {}), **(do_fluxo or {})}


def juntar_3_vias(base, main, fluxo, nivel: int = 0):
    """O que o fluxo mudou em relação à base vai por cima do main; o que ele não tocou fica como está no main."""
    if fluxo == base:
        return main
    if main == base:
        return fluxo
    if isinstance(fluxo, dict) and isinstance(main, dict) and isinstance(base, dict) and nivel < 2:
        out = dict(main)
        for k, v in fluxo.items():
            if k not in base or v != base[k]:
                out[k] = juntar_3_vias(base.get(k), main.get(k), v, nivel + 1) if k in main else v
        for k in base:
            if k not in fluxo and k in out and out[k] == base[k]:
                out.pop(k)                                    # o fluxo retirou e ninguém mexeu depois
        return out
    if isinstance(fluxo, list) and isinstance(main, list) and isinstance(base, list):
        return main + [x for x in fluxo if x not in base and x not in main]   # histórico: acréscimos dos dois
    return fluxo


def juntar_linhas(base: str, main: str, fluxo: str) -> str:
    vistas = set(base.splitlines()) | set(main.splitlines())
    novas = [l for l in fluxo.splitlines() if l.strip() and l not in vistas]
    corpo = main if main.endswith("\n") or not main else main + "\n"
    return corpo + "".join(l + "\n" for l in novas)


def _copiar(origem: Path, c: str) -> None:
    destino = ROOT / c
    destino.parent.mkdir(parents=True, exist_ok=True)
    if c in JUNTADOS_3_VIAS and destino.is_file():
        b = GUARDA / "base" / c
        base_txt = b.read_text(encoding="utf-8") if b.is_file() else ""
        main_txt, fluxo_txt = destino.read_text(encoding="utf-8"), origem.read_text(encoding="utf-8")
        if c.endswith(".jsonl"):
            destino.write_text(juntar_linhas(base_txt, main_txt, fluxo_txt), encoding="utf-8")
            print(f"{c}: linhas novas do fluxo acrescentadas ao main")
            return
        try:
            base, main, fluxo = (json.loads(base_txt) if base_txt else {}), json.loads(main_txt), json.loads(fluxo_txt)
        except ValueError:
            raise RuntimeError(f"{c}: arquivo de controle ilegível — nada gravado para não apagar o que outro fluxo gravou")
        destino.write_text(json.dumps(juntar_3_vias(base, main, fluxo), ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{c}: juntado em 3 vias (só o que este fluxo mudou foi por cima do main)")
        return
    if c in INDICES_JUNTADOS and destino.is_file():
        try:
            no_main = json.loads(destino.read_text(encoding="utf-8"))
            do_fluxo = json.loads(origem.read_text(encoding="utf-8"))
        except ValueError:
            raise RuntimeError(f"{c}: índice ilegível no main ou no fluxo — nada gravado para não apagar entradas")
        if isinstance(no_main, dict) and isinstance(do_fluxo, dict):
            junto = juntar_indice(no_main, do_fluxo)
            destino.write_text(json.dumps(junto, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
            print(f"{c}: juntado (main {len(no_main)} + fluxo {len(do_fluxo)} = {len(junto)} entradas)")
            return
    shutil.copy2(origem, destino)


def _git(*a, ok=False) -> str:
    r = subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
    if r.returncode and not ok:
        raise RuntimeError(f"git {' '.join(a)}: {r.stderr.strip()[:300]}")
    return r.stdout


def salvar() -> dict:
    mud = [l for l in _git("status", "--porcelain", "--untracked-files=all", "--", *AREAS).splitlines() if l.strip()]
    alterados, apagados = [], []
    for l in mud:
        caminho = l[3:].split(" -> ")[-1].strip().strip('"')
        (apagados if l[:2].strip() == "D" else alterados).append(caminho)
    try:                                              # 16/10/2026 (titular): TRAVA — dado de oportunidade só nos livros
        sys.path.insert(0, str(ROOT))
        from src.livro_arquivo import proibido
        recusados = [c for c in alterados if proibido(c)]
        if recusados:
            print(f"TRAVA: {len(recusados)} arquivo(s) em pasta proibida recusado(s) (o dado só existe nos livros): {recusados[:3]}")
            alterados = [c for c in alterados if not proibido(c)]
    except Exception:  # noqa: BLE001
        pass
    if GUARDA.exists():
        shutil.rmtree(GUARDA)
    for c in alterados:
        d = GUARDA / "arquivos" / c
        d.parent.mkdir(parents=True, exist_ok=True)
        if (ROOT / c).is_file():
            shutil.copy2(ROOT / c, d)
        if c in JUNTADOS_3_VIAS:                          # 17/10: a versão de onde o fluxo partiu (para a junção em 3 vias)
            r = subprocess.run(["git", "show", f"HEAD:{c}"], cwd=ROOT, capture_output=True)
            if r.returncode == 0:
                (GUARDA / "base" / c).parent.mkdir(parents=True, exist_ok=True)
                (GUARDA / "base" / c).write_bytes(r.stdout)
    m = {"alterados": alterados, "apagados": apagados}
    GUARDA.mkdir(parents=True, exist_ok=True)
    (GUARDA / "manifesto.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"guardados {len(alterados)} alterado(s) e {len(apagados)} apagado(s)")
    return m


def aplicar(msg: str, tentativas: int = 6) -> bool:
    m = json.loads((GUARDA / "manifesto.json").read_text(encoding="utf-8"))
    if not m["alterados"] and not m["apagados"]:
        print("nada a gravar"); return True
    for i in range(1, tentativas + 1):
        _git("fetch", "-q", "origin", "main")
        _git("reset", "-q", "--hard", "origin/main")                 # sempre o main MAIS RECENTE
        for c in m["alterados"]:
            o = GUARDA / "arquivos" / c
            if o.is_file():
                _copiar(o, c)                                 # 17/10: índices são JUNTADOS, não substituídos
        for c in m["apagados"]:
            if c in INDICES_JUNTADOS or c in JUNTADOS_3_VIAS:
                continue                                       # 17/10: um fluxo nunca apaga o índice compartilhado
            if (ROOT / c).exists():
                _git("rm", "-q", "--", c, ok=True)
        # 17/10/2026 (titular): TRAVA DOS LIVROS — as mudanças desta passagem já estão sobre o main mais recente (HEAD):
        # nenhum livro apagado nem sobrescrito; só informação nova (o que outra gravação fez no main é preservado)
        subprocess.run([sys.executable, "-m", "src.trava_livros"], cwd=ROOT, capture_output=True)
        # 17/10 (titular): a Bússola recalculada pelo catálogo FINAL (o que vai ser gravado agora)
        subprocess.run([sys.executable, "-c", "from src import fluxo_oportunidades as F; F.sincronizar_catalogo()"], cwd=ROOT, capture_output=True)
        _cat = "biblioteca_alexandria/fontes/motores.json"
        _extra = [_cat] if _git("diff", "--name-only", "--", _cat).strip() else []
        _flx = "docs/dados/fluxo_oportunidades.json"
        _extra += [_flx] if _git("diff", "--name-only", "--", _flx).strip() and _flx not in m["alterados"] else []
        _extra += [l[3:] for l in _git("status", "--porcelain", "--", "biblioteca_alexandria/livros").splitlines()
                   if l.strip() and l[3:] not in m["alterados"]]
        _git("add", "--", *[c for c in m["alterados"] + _extra if (ROOT / c).exists()], ok=True)
        if not _git("diff", "--cached", "--name-only"):
            print("nada mudou em relação ao main"); return True
        _git("commit", "-q", "-m", msg)
        if subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], cwd=ROOT).returncode == 0:
            print(f"gravado na tentativa {i}: só os {len(m['alterados'])} arquivo(s) deste fluxo"); return True
        time.sleep(5 * i)
    print("REGISTRO FALHOU — nenhum arquivo de outro fluxo foi sobrescrito"); return False


if __name__ == "__main__":
    if sys.argv[1:2] == ["salvar"]:
        salvar()
    elif sys.argv[1:2] == ["aplicar"]:
        sys.exit(0 if aplicar(sys.argv[2] if len(sys.argv) > 2 else "dados") else 1)
    else:
        print(__doc__)
