"""Sem cidade verificada não se elimina (titular, 17/10/2026): deve ser estadual. Só sai o município do interior de
outro estado com o NOME do município no texto (ou no endereço, quando o texto diz que o órgão é municipal)."""
import unittest

from src.repositorio_unico import municipal_fora_de_goias as MF

FICA = [
    {"titulo": "Chamamento Público Nº 005/2026", "orgao": "Prefeitura Municipal", "uf": "BA"},          # sem cidade
    {"titulo": "Edital da Câmara Municipal", "orgao": "Câmara Municipal", "uf": "RS"},                   # sem cidade
    {"titulo": "Prefeitura de Goiânia: chamamento para seleção", "uf": "BR"},                           # GO, UF "BR"
    {"titulo": "CHAMAMENTO PÚBLICO VISANDO CELEBRAR", "orgao": "MUNICIPIO DE PIRENOPOLIS", "uf": "BR"},  # GO sem acento
    {"titulo": "Aparecida de Goiânia — Diário Oficial de Aparecida de Goiânia", "uf": "BR"},
    {"titulo": "ABCR — Associação Brasileira de Captadores — oportunidades", "orgao": "ABCR",
     "url": "https://santaluziadoparua.ma.gov.br/x"},                                                   # fonte nacional
    {"titulo": "Querido Diário — diários oficiais municipais — oportunidades", "url": "https://arapongas.pr.gov.br/x", "uf": "PR"},
    {"titulo": "Seleção de projetos", "orgao": "Prefeitura Municipal de Salvador", "uf": "BA"},          # capital
    {"titulo": "Edital", "orgao": "Secretaria de Estado da Cultura", "uf": "SP"},                        # estadual
]
SAI = [
    {"titulo": "CHAMAMENTO PÚBLICO", "orgao": "MUNICIPIO DE INDAIATUBA", "uf": "SP"},
    {"titulo": "Diário Oficial de Iracemápolis (SP) 2026 — edital"},
    {"titulo": "Chamamento Público 02/2026", "orgao": "Prefeitura Municipal de Balsas", "uf": "MA"},
]


class CidadeVerificada(unittest.TestCase):
    def test_sem_cidade_goiano_nacional_capital_e_estadual_ficam(self):
        for c in FICA:
            self.assertIsNone(MF(c), c)

    def test_so_sai_o_municipio_de_outro_estado_com_o_nome_verificado(self):
        for c in SAI:
            self.assertTrue(MF(c), c)
