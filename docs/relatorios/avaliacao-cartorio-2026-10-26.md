# Avaliação do Cartório com gabarito — 2026-10-26 16:20 UTC

Casos comprovados: **74** · documentos lidos: **50** · acerto geral: **68.6%** (precisão 86.6%) sobre 350 itens medidos.

Acerto = achou e confere ÷ (acerto + erro + falta). Precisão = acerto ÷ (acerto + erro). 'Fora' = o trecho do gabarito não está no documento lido (não conta contra a regra). 'Sem texto' = documento não lido.

| Item | Acerto | Precisão | Acertos | Erros | Faltas | Fora | Sem texto |
|---|---|---|---|---|---|---|---|
| Objeto | 62.8% | 84.4% | 27 | 5 | 11 | 2 | 24 |
| Prazo de inscrição | 47.4% | 75.0% | 18 | 6 | 14 | 6 | 20 |
| Resultado | 50.0% | 86.7% | 13 | 2 | 11 | 3 | 13 |
| Prazo de recurso | 95.5% | 95.5% | 21 | 1 | 0 | 4 | 11 |
| Valor | 92.3% | 96.0% | 24 | 1 | 1 | 4 | 15 |
| Órgão / financiador | 75.7% | 90.3% | 28 | 3 | 6 | 2 | 19 |
| Território | 62.9% | 84.6% | 22 | 4 | 9 | 0 | 15 |
| Esfera | 71.4% | 83.3% | 25 | 5 | 5 | 0 | 17 |
| Requisitos | 48.3% | 66.7% | 14 | 7 | 8 | 4 | 12 |
| Anexos | 69.2% | 90.0% | 18 | 2 | 6 | 5 | 12 |
| Modalidade | None% | None% | 0 | 0 | 0 | 0 | 0 |
| Área de atuação | 90.9% | 96.8% | 30 | 1 | 2 | 0 | 16 |

## Documentos não lidos

- ?: 7
- erro_rede: RemoteDisconnected: 7
- erro_rede: HTTPError: 3
- pdf_corrompido: 1
- robots_proibe: 1
- pagina_vazia: 1
- pdf_escaneado: 1
- zip_sem_pdf: 1
- formato_desconhecido: 1
- erro_rede: URLError: 1

## Causas das falhas por item

**Objeto**
- 11× falta: a seção do item não tem título reconhecido (numeração ou nome fora do padrão)
- 1× erro: pegou outro trecho (página 15); o certo está na página 1
- 1× erro: pegou outro trecho (página 3); o certo está na página 1
- 1× erro: pegou outro trecho (página 14); o certo está na página 1
- 1× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- 1× erro: pegou outro trecho (página 14); o certo está na página 9

**Prazo de inscrição**
- 14× falta: datas do período não estão junto da palavra de inscrição/recebimento (cronograma em tabela ou rótulo diferente)
- 6× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)

**Resultado**
- 11× falta: o cronograma usa outro rótulo ou o prazo vem por extenso/sem a palavra-chave perto do número
- 1× erro: pegou outro trecho (página 3); o certo está na página 4
- 1× erro: pegou outro trecho (página 7); o certo está na página 5

**Prazo de recurso**
- 1× erro: pegou outro trecho (página 17); o certo está na página 9

**Valor**
- 1× erro: pegou outro trecho (página 40); o certo está na página 1
- 1× falta: o valor não vem com 'valor global/total/teto' perto do R$ e não tem milhar com ponto

**Órgão / financiador**
- 6× falta: o órgão não está na 1ª página com prefixo conhecido (Prefeitura, Secretaria, Ministério…)
- 3× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)

**Território**
- 9× falta: regra não reconheceu o trecho que está no documento
- 4× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)

**Esfera**
- 5× falta: regra não reconheceu o trecho que está no documento
- 4× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- 1× erro: pegou outro trecho (página 1); o certo está na página 13

**Requisitos**
- 8× falta: a seção do item não tem título reconhecido (numeração ou nome fora do padrão)
- 3× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- 2× erro: pegou outro trecho (página 3); o certo está na página 2
- 1× erro: pegou outro trecho (página 3); o certo está na página 4
- 1× erro: pegou outro trecho (página 4); o certo está na página 5

**Anexos**
- 6× falta: regra não reconheceu o trecho que está no documento
- 1× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- 1× erro: pegou outro trecho (página 9); o certo está na página 14

**Área de atuação**
- 2× falta: regra não reconheceu o trecho que está no documento
- 1× erro: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)

## Exemplos (até 3 por item)

- **Órgão / financiador** (falta) · caso `c9cef45043042a48d03c` · https://www.contrafluxofestival.com.br/wp-content/uploads/2026/10/CONVOCATORIA-PARA-ORGANIZACOES-SOCIAIS.pdf  
  gabarito: Festival ContraFluxo — Trópico Audiovisual Ltda. (projeto cultural incentivado) (p. 1)  
  extraído: — (p. —)  
  causa: o órgão não está na 1ª página com prefixo conhecido (Prefeitura, Secretaria, Ministério…)
- **Território** (falta) · caso `c9cef45043042a48d03c` · https://www.contrafluxofestival.com.br/wp-content/uploads/2026/10/CONVOCATORIA-PARA-ORGANIZACOES-SOCIAIS.pdf  
  gabarito: Curitiba/PR — sede ou atuação comprovada e continuada no município (p. 3)  
  extraído: — (p. —)  
  causa: regra não reconheceu o trecho que está no documento
- **Requisitos** (falta) · caso `c9cef45043042a48d03c` · https://www.contrafluxofestival.com.br/wp-content/uploads/2026/10/CONVOCATORIA-PARA-ORGANIZACOES-SOCIAIS.pdf  
  gabarito: PJ de direito privado sem fins lucrativos (associação, instituto, fundação, OSC) com atuação comprovável no tema; inscrição por formulário c (p. 2)  
  extraído: — (p. —)  
  causa: a seção do item não tem título reconhecido (numeração ou nome fora do padrão)
- **Órgão / financiador** (erro) · caso `097bcd4b298c7e73615e` · https://www.gov.br/ibama/pt-br/assuntos/notas/2026/edital-de-chamamento-publico-seleciona-organizacao-para-executar-aplicacao-de-recursos-do-fundo-rio-doce/20260923_SEI_Ibama_28844023_Edital_3.pdf  
  gabarito: Ibama — recursos privados do Fundo Rio Doce (p. 1)  
  extraído: INSTITUTO BRASILEIRO DO MEIO AMBIENTE E DOS RECURSOS NATURAIS RENOVÁVEIS (p. 1)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Território** (falta) · caso `097bcd4b298c7e73615e` · https://www.gov.br/ibama/pt-br/assuntos/notas/2026/edital-de-chamamento-publico-seleciona-organizacao-para-executar-aplicacao-de-recursos-do-fundo-rio-doce/20260923_SEI_Ibama_28844023_Edital_3.pdf  
  gabarito: Execução na Bacia do Rio Doce (MG e ES); OSC de qualquer UF (p. 23)  
  extraído: — (p. —)  
  causa: regra não reconheceu o trecho que está no documento
- **Anexos** (falta) · caso `097bcd4b298c7e73615e` · https://www.gov.br/ibama/pt-br/assuntos/notas/2026/edital-de-chamamento-publico-seleciona-organizacao-para-executar-aplicacao-de-recursos-do-fundo-rio-doce/20260923_SEI_Ibama_28844023_Edital_3.pdf  
  gabarito: Anexos I a V (declaração de ciência, relação de dirigentes, roteiro da proposta, minuta do instrumento, modelo de plano de trabalho) (p. 9)  
  extraído: — (p. —)  
  causa: regra não reconheceu o trecho que está no documento
- **Órgão / financiador** (erro) · caso `b06dc0bf0fa9f50b01ba` · https://pncp.gov.br/pncp-api/v1/orgaos/24134488000108/compras/2027/3/arquivos/2  
  gabarito: UNIVERSIDADE FEDERAL DE PERNAMBUCO — PREFEITURA DA CIDADE UNIVERSITARIA DA UFPE (p. 1)  
  extraído: Município de Recife (p. 1)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Esfera** (erro) · caso `b06dc0bf0fa9f50b01ba` · https://pncp.gov.br/pncp-api/v1/orgaos/24134488000108/compras/2027/3/arquivos/2  
  gabarito: F (Federal) (p. None)  
  extraído: municipal (p. 1)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Esfera** (erro) · caso `1f6f8ec7518f17718fc9` · https://pncp.gov.br/pncp-api/v1/orgaos/20260121000180/compras/2026/1/arquivos/1  
  gabarito: M (Municipal) (p. None)  
  extraído: privada (p. 1)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Resultado** (erro) · caso `52a1fdf5d0e54202eeb0` · https://pncp.gov.br/pncp-api/v1/orgaos/10648539000105/compras/2025/3/arquivos/1  
  gabarito: Comissão publica a lista de habilitadas/inabilitadas após a análise; homologação pelo Diretor-Geral (credenciamento contínuo, sem data única (p. 4)  
  extraído: lista de credenciadas que será publicada e mantida atualizada no portal do IFSULDEMINAS - Campus Inconfidentes, para cadastramento permanente de novos interessados, nos termos do art. (p. 3)  
  causa: pegou outro trecho (página 3); o certo está na página 4
- **Território** (erro) · caso `52a1fdf5d0e54202eeb0` · https://pncp.gov.br/pncp-api/v1/orgaos/10648539000105/compras/2025/3/arquivos/1  
  gabarito: Pouso Alegre/MG (p. None)  
  extraído: no Estado de Minas Gerais (p. 9)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Resultado** (falta) · caso `6e7349afbef4f1ca58af` · https://pncp.gov.br/pncp-api/v1/orgaos/00509018000113/compras/2025/981/arquivos/3  
  gabarito: conforme trecho do edital (p. 5)  
  extraído: — (p. —)  
  causa: o cronograma usa outro rótulo ou o prazo vem por extenso/sem a palavra-chave perto do número
- **Prazo de inscrição** (falta) · caso `332e8f675e56e5916eed` · https://data.queridodiario.ok.org.br/3305158/2026-09-22/89d032417f88818ceb76b2715c0457c04116affb.pdf  
  gabarito: 24/09/2026 (republicação) a 26/10/2026 (p. 5)  
  extraído: — (p. —)  
  causa: datas do período não estão junto da palavra de inscrição/recebimento (cronograma em tabela ou rótulo diferente)
- **Resultado** (falta) · caso `332e8f675e56e5916eed` · https://data.queridodiario.ok.org.br/3305158/2026-09-22/89d032417f88818ceb76b2715c0457c04116affb.pdf  
  gabarito: Preliminar 05/11/2026; homologação 01/12/2026 (p. 5)  
  extraído: — (p. —)  
  causa: o cronograma usa outro rótulo ou o prazo vem por extenso/sem a palavra-chave perto do número
- **Requisitos** (erro) · caso `332e8f675e56e5916eed` · https://data.queridodiario.ok.org.br/3305158/2026-09-22/89d032417f88818ceb76b2715c0457c04116affb.pdf  
  gabarito: OSC sem fins lucrativos, finalidade compatível, experiência prévia; estatuto, ata, CNPJ, certidões, declarações MROSC e plano de trabalho vi (p. 4)  
  extraído: Poderão participar do presente Chamamento (p. 3)  
  causa: pegou outro trecho (página 3); o certo está na página 4
- **Requisitos** (falta) · caso `6304cd5b5ce07ac96cdf` · https://ufsj.edu.br/portal2-repositorio/File/centrocultural/Edital%20de%20Galerias%202027.pdf  
  gabarito: Só pessoas físicas autoras das obras (ou representante de proposta coletiva) (p. 1)  
  extraído: — (p. —)  
  causa: a seção do item não tem título reconhecido (numeração ou nome fora do padrão)
- **Prazo de inscrição** (erro) · caso `64efa7e36bef2f9468d1` · https://santabarbara.pa.gov.br/wp-content/uploads/2026/10/Edital-no-102026-PNAB-Santa-Barbara-do-Para.pdf  
  gabarito: 07/10/2026 8h a 25/10/2026 17h, por formulário eletrônico (reaberto/republicado; o DOU anterior indicava 16/10) (p. 2)  
  extraído: até 07 de outubro de 2026 (p. 2)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Esfera** (erro) · caso `64efa7e36bef2f9468d1` · https://santabarbara.pa.gov.br/wp-content/uploads/2026/10/Edital-no-102026-PNAB-Santa-Barbara-do-Para.pdf  
  gabarito: Municipal (recursos federais PNAB) (p. 1)  
  extraído: estadual (p. 1)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Objeto** (falta) · caso `743a5444299dcb88b228` · https://aderes.es.gov.br/edital-de-chamamento-publico-no-108-2026-selecao-de-organizacao-da-sociedade-civil-osc-especializada-na-prestacao-de-servicos-de-capacitacao-presencial-em-gestao-empresarial-para-a-execucao-do-projeto-colibris-2026  
  gabarito: Edital ADERES 108/2026: seleção de OSC especializada em capacitação presencial em gestão empresarial para o Projeto Colibris 2026 (p. 1)  
  extraído: — (p. —)  
  causa: a seção do item não tem título reconhecido (numeração ou nome fora do padrão)
- **Objeto** (falta) · caso `a98c4d91f7500fe564d2` · https://www.mapfre.com.br/media/edital-mapfre-2026-informacoes-vf.pdf  
  gabarito: Edital Mapfre 2026 de patrocínio a projetos já aprovados em leis de incentivo (janela ainda aberta: PRONAS/PCD e PRONON) (p. 3)  
  extraído: — (p. —)  
  causa: a seção do item não tem título reconhecido (numeração ou nome fora do padrão)
- **Prazo de inscrição** (erro) · caso `a98c4d91f7500fe564d2` · https://www.mapfre.com.br/media/edital-mapfre-2026-informacoes-vf.pdf  
  gabarito: PRONAS e PRONON: 11/05 a 15/12/2026 (cultura, esporte, FIA, Idoso e reciclagem fecharam em 30/09/2026) (p. 15)  
  extraído: 11/05/2026 a 30/09/2026 (p. 15)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Objeto** (falta) · caso `d94cd9a3d245f2393f2f` · https://www.fundobrasil.org.br/edital/apoio-emergencial-defensores-de-direitos-humanos/  
  gabarito: Medidas de proteção a defensores de DH, familiares e organizações (p. 1)  
  extraído: — (p. —)  
  causa: a seção do item não tem título reconhecido (numeração ou nome fora do padrão)
- **Prazo de recurso** (erro) · caso `6d06351ee0a98f70bf95` · https://institutogenesio.org.br/wp-content/uploads/2026/10/Edital-Nao-Incentivado-Instituto-Genesio-A-Mendes-2026.pdf  
  gabarito: 04/12/2026 (p. 9)  
  extraído: 15 dias (p. 17)  
  causa: pegou outro trecho (página 17); o certo está na página 9
- **Anexos** (falta) · caso `6d06351ee0a98f70bf95` · https://institutogenesio.org.br/wp-content/uploads/2026/10/Edital-Nao-Incentivado-Instituto-Genesio-A-Mendes-2026.pdf  
  gabarito: Modelo de projeto (item 4); Anexo III – comprovante de gratuidade; modelos de relatório de prestação de contas e de recibo (p. 7)  
  extraído: — (p. —)  
  causa: regra não reconheceu o trecho que está no documento
- **Valor** (erro) · caso `0dfc53b2787c26812fd2` · https://pncp.gov.br/pncp-api/v1/orgaos/13950733000139/compras/2026/2/arquivos/1  
  gabarito: R$ 5.814,18 (p. 1)  
  extraído: R$ 4.086,00 (quatro mil e oitenta e seis reais) (p. 40)  
  causa: pegou outro trecho (página 40); o certo está na página 1
- **Anexos** (erro) · caso `e1a46fb1b974d54599f6` · https://pncp.gov.br/pncp-api/v1/orgaos/51174001000193/compras/2025/260/arquivos/2  
  gabarito: Anexo I – TERMO DE REFER NCIA (Lei n∫ 14; Anexo II – RelaÁ„o de ImÛveis CÛdigo ImÛv CÛdigo; Anexo III – PLANO DE TRABALHO I - PartÌcipes: TR (p. 21)  
  extraído: ANEXO I TERMO DE REFER˚NCIA; ANEXO II Relaçªo de Imóveis; ANEXO III PLANO DE TRABALHO; ANEXO IV - Estimativa diÆria de resíduos reciclÆveis (p. 21)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Área de atuação** (erro) · caso `a8b026eec92ee050dabe` · https://pncp.gov.br/pncp-api/v1/orgaos/12473062000108/compras/2024/121/arquivos/1  
  gabarito: Meio ambiente (p. 1)  
  extraído: Cultura (p. 1)  
  causa: pegou o trecho certo da região, mas o valor não confere (formato, intervalo ou item vizinho)
- **Área de atuação** (falta) · caso `9b629429aba64de24cec` · https://pncp.gov.br/pncp-api/v1/orgaos/00509968000148/compras/2024/969/arquivos/1  
  gabarito: Meio ambiente (p. 2)  
  extraído: — (p. —)  
  causa: regra não reconheceu o trecho que está no documento
- **Área de atuação** (falta) · caso `b24cea7e537e90571411` · https://crefito4.org.br/site/wp-content/uploads/2026/02/Edital-de-chamamento-publico-de-22-de-janeiro-de-2026.pdf  
  gabarito: Desenvolvimento profissional e científico da Fisioterapia e da Terapia Ocupacional (p. 1)  
  extraído: — (p. —)  
  causa: regra não reconheceu o trecho que está no documento
- **Valor** (falta) · caso `6d4e30ab99202f86a24d` · https://www.gov.br/mdh/pt-br/assuntos/noticias/2026/defeso-eleitoral/outubro/prazo-de-inscricoes-e-prorrogado-para-edital-do-conanda-e-da-sndca-que-preve-parcerias-com-organizacoes-da-sociedade-civil  
  gabarito: R$ 6 milhões no total, até R$ 1 milhão por projeto (p. 1)  
  extraído: — (p. —)  
  causa: o valor não vem com 'valor global/total/teto' perto do R$ e não tem milhar com ponto
