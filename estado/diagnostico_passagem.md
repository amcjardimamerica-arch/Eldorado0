# Diagnóstico do sistema · 2026-10-17 18:43 UTC

## Cumprimento da finalidade · índice geral 70%
- Motores: 100% (ok) — todo motor ativo lê dentro da sua cadência
- Maestro: 78% (atencao) — cobertura completa do dia planejado
- Rede neural: 99% (ok) — discernimento (AUC) de pelo menos 0,85
- Biblioteca: 100% (ok) — toda oportunidade aberta aplicável com livro existente
- Validação: 38% (falha) — toda oportunidade aberta validada
- Site oficial: 68% (falha) — toda aberta com site oficial
- Prazo: 35% (falha) — toda aberta com prazo (ou fluxo contínuo)
- Cartório: 55% (falha) — 12 de 12 itens certificados na fonte oficial
- Tela e fichas: 100% (ok) — tudo que está aberto aparece na tela e tem ficha
- Integração: 100% (ok) — mesmas contagens e dados em dia em todos os sistemas
- Fluxos automáticos: 55% (falha) — todo fluxo agendado roda na cadência e sem falha
- Execução sem falha silenciosa: 10% (falha) — nenhuma etapa falha em silêncio

## Execução · fluxos: {'falha': 2, 'ok': 30, 'atencao': 8, 'atrasado': 2, 'manual': 2}
- 00 · Verificar prontidão: falha · última 2026-10-17T18:15 · sucesso 0% · cadência 24.0 h
- 35 · Alimentação diária externa (editais abertos): atencao · última 2026-10-17T13:10 · sucesso 30% · cadência 24.0 h
- 06 · Alimentação manual (arquivos e links do titular): atencao · última 2026-10-17T18:15 · sucesso 40% · cadência None h
- 05 · Busca ativa (a cada 3 dias): atencao · última 2026-10-15T17:32 · sucesso 10% · cadência None h
- 09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes: atrasado · última 2026-10-03T11:56 · sucesso 100% · cadência 24.0 h
- 10 · Histórico de doações da Rouanet (empresa por empresa) — retoma sozinho até completar: atencao · última 2026-10-15T16:09 · sucesso 25% · cadência None h
- 12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos: falha · última 2026-10-17T18:41 · sucesso 0% · cadência 1.0 h
- 01 · Eldorado — motores por hora (00h–06h BRT): atencao · última 2026-10-17T12:52 · sucesso 50% · cadência 24.0 h
- 22 · Motores da vez — cada passagem calcula sozinha o que está pendente (agenda + maestro): atencao · última 2026-10-17T18:13 · sucesso 78% · cadência 1.0 h
- 34 · Motores de empresas (semanal, com recuperação): atencao · última 2026-10-17T10:57 · sucesso 67% · cadência 24.0 h
- 03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês): atencao · última 2026-10-17T15:09 · sucesso 50% · cadência 6.0 h
- 02 · Alexandria — revisão mensal de leis e procedimentos: atrasado · última 2026-10-01T10:36 · sucesso 50% · cadência 24.0 h
- falha silenciosa em monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-in

## Sala de controle · 34 indicadores · atualizada há 0.0 h
- divergências com a fonte: nenhuma
- sem leitura: ['Última importação do Chrome']
- estados incoerentes: nenhum
- sugestões de apresentação: ['decisões da titular (descartadas/inscritas aguardando aplicação e livros sinalizados para o Claude)']

## Oportunidades
- abertas: 168 · validadas: 63 (37.5%) · por estado: {'em_verificacao': 88, 'validada': 63, 'validacao_manual': 17}
- com livro: 162 · sem livro (problema): 0 · sem livro por regra: 6 {'fora da abrangência: oportunidade pública municipal de outro estado (só Goiás tem livros m': 4, 'não é seleção aberta a associações (dispensa/inexigibilidade de chamamento, credenciamento': 2} · livro inexistente: 0
- sem site oficial: 54 · sem prazo: 110 · prazo vencido ainda aberta: 0
- fora da tela: 0 · sem ficha: 0
- itens que mais faltam: {'Prazo de recurso': 87, 'Anexos': 81, 'Requisitos': 74, 'Valor': 73, 'Objeto': 72, 'Resultado': 72, 'Território': 71, 'Prazo de inscrição': 69, 'Modalidade': 36, 'Área de atuação': 30, 'Esfera': 30, 'Órgão / financiador': 27}

## Sistemas
- motores: 43 funcionando · 0 em falha · 2 inativos · 4 com leitura parcial
- maestro: cobertura 78.3% · esgotados 26
- rede neural: AUC 0.843 · rotulados 1690 · treinada em 2026-10-14T05:54:08+00:00
- Cartório: 0.5508 certificado · fluxos do GitHub com falha: ['00 · Verificar prontidão', '06 · Alimentação manual (arquivos e links do titular)']
- saúde: 7 alerta(s) · índice da sala de controle: 86

## Integração
- contagens: {'repositorio_abertas': 168, 'diagnostico_abertas': 168, 'tela_cartoes': 168, 'fichas': 328, 'sala_controle_abertas': 168}
- idade (h): {'repositorio': 0.0, 'fluxo': 0.1, 'fichas': 0.0, 'sala_controle': 0.0, 'status_motores': 0.5, 'maestro': 0.5, 'rede_neural': 0.1, 'saude': 4.5}
- decisões da titular: 0 · não aplicadas: 0

## Problemas (19)
- [alta] 8 etapa(s) com erro nos ciclos de hoje: recalcular: recalcular:1: código 124 | recalcular: recalcular:1: código 124 | recalcular: recalcular:1: código 124 → investigar a etapa (sem correção automática)
- [alta] 9 etapa(s) falharam em silêncio na última execução de monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu → investigar a etapa (sem correção automática)
- [alta] fluxo '00 · Verificar prontidão' falhou nas últimas execuções (0% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] fluxo '12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos' falhou nas últimas execuções (0% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] 3 módulos de teste em quarentena por DEFEITO REAL → corrigir o código e tirar da quarentena (sem correção automática)
- [media] fluxo '09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes' sem rodar há 342.8 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] fluxo '02 · Alexandria — revisão mensal de leis e procedimentos' sem rodar há 392.1 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] 125 livros municipais de outros estados no catálogo (só Goiás tem livros municipais) → refazer a tela
- [media] 81 página(s)/documento(s) fora da fila após 5 erros iguais → corrigir a rota ou ler no Chrome (sem correção automática)
- [media] saúde · claude: 244 item(ns) esperando a análise do Claude (próxima: 2026-10-17) → ver o fluxo/arquivo indicado
- [media] saúde · coerência: mapa e lista divergem em GO, __nac__, AM, SC, MG → refazer tela e indicadores
- [media] saúde · gerador: o gerador principal do painel falhou depois da última geração → ver o fluxo/arquivo indicado
- [media] saúde · mapa: 1 oportunidade(s) no mapa sem decisão (curadoria) → ver o fluxo/arquivo indicado
- [media] saúde · opressores: 34 opressor(es) duplicado(s) no catálogo → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 00 · Verificar prontidão: últimas 5 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] saúde · workflows: 12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos: últimas 4 execuções sem sucesso → ver o fluxo/arquivo indicado
- [media] 54 abertas ainda sem site oficial → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 110 abertas sem prazo de inscrição conhecido → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 18 módulos de teste em quarentena (envelhecidos) → atualizar o teste à regra atual (sem correção automática)

## Workflow (estrutura de 15/10)
- comando único: 22 ciclo(s) hoje · 6 vermelho(s) · 8 etapa(s) com erro · fases puladas {'modalidade': 22, 'treinar_rede': 22, 'expurgo': 21, 'migracao_livros': 22, 'unir_livros': 21, 'biblioteca_diaria': 21, 'vigilancia_diaria': 21, 'recalcular': 4}
- cobertura do dia: 78.3% de 129 motores
- retentativa: {'aguardando_retentativa': 951, 'fora_da_fila': 81, 'fora_da_fila_por_escopo': {'outras-oportunidades-1': 4, 'outras-oportunidades-6': 4, 'recorrencia': 4, 'outras-oportunidades-5': 5, 'outras-oportunidades-8': 3, 'outras-oportunidades-3': 4, 'f260-captacao-044': 1, 'outras-oportunidades-2': 2, 'plat-empresas-editais-incentivados': 2, 'f260-captacao-238': 2, 'cartorio': 40, 'outras-oportunidades-7': 3, 'f260-captacao-242': 1, 'f260-captacao-224': 1, 'empresas-incentivadas': 1, 'f260-espalhado-sistema-mirassoldoeste-mt-gov-br': 1, 'f260-captacao-218': 1, 'f260-captacao-001': 1, 'f260-captacao-113': 2}, 'regra': 'volta em 30 min; sai após 5 tentativas com o mesmo erro', 'destinos': {'Claude no Chrome': 40, 'rota quebrada': 1, 'ponte ou Chrome': 39, 'sem destino': 2}} · leitura parcial na fila: 812
- curadoria do link oficial: {'aprovado': 51, 'reprovado': 53, 'em curadoria': 196, 'sem link oficial': 23}
- validação por exceção: trava fechada: acerto do Cartório 77.4% < 85.0% — candidatas vão à frente da conferência humana
- auditorias: {'gabarito_do_cartorio': {'em': '2026-10-15T19:53:25+00:00', 'acerto_pct': 77.4, 'documentos_lidos': 142}, 'varredura_referencia': '2026-10-01_2026-10-15', 'robots': {'em': '2026-10-15T10:07:53+00:00', 'motores_com_bloqueio': 5}, 'ponte': {'ponte_ok': 7, 'direto_ok': 5, 'so_pela_ponte': ['ALEGO · SPL (proposições)', 'MPGO'], 'nenhum': ['TJGO · portal'], 'total': 8}}
- legislativo: {'atualizado_em': '2026-10-17T18:40:34+00:00', 'proposicoes': 12}

## Decisões do Eldorado: agiu como deveria?
- decidir · motores escolhidos para ler na passagem: **correto** (0 de 129) — regra: todo motor pendente ou parcial com tentativa sobrando entra na passagem (sem agenda)
- qualificar · oportunidades abertas para associação: **correto** (0 de 168) — regra: pregão, registro de preços, credenciamento de prestadores, contratação de empresa, OS da saúde e seleção de pessoal não são oportunidade (ruído ou acompanhar)
- legislativo · atos legislativos fora das oportunidades: **correto** (0 de 168) — regra: projeto de lei, utilidade pública e orçamento vão ao acompanhamento legislativo, nunca às abertas
- prazo · oportunidades contadas como abertas: **correto** (0 de 168) — regra: prazo vencido sai das abertas
- site_oficial · link oficial gravado no repositório: **correto** (0 de 114) — regra: agregador ou replicador nunca é link oficial
- certificar · itens certificados pelo Cartório: **correto** (0 de 466) — regra: todo item certificado tem trecho literal e documento
- validar · validação por exceção: **correto** (0 de 0) — regra: só valida sozinho com acerto do Cartório ≥ 85% no gabarito e link oficial aprovado na curadoria
- farol · oportunidades prontas para o Farol: **correto** (0 de 22) — regra: pronta só com prazo vigente e link oficial aprovado na curadoria
- biblioteca · livros da Biblioteca: **correto** (0 de 2572) — regra: ato legislativo não gera livro
