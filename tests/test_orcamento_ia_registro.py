"""O orçamento de IA por tarefa (5% do período) soma os dois formatos de registro de estado/ia_uso.jsonl:
o de src/livros_monitoramento (campo "uso") e o de src/ia.py (tokens_entrada / tokens_saida)."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src import livros_monitoramento as lm
from src.nucleo import now_iso


class TesteOrcamentoSomaOsDoisFormatos(unittest.TestCase):
    def test_gasto_inclui_registro_de_src_ia(self):
        with tempfile.TemporaryDirectory() as d:
            raiz = Path(d); (raiz / "estado").mkdir(); (raiz / "config").mkdir()
            em = now_iso()
            linhas = [{"em": em, "tarefa": "edital-x", "uso": {"input_tokens": 100, "output_tokens": 50}},
                      {"em": em, "tarefa": "edital-x", "tokens_entrada": 1000, "tokens_saida": 200},
                      {"em": em, "tarefa": "outro", "tokens_entrada": 9999, "tokens_saida": 1}]
            (raiz / "estado/ia_uso.jsonl").write_text("\n".join(json.dumps(x) for x in linhas) + "\n", encoding="utf-8")
            with mock.patch.object(lm, "ROOT", raiz):
                o = lm._orcamento("edital-x")
        self.assertEqual(o["gasto_tarefa"], 1350)


if __name__ == "__main__":
    unittest.main()
