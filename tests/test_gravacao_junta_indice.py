"""17/10/2026 — a gravação dos fluxos copiava o índice dos livros INTEIRO por cima do main.

Duas execuções simultâneas: a que terminava por último apagava o que a outra tinha acrescentado (o índice ficou em 263
entradas depois de cair para 1). A gravação agora junta os índices: nada do main se perde; o do fluxo prevalece.
"""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("gsa", RAIZ / "scripts/gravar_somente_alterados.py")
G = importlib.util.module_from_spec(spec); spec.loader.exec_module(G)
REL = "biblioteca_alexandria/livros/_origens.json"


class TesteJuntaIndice(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); self._root = G.ROOT; G.ROOT = self.tmp / "repo"
        (G.ROOT / REL).parent.mkdir(parents=True)

    def tearDown(self):
        G.ROOT = self._root; shutil.rmtree(self.tmp, ignore_errors=True)

    def _gravar(self, main: dict, fluxo: dict) -> dict:
        (G.ROOT / REL).write_text(json.dumps(main), encoding="utf-8")
        o = self.tmp / "fluxo.json"; o.write_text(json.dumps(fluxo), encoding="utf-8")
        G._copiar(o, REL)
        return json.loads((G.ROOT / REL).read_text(encoding="utf-8"))

    def test_fluxo_concorrente_nao_apaga_entradas_do_main(self):
        main = {f"estado/a{i}.json": {"inteiro": ["op-1", str(i)]} for i in range(8000)}
        fluxo = {"estado/novo.json": {"inteiro": ["op-2", "0"]}}          # fluxo que partiu de um índice menor
        junto = self._gravar(main, fluxo)
        self.assertEqual(len(junto), 8001)

    def test_entrada_regravada_pelo_fluxo_prevalece(self):
        junto = self._gravar({"x": {"inteiro": ["op-velho", "0"]}}, {"x": {"inteiro": ["op-novo", "0"]}})
        self.assertEqual(junto["x"]["inteiro"][0], "op-novo")

    def test_indice_ilegivel_nao_e_gravado(self):
        (G.ROOT / REL).write_text('{"cortado": ', encoding="utf-8")
        o = self.tmp / "f.json"; o.write_text("{}", encoding="utf-8")
        with self.assertRaises(RuntimeError):
            G._copiar(o, REL)

    def test_outros_arquivos_seguem_substituidos(self):
        (G.ROOT / "estado").mkdir(parents=True); (G.ROOT / "estado/x.json").write_text('{"a":1}', encoding="utf-8")
        o = self.tmp / "x.json"; o.write_text('{"b":2}', encoding="utf-8")
        G._copiar(o, "estado/x.json")
        self.assertEqual(json.loads((G.ROOT / "estado/x.json").read_text(encoding="utf-8")), {"b": 2})


class TesteJuncao3Vias(unittest.TestCase):
    """17/10/2026 (chat de testes, item 6): os arquivos de controle com 3+ gravadores juntam em 3 vias."""
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); self._root, self._guarda = G.ROOT, G.GUARDA
        G.ROOT = self.tmp / "repo"; G.GUARDA = self.tmp / "guarda"

    def tearDown(self):
        G.ROOT, G.GUARDA = self._root, self._guarda; shutil.rmtree(self.tmp, ignore_errors=True)

    def _gravar(self, rel, base, main, fluxo):
        for raiz, txt in ((G.GUARDA / "base", base), (G.ROOT, main)):
            (raiz / rel).parent.mkdir(parents=True, exist_ok=True); (raiz / rel).write_text(txt, encoding="utf-8")
        o = self.tmp / "fluxo"; o.write_text(fluxo, encoding="utf-8")
        G._copiar(o, rel)
        return (G.ROOT / rel).read_text(encoding="utf-8")

    def test_os_tres_mais_criticos_estao_cobertos(self):
        self.assertIn("estado/livros_monitoramento.json", G.JUNTADOS_3_VIAS)   # ex-estado/opressores.json, 10 gravadores
        self.assertIn("estado/auditoria.jsonl", G.JUNTADOS_3_VIAS)             # 10 gravadores
        src = (RAIZ / "scripts/gravar_somente_alterados.py").read_text(encoding="utf-8")
        self.assertIn('"-m", "src.trava_livros"', src, "o catálogo (30 gravadores) é juntado pela trava dos livros")

    def test_livros_monitoramento_nao_perde_o_que_outro_fluxo_gravou(self):
        base = {"ligados": {"a": 1, "b": 1}, "historico": ["h1"], "atualizado_em": "t0"}
        main = {"ligados": {"a": 1, "b": 1, "c": 1}, "historico": ["h1", "h2"], "atualizado_em": "t1"}   # outro fluxo
        fluxo = {"ligados": {"a": 2, "d": 1}, "historico": ["h1", "h3"], "atualizado_em": "t2"}         # este fluxo
        j = json.loads(self._gravar("estado/livros_monitoramento.json", json.dumps(base), json.dumps(main), json.dumps(fluxo)))
        self.assertEqual(j["ligados"], {"a": 2, "c": 1, "d": 1}, "c (do outro) fica; a e d (deste) entram; b, retirado por este, sai")
        self.assertEqual(j["historico"], ["h1", "h2", "h3"]); self.assertEqual(j["atualizado_em"], "t2")

    def test_registro_jsonl_so_acrescenta(self):
        base = '{"e":1}\n'; main = '{"e":1}\n{"e":2}\n'; fluxo = '{"e":1}\n{"e":3}\n'
        out = self._gravar("estado/auditoria.jsonl", base, main, fluxo)
        self.assertEqual(out.splitlines(), ['{"e":1}', '{"e":2}', '{"e":3}'])

    def test_controle_ilegivel_nao_e_gravado(self):
        with self.assertRaises(RuntimeError):
            self._gravar("estado/livros_monitoramento.json", "{}", '{"cortado": ', "{}")


if __name__ == "__main__":
    unittest.main()
