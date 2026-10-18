"""Pilotos (titular, 18/10/2026): o Interceptador parou por um nome indefinido; o Espião perdeu a configuração aprendida."""
import random
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class NenhumNomeIndefinido(unittest.TestCase):
    def test_codigo_sem_nome_indefinido(self):
        """Uma linha órfã ('el', deixada pelo #275 em 16/10) parou TODOS os voos do Interceptador; o Diário da União
        quebrava no fim da fonte B pelo mesmo motivo. A varredura acusa qualquer novo caso antes de um motor parar."""
        try:
            import pyflakes  # noqa: F401
        except ImportError:
            self.skipTest("pyflakes ausente")
        r = subprocess.run([sys.executable, "-m", "pyflakes", "src", "scripts"], cwd=ROOT, capture_output=True, text=True)
        indefinidos = [l for l in r.stdout.splitlines() if "undefined name" in l]
        self.assertEqual(indefinidos, [])


class EspiaoVoaPelaConfiguracaoAprendida(unittest.TestCase):
    def test_quatro_em_cinco_pelo_aprendizado(self):
        from src import espiao_foco as E
        chamadas = {"thompson": 0, "rodizio": 0}
        orig_t, orig_r = E._escolher_thompson, E._escolher_rodizio
        E._escolher_thompson = lambda c, r=None: (chamadas.__setitem__("thompson", chamadas["thompson"] + 1), ("t", "q"))[1]
        E._escolher_rodizio = lambda c, r=None: (chamadas.__setitem__("rodizio", chamadas["rodizio"] + 1), ("r", "q"))[1]
        try:
            rnd = random.Random(7)
            for _ in range(1000):
                E.escolher({"familias": {}, "consultas": {}}, rnd)
        finally:
            E._escolher_thompson, E._escolher_rodizio = orig_t, orig_r
        self.assertGreater(chamadas["thompson"], 700)
        self.assertGreater(chamadas["rodizio"], 100, "o rodízio continua: nenhuma família esquecida")


class DuckDuckGoEmDescansoNaoEInsistido(unittest.TestCase):
    def test_via_bloqueada_ha_pouco_nao_esta_disponivel(self):
        import time
        from src import piloto_busca as B
        self.assertFalse(B._via_disponivel("duckduckgo", {"situacao": {"duckduckgo": {"bloqueada_em": time.time() - 60}}}))
        self.assertTrue(B._via_disponivel("duckduckgo", {"situacao": {"duckduckgo": {"bloqueada_em": time.time() - 3600}}}))
