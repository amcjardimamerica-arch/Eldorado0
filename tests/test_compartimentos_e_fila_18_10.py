"""Sala de controle em compartimentos e fila de livros (titular, 18/10/2026)."""
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from src import fila_livros as FL
from src import sala_controle as S


class FilaDeLivros(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.p = mock.patch.object(FL, "ARQ", Path(self.tmp.name) / "fila.json"); self.p.start()

    def tearDown(self):
        self.p.stop(); self.tmp.cleanup()

    def test_no_maximo_3_tentativas_com_intervalo(self):
        FL.montar({"op-1": {"certificar"}})
        self.assertTrue(FL.pode("op-1", "certificar"))
        FL.tentativa("op-1", "certificar")
        self.assertFalse(FL.pode("op-1", "certificar"), "a 2ª só depois de 6 h")
        t0 = datetime.now(timezone.utc)
        with mock.patch.object(FL, "_agora", lambda: t0 + timedelta(hours=7)):
            self.assertTrue(FL.pode("op-1", "certificar"))
            FL.tentativa("op-1", "certificar")
        with mock.patch.object(FL, "_agora", lambda: t0 + timedelta(hours=20)):
            self.assertFalse(FL.pode("op-1", "certificar"), "a 3ª só depois de 24 h")
        with mock.patch.object(FL, "_agora", lambda: t0 + timedelta(hours=40)):
            self.assertTrue(FL.pode("op-1", "certificar"))
            FL.tentativa("op-1", "certificar")
        with mock.patch.object(FL, "_agora", lambda: t0 + timedelta(days=30)):
            self.assertFalse(FL.pode("op-1", "certificar"), "esgotado depois de 3 tentativas")
        self.assertEqual(FL.resumo()["esgotados_em_alguma_ferramenta"], 1)

    def test_resolvido_nao_tenta_de_novo_e_quem_fechou_sai_da_fila(self):
        FL.montar({"op-1": {"site_oficial"}, "op-2": {"validar"}})
        FL.tentativa("op-1", "site_oficial", resolvido=True)
        self.assertFalse(FL.pode("op-1", "site_oficial"))
        self.assertEqual(FL.montar({"op-1": set()})["na_fila"], 1)


class SalaEmCompartimentos(unittest.TestCase):
    def test_nove_compartimentos_na_ordem(self):
        self.assertEqual([c[2] for c in S.COMPARTIMENTOS],
                         ["Regência", "Coleta", "Certificação", "Investigação", "Verificação externa", "Repositório",
                          "Biblioteca", "Pertinência e aprendizado", "Farol de Alexandria"])

    def test_nenhum_instrumento_fica_de_fora_nem_repetido(self):
        ids = [i for c in S.COMPARTIMENTOS for i in c[3]]
        self.assertEqual(len(ids), len(set(ids)))
        for antigo in ("ma_cobertura", "mo_saude", "ca_12", "pi_interceptador", "ve_para_o_chrome", "es_abertas", "es_livros",
                       "rn_auc", "es_validadas", "mo_retentativa", "es_curadoria", "es_banco_unico", "hi_frio", "al_externa"):
            self.assertIn(antigo, ids)
