"""17/10/2026 (chat de testes, grupo i): consistência transversal — os mesmos números e dados em todo lugar.

F06.01 diagnóstico da mesma passagem · F06.07 ficha copia o repositório · F06.08/F07.06 toda capa tem o arquivo de
conteúdo · F07.03 validada só com 12/12 · F07.05 índice refeito do catálogo · F08.04 vetor nunca é fonte (também nas
certidões já guardadas) · F08.08 relatório do Cartório das certidões guardadas · F11.01 URL pré-assinada sem assinatura.
"""
import json
import re
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


class VetorNuncaEFonte(unittest.TestCase):
    def test_regua_nas_certidoes(self):
        from src.cartorio_leitura import aplicar_regua_certidao, e_vetor
        self.assertTrue(e_vetor("https://capitaai.com.br/captacao/x"))
        self.assertTrue(e_vetor("https://www.idis.org.br/ia-ponto3"))            # republicador catalogado
        self.assertTrue(e_vetor("https://pt.surveymonkey.com/r/EDITAL"))         # formulário não é documento
        self.assertTrue(e_vetor("https://abong.org.br/nanet/"))
        self.assertFalse(e_vetor("https://www.fapemig.br/edital.pdf"))           # domínio não reconhecido não é vetor
        self.assertFalse(e_vetor("https://www.gov.br/ibama/edital.pdf"))
        self.assertFalse(e_vetor(None))
        c = {"itens": {"Valor": {"valor": "R$ 10 mil", "trecho": "t", "documento": "https://capitaai.com.br/x"},
                       "Objeto": {"valor": "apoio", "trecho": "t", "documento": "https://www.gov.br/x.pdf"}},
             "resolvidos": ["Valor", "Objeto"], "ainda_faltam": ["Anexos"], "link_oficial": "https://captadores.org.br/editais/x"}
        self.assertEqual(aplicar_regua_certidao(c), 1)
        self.assertEqual(set(c["itens"]), {"Objeto"})
        self.assertEqual(c["nao_comprovados"]["Valor"]["valor"], "R$ 10 mil")   # o que foi lido não se perde
        self.assertIn("vetor", c["nao_comprovados"]["Valor"]["motivo"])
        self.assertEqual(c["resolvidos"], ["Objeto"]); self.assertIn("Valor", c["ainda_faltam"])   # volta à fila
        self.assertIsNone(c["link_oficial"]); self.assertTrue(c["link_oficial_vetor"])
        self.assertEqual(aplicar_regua_certidao(c), 0)                           # idempotente

    def test_a_gravacao_das_certidoes_aplica_a_regua(self):
        from src import livro_arquivo as LA
        doc = {"certidoes": {"estrela:x": {"itens": {"Valor": {"valor": "R$ 1", "trecho": "t", "documento": "https://prosas.com.br/x"}}}}}
        LA._regua_nas_certidoes("estado/cartorio/certidoes_manuais.json", doc)
        self.assertEqual(doc["certidoes"]["estrela:x"]["itens"], {})
        outro = {"certidoes": {"estrela:x": {"itens": {"Valor": {"documento": "https://prosas.com.br/x"}}}}}
        LA._regua_nas_certidoes("estado/outro.json", outro)
        self.assertIn("Valor", outro["certidoes"]["estrela:x"]["itens"])        # só nos arquivos de certidões
        src = (ROOT / "src/livro_arquivo.py").read_text(encoding="utf-8")
        self.assertEqual(src.count("_regua_nas_certidoes(_rel(caminho), obj)") + src.count("_regua_nas_certidoes(rel, obj)"), 2)

    def test_prova_do_repositorio(self):
        from src.repositorio_unico import prova_valida
        ok = {"valor": "R$ 300 mil", "trecho": "valor global", "documento": "https://editais.baoba.org.br/x"}
        self.assertTrue(prova_valida(ok))
        self.assertFalse(prova_valida({**ok, "valor": None}))                    # sem valor não comprova
        self.assertFalse(prova_valida({**ok, "valor": "não informado"}))
        self.assertFalse(prova_valida({**ok, "trecho": ""}))
        self.assertFalse(prova_valida({**ok, "documento": None}))
        self.assertFalse(prova_valida({**ok, "documento": "https://capitaai.com.br/x"}))
        self.assertFalse(prova_valida({**ok, "estado": "falta"}))                # a revisão marcou como falta

    def test_dados_sem_prova_em_vetor(self):
        from src import livro_arquivo as LA
        from src.cartorio_leitura import e_vetor
        for n in ("certidoes", "certidoes_manuais"):
            d = LA.ler_arquivo(ROOT / f"estado/cartorio/{n}.json", {}) or {}
            ruins = [f"{k} · {i}" for k, c in (d.get("certidoes") or {}).items() for i, v in (c.get("itens") or {}).items()
                     if isinstance(v, dict) and e_vetor(v.get("documento"))]
            self.assertEqual(ruins, [], n)
        R = json.loads((ROOT / "biblioteca_alexandria/livros/_vistas/repositorio_unico.json").read_text(encoding="utf-8"))["registros"]
        self.assertEqual([f"{r['id']} · {k}" for r in R for k, it in (r.get("itens") or {}).items()
                          if it.get("estado") == "comprovado" and e_vetor(it.get("documento"))], [])


class ValidadaSoComDoze(unittest.TestCase):
    def test_validada_tem_os_12(self):
        from src.criterio_selos import resolvido
        R = json.loads((ROOT / "biblioteca_alexandria/livros/_vistas/repositorio_unico.json").read_text(encoding="utf-8"))["registros"]
        val = [r for r in R if r.get("estado") == "validada"]
        self.assertTrue(val)
        for r in val:
            it = r["itens"]
            prova = {k: {"s": "ok", "v": str(v.get("valor") or "")} if v.get("estado") == "comprovado" else
                     {"s": "disp", "v": v.get("motivo") or ""} if v.get("estado") == "dispensado" else {"s": "falta"} for k, v in it.items()}
            self.assertEqual([k for k, p in prova.items() if not resolvido(p)], [], r["id"])
            self.assertTrue(r.get("link_oficial") or r.get("motivo_estado", "").startswith("ouro na revisão (12/12"), r["id"])
        self.assertFalse([r["id"] for r in val if r.get("motivo_estado") in ("ouro na revisão",
                          "objeto e prazo comprovados no documento oficial + site oficial")])
        src = (ROOT / "src/repositorio_unico.py").read_text(encoding="utf-8")
        self.assertIn('sem os 12 itens', src)


class URLPreAssinada(unittest.TestCase):
    URL = ("https://prosas-prod-files.s3.sa-east-1.amazonaws.com/arquivos/x/Edital.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256"
           "&X-Amz-Credential=AKIA" + "X" * 16 + "%2F20261015%2Fsa-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261015T000000Z"
           "&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=" + "a" * 64)

    def test_sem_assinatura(self):
        from src.nucleo import sem_assinatura, sem_assinaturas
        self.assertEqual(sem_assinatura(self.URL), "https://prosas-prod-files.s3.sa-east-1.amazonaws.com/arquivos/x/Edital.pdf")
        self.assertEqual(sem_assinatura("https://a.gov.br/x?id=3"), "https://a.gov.br/x?id=3")
        self.assertEqual(sem_assinatura(self.URL.replace("&", "&amp;") + "&amp;v=2"),
                         "https://prosas-prod-files.s3.sa-east-1.amazonaws.com/arquivos/x/Edital.pdf?v=2")
        d = sem_assinaturas({self.URL: {"pdfs": [self.URL], "texto": f"ver {self.URL} ."}})
        self.assertNotIn("X-Amz", json.dumps(d))

    def test_pontos_de_gravacao(self):
        from src import nucleo, fila_retentativa as FR
        t = Path(tempfile.mkdtemp()) / "x.json"
        nucleo.write_json(t, {"anexos": [self.URL]})
        self.assertNotIn("X-Amz", t.read_text(encoding="utf-8"))
        with mock.patch.object(FR, "_CACHE", {"fila": {}, "fora_da_fila": {}}):
            FR.falhou(self.URL, "cartorio", "HTTP 403")
            self.assertEqual(list(FR._CACHE["fila"]), ["https://prosas-prod-files.s3.sa-east-1.amazonaws.com/arquivos/x/Edital.pdf"])
            self.assertTrue(FR.aguardando(self.URL))                              # a consulta usa a mesma chave
        self.assertIn("sem_assinaturas(ant)", (ROOT / "scripts/treino_fontes.py").read_text(encoding="utf-8"))
        self.assertIn("sem_assinaturas(d)", (ROOT / "src/livro_arquivo.py").read_text(encoding="utf-8"))

    def test_dados_publicos_limpos(self):
        pad = re.compile(r"AKIA[0-9A-Z]{16}|X-Amz-Credential")
        for base in ("docs/dados", "estado"):
            for p in (ROOT / base).rglob("*.json"):
                if p.stat().st_size < 5_000_000:
                    self.assertIsNone(pad.search(p.read_text(encoding="utf-8", errors="ignore")), str(p.relative_to(ROOT)))


class CapaConteudoIndice(unittest.TestCase):
    def test_conteudo_das_capas(self):
        from src import livro_arquivo as LA
        r = Path(tempfile.mkdtemp()); cat = r / "motores.json"; pasta = r / "livros"; pasta.mkdir()
        cat.write_text(json.dumps({"motores": [{"id": "a"}, {"id": "b"}, {"id": None}]}))
        (pasta / "a.json").write_text('{"id": "a", "acervo": {"x": 1}}')
        st = LA.conteudo_das_capas(cat=cat, pasta=pasta)
        self.assertEqual(st["ids"], ["b"])
        self.assertEqual(json.loads((pasta / "a.json").read_text()), {"id": "a", "acervo": {"x": 1}})   # não toca no que existe
        self.assertEqual(json.loads((pasta / "b.json").read_text())["acervo"], {})
        self.assertEqual(LA.conteudo_das_capas(cat=cat, pasta=pasta)["arquivos_abertos"], 0)

    def test_dados_toda_capa_tem_arquivo_e_indice_do_catalogo(self):
        L = ROOT / "biblioteca_alexandria/livros"
        cat = {m.get("id") for m in json.loads((ROOT / "biblioteca_alexandria/fontes/motores.json").read_text(encoding="utf-8"))["motores"] if m.get("id")}
        self.assertEqual(sorted(i for i in cat if not (L / f"{i}.json").exists()), [])
        idx = {e["id"] for e in json.loads((L / "_indice.json").read_text(encoding="utf-8"))["livros"]}
        self.assertEqual(idx, cat)
        R = json.loads((L / "_vistas/repositorio_unico.json").read_text(encoding="utf-8"))["registros"]
        self.assertEqual([r["id"] for r in R if r.get("livro") and not (L / f"{r['livro']}.json").exists()], [])
        self.assertEqual([r["id"] for r in R if r.get("estado") != "fechada" and r.get("livro") and r["livro"] not in cat], [])


class MesmoRetrato(unittest.TestCase):
    def test_ordem_do_fechamento(self):
        from src import comando as C
        F = C.fases({})
        nomes = [f["etapa"] for f in F]
        self.assertLess(nomes.index("fechamento"), nomes.index("fichas_farol"))          # fichas do mesmo repositório
        self.assertLess(nomes.index("fichas_farol"), nomes.index("sala_de_controle"))
        fe = [" ".join(c) for c in next(f for f in F if f["etapa"] == "fechamento")["cmds"]]
        i = lambda t: next(n for n, c in enumerate(fe) if t in c)  # noqa: E731
        self.assertLess(i("livros_curadoria"), i("R.construir()"))                         # catálogo arrumado antes
        self.assertLess(i("unir_duplicados"), i("R.construir()"))
        self.assertLess(i("IL.construir()"), i("R.construir()"))
        self.assertLess(i("regua_nas_certidoes"), i("R.construir()"))
        # 17/10 (junção h+i): o relatório do Cartório é republicado das certidões guardadas COM a fila do retrato final
        # (republicar_relatorio, que faz o que relatorio_atual fazia e recalcula a fila) — depois do repositório
        self.assertLess(i("R.construir()"), i("republicar_relatorio"))
        self.assertLess(i("C.pendencias()"), i("republicar_relatorio"))
        ult_trava = max(n for n, c in enumerate(fe) if c.endswith("src.trava_livros"))
        self.assertLess(i("R.construir()"), ult_trava)                                       # a trava depois do repositório
        self.assertLess(ult_trava, i("conteudo_das_capas"))                                  # toda capa com arquivo
        self.assertLess(ult_trava, i("src.dashboard_dados"))                                 # o painel conta o catálogo gravado
        self.assertLess(ult_trava, i("sincronizar_catalogo"))

    def test_ficha_copia_o_repositorio(self):
        R = json.loads((ROOT / "biblioteca_alexandria/livros/_vistas/repositorio_unico.json").read_text(encoding="utf-8"))["registros"]
        F = json.loads((ROOT / "docs/dados/fichas_oportunidades.json").read_text(encoding="utf-8"))["fichas"]
        div = [f"{r['id']} · {c}" for r in R if r["id"] in F for c in ("fim", "link_oficial", "titulo", "orgao", "uf")
               if r.get(c) and F[r["id"]].get(c) and str(r[c]).strip() != str(F[r["id"]][c]).strip()]
        self.assertEqual(div, [])
        self.assertIn('"link_oficial": r.get("link_oficial")', (ROOT / "src/fichas_oportunidades.py").read_text(encoding="utf-8"))

    def test_relatorio_do_cartorio_das_certidoes_guardadas(self):
        from src import cartorio as C, livro_arquivo as LA
        n = len((LA.ler_arquivo(ROOT / "estado/cartorio/certidoes.json", {}) or {}).get("certidoes") or {})
        r = C.relatorio_atual(gravar=False)
        self.assertGreaterEqual(r["certidoes"], n)
        pub = json.loads((ROOT / "docs/dados/cartorio.json").read_text(encoding="utf-8"))["resumo"]
        self.assertEqual((pub["certidoes"], pub["com_link_oficial"]), (r["certidoes"], r["com_link_oficial"]))

    def test_leitura_sem_ciclo_preserva_o_ciclo_da_analise(self):
        src = (ROOT / "src/diagnostico_sistema.py").read_text(encoding="utf-8")
        self.assertIn('res["ciclo_de_analise"] = ciclo if ciclo_ else anterior.get("ciclo_de_analise")', src)


if __name__ == "__main__":
    unittest.main()
