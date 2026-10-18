# Diagnóstico do sistema · 2026-10-18 16:54 UTC

## Cumprimento da finalidade · índice geral 69%
- Motores: 98% (ok) — todo motor ativo lê dentro da sua cadência
- Maestro: 82% (atencao) — cobertura completa do dia planejado
- Rede neural: 99% (ok) — discernimento (AUC) de pelo menos 0,85
- Biblioteca: 95% (ok) — toda oportunidade aberta aplicável com livro existente
- Validação: 28% (falha) — toda oportunidade aberta validada
- Site oficial: 71% (atencao) — toda aberta com site oficial
- Prazo: 33% (falha) — toda aberta com prazo (ou fluxo contínuo)
- Cartório: 69% (falha) — 12 de 12 itens certificados na fonte oficial
- Tela e fichas: 100% (ok) — tudo que está aberto aparece na tela e tem ficha
- Integração: 100% (ok) — mesmas contagens e dados em dia em todos os sistemas
- Fluxos automáticos: 52% (falha) — todo fluxo agendado roda na cadência e sem falha
- Execução sem falha silenciosa: 0% (falha) — nenhuma etapa falha em silêncio

## Execução · fluxos: {'falha': 3, 'atrasado': 3, 'ok': 29, 'atencao': 7, 'manual': 2}
- 00 · Verificar prontidão: falha · última 2026-10-18T13:15 · sucesso 0% · cadência 24.0 h
- acesso-mensal: atrasado · última 2026-09-01T09:14 · sucesso 100% · cadência 24.0 h
- 35 · Alimentação diária externa (editais abertos): atencao · última 2026-10-18T13:31 · sucesso 40% · cadência 24.0 h
- 06 · Alimentação manual (arquivos e links do titular): atencao · última 2026-10-17T18:15 · sucesso 40% · cadência None h
- 05 · Busca ativa (a cada 3 dias): atencao · última 2026-10-15T17:32 · sucesso 10% · cadência None h
- 09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes: atrasado · última 2026-10-03T11:56 · sucesso 100% · cadência 24.0 h
- 10 · Histórico de doações da Rouanet (empresa por empresa) — retoma sozinho até completar: atencao · última 2026-10-15T16:09 · sucesso 25% · cadência None h
- 12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos: falha · última 2026-10-18T16:53 · sucesso 0% · cadência 1.0 h
- 01 · Eldorado — motores por hora (00h–06h BRT): atencao · última 2026-10-18T13:08 · sucesso 60% · cadência 24.0 h
- 22 · Motores da vez — cada passagem calcula sozinha o que está pendente (agenda + maestro): atencao · última 2026-10-18T16:52 · sucesso 0% · cadência 1.0 h
- 34 · Motores de empresas (semanal, com recuperação): atencao · última 2026-10-18T11:23 · sucesso 71% · cadência 24.0 h
- 03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês): falha · última 2026-10-18T15:32 · sucesso 30% · cadência 6.0 h
- 02 · Alexandria — revisão mensal de leis e procedimentos: atrasado · última 2026-10-01T10:36 · sucesso 50% · cadência 24.0 h
- falha silenciosa em motores-da-vez.yml: ##[error]catalogar:4: KeyError: 'esqueleto' | ##[error]certificar:1: KeyError: 'dado' | ##[error]curadoria:1: KeyError: 'dado' | ##[error]fechamento:3: KeyError: 'dado'
- falha silenciosa em motor-agregadores.yml: "rede: robots.txt inacessível: URLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)" | "rede: robots.txt inacessível: URLError: timed out", | mapa: falhou
- falha silenciosa em monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-in

## Sala de controle · 34 indicadores · atualizada há 0.0 h
- divergências com a fonte: nenhuma
- sem leitura: nenhum
- estados incoerentes: nenhum
- sugestões de apresentação: ['decisões da titular (descartadas/inscritas aguardando aplicação e livros sinalizados para o Claude)']

## Oportunidades
- abertas: 224 · validadas: 62 (27.7%) · por estado: {'em_verificacao': 142, 'validada': 62, 'validacao_manual': 20}
- com livro: 221 · sem livro (problema): 1 · sem livro por regra: 2 {'não é seleção aberta a associações (dispensa/inexigibilidade de chamamento, credenciamento': 2} · livro inexistente: 9
- sem site oficial: 65 · sem prazo: 150 · prazo vencido ainda aberta: 0
- fora da tela: 0 · sem ficha: 0
- itens que mais faltam: {'Prazo de recurso': 137, 'Anexos': 133, 'Resultado': 114, 'Requisitos': 114, 'Objeto': 114, 'Valor': 114, 'Território': 111, 'Prazo de inscrição': 106, 'Modalidade': 67, 'Órgão / financiador': 50, 'Área de atuação': 49, 'Esfera': 48}

## Sistemas
- motores: 42 funcionando · 1 em falha · 2 inativos · 5 com leitura parcial
  - em falha: Piloto - Interceptador — comprova na fonte oficial — falha — não lê há 1 dia(s) (29 h); última leitura 17/10 08:29
- maestro: cobertura 82.3% · esgotados 23
- rede neural: AUC 0.843 · rotulados 1699 · treinada em 2026-10-14T05:54:08+00:00
- Cartório: 0.6852 certificado · fluxos do GitHub com falha: ['03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês)']
- saúde: 8 alerta(s) · índice da sala de controle: 53

## Integração
- contagens: {'repositorio_abertas': 224, 'diagnostico_abertas': 224, 'tela_cartoes': 224, 'fichas': 236, 'sala_controle_abertas': 224}
- idade (h): {'repositorio': 13.0, 'fluxo': 13.0, 'fichas': 0.0, 'sala_controle': 0.0, 'status_motores': 0.0, 'maestro': 0.0, 'rede_neural': 13.1, 'saude': 3.6}
- decisões da titular: 0 · não aplicadas: 0

## Problemas (29)
- [alta] 336 etapa(s) com erro nos ciclos de hoje: catalogar: catalogar:4: KeyError: 'esqueleto' | pncp: pncp:1: KeyError: 'dado' | certificar: certificar:1: KeyError: 'dado' → investigar a etapa (sem correção automática)
- [alta] 7 etapa(s) falharam em silêncio na última execução de motores-da-vez.yml: ##[error]catalogar:4: KeyError: 'esqueleto' | ##[error]certificar:1: KeyError: 'dado' | ##[error]curadoria:1: KeyError: 'dado' → investigar a etapa (sem correção automática)
- [alta] 3 etapa(s) falharam em silêncio na última execução de motor-agregadores.yml: "rede: robots.txt inacessível: URLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)" | "rede: robots.txt inacessível: URLError: timed out", | mapa: falhou → investigar a etapa (sem correção automática)
- [alta] 8 etapa(s) falharam em silêncio na última execução de monitoramento-diario.yml: "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ba | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-ed | "erro": "FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/Eldorado/Eldorado/biblioteca_alexandria/livros/anexos/abcr-continue-lendo-fu → investigar a etapa (sem correção automática)
- [alta] fluxo '00 · Verificar prontidão' falhou nas últimas execuções (0% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] fluxo '12 · Piloto - Interceptador — um alvo por voo, a cada 3 segundos' falhou nas últimas execuções (0% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] fluxo '03 · Eldorado — carga histórica de cinco anos (campanha única, mês a mês)' falhou nas últimas execuções (30% de sucesso) → investigar o fluxo (sem correção automática)
- [alta] 9 oportunidades apontam para livro que não existe no catálogo → criar/vincular livros e refazer o repositório
- [alta] motor em falha: Piloto - Interceptador — comprova na fonte oficial — falha — não lê há 1 dia(s) (29 h); última leitura 17/10 08:29 → investigar o motor (sem correção automática)
- [alta] 1 de 224 oportunidades abertas sem livro e sem regra que justifique → criar/vincular livros
- [alta] 3 módulos de teste em quarentena por DEFEITO REAL → corrigir o código e tirar da quarentena (sem correção automática)
- [media] fluxo sem atualização há 13.0 h (limite 3 h) → refazer a tela
- [media] repositorio sem atualização há 13.0 h (limite 3 h) → refazer o repositório
- [media] fluxo 'acesso-mensal' sem rodar há 1135.7 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] fluxo '09 · Base histórica dos incentivos (5 anos) — Rouanet, Esporte, PRONON, PRONAS, FIA, Idoso, PAT, Goyazes' sem rodar há 365.0 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
- [media] fluxo '02 · Alexandria — revisão mensal de leis e procedimentos' sem rodar há 414.3 h (cadência 24.0 h) → investigar o agendamento (sem correção automática)
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
- [media] 65 abertas ainda sem site oficial → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 150 abertas sem prazo de inscrição conhecido → Cartório/Interceptador (sem correção automática imediata)
- [baixa] 18 módulos de teste em quarentena (envelhecidos) → atualizar o teste à regra atual (sem correção automática)

## Workflow (estrutura de 15/10)
- comando único: 48 ciclo(s) hoje · 48 vermelho(s) · 336 etapa(s) com erro · fases puladas {'modalidade': 48, 'treinar_rede': 48, 'expurgo': 48, 'migracao_livros': 48, 'recalcular': 48, 'unir_livros': 48, 'biblioteca_diaria': 48, 'vigilancia_diaria': 48}
- cobertura do dia: 82.3% de 130 motores
- retentativa: {'aguardando_retentativa': 1199, 'fora_da_fila': 90, 'fora_da_fila_por_escopo': {'outras-oportunidades-1': 4, 'outras-oportunidades-6': 5, 'recorrencia': 4, 'outras-oportunidades-5': 5, 'outras-oportunidades-8': 3, 'outras-oportunidades-3': 4, 'f260-captacao-044': 1, 'outras-oportunidades-2': 3, 'plat-empresas-editais-incentivados': 2, 'f260-captacao-238': 2, 'cartorio': 46, 'outras-oportunidades-7': 3, 'f260-captacao-242': 1, 'f260-captacao-224': 1, 'empresas-incentivadas': 1, 'f260-espalhado-sistema-mirassoldoeste-mt-gov-br': 1, 'f260-captacao-218': 1, 'f260-captacao-113': 3}, 'regra': 'volta em 30 min; sai após 5 tentativas com o mesmo erro', 'destinos': {'Claude no Chrome': 46, 'rota quebrada': 0, 'ponte ou Chrome': 42, 'sem destino': 2}} · leitura parcial na fila: 1054
- curadoria do link oficial: {'em curadoria': 74, 'reprovado': 50, 'aprovado': 40, 'sem link oficial': 26}
- validação por exceção: trava fechada: acerto do Cartório 77.4% < 85.0% — candidatas vão à frente da conferência humana
- auditorias: {'gabarito_do_cartorio': {'em': '2026-10-15T19:53:25+00:00', 'acerto_pct': 77.4, 'documentos_lidos': 142}, 'varredura_referencia': '2026-10-01_2026-10-15', 'robots': {'em': '2026-10-15T10:07:53+00:00', 'motores_com_bloqueio': 5}, 'ponte': {'ponte_ok': 7, 'direto_ok': 5, 'so_pela_ponte': ['ALEGO · SPL (proposições)', 'MPGO'], 'nenhum': ['TJGO · portal'], 'total': 8}}
- legislativo: {'atualizado_em': '2026-10-18T16:53:24+00:00', 'proposicoes': 11}

## Decisões do Eldorado: agiu como deveria?
- erro · conferência das decisões: **não conferido: KeyError: 'dado'** (0 de 0) — regra: 
