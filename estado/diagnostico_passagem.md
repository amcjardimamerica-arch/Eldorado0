# Diagnóstico do sistema · 2026-10-18 02:06 UTC

## Cumprimento da finalidade · índice geral 70%
- Motores: 100% (ok) — todo motor ativo lê dentro da sua cadência
- Maestro: 80% (atencao) — cobertura completa do dia planejado
- Rede neural: 99% (ok) — discernimento (AUC) de pelo menos 0,85
- Biblioteca: 99% (ok) — toda oportunidade aberta aplicável com livro existente
- Validação: 27% (falha) — toda oportunidade aberta validada
- Site oficial: 59% (falha) — toda aberta com site oficial
- Prazo: 33% (falha) — toda aberta com prazo (ou fluxo contínuo)
- Cartório: 69% (falha) — 12 de 12 itens certificados na fonte oficial
- Tela e fichas: 100% (ok) — tudo que está aberto aparece na tela e tem ficha
- Integração: 100% (ok) — mesmas contagens e dados em dia em todos os sistemas
- Fluxos automáticos: 60% (falha) — todo fluxo agendado roda na cadência e sem falha
- Execução sem falha silenciosa: 10% (falha) — nenhuma etapa falha em silêncio

## Execução · fluxos: {'falha': 3, 'ok': 31, 'atencao': 6, 'atrasado': 2, 'manual': 2}
- 00 · Verificar prontidão: falha · última 2026-10-17T21:37 · sucesso 0% · cadência 24.0 h
- 35 · Alimentação diária externa (editais abertos): atencao · última 2026-10-17T13:10 · sucesso 30% · cadência 24.0 h
- 06 · Alimentação manual (arquivos e links do titular): atencao · última 2026-10-17T18:15 · sucesso 40% · cadência None h
- 05 · Busca ativa (a cada 3 dias): atencao · última 2026-10-15T17:32 · sucesso 10% · cadência None h
- 09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes: atrasado · última 2026-10-03T11:56 · sucesso 100% · cadência 24.0 h
- 10 · Histórico de doações da Rouanet (empresa por empresa) — retoma sozinho até completar: atencao · última 2026-10-15T16:09 · sucesso 25% · cadência None h
- 12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos: falha · última 2026-10-18T01:54 · sucesso 0% · cadência 1.0 h
- 01 · Eldorado — motores por hora (00h–06h BRT): atencao · última 2026-10-17T12:52 · sucesso 50% · cadência 24.0 h
- 34 · Motores de empresas (semanal, com recuperação): atencao · última 2026-10-17T10:57 · sucesso 67% · cadência 24.0 h
- 03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês): falha · última 2026-10-17T20:16 · sucesso 50% · cadência 6.0 h
- 02 · Alexandria — revisão mensal de leis e procedimentos: atrasado · última 2026-10-01T10:36 · sucesso 50% · cadência 24.0 h
- falha silenciosa em monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-in

## Sala de controle · 34 indicadores · atualizada há 0.0 h
- divergências com a fonte: nenhuma
- sem leitura: nenhum
- estados incoerentes: nenhum
- sugestões de apresentação: ['decisões da titular (descartadas/inscritas aguardando aplicação e livros sinalizados para o Claude)']

## Oportunidades
- abertas: 222 · validadas: 61 (27.5%) · por estado: {'em_verificacao': 141, 'validada': 61, 'validacao_manual': 20}
- com livro: 219 · sem livro (problema): 2 · sem livro por regra: 1 {'não é seleção aberta a associações (dispensa/inexigibilidade de chamamento, credenciamento': 1} · livro inexistente: 0
- sem site oficial: 91 · sem prazo: 148 · prazo vencido ainda aberta: 0
- fora da tela: 0 · sem ficha: 0
- itens que mais faltam: {'Prazo de recurso': 135, 'Anexos': 131, 'Resultado': 112, 'Requisitos': 112, 'Objeto': 110, 'Valor': 110, 'Território': 107, 'Prazo de inscrição': 104, 'Modalidade': 63, 'Órgão / financiador': 46, 'Área de atuação': 45, 'Esfera': 44}

## Sistemas
- motores: 43 funcionando · 0 em falha · 2 inativos · 4 com leitura parcial
- maestro: cobertura 79.5% · esgotados 27
- rede neural: AUC 0.843 · rotulados 1697 · treinada em 2026-10-14T05:54:08+00:00
- Cartório: 0.6854 certificado · fluxos do GitHub com falha: []
- saúde: 7 alerta(s) · índice da sala de controle: 81

## Integração
- contagens: {'repositorio_abertas': 222, 'diagnostico_abertas': 222, 'tela_cartoes': 222, 'fichas': 234, 'sala_controle_abertas': 222}
- idade (h): {'repositorio': 0.0, 'fluxo': 0.0, 'fichas': 0.0, 'sala_controle': 0.0, 'status_motores': 0.3, 'maestro': 0.3, 'rede_neural': 0.0, 'saude': 11.8}
- decisões da titular: 0 · não aplicadas: 0

## Problemas (20)
- [alta] 9 etapa(s) falharam em silêncio na última execução de monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu → investigar a etapa (sem correção automática)
- [alta] fluxo '00 · Verificar prontidão' falhou nas últimas execuções (0% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] fluxo '12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos' falhou nas últimas execuções (0% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] fluxo '03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês)' falhou nas últimas execuções (50% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] 2 de 222 oportunidades abertas sem livro e sem regra que justifique → criar/vincular livros
- [alta] 3 módulos de teste em quarentena por DEFEITO REAL → corrigir o código e tirar da quarentena (sem correção automática)
- [media] fluxo '09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes' sem rodar há 350.2 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] fluxo '02 · Alexandria — revisão mensal de leis e procedimentos' sem rodar há 399.5 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] 54 livros municipais de outros estados no catálogo (só Goiás tem livros municipais) → refazer a tela
- [media] 89 página(s)/documento(s) fora da fila após 5 erros iguais → corrigir a rota ou ler no Chrome (sem correção automática)
- [media] saúde · claude: 244 item(ns) esperando a análise do Claude (próxima: 2026-10-17) → ver o fluxo/arquivo indicado
- [media] saúde · coerência: mapa e lista divergem em GO, __nac__, AM, SC, MG → refazer tela e indicadores
- [media] saúde · gerador: o gerador principal do painel falhou depois da última geração → ver o fluxo/arquivo indicado
- [media] saúde · mapa: 1 oportunidade(s) no mapa sem decisão (curadoria) → ver o fluxo/arquivo indicado
- [media] saúde · opressores: 34 opressor(es) duplicado(s) no catálogo → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 00 · Verificar prontidão: últimas 5 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos: últimas 4 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] 91 abertas ainda sem site oficial → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 148 abertas sem prazo de inscrição conhecido → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 18 módulos de teste em quarentena (envelhecidos) → atualizar o teste à regra atual (sem correção automática)

## Workflow (estrutura de 15/10)
- comando único: 0 ciclo(s) hoje · 6 vermelho(s) · 0 etapa(s) com erro · fases puladas {}
- cobertura do dia: 79.5% de 132 motores
- retentativa: {'aguardando_retentativa': 1179, 'fora_da_fila': 89, 'fora_da_fila_por_escopo': {'outras-oportunidades-1': 4, 'outras-oportunidades-6': 4, 'recorrencia': 4, 'outras-oportunidades-5': 5, 'outras-oportunidades-8': 3, 'outras-oportunidades-3': 4, 'f260-captacao-044': 1, 'outras-oportunidades-2': 2, 'plat-empresas-editais-incentivados': 2, 'f260-captacao-238': 2, 'cartorio': 47, 'outras-oportunidades-7': 3, 'f260-captacao-242': 1, 'f260-captacao-224': 1, 'empresas-incentivadas': 1, 'f260-espalhado-sistema-mirassoldoeste-mt-gov-br': 1, 'f260-captacao-218': 1, 'f260-captacao-113': 3}, 'regra': 'volta em 30 min; sai após 5 tentativas com o mesmo erro', 'destinos': {'Claude no Chrome': 47, 'rota quebrada': 0, 'ponte ou Chrome': 40, 'sem destino': 2}} · leitura parcial na fila: 1031
- curadoria do link oficial: {'em curadoria': 89, 'reprovado': 77, 'aprovado': 41, 'sem link oficial': 15}
- validação por exceção: trava fechada: acerto do Cartório 77.4% < 85.0% — candidatas vão à frente da conferência humana
- auditorias: {'gabarito_do_cartorio': {'em': '2026-10-15T19:53:25+00:00', 'acerto_pct': 77.4, 'documentos_lidos': 142}, 'varredura_referencia': '2026-10-01_2026-10-15', 'robots': {'em': '2026-10-15T10:07:53+00:00', 'motores_com_bloqueio': 5}, 'ponte': {'ponte_ok': 7, 'direto_ok': 5, 'so_pela_ponte': ['ALEGO · SPL (proposições)', 'MPGO'], 'nenhum': ['TJGO · portal'], 'total': 8}}
- legislativo: {'atualizado_em': '2026-10-18T02:05:14+00:00', 'proposicoes': 12}

## Decisões do Eldorado: agiu como deveria?
- decidir · motores escolhidos para ler na passagem: **correto** (0 de 132) — regra: todo motor pendente ou parcial com tentativa sobrando entra na passagem (sem agenda)
- qualificar · oportunidades abertas para associação: **correto** (0 de 222) — regra: pregão, registro de preços, credenciamento de prestadores, contratação de empresa, OS da saúde e seleção de pessoal não são oportunidade (ruído ou acompanhar)
- legislativo · atos legislativos fora das oportunidades: **correto** (0 de 222) — regra: projeto de lei, utilidade pública e orçamento vão ao acompanhamento legislativo, nunca às abertas
- prazo · oportunidades contadas como abertas: **correto** (0 de 222) — regra: prazo vencido sai das abertas
- site_oficial · link oficial gravado no repositório: **correto** (0 de 131) — regra: agregador ou replicador nunca é link oficial
- certificar · itens certificados pelo Cartório: **correto** (0 de 2685) — regra: todo item certificado tem trecho literal e documento
- validar · validação por exceção: **correto** (0 de 0) — regra: só valida sozinho com acerto do Cartório ≥ 85% no gabarito e link oficial aprovado na curadoria
- farol · oportunidades prontas para o Farol: **correto** (0 de 19) — regra: pronta só com prazo vigente e link oficial aprovado na curadoria
- biblioteca · livros da Biblioteca: **correto** (0 de 2696) — regra: ato legislativo não gera livro
