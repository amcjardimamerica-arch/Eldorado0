"""EXPURGO DO QUE NÃO É OPORTUNIDADE (titular, 15/10/2026).

"Não quero dado inútil; oportunidade que não se utiliza é dado inútil. Uma vez eliminada e descartada, deve ter removido
o seu registro por completo." Começa pelo PNCP, de onde vem a maior parte do ruído.

1. CLASSIFICA cada compra do PNCP citada em QUALQUER arquivo de dados: é INVÁLIDA só com motivo explícito do portão de
   captação (território, licitação/compra, contrato de serviço, contratação de vagas, PNAE, pessoa física, ILPI e
   acolhimento fora de Goiás e das capitais). Dúvida (título curto, sem sinal claro) NÃO é apagada.
2. REMOVE um registro (elemento de lista, entrada de dicionário, linha de JSONL, linha do banco) só quando TODAS as
   compras do PNCP que ele cita são inválidas — um livro com edições válidas e inválidas não se perde.
3. Alcança: dados/, estado/, docs/dados/, biblioteca_alexandria/ (JSON e JSONL), o banco biblioteca_alexandria/livros/_acervo/banco/eldorado.db, o catálogo
   de livros e as PASTAS dos livros eliminados, e o registro de releitura (estado/achados_vistos.json).
4. Simulação primeiro (--simular); a execução grava estado/expurgo/AAAA-MM-DD.json com o que saiu de cada lugar.
"""
from __future__ import annotations

import json
import re
import shutil
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from .nucleo import ROOT

VERSAO = 4          # 16/10/2026: v4 = histórico só ligado a livro de oportunidade; achado só trecho e links; v3 = o acervo de histórico também passa pelos portões; v2: regra territorial em todo o sistema — mudou a regra, o expurgo roda de novo no mesmo dia
PNCP = re.compile(r"pncp\.gov\.br/(?:app/editais|pncp-api/v1/orgaos|api/(?:pncp|consulta)/v1/orgaos)/(\d{14})/(?:compras/)?(\d{4})/(\d+)", re.I)
AREAS = ["dados", "estado", "docs/dados", "biblioteca_alexandria"]
# 16/10/2026 (titular): o Eldorado e o Farol são as duas metades do sistema; a regra dos livros e os expurgos valem SÓ
# para o Eldorado — os dados da associação e do Farol nunca são tocados
FAROL = re.compile(r"(^|/)(dados/farol|dados/associacoes|biblioteca_alexandria/associacoes)(/|$)|preparacao_farol\.json$")
NUNCA = re.compile(r"(^|/)(config|tests|src|scripts)/|estado/expurgo/|estado/pncp/estudo_mes\.json|/arquivo_frio/")
TITULO = ("titulo", "nome", "programa", "nome_classificado", "objeto")


URL = re.compile(r"https?://[^\s\"'<>\\]+")
VEREDITO: dict = {}          # chave → True (inválida) / False (válida); só chaves JULGADAS contam


def _url_chave(u: str) -> str:
    from .vistos import chave
    return chave({"url": u.rstrip(".,;)")})


def _chaves(txt: str) -> set:
    ks = {f"{a}/{b}/{int(c)}" for a, b, c in PNCP.findall(txt)}
    if VEREDITO:
        for u in URL.findall(txt):
            if "pncp.gov.br" not in u:
                k = _url_chave(u)
                if k in VEREDITO:
                    ks.add(k)
    return ks


def _arquivos():
    for a in AREAS:
        for p in (ROOT / a).rglob("*"):
            rel = str(p.relative_to(ROOT))
            if p.is_file() and p.suffix in (".json", ".jsonl", ".txt") and not NUNCA.search(rel) and not FAROL.search(rel) \
                    and p.stat().st_size < 120_000_000:
                yield p


def _carregar(p: Path):
    txt = p.read_text(encoding="utf-8", errors="replace")
    if p.suffix == ".jsonl":
        linhas = []
        for l in txt.splitlines():
            try:
                linhas.append(json.loads(l))
            except ValueError:
                linhas.append(l)
        return "jsonl", linhas
    try:
        return "json", json.loads(txt)
    except ValueError:
        return None, None


# ── 1. CLASSIFICAR ─────────────────────────────────────────────────────────────────────────────────────────────────
def _julgar_territorio(obj, juizo: dict):
    """16/10/2026 (titular): em outros estados só ESTADUAIS e CAPITAIS — julga cada registro com endereço."""
    if isinstance(obj, dict):
        u = next((obj.get(f) for f in ("url", "pagina", "link_oficial", "site_oficial") if isinstance(obj.get(f), str) and obj[f].startswith("http")), None)
        t = next((obj.get(f) for f in TITULO if isinstance(obj.get(f), str)), None)
        if u and t and "pncp.gov.br" not in u:
            from .repositorio_unico import municipal_fora_de_goias
            try:
                ruim = bool(municipal_fora_de_goias({"titulo": t, "orgao": obj.get("orgao"), "url": u, "uf": obj.get("uf"),
                                                      "nivel": obj.get("nivel"), "link_oficial": obj.get("link_oficial")}))
            except Exception:  # noqa: BLE001
                ruim = False
            k = _url_chave(u); juizo.setdefault(k, set()).add(ruim)
        for v in obj.values():
            if isinstance(v, (dict, list)):
                _julgar_territorio(v, juizo)
    elif isinstance(obj, list):
        for v in obj:
            _julgar_territorio(v, juizo)


def _coletar_registros(obj, out: dict):
    """Para cada chave do PNCP, o melhor título/órgão/UF que algum registro traz."""
    if isinstance(obj, dict):
        ks = _chaves(json.dumps(obj, ensure_ascii=False)) if any(isinstance(v, str) and "pncp.gov.br" in v for v in obj.values()) else set()
        if len(ks) == 1:
            k = next(iter(ks)); r = out.setdefault(k, {})
            for f in TITULO:
                if isinstance(obj.get(f), str) and len(obj[f]) > len(r.get("titulo") or ""):
                    r["titulo"] = obj[f]
            for f in ("orgao", "uf", "municipio", "esfera", "modalidade"):
                if obj.get(f) and not r.get(f):
                    r[f] = obj[f]
            uf = str(obj.get("uf") or "").strip().upper()[:2]
            if len(uf) == 2 and uf.isalpha() and uf not in ("BR", "NO"):
                r.setdefault("_ufs", set()).add(uf)           # 17/10: todas as UFs declaradas para a mesma compra
        for v in obj.values():
            if isinstance(v, (dict, list)):
                _coletar_registros(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _coletar_registros(v, out)


def classificar(info: dict) -> tuple[bool, str | None]:
    """(inválida?, motivo). Inválida SÓ com motivo explícito do portão de captação."""
    from .pncp_osc import _N, portao_associacao
    from .repositorio_unico import uf_por_municipio
    t = str(info.get("titulo") or "")
    orgao = str(info.get("orgao") or t.partition(" — ")[0])
    uf = str(info.get("uf") or "")[:2].upper() if len(str(info.get("uf") or "")) >= 2 and str(info.get("uf")).upper() not in ("BR", "NONE") else None
    uf = uf or uf_por_municipio(orgao)
    mo = re.search(r"(?:MUNICIPIO|PREFEITURA MUNICIPAL|CAMARA MUNICIPAL|FUNDO MUNICIPAL DE [A-Z ]{3,40}?) DE ([A-Z ]{3,40})", _N(orgao))
    esfera = str(info.get("esfera") or "")[:1].upper() or None
    if esfera not in ("M", "E", "F", "D"):
        esfera = "M" if re.search(r"MUNICIP|PREFEIT|CAMARA MUNICIPAL|CONSORCIO", _N(orgao)) else None
    m = {"titulo": t, "orgao": orgao, "uf": uf, "municipio": info.get("municipio") or (mo.group(1).title() if mo else None),
         "esfera": esfera, "modalidade": info.get("modalidade")}
    motivo = portao_associacao(m, _N(f"{t} {info.get('objeto') or ''}"))
    return (bool(motivo), motivo)


# ── 2. REMOVER ─────────────────────────────────────────────────────────────────────────────────────────────────────
def _invalido(obj, inval: set) -> bool:
    ks = _chaves(json.dumps(obj, ensure_ascii=False) if not isinstance(obj, str) else obj)
    julgadas = {k for k in ks if k in inval or VEREDITO.get(k) is False or "/" in k and not k.startswith(("url:", "txt:"))}
    return bool(julgadas) and julgadas <= inval


def _colunar(obj: dict, inval: set, cont: Counter) -> dict:
    """Formato colunar (schema + linhas, com ou sem dicionários de valores): remove a LINHA inteira, decodificada;
    os dicionários de valores ficam intactos (as posições que as outras linhas usam não mudam)."""
    sc = obj.get("schema") or obj.get("campos") or []
    dic = obj.get("dicionarios") or obj.get("dicionario") or obj.get("dic") or {}
    def texto(l):
        partes = []
        for i, x in enumerate(l if isinstance(l, list) else []):
            c = sc[i] if i < len(sc) else None
            if c in dic and isinstance(x, int) and isinstance(dic[c], list) and x < len(dic[c]):
                x = dic[c][x]
            partes.append(json.dumps(x, ensure_ascii=False) if not isinstance(x, str) else x)
        return " ".join(partes)
    novas = []
    for l in obj.get("linhas") or []:
        ks = _chaves(texto(l))
        if ks and ks <= inval:
            cont["removidos"] += 1; continue
        novas.append(l)
    return {**obj, "linhas": novas}


def _filtrar(obj, inval: set, cont: Counter):
    if isinstance(obj, dict) and isinstance(obj.get("linhas"), list) and isinstance(obj.get("schema") or obj.get("campos"), list):
        return _colunar(obj, inval, cont)
    if isinstance(obj, list):
        registros = bool(obj) and all(isinstance(v, dict) for v in obj)      # só lista de REGISTROS (nunca uma linha colunar)
        novo = []
        for v in obj:
            if registros and _invalido(v, inval):
                cont["removidos"] += 1; continue
            novo.append(_filtrar(v, inval, cont) if isinstance(v, (dict, list)) and not isinstance(v, list) or registros else v)
        return novo
    if isinstance(obj, dict):
        novo, colecao = {}, _eh_colecao(obj)
        for k, v in obj.items():
            if (colecao or k not in _CAMPOS_DO_REGISTRO) and isinstance(v, dict) and _eh_registro(v) and _invalido(v, inval):
                cont["removidos"] += 1; continue
            novo[k] = _filtrar(v, inval, cont)
        return novo
    return obj


_CAMPOS_DE_REGISTRO = TITULO + ("url", "link_oficial", "pagina", "site_oficial", "link_documento", "veredito", "fim", "prazo")


def _eh_registro(v: dict) -> bool:
    """17/10/2026 (chat de testes): só um REGISTRO pode ser removido inteiro; uma COLEÇÃO (dicionário cujos valores são
    todos dicionários/listas, ex.: {"derivadas": {...}} ou {"itens": {...}}) é percorrida item a item. Antes, uma coleção
    em que a ÚNICA compra do PNCP citada era inválida saía inteira — assim as 28 derivadas da revisão humana
    (dados/editais/derivadas_revisao.json) sumiram no expurgo de 16/10 00:56 por causa de um único registro.
    Ainda 17/10: um BLOCO de uma ficha sem campo que identifique um registro (ex.: "historico_5_anos" = {ocorrencias,
    por_ano, por_mes, ultimas} ou "local_publicacao" = {pagina_de_publicacao, vetores_observados…}) também é
    percorrido, não removido: antes bastava um valor escalar para o bloco contar como registro, e o expurgo de 16/10
    00:56 tirou esses dois blocos de 166 das 260 fichas de parâmetros das fontes porque as edições citadas eram compras
    inválidas do PNCP — a contagem de 5 anos e a página oficial de publicação da fonte se perderam junto."""
    return any(isinstance(v.get(f), str) for f in _CAMPOS_DE_REGISTRO + ("id",))



def _eh_colecao(obj: dict) -> bool:
    """Dicionário cujos valores são todos dicionários/listas (ex.: {"itens": {...}}, analises.json por id)."""
    return bool(obj) and all(isinstance(x, (dict, list)) for x in obj.values())


def _uf_em_disputa(info: dict, motivo: str | None) -> bool:
    """17/10/2026 (chat de testes): a mesma compra citada com UFs diferentes não é "município de outro estado" com
    certeza — é dúvida, e dúvida não é apagada. Antes, o primeiro registro lido decidia: um registro de extração errada
    (Alvorada do Norte/GO gravado como "Alvora do Norte/BA") condenou em 16/10 dois chamamentos válidos de Goiás em todo o
    sistema. Só vale para o motivo territorial; os motivos de objeto (compra, credenciamento remunerado…) seguem."""
    ufs = info.get("_ufs") or set()
    return str(motivo or "").startswith("município de outro estado") and ("GO" in ufs or len(ufs) > 1)


_COLECOES = ("itens", "registros")
_TOTAIS = ("total", "quantidade")


def _ids(col) -> list:
    if isinstance(col, dict):
        return list(col)
    return [str(x.get("id")) for x in col if isinstance(x, dict) and x.get("id") is not None]


def _registros(col) -> list:
    return [x for x in (col.values() if isinstance(col, dict) else col) if isinstance(x, dict)]


def _campo_do_contador(cont: dict, itens: list) -> str | None:
    """O campo dos registros que o contador (valor → quantidade) conta — só se batia EXATAMENTE antes do expurgo."""
    if not cont or not itens or not all(isinstance(n, int) and not isinstance(n, bool) for n in cont.values()):
        return None
    for f in {f for x in itens for f in x}:
        c = Counter(str(x.get(f)) for x in itens if x.get(f) is not None)
        if c and dict(c) == {str(k): n for k, n in cont.items() if n}:
            return f
    return None


def recontar(antes: dict, depois: dict, em: str | None = None, removidos_antes: list | None = None) -> list:
    """17/10/2026 (chat de testes): o expurgo tirava registros de uma base e deixava o resumo velho (verificacao_63:
    37 itens e resumo de 63; abertos_sem_informacao: total 107 e 19 itens; validacao_2026-09-27: contagem 1046 e 1031
    itens). Agora, em toda base com coleção ("itens"/"registros") e metadados:
      • o que no resumo/contagem era RECALCULÁVEL e batia com a lista antes (total da lista, contador de um campo) é
        recontado sobre a lista que ficou;
      • o "total" de primeiro nível é o universo HISTÓRICO da base (o que foi verificado naquele dia) e não muda: a
        base ganha o bloco "expurgo" com os ids que saíram, e total = itens + expurgo.removidos;
      • os demais números do resumo (que não dá para recalcular a partir da lista) ficam como o dia os gravou.
    Devolve os ids que saíram (para o CSV que acompanha a base)."""
    if not isinstance(antes, dict) or not isinstance(depois, dict) or _eh_colecao(antes):
        return []
    saiu_total: list = []
    for ck in _COLECOES:
        a, d = antes.get(ck), depois.get(ck)
        if not isinstance(a, (dict, list)) or not isinstance(d, (dict, list)):
            continue
        ficou = set(_ids(d))
        saiu = [i for i in _ids(a) if i not in ficou] if removidos_antes is None else list(removidos_antes)
        if not saiu:
            continue
        ia, idp = _registros(a), _registros(d)
        for sk in ("resumo", "contagem", "contagens", "totais"):
            S = depois.get(sk)
            if not isinstance(S, dict):
                continue
            f = _campo_do_contador(S, ia)
            if f:                                                   # o próprio bloco é um contador
                novo = Counter(str(x.get(f)) for x in idp if x.get(f) is not None)
                depois[sk] = {k: novo[str(k)] for k in S if novo[str(k)]}
                continue
            for k, v in list(S.items()):
                if k in _TOTAIS and isinstance(v, int) and v == len(a):
                    S[k] = len(d)
                elif isinstance(v, dict):
                    f = _campo_do_contador(v, ia)
                    if f:
                        novo = Counter(str(x.get(f)) for x in idp if x.get(f) is not None)
                        S[k] = {kk: novo[str(kk)] for kk in v if novo[str(kk)]}
        bloco = dict(depois.get("expurgo") or antes.get("expurgo") or {})
        ids = list(bloco.get("ids") or [])
        ids += [i for i in saiu if i not in ids]
        bloco.update({"regra": "registros que o expurgo tirou desta base (o que não é oportunidade sai por completo; "
                               "o id fica para a contabilidade: total = itens + removidos)",
                      "colecao": ck, "removidos": len(ids), "ids": ids,
                      "execucoes": (bloco.get("execucoes") or []) + [{"em": em or date.today().isoformat(), "removidos": len(saiu)}]})
        depois["expurgo"] = bloco
        saiu_total += saiu
    return saiu_total


def _csv_irmao(p: Path, saiu: list, simular: bool) -> int:
    """O CSV que acompanha a base (mesmo nome) perde as mesmas linhas, pela coluna id."""
    import csv
    import io
    c = p.with_suffix(".csv")
    if not saiu or not c.exists():
        return 0
    bruto = c.read_bytes()
    bom = bruto.startswith(b"\xef\xbb\xbf")
    txt = bruto.decode("utf-8-sig", errors="replace")
    cab = txt.splitlines()[0] if txt else ""
    sep = ";" if cab.count(";") >= cab.count(",") else ","
    linhas = list(csv.reader(io.StringIO(txt), delimiter=sep))
    if not linhas or "id" not in linhas[0]:
        return 0
    i, fora = linhas[0].index("id"), set(map(str, saiu))
    novas = [linhas[0]] + [l for l in linhas[1:] if not (len(l) > i and l[i] in fora)]
    n = len(linhas) - len(novas)
    if n and not simular:
        out = io.StringIO(); csv.writer(out, delimiter=sep, lineterminator="\r\n").writerows(novas)
        c.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.getvalue().encode("utf-8"))
    return n


# campos que fazem parte do próprio registro: nunca saem sozinhos (o registro sai inteiro ou fica inteiro). Uma
# referência a um registro inválido dentro de uma ficha (ex.: "ultimo_edital") é removida.
_CAMPOS_DO_REGISTRO = {"dados", "doze_itens", "edital_referencia", "itens", "checklist12", "prazo"}


def _gravar_registro_do_dia(arq: Path, novo: dict) -> None:
    """17/10/2026 (chat de testes): o expurgo roda mais de uma vez no mesmo dia (mudança de regra → roda de novo) e cada
    execução SOBRESCREVIA o registro do dia: o de 16/10 perdeu o que saiu às 00:56 (verificacao_63: 20, derivadas…).


    Agora o registro do dia ACUMULA: contagens somadas por arquivo, listas unidas e a lista das execuções."""
    ant = {}
    if arq.exists():
        try:
            ant = json.loads(arq.read_text(encoding="utf-8"))
        except ValueError:
            ant = {}
    desta = int(novo.get("total_registros_removidos") or 0)
    if ant and not ant.get("simulacao"):
        por = Counter(ant.get("registros_removidos_por_arquivo") or {}); por.update(novo.get("registros_removidos_por_arquivo") or {})
        novo["registros_removidos_por_arquivo"] = dict(sorted(por.items(), key=lambda x: -x[1]))
        novo["total_registros_removidos"] = sum(por.values())
        for campo in ("livros_removidos", "pastas_de_livros_removidas", "chaves_invalidas"):
            novo[campo] = sorted(set(ant.get(campo) or []) | set(novo.get(campo) or []))
        banco = Counter(ant.get("linhas_do_banco_removidas") or {}); banco.update(novo.get("linhas_do_banco_removidas") or {})
        novo["linhas_do_banco_removidas"] = dict(banco)
        novo["registro_de_releitura"] = int(ant.get("registro_de_releitura") or 0) + int(novo.get("registro_de_releitura") or 0)
        novo["execucoes"] = (ant.get("execucoes") or [{"versao": ant.get("versao"), "removidos": ant.get("total_registros_removidos")}]) + \
            [{"versao": novo.get("versao"), "removidos": desta}]
    arq.write_text(json.dumps(novo, ensure_ascii=False, indent=1), encoding="utf-8")


def executar(simular: bool = True) -> dict:
    VEREDITO.clear()
    regs: dict = {}
    arqs = list(_arquivos())
    cache = {}
    for p in arqs:
        tipo, obj = _carregar(p)
        if tipo:
            cache[p] = (tipo, obj); _coletar_registros(obj, regs)
    # chaves citadas só em texto (sem registro com título): ficam como dúvida (não apagadas)
    inval, motivos = set(), Counter()
    try:                                                   # o que o repositório DESCARTOU também sai por completo
        from . import repositorio_unico as R
        R.construir(gravar=False)
        for d in R.DESCARTADAS:
            for k in _chaves(f"{d.get('url')} {d.get('link_oficial')}"):
                inval.add(k); motivos["descartada no repositório"] += 1
    except Exception:  # noqa: BLE001
        pass
    exemplos = defaultdict(list)
    juizo: dict = {}
    for p_, (tipo_, obj_) in cache.items():
        _julgar_territorio(obj_, juizo)
    VEREDITO.clear()
    for k, vs in juizo.items():
        VEREDITO[k] = (vs == {True})                  # inválida só se TODO registro que cita o endereço é inválido
        if VEREDITO[k]:
            inval.add(k); motivos["município de outro estado (não capital)"] += 1
    for k, info in regs.items():
        if k in inval:
            continue
        ruim, mot = classificar(info)
        if ruim and _uf_em_disputa(info, mot):
            motivos["dúvida: registros dão UFs diferentes (não apagada)"] += 1; continue
        if ruim:
            inval.add(k); g = mot.split(" (")[0].split(" —")[0][:60]; motivos[g] += 1
            if len(exemplos[g]) < 5:
                exemplos[g].append(str(info.get("titulo"))[:120])
    por_arquivo, livros_removidos = {}, []
    for p, (tipo, obj) in cache.items():
        cont = Counter()
        if tipo == "jsonl":
            novo = [l for l in obj if not (isinstance(l, dict) and _invalido(l, inval) and (cont.update(removidos=1) or True))]
        else:
            novo = _filtrar(obj, inval, cont)
            if cont["removidos"]:
                _csv_irmao(p, recontar(obj, novo), simular)
        if cont["removidos"]:
            rel = str(p.relative_to(ROOT)); por_arquivo[rel] = cont["removidos"]
            if rel.endswith("fontes/motores.json"):
                antes = {l.get("id") for l in (obj.get("motores") or [])}
                depois = {l.get("id") for l in (novo.get("motores") or [])}
                livros_removidos = sorted(antes - depois)
            if not simular:
                if tipo == "jsonl":
                    p.write_text("\n".join(json.dumps(l, ensure_ascii=False) if not isinstance(l, str) else l for l in novo) + "\n", encoding="utf-8")
                else:
                    ini = p.read_text(encoding="utf-8", errors="replace")[:300]
                    compacto = "\n" not in ini.strip()[:200]
                    p.write_text(json.dumps(novo, ensure_ascii=False, separators=(",", ":")) if compacto else
                                 json.dumps(novo, ensure_ascii=False, indent=2 if ini.startswith(("{\n  ", "[\n  ")) else 1), encoding="utf-8")
    # pastas dos livros eliminados (biblioteca_alexandria/livros/anexos/<pasta>) que só citam compras inválidas
    pastas = []
    base = ROOT / "biblioteca_alexandria/livros/anexos"
    for d in (base.iterdir() if base.exists() else []):
        if d.is_dir():
            txt = " ".join(f.read_text(encoding="utf-8", errors="replace") for f in d.rglob("*") if f.is_file() and f.stat().st_size < 5_000_000)
            ks = _chaves(txt)
            if ks and ks <= inval:
                pastas.append(str(d.relative_to(ROOT)))
                if not simular:
                    shutil.rmtree(d)
    # banco
    banco = {}
    db = ROOT / "biblioteca_alexandria/livros/_acervo/banco/eldorado.db"
    if db.exists() and inval:
        con = sqlite3.connect(db)
        for (tab,) in con.execute("select name from sqlite_master where type='table'"):
            cols = [r[1] for r in con.execute(f"pragma table_info('{tab}')")]
            n = 0
            for (rowid, *vals) in con.execute(f"select rowid, * from '{tab}'"):
                txt = " ".join(str(v) for v in vals if isinstance(v, str))
                ks = _chaves(txt)
                if ks and ks <= inval:
                    n += 1
                    if not simular:
                        con.execute(f"delete from '{tab}' where rowid=?", (rowid,))
            if n:
                banco[tab] = n
        if not simular:
            con.commit(); con.execute("vacuum")
        con.close()
    # registro de releitura
    vist = ROOT / "estado/achados_vistos.json"
    nv = 0
    if vist.exists():
        V = json.loads(vist.read_text(encoding="utf-8"))
        for m_ in V.values():
            for k in [k for k in m_ if (k.startswith("pncp:") and k[5:] in inval) or k in inval]:
                nv += 1
                if not simular:
                    del m_[k]
        if not simular:
            vist.write_text(json.dumps(V, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    res = {"em": date.today().isoformat(), "versao": VERSAO, "simulacao": simular, "compras_pncp_citadas": len(regs), "invalidas": len(inval),
           "motivos": dict(motivos.most_common()), "exemplos": dict(exemplos), "registros_removidos_por_arquivo": dict(sorted(por_arquivo.items(), key=lambda x: -x[1])),
           "total_registros_removidos": sum(por_arquivo.values()), "livros_removidos": livros_removidos, "pastas_de_livros_removidas": pastas,
           "linhas_do_banco_removidas": banco, "registro_de_releitura": nv}
    if not simular:
        d = ROOT / "estado/expurgo"; d.mkdir(parents=True, exist_ok=True)
        _gravar_registro_do_dia(d / f"{res['em']}.json", {**res, "chaves_invalidas": sorted(inval)})
    return res


if __name__ == "__main__":
    r = executar(simular="--executar" not in sys.argv)
    print(json.dumps({k: (v if k not in ("exemplos",) else v) for k, v in r.items() if k not in ("registros_removidos_por_arquivo",)}, ensure_ascii=False, indent=1)[:5000])
    print("arquivos:", json.dumps(dict(list(r["registros_removidos_por_arquivo"].items())[:40]), ensure_ascii=False, indent=0))



def reter_controle(dias_registros: int = 30, dias_vistos: int = 180, gravar: bool = True) -> dict:
    """17/10/2026 (titular): RETENÇÃO DO CONTROLE — o controle é memória de trabalho, não banco que cresce sem fim.
    Registros datados (relatórios, logs por dia, Interceptador) com mais de 30 dias são apagados; a memória de "já
    visto" esquece links com mais de 180 dias. Pontos de parada, estado de motor e modelos são sobrescritos (não crescem)."""
    import re as _re
    from datetime import date as _d, timedelta as _td
    raiz = ROOT / "estado"
    corte = (_d.today() - _td(days=dias_registros)).isoformat()
    apagados = 0
    for p in raiz.rglob("*"):
        if not p.is_file():
            continue
        m = _re.search(r"(20\d\d-\d\d-\d\d)", p.name)
        if m and m.group(1) < corte and p.suffix in (".json", ".jsonl", ".txt", ".md", ".log", ".csv"):
            if gravar:
                p.unlink()
            apagados += 1
    vistos = raiz / "achados_vistos.json"
    esquecidos = 0
    if vistos.exists():
        try:
            d = json.loads(vistos.read_text(encoding="utf-8"))
            corte_v = (_d.today() - _td(days=dias_vistos)).isoformat()
            itens = d.get("itens") if isinstance(d, dict) and isinstance(d.get("itens"), dict) else None
            if itens is not None:
                velhos = [k for k, v in itens.items() if isinstance(v, dict) and str(v.get("visto_em") or v.get("em") or "9")[:10] < corte_v]
                for k in velhos:
                    itens.pop(k, None)
                esquecidos = len(velhos)
                if gravar and velhos:
                    vistos.write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass
    return {"registros_apagados": apagados, "vistos_esquecidos": esquecidos, "regra": f"registros datados {dias_registros} dias; já visto {dias_vistos} dias"}
