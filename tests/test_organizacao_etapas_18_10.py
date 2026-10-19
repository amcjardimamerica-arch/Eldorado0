"""Etapas unificadas (titular, 18/10/2026): cada etapa é UMA só e usa as suas ferramentas conforme a situação."""
import unittest

from src import comando as C


class EtapasUnificadas(unittest.TestCase):
    def test_tres_etapas_e_as_suas_ferramentas(self):
        self.assertEqual(C.ETAPAS["decidir"]["ferramentas"], ("treinar_rede",))
        self.assertEqual(C.ETAPAS["motores"]["ferramentas"], ("pncp", "achados_dos_motores", "recalcular", "vigilancia_diaria"))
        self.assertEqual(C.ETAPAS["certificar"]["ferramentas"],
                         ("regra_dos_livros", "site_oficial", "expurgo", "certificar", "curadoria", "validar", "livros",
                          "unir_livros", "biblioteca_diaria", "banco_unico", "fichas_farol"))

    def test_a_sequencia_tem_o_cartorio_como_uma_etapa_so(self):
        F = C.fases({})
        self.assertEqual([f["etapa"] for f in F], ["certificar", "legislativo", "fechamento", "sala_de_controle", "diagnostico"])
        self.assertEqual(F[0].get("hub"), "certificar")

    def test_migracoes_fora_e_regra_dos_livros(self):
        T = C.ferramentas({})
        for e in ("modalidade", "absorver", "migracao_livros"):
            self.assertNotIn(e, T)
        regra = " ".join(" ".join(c) for c in T["regra_dos_livros"]["cmds"])
        self.assertIn("absorver_proibidos", regra); self.assertIn("registrar_do_estado_dos_motores", regra)
        fe = " ".join(" ".join(c) for c in T["fechamento"]["cmds"])
        for x in ("scripts/migracoes/", "migrar_nome_antigo", "scripts/restaurar_livros.py"):
            self.assertNotIn(x, fe)

    def test_ferramenta_sem_tempo_fica_para_a_proxima_passagem(self):
        orig = C.ferramentas
        C.ferramentas = lambda ctx: {"pncp": {"t": 600, "pular": None, "cmds": [["true"]]}}
        try:
            r = C.executar_etapa("motores", {}, 30)
        finally:
            C.ferramentas = orig
        self.assertEqual(r["ferramentas"][0]["uso"], "adiada")
