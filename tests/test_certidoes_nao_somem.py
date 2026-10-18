"""17/10/2026 — as certidões do Cartório caíram de 2.158 para 140 entre 01:37 e 02:23 (logo depois do PR #319).

Medido no histórico: às 01:37 o índice dos livros tinha 2.158 certidões e todos os livros guardavam o dado; às 02:23 o
Cartório regravou com 140. O catálogo estava momentaneamente com 1.209 dos 2.010 livros: a absorção descartava a
certidão cujo livro não estava no catálogo (embora o arquivo do livro existisse) e o índice era regravado só com o que
a gravação nova trouxe. Regra de regressão: certidão gravada não some numa regravação; sai só quando o livro sai.
"""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src import livro_arquivo as LA

REL = "estado/cartorio/certidoes.json"


def _cert(lid: str, valor: str) -> dict:
    return {"id": lid, "tipo": "livro", "titulo": f"Edital {lid}", "itens": {"Objeto": {"valor": valor}}, "link_oficial": f"https://{lid}.go.gov.br"}


class CertidaoNaoSome(unittest.TestCase):
    def setUp(self):
        self.r = Path(tempfile.mkdtemp())
        (self.r / "biblioteca_alexandria/fontes").mkdir(parents=True)
        self.cat = self.r / "biblioteca_alexandria/fontes/motores.json"
        self._catalogo(["lv1", "lv2", "lv3"])
        self.p = [mock.patch.object(LA, "ROOT", self.r), mock.patch.object(LA, "PASTA", self.r / "biblioteca_alexandria/livros"),
                  mock.patch.object(LA, "ORIGENS", self.r / "biblioteca_alexandria/livros/_origens.json"),
                  mock.patch.object(LA, "CAT", self.cat)]
        for x in self.p:
            x.start()
        self.arq = self.r / REL

    def tearDown(self):
        for x in self.p:
            x.stop()
        for m in (LA._MEMO, LA._RO, LA._IDX_MEMO, LA._INDICE_SO_LEITURA):
            m.clear()
        shutil.rmtree(self.r, ignore_errors=True)

    def _catalogo(self, ids):
        self.cat.write_text(json.dumps({"motores": [{"id": i, "programa": f"Programa {i}"} for i in ids]}), encoding="utf-8")
        LA._IDX_MEMO.clear()

    def _gravar(self, certs: dict):
        for m in (LA._MEMO, LA._RO):
            m.clear()
        return LA.guardar_lote([(self.arq, {"em": "agora", "certidoes": certs})])

    def _ler(self) -> dict:
        for m in (LA._MEMO, LA._RO):
            m.clear()
        return (LA.ler_arquivo(self.arq, {}) or {}).get("certidoes") or {}

    def test_regravacao_parcial_nao_apaga_as_que_ja_existiam(self):
        self._gravar({f"livro:{i}": _cert(i, "v1") for i in ("lv1", "lv2", "lv3")})
        self.assertEqual(len(self._ler()), 3)
        self._gravar({"livro:lv2": _cert("lv2", "v2")})            # quem leu só uma (leitura parcial) e regravou
        c = self._ler()
        self.assertEqual(sorted(c), ["livro:lv1", "livro:lv2", "livro:lv3"])
        self.assertEqual(c["livro:lv2"]["itens"]["Objeto"]["valor"], "v2")    # a regravação vale para a que ela trouxe
        self.assertEqual(c["livro:lv1"]["itens"]["Objeto"]["valor"], "v1")

    def test_regravacao_vazia_nao_apaga(self):
        self._gravar({f"livro:{i}": _cert(i, "v1") for i in ("lv1", "lv2", "lv3")})
        self._gravar({})                                             # leitura falhou e voltou {}
        self.assertEqual(len(self._ler()), 3)

    def test_catalogo_reduzido_por_um_momento_nao_descarta(self):
        self._gravar({f"livro:{i}": _cert(i, "v1") for i in ("lv1", "lv2", "lv3")})
        self._catalogo(["lv1"])                                      # 17/10 02:23: catálogo com 1.209 de 2.010 livros
        self._gravar({f"livro:{i}": _cert(i, "v2") for i in ("lv1", "lv2", "lv3")})
        c = self._ler()
        self.assertEqual(len(c), 3)
        self.assertEqual(c["livro:lv3"]["itens"]["Objeto"]["valor"], "v2")    # religada ao livro que ainda existe

    def test_certidao_sai_quando_o_livro_sai(self):
        self._gravar({f"livro:{i}": _cert(i, "v1") for i in ("lv1", "lv2", "lv3")})
        (LA.PASTA / "lv3.json").unlink()                             # o expurgo removeu o livro
        self._catalogo(["lv1", "lv2"])
        self._gravar({"livro:lv1": _cert("lv1", "v2")})
        self.assertEqual(sorted(self._ler()), ["livro:lv1", "livro:lv2"])

    def test_cartorio_grava_pelo_caminho_preservado(self):
        self.assertIn(REL, LA.PRESERVAR)
        self.assertIn("estado/cartorio/certidoes_manuais.json", LA.PRESERVAR)


if __name__ == "__main__":
    unittest.main()
