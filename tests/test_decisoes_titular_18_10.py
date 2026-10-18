"""Decisões do titular de 18/10/2026 sobre vereditos da pesquisa externa (o veredito original fica guardado no livro)."""
import unittest

from src.decisoes_titular import veredito_efetivo as V


class EditaisDeGoiasRestritosSaoDoPerfil(unittest.TestCase):
    def test_goias_restrito_a_residentes_ou_sede_fica(self):
        for motivo, r in (("Edital 001/CMDCA/2026 de Itaberaí: restrito a OSC com sede no município",
                           {"titulo": "Itaberaí — EDITAL DE CHAMAMENTO PÚBLICO", "uf": "BR"}),
                          ("PNAB de Rubiataba: só residentes no município", {"titulo": "Prefeitura de Rubiataba — AVISO", "uf": None}),
                          ("Arranjos Regionais da Secult Goiás, restrito a produtoras sediadas em Goiás", {"titulo": "Edital Arranjos Regionais FSA"})):
            self.assertIsNone(V({"veredito": "fora_perfil", "motivo": motivo}, r)[0], motivo)

    def test_restricao_de_outro_estado_continua_fora(self):
        v, _d = V({"veredito": "fora_perfil", "motivo": "Edital PNAB de Jaguaretama/CE, restrito a residentes"},
                  {"titulo": "PNAB JAGUARETAMA - EDITAL", "uf": "CE"})
        self.assertEqual(v, "fora_perfil")

    def test_fora_do_perfil_por_outro_motivo_continua(self):
        self.assertEqual(V({"veredito": "fora_perfil", "motivo": "só pessoa física"}, {"titulo": "Edital de Goiânia", "uf": "GO"})[0],
                         "fora_perfil")


class EmendaNaoERuido(unittest.TestCase):
    def test_emendas_constam(self):
        for r in ({"id": "emenda-federal-2026", "titulo": "Emenda Parlamentar — Câmara e Senado — captação 2026"},
                  {"id": "op-x", "titulo": "Emenda Parlamentar Municipal — Goiânia — captação 2026"},
                  {"id": "op-y", "titulo": "Emenda Parlamentar Estadual — Goiás — captação 2026"}):
            self.assertIsNone(V({"veredito": "ruido", "motivo": "página institucional"}, r)[0], r["titulo"])

    def test_diario_que_cita_emenda_nao_e_emenda(self):
        self.assertEqual(V({"veredito": "ruido", "motivo": "edição sem chamamento"},
                           {"id": "op-z", "titulo": "Diário Oficial de Goiânia (GO) 2026-09-25 — edital"})[0], "ruido")
