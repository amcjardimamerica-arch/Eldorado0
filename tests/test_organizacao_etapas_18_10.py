"""Etapas integradas (titular, 18/10/2026): cada etapa é UMA só; as ferramentas são usadas conforme o que as
oportunidades precisam, sem subetapas e sem sequência fixa, até a oportunidade ser validada."""
import unittest
from unittest import mock

from src import comando as C


class EtapasIntegradas(unittest.TestCase):
    def test_a_sequencia_tem_o_cartorio_como_uma_etapa_so(self):
        F = C.fases({})
        self.assertEqual([f["etapa"] for f in F], ["certificar", "legislativo", "fechamento", "sala_de_controle", "diagnostico"])
        self.assertFalse(hasattr(C, "ETAPAS"), "sem subetapas")

    def test_cartorio_usa_a_ferramenta_da_maior_necessidade_e_nao_repete_o_que_nao_resolve(self):
        usadas, nec = [], {"site_oficial": 5, "certificar": 9, "validar": 0, "curadoria": 0, "regra_dos_livros": 0, "unir_livros": 0}
        def rodar(F, fn, etapa, resto):
            usadas.append(fn)
            if fn == "certificar":
                nec["certificar"] = 2                       # certificou 7: resolveu
                nec["validar"] = 7                          # e 7 ficaram prontas para validar
            elif fn == "validar":
                nec["validar"] = 0
            return 1.0, None                                # site oficial não resolveu nada
        F = {k: {"pular": None, "t": 60, "cmds": []} for k in ("banco_unico", "site_oficial", "certificar", "validar", "curadoria",
                                                                "regra_dos_livros", "unir_livros", "livros", "fichas_farol")}
        F.update({"expurgo": {"pular": "já feito hoje"}, "biblioteca_diaria": {"pular": "já feita hoje"}})
        from src import fila_livros as FL
        porl = lambda: {"op-1": {k for k, v in nec.items() if v}}  # noqa: E731
        with mock.patch.object(C, "ferramentas", lambda ctx: F), mock.patch.object(C, "_rodar", rodar), \
             mock.patch.object(C, "_remontar", lambda F, r: None), mock.patch.object(C, "necessidades_cartorio", lambda: dict(nec)), \
             mock.patch.object(C, "necessidades_por_livro", porl), mock.patch.object(FL, "pode", lambda *a, **k: True), \
             mock.patch.object(FL, "tentativa", lambda *a, **k: {}), mock.patch.object(FL, "_ler", lambda: {"livros": {}}), \
             mock.patch.object(FL, "_gravar", lambda d: None), mock.patch.object(FL, "montar", lambda n: {"na_fila": 1}):
            r = C.executar_cartorio({}, 3600)
        # 18/10: a regra dos livros e a fila de livros vêm primeiro (um banco só, depois um a um)
        self.assertEqual(usadas[:5], ["regra_dos_livros", "banco_unico", "certificar", "validar", "site_oficial"])
        self.assertEqual(usadas.count("site_oficial"), 1, "ação sem efeito não se repete")
        self.assertEqual(r["etapa"], "certificar")
        self.assertTrue(all("acao" in a for a in r["acoes"]))

    def test_regra_dos_livros_e_migracoes_fora(self):
        T = C.ferramentas({})
        for e in ("modalidade", "absorver", "migracao_livros"):
            self.assertNotIn(e, T)
        regra = " ".join(" ".join(c) for c in T["regra_dos_livros"]["cmds"])
        self.assertIn("absorver_proibidos", regra); self.assertIn("registrar_do_estado_dos_motores", regra)
