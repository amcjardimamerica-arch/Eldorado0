"""Organização das etapas (titular, 18/10/2026): menos coisas para dar problema, só o que resolve."""
import unittest

from src import comando as C


class OrganizacaoDasEtapas(unittest.TestCase):
    def setUp(self):
        self.F = C.fases({})
        self.E = [f["etapa"] for f in self.F]

    def test_migracoes_de_uma_vez_so_fora_do_fluxo(self):
        for e in ("modalidade", "absorver", "migracao_livros"):
            self.assertNotIn(e, self.E)
        fe = " ".join(" ".join(c) for f in self.F if f["etapa"] == "fechamento" for c in f["cmds"])
        for x in ("scripts/migracoes/", "migrar_nome_antigo", "scripts/restaurar_livros.py"):
            self.assertNotIn(x, fe)

    def test_catalogar_tem_a_regra_dos_livros(self):
        cat = " ".join(" ".join(c) for f in self.F if f["etapa"] == "catalogar" for c in f["cmds"])
        self.assertIn("absorver_proibidos", cat, "nenhum dado fora dos livros")
        self.assertIn("registrar_do_estado_dos_motores", cat, "toda oportunidade cria ou vincula um livro")

    def test_grupo_certificar_em_sequencia(self):
        g = [f["etapa"] for f in self.F if f.get("grupo") == "certificar"]
        self.assertEqual(g, ["catalogar", "site_oficial", "expurgo", "certificar", "curadoria", "validar", "livros",
                             "unir_livros", "biblioteca_diaria", "banco_unico", "fichas_farol"])
        i = self.E.index("catalogar")
        self.assertEqual(self.E[i:i + len(g)], g, "as etapas do Cartório rodam em sequência")
        self.assertLess(self.E.index("fichas_farol"), self.E.index("fechamento"))
