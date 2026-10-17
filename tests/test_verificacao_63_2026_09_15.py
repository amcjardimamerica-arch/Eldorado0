"""A verificacao de 15/09/2026 tem de estar no sistema, e as correcoes tem de valer.

Os 63 editais que o relatorio listava como nao verificados foram conferidos um a
um na fonte oficial. Dois resultados desta rodada nao podem se perder:

  CONANDA/MDHC 01/2026 — a RETIFICACAO publicada ao lado do edital prorrogou o
  envio de propostas de 17/09 para 11/10/2026 e elevou a abrangencia exigida de
  tres para cinco regioes. O sistema tinha a data velha.

  Fundacao Maria Emilia — o dominio antigo tem certificado invalido e o dominio
  vivo e mariaemilia.org.br. O edital FME Transforma 02/2026 vai ate 30/10/2026.
  Essa pendencia estava aberta desde 09/09 como "precisa de telefone".
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/dados/verificacao_63_2026-09-15.json"

# 16/10/2026 (titular): em outros estados só ESTADUAIS e CAPITAIS; o expurgo tirou da base os 26 registros municipais
# de fora de Goiás (20 às 00:56 e 6 às 11:00 UTC — estado/expurgo/2026-10-16.json). A identificação de cada um fica
# aqui para o teste conferir, com o portão de captação, que a saída foi pela regra e não por perda.
EXPURGADOS = {
    "8c6a2a0e25ff8b32702d": ("MUNICIPIO DE JARU", "RO"),
    "ccf2796183121fdbd963": ("MUNICIPIO DE JARU", "RO"),
    "2ba35f9a49970753e57d": ("MUNICIPIO DE IPU", "CE"),
    "0b2e6b2eabe51d022e5e": ("MUNICIPIO DE LAGOA VERMELHA", "RS"),
    "20ec3e11386b87af1e16": ("MUNICIPIO DE FARROUPILHA", "RS"),
    "bf89ef0c39788a84b9d1": ("MUNICIPIO DE GUAIRA", "PR"),
    "7c1d235d56365c9c24b4": ("IPOJUCA CAMARA MUNICIPAL", "PE"),
    "d297e885025d1befc94d": ("MUNICIPIO DE TRIUNFO", "RS"),
    "6110c2223fa6ce0f8e0e": ("MUNICIPIO DE GRAVATAI", "RS"),
    "97e10cdefb4a772fb529": ("MUNICIPIO DE GRAVATAI", "RS"),
    "ae150797cb8ff2c5fa0f": ("FUNDO MUNICIPAL DOS DIREITOS DA CRIANCA E DO ADOLESCENTE DE GUARAMIRIM", "SC"),
    "b8c90c7a8928773bd959": ("MUNICIPIO DE ROSARIO DO SUL", "RS"),
    "42d12155e382f973b4a6": ("MUNICIPIO DE PORTO FELIZ", "SP"),
    "d54cfaf8f5934750f912": ("MUNICIPIO DE GUAIRA", "PR"),
    "e59147d5c5bbf24f3208": ("BOM JESUS DO ITABAPOANA PREFEITURA", "RJ"),
    "f0808d006f8c34765c9a": ("MUNICIPIO DE ITATINGA", "SP"),
    "4e8961e172feb22c5227": ("MUNICIPIO DE MAMBORE", "PR"),
    "80283fe7346eec3fae05": ("MUNICIPIO DE ALVORADA", "RS"),
    "95ca296b9b2eb1502b2f": ("FUNDO MUNICIPAL DE ASSISTENCIA SOCIAL", "SC"),
    "eaa12d99fc473fb7ac68": ("MUNICIPIO DE VILA RICA", "MT"),
    "81a444690ae9d6a7fc56": ("MUNICIPIO DE OSORIO", "RS"),
    "30ec946c0da038e039cc": ("MUNICIPIO DE IBIAPINA", "CE"),
    "f1ca92b53138bf67e586": ("MUNICIPIO DE CARIRE", "CE"),
    "ddf352133bbf37885a89": ("MUNICIPIO DE QUIXERAMOBIM", "CE"),
    "5b2002af84d7311550c8": ("MUNICIPIO DE XANXERE", "SC"),
    "a36ee8a76017ea615080": ("MUNICIPIO DE RONDONOPOLIS", "MT"),
}


def base():
    return json.loads(BASE.read_text(encoding="utf-8"))


def municipal_de_fora(orgao: str, uf: str) -> bool:
    """O portão de captação (o mesmo que o expurgo usa) reprova pela regra territorial de 16/10."""
    from src.expurgo import classificar
    ruim, motivo = classificar({"titulo": orgao, "orgao": orgao, "uf": uf})
    return ruim and str(motivo).startswith("município de outro estado")


def registrado_no_expurgo(caminho: str) -> int:
    """Quanto os registros diários do expurgo dizem ter tirado deste arquivo (menos o que foi restaurado depois)."""
    n = 0
    for arq in sorted((ROOT / "estado/expurgo").glob("*.json")):
        r = json.loads(arq.read_text(encoding="utf-8"))
        n += int((r.get("registros_removidos_por_arquivo") or {}).get(caminho) or 0)
        n -= sum(1 for x in r.get("restaurados") or [] if x.get("arquivo") == caminho and not x.get("campo"))
    return n


class TesteBaseDaVerificacao(unittest.TestCase):
    def test_a_base_existe_e_tem_os_63(self):
        """O universo verificado em 15/09 continua 63: o que ficou mais o que o expurgo tirou."""
        d = base()
        self.assertEqual(d["total"], 63)
        saiu = (d.get("expurgo") or {}).get("ids") or []
        self.assertEqual(len(saiu), len(set(saiu)), "id repetido na contabilidade do expurgo")
        self.assertFalse(set(saiu) & set(d["itens"]), "registro dado como expurgado continua na base")
        self.assertEqual(len(d["itens"]) + len(saiu), 63)
        self.assertEqual(d["expurgo"]["removidos"], len(saiu))
        self.assertEqual(registrado_no_expurgo("docs/dados/verificacao_63_2026-09-15.json"), len(saiu),
                         "o registro diário do expurgo (estado/expurgo) tem de contar o mesmo que a base")

    def test_todo_ausente_saiu_pela_regra_territorial(self):
        """Nenhum dos 63 some sem motivo: cada ausente é municipal de outro estado, fora das capitais."""
        saiu = set(base()["expurgo"]["ids"])
        self.assertEqual(saiu, set(EXPURGADOS), "saída sem identificação conferida neste teste")
        for chave, (orgao, uf) in EXPURGADOS.items():
            self.assertNotEqual(uf, "GO", chave)
            self.assertTrue(municipal_de_fora(orgao, uf), f"{chave} ({orgao}/{uf}) não é municipal de fora de Goiás")
        # o portão não reprova qualquer coisa: Goiás, capital de outro estado e órgão estadual de fora ficam
        self.assertFalse(municipal_de_fora("MUNICIPIO DE GOIANIA", "GO"))
        self.assertFalse(municipal_de_fora("MUNICIPIO DE PORTO ALEGRE", "RS"))
        self.assertFalse(municipal_de_fora("SANTA CATARINA TRIBUNAL DE JUSTICA", "SC"))

    def test_resumo_bate_com_a_lista(self):
        d = base()
        vere = {}
        for item in d["itens"].values():
            vere[item["veredito"]] = vere.get(item["veredito"], 0) + 1
        self.assertEqual(vere, d["resumo"]["veredito"])

    def test_todo_registro_que_ficou_e_desta_verificacao(self):
        for chave, item in base()["itens"].items():
            self.assertEqual(item.get("verificado_em"), "2026-09-15", chave)

    def test_todo_item_declara_a_rota_e_a_observacao(self):
        for chave, item in base()["itens"].items():
            self.assertTrue(item.get("observacao"), chave)
            self.assertTrue(item.get("rota_usada"), chave)

    def test_nenhuma_data_sem_observacao_que_a_explique(self):
        """Data nula so vale com o motivo escrito — e a regra do nulo honesto."""
        for chave, item in base()["itens"].items():
            if not item.get("fim"):
                self.assertGreater(len(item.get("observacao") or ""), 40, chave)


class TesteCorrecoesQueNaoPodemSePerder(unittest.TestCase):
    def test_conanda_foi_prorrogado_para_onze_de_outubro(self):
        item = base()["itens"]["97292f2d3c686703e79e"]
        self.assertEqual(item["fim"], "2026-10-11",
                         "a retificacao do MDHC prorrogou de 17/09 para 11/10/2026")
        self.assertIn("RETIFICACAO", item["observacao"].upper())
        self.assertIn("11/10/2026", item["observacao"])
        self.assertEqual(item["veredito"], "aprovado")

    def test_fundacao_maria_emilia_com_o_dominio_vivo(self):
        item = base()["itens"]["0c3d1eb59b2a598a0393"]
        self.assertEqual(item["fim"], "2026-10-30")
        self.assertIn("mariaemilia.org.br", item["pagina_oficial"])
        self.assertNotIn("fundacaomariaemilia.org.br", item["pagina_oficial"])

    def test_ipu_fecha_um_dia_antes_do_que_a_base_tinha(self):
        """16/10: IPU/CE e municipal de fora de Goias — saiu pela regra territorial. Se voltar (mudanca de regra),
        volta com a correcao de prazo desta verificacao."""
        d = base()
        item = d["itens"].get("2ba35f9a49970753e57d")
        if item is None:
            self.assertIn("2ba35f9a49970753e57d", d["expurgo"]["ids"])
            self.assertTrue(municipal_de_fora("MUNICIPIO DE IPU", "CE"))
            return
        self.assertEqual(item["fim"], "2026-09-23")
        self.assertEqual(item["fim_anterior"], "2026-09-24")
        self.assertTrue(item["mudou_prazo"])

    def test_jaru_sao_dois_editais_diferentes(self):
        """16/10: os dois de Jaru/RO sairam juntos pela regra territorial; se voltarem, voltam como dois."""
        d = base()
        itens, ids = d["itens"], ("8c6a2a0e25ff8b32702d", "ccf2796183121fdbd963")
        presentes = [i for i in ids if i in itens]
        if not presentes:
            for i in ids:
                self.assertIn(i, d["expurgo"]["ids"])
            self.assertTrue(municipal_de_fora("MUNICIPIO DE JARU", "RO"))
            return
        self.assertEqual(len(presentes), 2, "os dois chamamentos de Jaru entram e saem juntos")
        self.assertNotEqual(itens[ids[0]]["fim"], itens[ids[1]]["fim"],
                            "196 e 197 sao chamamentos distintos, com prazos distintos")


class TesteLigacaoComAsRotinas(unittest.TestCase):
    """A base nova nao pode virar arquivo orfao, como aconteceu com a de 09/09."""

    def test_o_vigia_de_prazos_le_esta_base(self):
        from src import prazos
        nomes = [c.name for c in prazos.BASES_VERIFICADAS]
        self.assertIn("verificacao_63_2026-09-15.json", nomes)
        # A regra e "a mais recente vence", nao "a de 15/09 vence". Fixar o nome
        # da base de 15/09 aqui fez este teste quebrar em 23/09, quando o
        # fechamento novo — que corrige a chave de Osorio/RS — assumiu a frente.
        # O que se cobra e a ORDEM: da mais nova para a mais velha.
        datas = [re.search(r"(\d{4}-\d{2}-\d{2})", n) for n in nomes]
        datadas = [m.group(1) for m in datas if m]
        self.assertEqual(datadas, sorted(datadas, reverse=True),
                         f"bases fora de ordem de recencia: {nomes}")
        self.assertGreaterEqual(datadas[0], "2026-09-15",
                                "a verificacao mais recente tem de vencer as anteriores")

    def test_a_fila_de_pesquisa_le_esta_base(self):
        from src import abertos_sem_informacao
        nomes = [c.name for c in abertos_sem_informacao.BASES_VERIFICADAS]
        self.assertIn("verificacao_63_2026-09-15.json", nomes)

    def test_o_prazo_do_conanda_chega_ao_alarme(self):
        from datetime import date
        from src import prazos
        linhas = prazos._linhas_verificadas(date(2026, 9, 15), [30, 15, 7, 3, 1], set())
        # a chave pode vir completa (20 caracteres) ou truncada em 8, conforme a
        # base de origem: o vigia usa a chave como ela esta em cada arquivo
        conanda = [x for x in linhas if str(x["id"]).startswith("97292f2d")]
        self.assertTrue(conanda, "o CONANDA nao chegou ao vigia de prazos")
        self.assertEqual(conanda[0]["vencimento"], "2026-10-11")


class TesteCuradoriaDaRodada(unittest.TestCase):
    def test_as_duas_fontes_novas_entraram(self):
        from src import curadoria_fontes
        programas = {f.get("programa") for f in curadoria_fontes.carregar()["fontes_novas"]}
        self.assertIn("MDHC / CONANDA — Chamamentos publicos de fomento a OSC", programas)
        self.assertIn("Fundacao Maria Emilia — Edital FME Transforma", programas)

    def test_a_armadilha_do_amparo_legal_esta_registrada(self):
        from src import curadoria_fontes
        urls = " ".join(a.get("url", "") for a in curadoria_fontes.carregar()["armadilhas"])
        self.assertIn("amparoLegal", urls)

    def test_o_dominio_morto_da_maria_emilia_e_armadilha(self):
        from src import curadoria_fontes
        arm = [a for a in curadoria_fontes.carregar()["armadilhas"]
               if "fundacaomariaemilia" in a.get("url", "")]
        self.assertEqual(len(arm), 1, "o dominio morto tem de ter UMA armadilha, nao duas")
        self.assertIn("mariaemilia.org.br", arm[0]["motivo"],
                      "a armadilha tem de dizer qual e o dominio vivo")


if __name__ == "__main__":
    unittest.main()
