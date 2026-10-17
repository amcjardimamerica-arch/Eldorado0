"""30/09: a curadoria dos livros trocou ids de livros pesquisados (12 parâmetros) e a regeneração desligou
os 'órfãos' — 329 ligados viraram 105. Pesquisado nunca some; todo ligado tem livro; todo JSON é válido."""
import json, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


class TestePesquisadosProtegidos(unittest.TestCase):
    def test_pesquisados_continuam_ligados_com_parametros(self):
        """01/10: todo livro pesquisado que continua na Biblioteca (dentro da abrangência) mantém os 12 parâmetros."""
        from src.livros_parametros import carregar
        C = {x["id"]: x for x in json.loads((ROOT / "biblioteca_alexandria/fontes/motores.json").read_text(encoding="utf-8"))["motores"]}
        L = json.loads((ROOT / "estado/livros_monitoramento.json").read_text(encoding="utf-8"))["ligados"]
        perdidos = [i for i, r in carregar().items() if r.get("decisao") != "D" and i in C and not (C[i].get("parametros") or (L.get(i) or {}).get("parametros"))]
        self.assertEqual(perdidos, [], "livro pesquisado perdeu os parâmetros")

    def test_a_pesquisa_nao_e_desviada_de_livro_que_continua_no_catalogo(self):
        """17/10: a fusão de 17/10 04:19 pôs os pesquisados (Impactarte, Emenda de Goiânia) em ids_juntados de livros
        novos sem parâmetros; o mapa de ids desviava a pesquisa para eles, embora o pesquisado continuasse no catálogo."""
        from src.livros_parametros import carregar, PASTA
        C = {x["id"] for x in json.loads((ROOT / "biblioteca_alexandria/fontes/motores.json").read_text(encoding="utf-8"))["motores"]}
        gravados = {r.get("id") for a in PASTA.glob("parametros_*.json")
                    for r in json.loads(a.read_text(encoding="utf-8")).get("itens") or []}
        desviados = [i for i, r in carregar().items() if i not in gravados and r.get("id_pesquisado") in C]
        self.assertEqual(desviados, [])

    def test_juntar_leva_os_parametros_do_pesquisado(self):
        from src.curadoria_biblioteca import _juntar
        fica = {"id": "novo", "historico": []}
        _juntar(fica, {"id": "pesquisado", "parametros": {"Objeto": "x"}, "parametros_em": "2026-10-01", "historico": []})
        self.assertEqual(fica["parametros"], {"Objeto": "x"})
        self.assertEqual(fica["parametros_em"], "2026-10-01")
        self.assertIn("pesquisado", fica["ids_juntados"])

    def test_unificacao_mantem_o_pesquisado(self):
        for trecho in ('return (not m.get("parametros"), not tem', 'return (not m.get("parametros"), not oficial'):
            self.assertIn(trecho, (ROOT / "src/unificar_livros.py").read_text(encoding="utf-8"))

    def test_todo_ligado_tem_livro(self):
        L = json.loads((ROOT / "estado/livros_monitoramento.json").read_text(encoding="utf-8"))["ligados"]
        C = {x["id"] for x in json.loads((ROOT / "biblioteca_alexandria/fontes/motores.json").read_text(encoding="utf-8"))["motores"]}
        self.assertEqual([k for k in L if k not in C], [])

    def test_curadoria_protege_pesquisado(self):
        for f, trecho in (("src/livros_curadoria.py", 'and not x.get("parametros")'), ("src/livros_repositorio.py", 'x.get("parametros") or not'),
                          ("src/motores.py", 'x.get("parametros") or not')):
            self.assertIn(trecho, (ROOT / f).read_text(encoding="utf-8"), f)

    def test_dados_json_validos(self):
        for f in ("biblioteca_alexandria/fontes/motores.json", "estado/livros_monitoramento.json", "docs/dados/motores.json", "docs/dados/fluxo_oportunidades.json"):
            json.loads((ROOT / f).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
