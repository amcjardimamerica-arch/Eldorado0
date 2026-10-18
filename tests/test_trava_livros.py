"""Trava dos livros (titular, 17/10/2026): livro criado não é apagado nem sobrescrito; só recebe informação nova."""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src import trava_livros as T


class TravaDosLivros(unittest.TestCase):
    def setUp(self):
        self.r = Path(tempfile.mkdtemp())
        (self.r / "biblioteca_alexandria/fontes").mkdir(parents=True); (self.r / "biblioteca_alexandria/livros").mkdir(parents=True)
        self.cat = self.r / T.CAT_REL
        self.cat.write_text(json.dumps({"motores": [
            {"id": "a", "programa": "PNAB Goiás", "orgao": "Secult-GO", "pagina": "https://goias.gov.br/pnab",
             "historico": [{"id": "e1"}, {"id": "e2"}], "coleta": {"x": 1}, "estado": "aberto"},
            {"id": "b", "programa": "Fundo do Idoso", "orgao": "Conanda"},
            {"id": "c", "programa": "PNAB Goiás (cópia)", "orgao": "Secult-GO"}]}))
        (self.r / "biblioteca_alexandria/livros/a.json").write_text(json.dumps({"id": "a", "anexos": {"edital": "u1"}}))
        g = lambda *a: subprocess.run(["git", *a], cwd=self.r, capture_output=True, check=True)  # noqa: E731
        g("init", "-q"); g("config", "user.email", "t@t"); g("config", "user.name", "t"); g("add", "-A"); g("commit", "-qm", "base")
        self.p = [mock.patch.object(T, "ROOT", self.r), mock.patch.object(T, "ARQUIVADOS", self.r / "biblioteca_alexandria/livros/_arquivados"),
                  mock.patch.object(T, "REGISTRO", self.r / "estado/trava_livros.json")]
        for x in self.p:
            x.start()

    def tearDown(self):
        for x in self.p:
            x.stop()

    def test_nada_se_perde_so_se_acrescenta(self):
        # o sistema: apaga "b" (sem união), une "c" em "a", troca a página de "a", tira um item do histórico,
        # muda o estado (operacional), acrescenta informação nova e apaga o arquivo do livro "a"
        self.cat.write_text(json.dumps({"motores": [
            {"id": "a", "programa": "PNAB Goiás", "orgao": "Secult-GO", "pagina": "https://goias.gov.br/pnab-2026",
             "historico": [{"id": "e2"}, {"id": "e3"}], "coleta": {"y": 2}, "estado": "fechado", "juntados": [{"id": "c"}]}]}))
        (self.r / "biblioteca_alexandria/livros/a.json").unlink()
        st = T.aplicar()
        L = {x["id"]: x for x in json.loads(self.cat.read_text())["motores"]}
        self.assertIn("b", L, "livro apagado sem união volta")
        self.assertNotIn("c", L); self.assertTrue((self.r / "biblioteca_alexandria/livros/_arquivados/c.json").exists(), "unido: guardado inteiro")
        a = L["a"]
        self.assertEqual(a["pagina"], "https://goias.gov.br/pnab-2026", "o valor novo fica")
        self.assertEqual(a["_anteriores"]["pagina"][0]["valor"], "https://goias.gov.br/pnab", "o anterior é guardado")
        self.assertEqual({h["id"] for h in a["historico"]}, {"e1", "e2", "e3"}, "histórico só ganha")
        self.assertEqual(a["coleta"], {"y": 2, "x": 1}, "coleta só ganha")
        self.assertEqual(a["estado"], "fechado", "campo operacional muda normalmente")
        self.assertTrue((self.r / "biblioteca_alexandria/livros/a.json").exists(), "arquivo do livro apagado volta")
        self.assertEqual(st["livros_devolvidos"], 1); self.assertEqual(st["livros_arquivados_por_uniao"], 1)

    def test_edicao_separada_pela_curadoria_nao_volta(self):
        """17/10/2026: a curadoria separa as edições de outro estado num livro próprio e registra em "separados"; a trava
        devolvia a edição ao livro de origem e ele voltava a misturar estados."""
        self.cat.write_text(json.dumps({"motores": [
            {"id": "a", "programa": "PNAB Goiás", "orgao": "Secult-GO", "pagina": "https://goias.gov.br/pnab", "coleta": {"x": 1},
             "historico": [{"id": "e1"}], "estado": "aberto", "separados": [{"id": "a-sp", "uf": "SP", "edicoes": [T._chave_item({"id": "e2"})]}]},
            {"id": "a-sp", "programa": "PNAB Goiás", "historico": [{"id": "e2"}]},
            {"id": "b", "programa": "Fundo do Idoso", "orgao": "Conanda"}, {"id": "c", "programa": "PNAB Goiás (cópia)", "orgao": "Secult-GO"}]}))
        T.aplicar()
        L = {x["id"]: x for x in json.loads(self.cat.read_text())["motores"]}
        self.assertEqual([h["id"] for h in L["a"]["historico"]], ["e1"], "a edição separada fica no livro do seu estado")
        self.assertEqual([h["id"] for h in L["a-sp"]["historico"]], ["e2"])

    def test_curadoria_separa_uma_vez_e_a_trava_mantem(self):
        from src import livros_curadoria as LC
        cat = {"motores": [{"id": "m", "programa": "Edital X", "uf": "GO", "historico": [{"id": "h1", "uf": "GO"}, {"id": "h2", "uf": "AP"}]}]}
        with tempfile.TemporaryDirectory() as d:
            c = Path(d) / "c.json"; c.write_text(json.dumps(cat))
            with mock.patch.object(LC, "CAT", c), mock.patch.object(LC, "LIG", Path(d) / "l.json"):
                LC.curar()
                m = json.loads(c.read_text())["motores"]
                m[0]["historico"].append({"id": "h2", "uf": "AP"})          # a trava devolveu (versão anterior à correção)
                c.write_text(json.dumps({"motores": m}))
                LC.curar()
                m = {x["id"]: x for x in json.loads(c.read_text())["motores"]}
        self.assertEqual(len(m), 2, "a segunda passagem não cria outro livro do mesmo estado")
        self.assertEqual(m["m"]["uf"], "GO", "empate: fica o estado do próprio livro")
        self.assertEqual({h["uf"] for h in m["m"]["historico"]}, {"GO"})
        self.assertTrue(all(s["edicoes"] == ['id:h2'] for s in m["m"]["separados"]))

    def test_sem_mudanca_nao_mexe(self):
        st = T.aplicar()
        self.assertFalse(any(st.values()))
