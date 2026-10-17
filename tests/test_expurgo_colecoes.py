"""Expurgo (17/10/2026, chat de testes): coleção não sai inteira por causa de um registro; registro do dia acumula."""
import json
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from src import expurgo as X

INVALIDA = "https://pncp.gov.br/app/editais/12345678000199/2026/7"
CHAVE = "12345678000199/2026/7"


class TesteColecaoPercorridaItemAItem(unittest.TestCase):
    def test_so_o_registro_invalido_sai_da_colecao(self):
        obj = {"derivadas": {
            "der-1": {"titulo": "Chamamento de outro estado", "url": INVALIDA, "veredito": "bronze"},
            "der-2": {"titulo": "Edital da Secult GO", "url": "https://goias.gov.br/cultura/edital-1", "veredito": "ouro"},
            "der-3": {"parecer": "revisão humana", "itens": {"Objeto": {"valor": "Fomento"}}, "veredito": "pendente"}}}
        cont = Counter()
        novo = X._filtrar(obj, {CHAVE}, cont)
        self.assertIn("derivadas", novo, "a coleção não pode sumir inteira")
        self.assertEqual(set(novo["derivadas"]), {"der-2", "der-3"})
        self.assertEqual(cont["removidos"], 1)

    def test_registro_invalido_continua_saindo(self):
        obj = {"itens": {"a": {"titulo": "Credenciamento", "url": INVALIDA}}}
        novo = X._filtrar(obj, {CHAVE}, Counter())
        self.assertEqual(novo["itens"], {})


class TesteBlocoDaFichaPercorrido(unittest.TestCase):
    def test_bloco_sem_identificacao_nao_sai_inteiro(self):
        """17/10: 'historico_5_anos' e 'local_publicacao' das fichas de parâmetros saíram inteiros em 16/10 00:56."""
        ficha = {"id": "captacao-001", "programa": "Lei Municipal de Cultura",
                 "historico_5_anos": {"ocorrencias": 2, "por_ano": {"2024": 2},
                                      "ultimas": [{"data": "2024-11-06", "titulo": "Credenciamento", "url": INVALIDA},
                                                  {"data": "2024-03-01", "titulo": "Chamamento", "url": "https://goiania.go.gov.br/ed"}]},
                 "local_publicacao": {"url_ultimo_edital": None, "pagina_de_publicacao": "https://goiania.go.gov.br/cultura/",
                                      "vetores_observados": [INVALIDA]},
                 "ultimo_edital": {"titulo": "Credenciamento", "url": INVALIDA}}
        cont = Counter()
        novo = X._filtrar(ficha, {CHAVE}, cont)                    # a ficha é o arquivo (raiz)
        self.assertEqual(novo["historico_5_anos"]["por_ano"], {"2024": 2})
        self.assertEqual([u["titulo"] for u in novo["historico_5_anos"]["ultimas"]], ["Chamamento"])   # o registro inválido sai
        self.assertEqual(novo["local_publicacao"]["pagina_de_publicacao"], "https://goiania.go.gov.br/cultura/")
        self.assertNotIn("ultimo_edital", novo)                                                      # registro inválido
        self.assertEqual(cont["removidos"], 2)


class TesteRegistroDoDiaAcumula(unittest.TestCase):
    def test_segunda_execucao_soma_a_primeira(self):
        with tempfile.TemporaryDirectory() as d:
            arq = Path(d) / "2026-10-16.json"
            X._gravar_registro_do_dia(arq, {"versao": 3, "simulacao": False, "registros_removidos_por_arquivo": {"a.json": 20, "b.json": 1},
                                            "total_registros_removidos": 21, "livros_removidos": ["op-1"], "chaves_invalidas": ["k1"]})
            X._gravar_registro_do_dia(arq, {"versao": 4, "simulacao": False, "registros_removidos_por_arquivo": {"a.json": 6},
                                            "total_registros_removidos": 6, "livros_removidos": ["op-2"], "chaves_invalidas": ["k2"]})
            r = json.loads(arq.read_text(encoding="utf-8"))
        self.assertEqual(r["registros_removidos_por_arquivo"], {"a.json": 26, "b.json": 1})
        self.assertEqual(r["total_registros_removidos"], 27)
        self.assertEqual(r["livros_removidos"], ["op-1", "op-2"])
        self.assertEqual(r["versao"], 4, "a versão do dia é a da última execução (o comando decide por ela)")
        self.assertEqual([e["removidos"] for e in r["execucoes"]], [21, 6])


class TesteCampoDeRegistroNuncaSaiSozinho(unittest.TestCase):
    """17/10: em 16/10 o registro de Vera Cruz/RS ficou sem os 12 "dados" e duas validações sem os "doze_itens"."""

    def test_campo_que_cita_compra_invalida_fica_no_registro_valido(self):
        boa = "https://pncp.gov.br/app/editais/01005727000124/2026/50"
        obj = {"itens": [{"id": "r1", "titulo": "Chamamento de OSC", "url": boa,
                          "edital_referencia": {"titulo": "edital anexo", "url": INVALIDA},
                          "dados": {"Anexos": {"valor": INVALIDA, "status": "confirmado"}}}]}
        novo = X._filtrar(obj, {CHAVE}, Counter())
        self.assertEqual(novo["itens"][0]["edital_referencia"]["url"], INVALIDA)
        self.assertIn("Anexos", novo["itens"][0]["dados"])

    def test_registro_inteiramente_invalido_sai_inteiro(self):
        obj = {"itens": [{"id": "r1", "titulo": "Credenciamento", "url": INVALIDA,
                          "dados": {"Anexos": {"valor": INVALIDA, "status": "confirmado"}}}]}
        self.assertEqual(X._filtrar(obj, {CHAVE}, Counter())["itens"], [])


class TesteUfEmDisputaEDuvida(unittest.TestCase):
    """17/10: 'Alvora do Norte'/BA (extração errada) condenou o chamamento de Alvorada do Norte/GO em todo o sistema."""

    def test_ufs_divergentes_para_a_mesma_compra(self):
        regs = {}
        X._coletar_registros({"itens": [
            {"titulo": "Chamamento 006/2026", "orgao": "Fundo Municipal de Educação de Alvora do Norte", "uf": "BA", "url": INVALIDA},
            {"titulo": "Chamamento 006/2026 — Goiás / Alvorada do Norte", "orgao": "FUNDO MUNICIPAL DE EDUCACAO DE ALVORADA DO NORTE",
             "uf": "GO", "url": INVALIDA}]}, regs)
        info = regs[CHAVE]
        self.assertEqual(info["_ufs"], {"BA", "GO"})
        self.assertTrue(X._uf_em_disputa(info, "município de outro estado (Alvora Do Norte/BA) — municipais só de Goiás e das capitais"))

    def test_motivo_de_objeto_e_uf_unica_seguem_valendo(self):
        self.assertFalse(X._uf_em_disputa({"_ufs": {"GO", "BA"}}, "compra, fornecimento ou contratação de empresa"))
        self.assertFalse(X._uf_em_disputa({"_ufs": {"RS"}}, "município de outro estado (Osorio/RS) — municipais só de Goiás"))


class TesteResumoRecontado(unittest.TestCase):
    """17/10: a base perdia registros e guardava o resumo velho (verificacao_63: 37 itens, resumo de 63)."""

    def _base(self):
        return {"gerado_em": "2026-09-15", "total": 3,
                "resumo": {"total": 3, "veredito": {"aprovado": 2, "reprovado": 1}, "com_prazo": 2},
                "itens": {"a": {"titulo": "A", "url": INVALIDA, "veredito": "aprovado"},
                          "b": {"titulo": "B", "url": "https://goias.gov.br/x", "veredito": "aprovado"},
                          "c": {"titulo": "C", "url": "https://goias.gov.br/y", "veredito": "reprovado"}}}

    def test_o_recalculavel_e_recontado_e_o_universo_historico_fica(self):
        antes = self._base()
        depois = X._filtrar(antes, {CHAVE}, Counter())
        saiu = X.recontar(antes, depois, em="2026-10-16")
        self.assertEqual(saiu, ["a"])
        self.assertEqual(depois["total"], 3, "o total de primeiro nível é o universo verificado naquele dia")
        self.assertEqual(depois["resumo"]["total"], 2)
        self.assertEqual(depois["resumo"]["veredito"], {"aprovado": 1, "reprovado": 1})
        self.assertEqual(depois["resumo"]["com_prazo"], 2, "o que não dá para recalcular fica como o dia gravou")
        self.assertEqual(depois["expurgo"]["ids"], ["a"])
        self.assertEqual(depois["total"], len(depois["itens"]) + depois["expurgo"]["removidos"])

    def test_segunda_execucao_acumula_os_ids(self):
        antes = self._base()
        d1 = X._filtrar(antes, {CHAVE}, Counter()); X.recontar(antes, d1, em="2026-10-16")
        d2 = json.loads(json.dumps(d1)); del d2["itens"]["c"]
        X.recontar(d1, d2, em="2026-10-17")
        self.assertEqual(d2["expurgo"]["ids"], ["a", "c"])
        self.assertEqual([e["removidos"] for e in d2["expurgo"]["execucoes"]], [1, 1])
        self.assertEqual(d2["resumo"]["veredito"], {"aprovado": 1})

    def test_colecao_pura_nao_ganha_bloco(self):
        antes = {"a": {"titulo": "A", "url": INVALIDA}, "b": {"titulo": "B", "url": "https://goias.gov.br/x"}}
        depois = X._filtrar(antes, {CHAVE}, Counter())
        self.assertEqual(X.recontar(antes, depois), [])
        self.assertNotIn("expurgo", depois)

    def test_csv_que_acompanha_a_base_perde_as_mesmas_linhas(self):
        with tempfile.TemporaryDirectory() as d:
            j = Path(d) / "base.json"; j.write_text("{}", encoding="utf-8")
            (Path(d) / "base.csv").write_bytes("\ufeffprioridade;titulo;id\r\n1;A;a\r\n2;B;b\r\n".encode("utf-8"))
            self.assertEqual(X._csv_irmao(j, ["a"], simular=False), 1)
            txt = (Path(d) / "base.csv").read_text(encoding="utf-8-sig")
        self.assertEqual(txt.splitlines(), ["prioridade;titulo;id", "2;B;b"])


if __name__ == "__main__":
    unittest.main()


class TesteCampoDoRegistroNaoSaiSozinho(unittest.TestCase):
    def test_dados_do_registro_ficam(self):
        """17/10: o registro de Vera Cruz/RS ficou sem os 12 'dados' em 16/10 — campo do registro não sai sozinho."""
        reg = {"id": "x", "titulo": "Chamamento GO", "url": "https://goias.gov.br/x",
               "dados": {"titulo": "Credenciamento", "url": INVALIDA}}
        novo = X._filtrar(reg, {CHAVE}, Counter())
        self.assertIn("dados", novo)
