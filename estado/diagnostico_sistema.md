# Diagnóstico do sistema · 2026-10-19 21:54 UTC

## Cumprimento da finalidade · índice geral 50%
- Motores: 58% (falha) — todo motor ativo lê dentro da sua cadência
- Maestro: 0% (falha) — cobertura completa do dia planejado
- Rede neural: 99% (ok) — discernimento (AUC) de pelo menos 0,85
- Biblioteca: 100% (ok) — toda oportunidade aberta aplicável com livro existente
- Validação: 24% (falha) — toda oportunidade aberta validada
- Site oficial: 71% (atencao) — toda aberta com site oficial
- Prazo: 30% (falha) — toda aberta com prazo (ou fluxo contínuo)
- Cartório: 66% (falha) — 12 de 12 itens certificados na fonte oficial
- Tela e fichas: 94% (atencao) — tudo que está aberto aparece na tela e tem ficha
- Integração: 10% (falha) — mesmas contagens e dados em dia em todos os sistemas
- Fluxos automáticos: 52% (falha) — todo fluxo agendado roda na cadência e sem falha
- Execução sem falha silenciosa: 0% (falha) — nenhuma etapa falha em silêncio

## Execução · fluxos: {'falha': 2, 'atrasado': 4, 'ok': 29, 'atencao': 7, 'manual': 2}
- 00 · Verificar prontidão: falha · última 2026-10-19T10:27 · sucesso 0% · cadência 24.0 h
- acesso-mensal: atrasado · última 2026-09-01T09:14 · sucesso 100% · cadência 24.0 h
- 35 · Alimentação diária externa (editais abertos): atencao · última 2026-10-18T13:31 · sucesso 40% · cadência 24.0 h
- 06 · Alimentação manual (arquivos e links do titular): atencao · última 2026-10-17T18:15 · sucesso 40% · cadência None h
- 05 · Busca ativa (a cada 3 dias): atencao · última 2026-10-15T17:32 · sucesso 10% · cadência None h
- 09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes: atrasado · última 2026-10-03T11:56 · sucesso 100% · cadência 24.0 h
- 10 · Histórico de doações da Rouanet (empresa por empresa) — retoma sozinho até completar: atencao · última 2026-10-15T16:09 · sucesso 25% · cadência None h
- 08 · Pacote do conselho (validação do Claude a cada 3 dias): atrasado · última 2026-10-16T11:47 · sucesso 100% · cadência 24.0 h
- 12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos: atencao · última 2026-10-19T21:43 · sucesso 0% · cadência 1.0 h
- 01 · Eldorado — motores por hora (00h–06h BRT): atencao · última 2026-10-18T13:08 · sucesso 60% · cadência 24.0 h
- 34 · Motores de empresas (semanal, com recuperação): atencao · última 2026-10-18T11:23 · sucesso 71% · cadência 24.0 h
- 03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês): falha · última 2026-10-19T18:37 · sucesso 20% · cadência 6.0 h
- 02 · Alexandria — revisão mensal de leis e procedimentos: atrasado · última 2026-10-01T10:36 · sucesso 50% · cadência 24.0 h
- falha silenciosa em motores-da-vez.yml: NameError: name 'fases' is not defined | NameError: name 'ferramentas' is not defined | Traceback (most recent call last):
- falha silenciosa em motor-agregadores.yml: "rede: robots.txt inacessível: URLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)" | "rede: robots.txt inacessível: URLError: timed out", | mapa: falhou
- falha silenciosa em monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-in

## Sala de controle · 36 indicadores · atualizada há 0.0 h
- divergências com a fonte: nenhuma
- sem leitura: nenhum
- estados incoerentes: nenhum
- sugestões de apresentação: ['decisões da titular (descartadas/inscritas aguardando aplicação e livros sinalizados para o Claude)']

## Oportunidades
- abertas: 234 · validadas: 55 (23.5%) · por estado: {'em_verificacao': 158, 'validada': 55, 'validacao_manual': 21}
- com livro: 234 · sem livro (problema): 0 · sem livro por regra: 0 {} · livro inexistente: 0
- sem site oficial: 69 · sem prazo: 164 · prazo vencido ainda aberta: 0
- fora da tela: 14 · sem ficha: 0
- itens que mais faltam: {'Prazo de recurso': 148, 'Anexos': 140, 'Requisitos': 136, 'Prazo de inscrição': 133, 'Valor': 131, 'Resultado': 129, 'Objeto': 125, 'Território': 125, 'Modalidade': 108, 'Área de atuação': 91, 'Órgão / financiador': 85, 'Esfera': 81}

## Sistemas
- motores: 25 funcionando · 18 em falha · 2 inativos · 0 com leitura parcial
  - em falha: Diário Oficial do Município de Goiânia — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:38
  - em falha: Diário Oficial da União — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:27
  - em falha: Câmara Municipal de Goiânia — processos legislativos, utilidade pública e chamamentos — falha — não lê há 1 dia(s) (40 h); última leitura 18/10 02:41
  - em falha: Congresso Nacional — Câmara, Senado e Comissão Mista de Orçamento (emendas, regras e chamamentos) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:38
  - em falha: PNCP — API de contratações (chamamentos e credenciamentos) — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:25
  - em falha: CNJ — destinação de prestações pecuniárias: busca no Portal do CNJ e regra nacional (Res. 558/2024) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:15
  - em falha: MP-GO — Programa Destina (cadastro de entidades para receber bens e valores de acordos) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:27
  - em falha: MPT-GO — editais de 5 dias para indicação de destinação de recursos ou bens (PRT 18ª Região) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:29
  - em falha: MPU — MPF, MPDFT, MPM e MPT nacional: destinação de bens e valores (com CNMP e FDD) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:29
  - em falha: Adaptador WordPress — sites oficiais pela API pública — falha — não lê há 1 dia(s) (38 h); última leitura 18/10 03:55
  - em falha: Adaptador Mapas Culturais — oportunidades com inscrição aberta — falha — não lê há 1 dia(s) (38 h); última leitura 18/10 03:54
  - em falha: GIFE — Grupo de Institutos, Fundações e Empresas — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:26
  - em falha: Lei Rouanet — janela de propostas no SALIC e projetos de Goiás (Ministério da Cultura) — falha — não lê há 1 dia(s) (38 h); última leitura 18/10 04:07
  - em falha: Prefeituras das 25 maiores cidades de Goiás — portais de editais — falha — não lê há 1 dia(s) (39 h); última leitura 18/10 03:49
  - em falha: Busca de empresas para FIA, Idoso, Lei de Incentivo ao Esporte, Pronas, Pronon e Goyazes — falha — não lê há 1 dia(s) (39 h); última leitura 18/10 03:26
  - em falha: CNPq / MCTI / Setec-MEC — chamadas com componente de extensão e parceria com OSC — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:29
  - em falha: Oportunidade Estaduais Governamentais de Goiás — falha — não lê há 1 dia(s) (40 h); última leitura 18/10 01:56
  - em falha: Piloto - Interceptador — comprova na fonte oficial — falha — não lê há 2 dia(s) (58 h); última leitura 17/10 08:29
- maestro: cobertura 0.0% · esgotados 0
- rede neural: AUC 0.843 · rotulados 1699 · treinada em 2026-10-14T05:54:08+00:00
- Cartório: 0.6646 certificado · fluxos do GitHub com falha: []
- saúde: 8 alerta(s) · índice da sala de controle: 49

## Integração
- contagens: {'repositorio_abertas': 234, 'diagnostico_abertas': 234, 'tela_cartoes': 224, 'fichas': 243, 'sala_controle_abertas': 234}
- idade (h): {'repositorio': 0.0, 'fluxo': 42.0, 'fichas': 0.0, 'sala_controle': 0.0, 'status_motores': 0.0, 'maestro': 4.7, 'rede_neural': 42.0, 'saude': 32.6}
- decisões da titular: 0 · não aplicadas: 0

## Problemas (49)
- [alta] o comando único não fecha um ciclo há 20.3 h (passa a cada 30 min) → investigar o fluxo 22 (sem correção automática)
- [alta] 3 etapa(s) falharam em silêncio na última execução de motores-da-vez.yml: NameError: name 'fases' is not defined | NameError: name 'ferramentas' is not defined | Traceback (most recent call last): → investigar a etapa (sem correção automática)
- [alta] 3 etapa(s) falharam em silêncio na última execução de motor-agregadores.yml: "rede: robots.txt inacessível: URLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)" | "rede: robots.txt inacessível: URLError: timed out", | mapa: falhou → investigar a etapa (sem correção automática)
- [alta] 8 etapa(s) falharam em silêncio na última execução de monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu → investigar a etapa (sem correção automática)
- [alta] fluxo '00 · Verificar prontidão' falhou nas últimas execuções (0% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] fluxo '03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês)' falhou nas últimas execuções (20% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] 14 abertas no repositório que não aparecem na tela de oportunidades → refazer a tela
- [alta] motor em falha: Diário Oficial do Município de Goiânia — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:38 → investigar o motor (sem correção automática)
- [alta] motor em falha: Diário Oficial da União — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:27 → investigar o motor (sem correção automática)
- [alta] motor em falha: Câmara Municipal de Goiânia — processos legislativos, utilidade pública e chamamentos — falha — não lê há 1 dia(s) (40 h); última leitura 18/10 02:41 → investigar o motor (sem correção automática)
- [alta] motor em falha: Congresso Nacional — Câmara, Senado e Comissão Mista de Orçamento (emendas, regras e chamamentos) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:38 → investigar o motor (sem correção automática)
- [alta] motor em falha: PNCP — API de contratações (chamamentos e credenciamentos) — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:25 → investigar o motor (sem correção automática)
- [alta] motor em falha: CNJ — destinação de prestações pecuniárias: busca no Portal do CNJ e regra nacional (Res. 558/2024) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:15 → investigar o motor (sem correção automática)
- [alta] motor em falha: MP-GO — Programa Destina (cadastro de entidades para receber bens e valores de acordos) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:27 → investigar o motor (sem correção automática)
- [alta] motor em falha: MPT-GO — editais de 5 dias para indicação de destinação de recursos ou bens (PRT 18ª Região) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:29 → investigar o motor (sem correção automática)
- [alta] motor em falha: MPU — MPF, MPDFT, MPM e MPT nacional: destinação de bens e valores (com CNMP e FDD) — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:29 → investigar o motor (sem correção automática)
- [alta] motor em falha: Adaptador WordPress — sites oficiais pela API pública — falha — não lê há 1 dia(s) (38 h); última leitura 18/10 03:55 → investigar o motor (sem correção automática)
- [alta] motor em falha: Adaptador Mapas Culturais — oportunidades com inscrição aberta — falha — não lê há 1 dia(s) (38 h); última leitura 18/10 03:54 → investigar o motor (sem correção automática)
- [alta] motor em falha: GIFE — Grupo de Institutos, Fundações e Empresas — falha — não lê há 1 dia(s) (42 h); última leitura 18/10 00:26 → investigar o motor (sem correção automática)
- [alta] motor em falha: Lei Rouanet — janela de propostas no SALIC e projetos de Goiás (Ministério da Cultura) — falha — não lê há 1 dia(s) (38 h); última leitura 18/10 04:07 → investigar o motor (sem correção automática)
- [alta] motor em falha: Prefeituras das 25 maiores cidades de Goiás — portais de editais — falha — não lê há 1 dia(s) (39 h); última leitura 18/10 03:49 → investigar o motor (sem correção automática)
- [alta] motor em falha: Busca de empresas para FIA, Idoso, Lei de Incentivo ao Esporte, Pronas, Pronon e Goyazes — falha — não lê há 1 dia(s) (39 h); última leitura 18/10 03:26 → investigar o motor (sem correção automática)
- [alta] motor em falha: CNPq / MCTI / Setec-MEC — chamadas com componente de extensão e parceria com OSC — falha — não lê há 1 dia(s) (41 h); última leitura 18/10 01:29 → investigar o motor (sem correção automática)
- [alta] motor em falha: Oportunidade Estaduais Governamentais de Goiás — falha — não lê há 1 dia(s) (40 h); última leitura 18/10 01:56 → investigar o motor (sem correção automática)
- [alta] motor em falha: Piloto - Interceptador — comprova na fonte oficial — falha — não lê há 2 dia(s) (58 h); última leitura 17/10 08:29 → investigar o motor (sem correção automática)
- [alta] tela mostra 224 oportunidades e o repositório conta 234 → refazer a tela
- [alta] 3 módulos de teste em quarentena por DEFEITO REAL → corrigir o código e tirar da quarentena (sem correção automática)
- [media] fluxo sem atualização há 42.0 h (limite 3 h) → refazer a tela
- [media] maestro sem atualização há 4.7 h (limite 3 h) → ver o fluxo que gera este dado
- [media] rede_neural sem atualização há 42.0 h (limite 26 h) → ver o fluxo que gera este dado
- [media] saude sem atualização há 32.6 h (limite 26 h) → refazer a saúde
- [media] [decidir] motores escolhidos para ler na passagem: 125 de 125 contrariam a regra — todo motor pendente ou parcial com tentativa sobrando entra na passagem (sem agenda) → investigar o comando (sem correção automática)
- [media] fluxo 'acesso-mensal' sem rodar há 1164.7 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] fluxo '09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes' sem rodar há 394.0 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] fluxo '08 · Pacote do conselho (validação do Claude a cada 3 dias)' sem rodar há 82.1 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] fluxo '02 · Alexandria — revisão mensal de leis e procedimentos' sem rodar há 443.3 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] 53 livros municipais de outros estados no catálogo (só Goiás tem livros municipais) → refazer a tela
- [media] 90 página(s)/documento(s) fora da fila após 5 erros iguais → corrigir a rota ou ler no Chrome (sem correção automática)
- [media] saúde · claude: 239 item(ns) esperando a análise do Claude (próxima: 2026-10-18) → ver o fluxo/arquivo indicado
- [media] saúde · coerência: mapa e lista divergem em GO, __nac__, PR, ES, RJ → refazer tela e indicadores
- [media] saúde · gerador: o gerador principal do painel falhou depois da última geração → ver o fluxo/arquivo indicado
- [media] saúde · livros_do_sistema: 4 livro(es) duplicado(s) no catálogo → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 00 · Verificar prontidão: últimas 5 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos: últimas 4 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 22 · Motores da vez — cada passagem calcula sozinha o que está pendente (agenda + maestro): últimas 4 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês): últimas 5 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] 69 abertas ainda sem site oficial → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 164 abertas sem prazo de inscrição conhecido → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 18 módulos de teste em quarentena (envelhecidos) → atualizar o teste à regra atual (sem correção automática)

## Workflow (estrutura de 15/10)
- comando único: 0 ciclo(s) hoje · 48 vermelho(s) · 0 etapa(s) com erro · fases puladas {}
- cobertura do dia: 0.0% de 125 motores
- retentativa: {'aguardando_retentativa': 1201, 'fora_da_fila': 90, 'fora_da_fila_por_escopo': {'outras-oportunidades-1': 4, 'outras-oportunidades-6': 5, 'recorrencia': 4, 'outras-oportunidades-5': 5, 'outras-oportunidades-8': 3, 'outras-oportunidades-3': 4, 'f260-captacao-044': 1, 'outras-oportunidades-2': 3, 'plat-empresas-editais-incentivados': 2, 'f260-captacao-238': 2, 'cartorio': 46, 'outras-oportunidades-7': 3, 'f260-captacao-242': 1, 'f260-captacao-224': 1, 'empresas-incentivadas': 1, 'f260-espalhado-sistema-mirassoldoeste-mt-gov-br': 1, 'f260-captacao-218': 1, 'f260-captacao-113': 3}, 'regra': 'volta em 30 min; sai após 5 tentativas com o mesmo erro'} · leitura parcial na fila: 1054
- curadoria do link oficial: {'em curadoria': 74, 'reprovado': 50, 'aprovado': 40, 'sem link oficial': 26}
- validação por exceção: trava fechada: acerto do Cartório 77.4% < 85.0% — candidatas vão à frente da conferência humana
- auditorias: {'gabarito_do_cartorio': {'em': '2026-10-15T19:53:25+00:00', 'acerto_pct': 77.4, 'documentos_lidos': 142}, 'varredura_referencia': '2026-10-01_2026-10-15', 'robots': {'em': '2026-10-15T10:07:53+00:00', 'motores_com_bloqueio': 5}, 'ponte': {'ponte_ok': 7, 'direto_ok': 5, 'so_pela_ponte': ['ALEGO · SPL (proposições)', 'MPGO'], 'nenhum': ['TJGO · portal'], 'total': 8}}
- legislativo: {'atualizado_em': '2026-10-19T01:36:02+00:00', 'proposicoes': 11}

## Decisões do Eldorado: agiu como deveria?
- decidir · motores escolhidos para ler na passagem: **incorreto** (125 de 125) — regra: todo motor pendente ou parcial com tentativa sobrando entra na passagem (sem agenda) · ex.: plat-piloto-aberto; pncp-api
- qualificar · oportunidades abertas para associação: **correto** (0 de 234) — regra: pregão, registro de preços, credenciamento de prestadores, contratação de empresa, OS da saúde e seleção de pessoal não são oportunidade (ruído ou acompanhar)
- legislativo · atos legislativos fora das oportunidades: **correto** (0 de 234) — regra: projeto de lei, utilidade pública e orçamento vão ao acompanhamento legislativo, nunca às abertas
- prazo · oportunidades contadas como abertas: **correto** (0 de 234) — regra: prazo vencido sai das abertas
- site_oficial · link oficial gravado no repositório: **correto** (0 de 165) — regra: agregador ou replicador nunca é link oficial
- certificar · itens certificados pelo Cartório: **correto** (0 de 2706) — regra: todo item certificado tem trecho literal e documento
- validar · validação por exceção: **correto** (0 de 0) — regra: só valida sozinho com acerto do Cartório ≥ 85% no gabarito e link oficial aprovado na curadoria
- farol · oportunidades prontas para o Farol: **correto** (0 de 17) — regra: pronta só com prazo vigente e link oficial aprovado na curadoria
- biblioteca · livros da Biblioteca: **correto** (0 de 2539) — regra: ato legislativo não gera livro
