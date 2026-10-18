"""17/10/2026 (chat de testes, integração): falhas de integração e de funcionamento que o grafo de produção apontou.

1. acesso-mensal sem agendamento (a senha do mês deixou de ser enviada no dia 1º);
2. estado/saida_brasil.txt com texto fixo — o Git não via mudança e o arquivo parecia parado;
3. escada do Cartório (etapa 12): as abordagens 4 a 8 e 10 não eram alcançadas;
4. pilotos resgates e radar com a entrega parada.
Sem rede."""
import json, sys, tempfile, unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "scripts"))


def _wf(nome):
    d = yaml.safe_load((ROOT / ".github/workflows" / nome).read_text(encoding="utf-8"))
    return d, d.get("on", d.get(True))


class TesteFluxos(unittest.TestCase):
    def test_acesso_mensal_agendado_no_dia_1_e_reenvio_manual(self):
        _d, on = _wf("acesso-mensal.yml")
        crons = [c["cron"] for c in on.get("schedule") or []]
        self.assertEqual(len(crons), 1, "um agendamento mensal")
        minuto, hora, dia, mes, semana = crons[0].split()
        self.assertEqual((dia, mes, semana), ("1", "*", "*"), "todo dia 1º")
        self.assertIn("workflow_dispatch", on, "o reenvio manual continua")
        self.assertIn("motivo", on["workflow_dispatch"]["inputs"])

    def test_saida_brasil_e_gravada_com_a_hora_antes_do_registro(self):
        d, _on = _wf("monitoramento-diario.yml")
        passos = d["jobs"]["monitorar"]["steps"]
        i_saida = next(i for i, p in enumerate(passos) if "estado/saida_brasil.txt" in str(p.get("run") or ""))
        i_reg = next(i for i, p in enumerate(passos) if "gravar_somente_alterados.py aplicar" in str(p.get("run") or ""))
        self.assertLess(i_saida, i_reg, "o arquivo é gravado antes do registro do fluxo")
        run = passos[i_saida]["run"]
        self.assertIn("tee estado/saida_brasil.txt", run)
        self.assertIn("date -u", run, "leva a hora da saída: o conteúdo muda a cada execução")
        self.assertEqual(run.count("tee estado/saida_brasil.txt"), 1, "um só ponto de gravação")
        from gravar_somente_alterados import AREAS
        self.assertIn("estado", AREAS, "estado/ entra no registro do fluxo")


class TesteEscadaDoCartorio(unittest.TestCase):
    def _prio(self, op):
        fim = str(op.get("fim") or "")[:10]
        novo = str(op.get("descoberto_em") or "")[:10] >= (date.today() - timedelta(days=1)).isoformat()
        return (0 if novo else 1, 0 if op.get("_faltam") else 1, 0 if fim else 1, fim or "9999", len(op["_usadas"]))

    def test_quem_esta_na_escada_nao_fica_atras_de_todos_os_novos(self):
        from src import cartorio as C
        nunca = [{"id": f"n{i}", "_faltam": ["Valor"], "_usadas": []} for i in range(50)]
        escada = [{"id": f"e{i}", "_faltam": ["Valor"], "_usadas": [1]} for i in range(5)]
        fila = C.fila_justa(nunca + escada, self._prio)
        self.assertEqual(len(fila), 55)
        self.assertEqual({o["id"] for o in fila[:10] if o["_usadas"]}, {f"e{i}" for i in range(5)},
                         "as 5 da escada sobem um degrau nas primeiras vagas")
        sorted_antigo = sorted(nunca + escada, key=self._prio)
        self.assertFalse(any(o["_usadas"] for o in sorted_antigo[:50]), "regra antiga: a escada ficava atrás de todos")

    def test_classes_do_titular_continuam_valendo(self):
        from src import cartorio as C
        hoje = date.today().isoformat()
        novo = {"id": "novo", "_faltam": ["Valor"], "_usadas": [], "descoberto_em": hoje}
        so_conferir = {"id": "conf", "_faltam": [], "_usadas": [1, 2]}
        falta = {"id": "falta", "_faltam": ["Valor"], "_usadas": [1]}
        fila = C.fila_justa([so_conferir, falta, novo], self._prio)
        self.assertEqual([o["id"] for o in fila], ["novo", "falta", "conf"],
                         "achado do dia primeiro; quem tem item faltando antes de quem só confere")

    def test_revisao_repetida_nao_esgota_a_escada(self):
        from src import cartorio as C
        from src import cartorio_linha as LN
        h = [{"n": 1, "nome": "revisão manual (chrome)", "em": "2026-10-16T10:00:00+00:00"}] * 14
        op = {"_tipo": "estrela", "id": "x"}
        vez, _ant, usadas = C._vez(op, {"estrela:x": {"abordagens": h, "assinatura": C._assinatura(op)}},
                                   datetime(2026, 10, 17, 12, tzinfo=timezone.utc))
        self.assertTrue(vez, "14 entradas da mesma abordagem não são 10 abordagens")
        self.assertEqual(usadas, [1])
        self.assertEqual(LN.proxima_abordagem("sem_estrela", usadas)[:3], [4, 3, 10])
        c = LN.acumular({"abordagens": h, "itens": {}}, {"em": "t"}, 4, ["Valor"])
        self.assertEqual(c["tentativa"], 2, "a tentativa conta abordagens diferentes")
        self.assertFalse(c.get("esgotada"))

    def test_importar_a_mesma_revisao_de_novo_nao_soma_tentativa(self):
        import importar_revisao_abertas as I
        rev = [{"n": 1, "nome": "revisão manual (chrome_2026_10_17)", "em": "t2"}]
        ant = [{"n": 1, "nome": "documento na mão", "em": "t0"}, {"n": 4, "nome": "biblioteca de sites", "em": "t0"}]
        j = I.juntar_abordagens(ant, rev)
        self.assertEqual(len(j), 3)
        self.assertEqual(I.juntar_abordagens(j, rev), j, "reimportar a mesma revisão não muda a escada")
        outra = [{"n": 1, "nome": "revisão manual (chrome_2026_10_18)", "em": "t3"}]
        self.assertEqual(len(I.juntar_abordagens(j, outra)), 4, "uma revisão nova entra")

    def test_a_escada_chega_as_abordagens_4_a_8_e_10_sem_rede(self):
        """Simula 10 passagens (12 h entre elas) de uma oportunidade sem estrela, com material para todas as abordagens."""
        from src import cartorio as C
        from src import cartorio_linha as LN
        orig_doc, orig_cert = LN.documentos, C.certificar
        tmp = tempfile.TemporaryDirectory(); T = Path(tmp.name)
        nomes = ("PASTA", "CERTIDOES", "LIVROS_OUT", "INTERCEPTADOR", "RELATORIO", "GABARITOS")
        salvos = {k: getattr(C, k) for k in nomes}; bib0 = LN.BIBLIOTECA
        try:
            C.PASTA = T; C.CERTIDOES = T / "c.json"; C.LIVROS_OUT = T / "l.jsonl"; C.INTERCEPTADOR = T / "i.json"
            C.RELATORIO = T / "r.json"; C.GABARITOS = T / "g.json"; LN.BIBLIOTECA = T / "b.json"; C._CACHE.clear()
            LN.documentos = lambda n, op, *a, **k: ([{"url": f"https://www.x.go.gov.br/{n}", "degrau": 0, "como": "teste"}], {})
            C.certificar = lambda op, faltam, *a, **k: {"id": op["id"], "tipo": "livro", "titulo": "t", "itens": {}, "dispensas": {},
                                                         "documentos": [], "em": C._agora(), "link_oficial": None}
            catalogo = {"motores": [{"id": f"L{i}", "programa": f"Edital {i}/2026", "esteira": {"selo": "bronze", "doze_faltando": ["Valor"]}}
                                    for i in range(3)]}
            usadas = []
            for passagem in range(10):
                C.run(5, 60, C.Rede(baixar=lambda u: (b"", ""), permitido=lambda u: True, pausa=0), {"itens_por_uf": {}}, catalogo)
                certs = json.loads(C.CERTIDOES.read_text())["certidoes"]
                for c in certs.values():                      # 12 h depois
                    for h in c["abordagens"]:
                        h["em"] = (datetime.now(timezone.utc) - timedelta(hours=13)).isoformat()
                C.CERTIDOES.write_text(json.dumps({"certidoes": certs}))
            usadas = [h["n"] for h in certs["livro:L0"]["abordagens"]]
            self.assertEqual(sorted(usadas), list(range(1, 11)), "as 10 abordagens, cada uma uma vez")
            self.assertTrue(certs["livro:L0"].get("esgotada"))
        finally:
            LN.documentos, C.certificar = orig_doc, orig_cert
            for k, v in salvos.items():
                setattr(C, k, v)
            LN.BIBLIOTECA = bib0; C._CACHE.clear(); tmp.cleanup()


class TesteEntregasDosPilotos(unittest.TestCase):
    def test_interceptador_devolve_o_resultado_a_fila_de_resgate(self):
        from src import interceptador as I
        import src.missao_especial as ME
        chamadas = []
        orig_reg, orig_registro = ME.registrar_resgate, I.registro
        ME.registrar_resgate = lambda *a: chamadas.append(a) or {}
        I.registro = lambda _id: {"fim": "2026-11-30", "pagina_oficial": "https://www.goias.gov.br/edital"}
        try:
            I._devolver_a_fila({"id": "e1", "fila_id": "cat-1"}, {"campos": {}})
        finally:
            ME.registrar_resgate, I.registro = orig_reg, orig_registro
        self.assertEqual(len(chamadas), 1, "antes: TypeError engolido (faltava o argumento achou)")
        self.assertEqual(chamadas[0][0], "cat-1"); self.assertTrue(chamadas[0][2])

    def test_fila_de_resgate_remontada_e_publicada_a_cada_voo(self):
        src = (ROOT / "src/interceptador.py").read_text(encoding="utf-8")
        corpo_voo = src.split("def voo(ia)")[1].split("\ndef ")[0]
        corpo_rodada = src.split("def rodada(")[1].split("\ndef ")[0]
        self.assertIn("_remontar_resgates()", corpo_voo); self.assertIn("_remontar_resgates()", corpo_rodada)
        import src.missao_especial as ME
        tmp = tempfile.TemporaryDirectory(); T = Path(tmp.name)
        from src import livro_arquivo as LA
        salvos = (ME.FILA, ME.PARA_O_CLAUDE, ME.PUB, ME._acervo); ler0 = LA.ler_arquivo
        try:
            LA.ler_arquivo = lambda c, p=None: {} if "candidatas_do_catalogo" in str(c) else ler0(c, p)
            ME.FILA, ME.PARA_O_CLAUDE, ME.PUB = T / "f.json", T / "c.json", T / "p.json"
            ME._acervo = lambda: [{"id": "a1", "titulo": "Chamamento público de projetos culturais para OSC", "uf": "GO",
                                   "pagina_oficial": "https://www.goiania.go.gov.br/edital", "origem": "motor x"}]
            r = ME.remontar_e_publicar()
            pub = json.loads(ME.PUB.read_text())
        finally:
            ME.FILA, ME.PARA_O_CLAUDE, ME.PUB, ME._acervo = salvos; LA.ler_arquivo = ler0; tmp.cleanup()
        self.assertGreaterEqual(r["na_fila"], 1)
        self.assertIn("a1", [x["id"] for x in pub["fila"]], "o painel recebe a fila nova")

    def test_acervo_le_o_achados_dia_por_dias(self):
        import src.missao_especial as ME
        tmp = tempfile.TemporaryDirectory(); T = Path(tmp.name)
        (T / "docs/dados").mkdir(parents=True)
        (T / "docs/dados/achados_dia.json").write_text(json.dumps({"dias": {"2026-10-17": {"total": 1, "motores": {"Motor A": [
            {"id": "abc", "titulo": "Edital de fomento", "url": "https://x.go.gov.br/e", "uf": "GO", "fim": "2026-11-10"}]}}}}))
        root0 = ME.ROOT
        try:
            ME.ROOT = T
            ac = ME._acervo()
        finally:
            ME.ROOT = root0; tmp.cleanup()
        self.assertEqual([(a["id"], a["prazo"], a["origem"]) for a in ac], [("abc", "2026-11-10", "motor Motor A")])

    def test_radar_entra_no_registro_do_piloto(self):
        d, _on = _wf("piloto.yml")
        txt = (ROOT / ".github/workflows/piloto.yml").read_text(encoding="utf-8")
        linha = next(l for l in txt.splitlines() if l.strip().startswith("PILOTO_PATHS="))
        from src import radar_piloto as R
        self.assertIn(str(R.RADAR.relative_to(ROOT)), linha.split(), "o radar descoberto no voo é gravado")
        self.assertIn("docs/dados", linha.split())
        it = (ROOT / ".github/workflows/interceptador.yml").read_text(encoding="utf-8")
        self.assertGreaterEqual(it.count("docs/dados/resgates_piloto.json"), 2, "guardado antes do reset e gravado")


if __name__ == "__main__":
    unittest.main()
