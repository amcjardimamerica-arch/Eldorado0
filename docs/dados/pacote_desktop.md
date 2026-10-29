# Pacote para o Claude Desktop — 2026-10-29

Você está no computador do titular, com IP brasileiro, navegador e o repositório Eldorado clonado. Use o modelo mais forte disponível (Opus 5) para validar. Trabalhe nesta ordem, sem pular etapa, e devolva os arquivos no formato indicado. Nunca estime datas; quando não houver base, escreva o motivo.

## Etapa 1 — motores que aguardam coleta local (portais que recusam IP estrangeiro)

Rode uma vez, na raiz do repositório:

```
python scripts/coleta_brasil.py
```

Ele lê com o seu IP e envia ao repositório.
Nenhum motor aguardando coleta local hoje.
- 26 oportunidade(s) da Etapa 3 em portal que recusa o robô do GitHub (IP fora do Brasil) — abrir depois da coleta.

## Etapa 2 — motores em alerta (não leram, falharam ou passaram da cadência)

- **MP-GO — Programa Destina (cadastro de entidades para receber bens e valores de acordos)** — 11 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://www.prt18.mpt.mp.br/servicos/editais-de-destinacao-de-recursos-bens e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
    - abrir https://www.prt18.mpt.mp.br/servicos/entidades-assistenciais e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
    - abrir https://www.prt18.mpt.mp.br/informe-se/noticias-do-mpt-go e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
- **MPT-GO — editais de 5 dias para indicação de destinação de recursos ou bens (PRT 18ª Região)** — 5 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://www.prt18.mpt.mp.br/servicos/editais-de-destinacao-de-recursos-bens e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
    - abrir https://www.prt18.mpt.mp.br/servicos/entidades-assistenciais e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
    - abrir https://www.prt18.mpt.mp.br/informe-se/noticias-do-mpt-go e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
- **MPU — MPF, MPDFT, MPM e MPT nacional: destinação de bens e valores (com CNMP e FDD)** — 11 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://www.prt18.mpt.mp.br/servicos/editais-de-destinacao-de-recursos-bens e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
    - abrir https://www.prt18.mpt.mp.br/servicos/entidades-assistenciais e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
    - abrir https://www.prt18.mpt.mp.br/informe-se/noticias-do-mpt-go e procurar: bens lesados, chamamento, chamamento público, destinação de recursos, edital de apoio, edital de destinação
- **Busca de empresas para FIA, Idoso, Lei de Incentivo ao Esporte, Pronas, Pronon e Goyazes** — 3 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://captadores.org.br/editais/ e procurar: edital, projetos incentivados, seleção de projetos, FIA, Fundo do Idoso, Lei de Incentivo ao Esporte
- **Oportunidade Estaduais Governamentais de Goiás** — 6 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://goias.gov.br/ e procurar: 
    - abrir https://goias.gov.br/cultura/editais/ e procurar: 
    - abrir https://goias.gov.br/social/editais/ e procurar: 
- **Prefeituras das 25 maiores cidades de Goiás — portais de editais** — 11 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://queridodiario.ok.org.br/ e procurar: chamamento público, termo de fomento, termo de colaboração, edital de seleção, organizações da sociedade civil, fundo municipal
    - abrir https://pncp.gov.br/ e procurar: chamamento público, termo de fomento, termo de colaboração, edital de seleção, organizações da sociedade civil, fundo municipal
- **Lei Rouanet — janela de propostas no SALIC e projetos de Goiás (Ministério da Cultura)** — 3 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://www.gov.br/cultura/pt-br/assuntos/acoes-programas-e-politicas/lei-rouanet e procurar: Lei Rouanet, PRONAC, Salic, proposta cultural, incentivo fiscal, mecenato
    - abrir https://salic.cultura.gov.br/ e procurar: Lei Rouanet, PRONAC, Salic, proposta cultural, incentivo fiscal, mecenato
    - abrir https://www.gov.br/cultura/pt-br/assuntos/acoes-programas-e-politicas/lei-rouanet/legislacao e procurar: Lei Rouanet, PRONAC, Salic, proposta cultural, incentivo fiscal, mecenato
- **Adaptador Mapas Culturais — oportunidades com inscrição aberta** — 11 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://mapa.cultura.gov.br/api/opportunity/find?@select=id,name,registrationTo e procurar: 
    - abrir https://mapa.cultura.gov.br/oportunidades/ e procurar: 
- **Adaptador WordPress — sites oficiais pela API pública** — 11 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://goias.gov.br/cultura/wp-json/wp/v2/posts?search=edital e procurar: 
    - abrir https://goias.gov.br/cultura/editais/ e procurar: 
- **PNCP — API de contratações (chamamentos e credenciamentos)** — 11 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://pncp.gov.br/api/consulta/v1/contratacoes/proposta e procurar: chamamento público, termo de fomento, termo de colaboração, organização da sociedade civil, Lei 13.019, seleção de OSC
    - abrir https://pncp.gov.br/api/search/ e procurar: chamamento público, termo de fomento, termo de colaboração, organização da sociedade civil, Lei 13.019, seleção de OSC
    - abrir https://pncp.gov.br/pncp-api/v1/orgaos/ e procurar: chamamento público, termo de fomento, termo de colaboração, organização da sociedade civil, Lei 13.019, seleção de OSC
- **Motor de Recorrência — revisita as oportunidades identificadas** — 11 dia(s) sem leitura (cadência 1). Ação: conferir escala e limite por execução.
    - abrir https://observatorio3setor.org.br/editais/ e procurar: retificação, prorrogação, errata, resultado, homologação, classificados

Para cada rota aberta, liste os editais publicados nos últimos 30 dias que casem com o léxico e que ainda não estejam em `biblioteca_alexandria/livros/_acervo/editais/`. Devolva em `biblioteca_alexandria/livros/_acervo/editais/coleta_navegador/<data>-motores.json` no formato `{"<id ou novo>": {"objeto":..., "inicio":..., "fim":..., "pagina_oficial":..., "observacao":...}}`.

## Etapa 3 — oportunidades aguardando ação externa (90)

- `op-op-6cce62c69c59` — Secretaria de Estado da Cultura (Secult) — Secult abre chamamento público de OSC para apoi · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/secult-abre-chamamento-publico-de-osc-para-apoio-com-a-politica-nacional-aldir-blanc-em-goias/
- `op-op-ac99e093c742` — SEGENP (gestão de negócios e parcerias) — Edital nº 001/2026 — Celebração de Termo de Cola · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/Download/legislacao/diariooficial/2026/do_20260925_000008871.pdf
- `9e37b9ad76d2ce6ca86c` — Secult Goiás lança edital para levar produção artística goiana ao Rio de Janeiro · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/secult-goias-lanca-edital-para-levar-producao-artistica-goiana-ao-rio-de-janeiro
- `op-op-258a0859666a` — Secretaria de Estado da Cultura (Secult) — Secult abre chamamento público para OSC atuar n · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/secult-abre-chamamento-publico-para-osc-atuar-na-operacionalizacao-do-2o-ciclo-da-pnab/
- `op-op-b75020fc639d` — Secretaria de Estado da Cultura (Secult) — Aberto chamamento público de OSC que apoiará Se · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/aberto-chamamento-publico-de-osc-que-apoiara-secult-goias-com-politica-nacional-aldir-blanc-2o-ciclo/
- `op-op-33b6a9ebbccb` — Governo de Goiás abre inscrições para novo edital de Pontos de Cultura, com investimento d · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/governo-de-goias-abre-inscricoes-para-novos-editais-dos-pontos-de-cultura-com-investimento-de-cerca-de-r-2-milhoes-2
- `op-33b6a9ebbccb` — Governo de Goiás abre inscrições para novo edital de Pontos de Cultura, com investimento d · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/governo-de-goias-abre-inscricoes-para-novos-editais-dos-pontos-de-cultura-com-investimento-de-cerca-de-r-2-milhoes-2
- `c546d1fd98c47238392c` — SECULT-GO (cultura) — Secult Goiás lança edital para levar produção artística goiana ao Ri · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/secult-goias-lanca-edital-para-levar-producao-artistica-goiana-ao-rio-de-janeiro/
- `2d949c7cfc9703097277` — Secult Goiás divulga resultado final do Edital Cultura no Social · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/cultura/secult-goias-divulga-resultado-final-do-edital-cultura-no-social-da-pnab
- `9e1e1f74c37de7287d8a` — Resultado Mérito Cultural – Edital 08 · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/11/pnab-2024-08-resultado-merito-cultural.pdf
- `7826358c0dca520f9ff9` — Resultado Mérito Cultural – Edital 09 · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/11/pnab-2024-09-resultado-merito-cultural.pdf
- `691bca382de42847e934` — Resultado Mérito Cultural – Edital 10 · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/11/pnab-2024-10-resultado-merito-cultural.pdf
- `fb1da95759619788cf6c` — Resultado Mérito Cultural – Edital 11 · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/11/pnab-2024-11-resultado-merito-cultural.pdf
- `2df02cd3dbc6e5be6fc3` — Resultado Mérito Cultural – Edital 12 · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/11/pnab-2024-12-resultado-merito-cultural.pdf
- `c98287d89bc5a7e7855f` — Edital 08 – Fomento Cultural I – Criação, Montagem, Circulação (PDF) · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/08/pnab-2024-08-edital-de-fomento-cultural-i-criacao-montagem-circulacao.pdf
- `7f3515e229987ba3c50d` — Edital 09 – Fomento Cultural II – Ações Formativas (PDF) · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/08/pnab-2024-09-edital-de-fomento-cultural-ii-acoes-formativas.pdf
- `835b3d527a6e20135ba1` — Edital 10 – Fomento Cultural III – Patrimônio Cultural (PDF) · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/08/pnab-2024-10-edital-de-fomento-cultural-iii-patrimonio-cultural.pdf
- `837499ca129ea5f43f36` — Edital 13 – Cultura Viva para fomento a Pontos de Cultura (PDF) · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/secult/wp-content/uploads/sites/5/2024/08/pnab-2024-13-edital-cultura-viva-para-fomento-a-pontos-de-cultura.pdf
- `65aa2703bbca74c02b19` — Aviso de Chamamento Público · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://saude.goiania.go.gov.br/editas-de-chamamento-publico/aviso-de-chamamento-publico-3
- `7a5b6e2eb4296c1398e4` — Secretaria de Estado de Desenvolvimento Social (SEDS) — fundos e conselhos (FIA/CEDCA, Ido · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/social/edital-de-chamamento-publico-001-2026-socioeducativo/
- `op-op-667f16f9b9ce` — Goiás Social — Governo de Goiás faz chamamento público para prestação de auxílios — Goiás · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/social/governo-de-goias-faz-chamamento-publico/
- `op-op-118285c06323` — Fundação de Amparo à Pesquisa do Estado de Goiás (FAPEG) — CHAMADA PÚBLICA FAPEG Nº 16/202 · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/fapeg/chamada-publica-fapeg-no-16-2025-apoio-a-projetos-de-pesquisa-e-inovacao-em-saude-digital/
- `op-op-33253e809b5c` — Agência Brasil Central — Seds abre edital de apoio financeiro a novas entidades filantrópi · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/abc/seds-abre-edital-de-apoio-financeiro-a-novas-entidades-filantropicas/
- `op-op-415e2d6da023` — SEGENP (gestão de negócios e parcerias) — Edital nº 001/2026 — Celebração de Termo de Cola · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://www.goiania.go.gov.br/Download/legislacao/diariooficial/2026/do_20260925_000008871.pdf
- `op-op-484819c58208` — Fundação de Amparo à Pesquisa do Estado de Goiás (FAPEG) — Chamada Pública nº12/2025 – Apo · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/fapeg/chamada-publica-no12-2025-apoio-a-projetos-de-extensao-de-instituicoes-de-ensino-superior-do-estado-de-goias/
- `op-4da58c0b7062` — Edital de Chamamento Público de Instituições sem Fins Lucrativos para a ... — Goiás · **o portal recusa o robô do GitHub (IP fora do Brasil)** → abrir no navegador do titular, com IP brasileiro · link: https://goias.gov.br/social/chamamento-publico-2025/
- `1a2b9a13f2ea2b6b8f6b` — Edital Paraná Festivais · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.cultura.pr.gov.br/Pagina/Edital-Parana-Festivais
- `772d1a8149592f6982c4` — Edital de Prêmio em Reconhecimento à Trajetória de Espaços Culturais (PNAB) · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.cultura.pr.gov.br/PNAB/Pagina/Edital-de-Premio-em-Reconhecimento-Trajetoria-de-Espacos-Culturais
- `op-op-db8328a79d07` — SES-GO (saúde) — Edital nº 01/2026 — Goiás — Goiás · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://diariooficial.abc.go.gov.br/portal/visualizacoes/pdf/7394/#e:7394
- `op-op-aff71483f39b` — Instituto Clima e Sociedade abre edital de até R$ 500 mil para projetos de comunicação cli · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://observatorio3setor.org.br/instituto-clima-e-sociedade-abre-edital-de-ate-r-500-mil-para-projetos-de-comunicacao-climatica
- `op-op-786e5f51f56a` — Edital Rouanet nas Favelas 2 (2026): Guia de Captação · Capitaai — Brasil · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14535.htm
- `op-op-fc3e32dc23e5` — Edital Itagibá 2026: Guia de Captação e Inscrições · Capitaai — Brasil · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.planalto.gov.br/ccivil_03/leis/L12305.htm
- `op-op-f2026a409e7c` — Goiânia — Diário Oficial de Goiânia — edição 8874 (2026-09-30) — chamamento público — Goiá · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://data.queridodiario.ok.org.br/5208707/2026-09-30/eae53a46f7108198ed438c9c4bc4996767a5a08a.pdf
- `61a6052d1609ca5e0201` — EDITAL LMIC 2026 – INCENTIVO FISCAL · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://prefeitura.pbh.gov.br/cultura/edital-lmic-2026-incentivo-fiscal
- `065b7985dc9f28ef38ad` — INSTITUTO NACIONAL DE APOSENTADOS DEFICIENTES E IDOSOS — EDITAL DE CONVOCAÇÃO — social; 3. · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.in.gov.br/web/dou/-/edital-de-convocacao-738193115
- `b0f47ddd92d4370c18fd` — MCTI (ciência e tecnologia) — EDITAL DE 15 DE JUNHO DE 2026 · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.in.gov.br/web/dou/-/edital-de-15-de-junho-de-2026-738154189
- `9eac54be7583d894bd3d` — MinC (cultura) — EDITAL DE CHAMAMENTO PÚBLICO MINC Nº 12, DE 13 DE OUTUBRO DE 2026 · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.in.gov.br/web/dou/-/edital-de-chamamento-publico-minc-n-12-de-13-de-outubro-de-2026-738183446
- `ad045b40c6a72fa9a820` — MinC (cultura) — EDITAL IPHAN Nº 3/2026 · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.in.gov.br/web/dou/-/edital-iphan-n-3/2026-738017249
- `838d74fe0f1282796d84` — MCTI (ciência e tecnologia) — EDITAL DE 3 DE JUNHO DE 2026 · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.in.gov.br/web/dou/-/edital-de-3-de-junho-de-2026-737721110
- `68098dda8d7c05de8f15` — Secretaria de Governança e Gestão Estratégica — EDITAL SGE/AGU Nº 1, DE 6 DE OUTUBRO DE 20 · **só existe o anúncio no PNCP/diário; o site do órgão não foi localizado** → procurar o site oficial do órgão e localizar o edital · link: https://www.in.gov.br/web/dou/-/edital-sge/agu-n-1-de-6-de-outubro-de-2026-737293277

## Etapa 4 — oportunidades parciais do modo completo, para validar com Opus 5 (40)

Para cada uma, abra a página oficial (nunca PNCP, diário ou portal de notícia; exceção: o arquivo do edital do órgão hospedado no PNCP, em `/arquivos/`), extraia OBJETO, PRAZO (início e fim) e URL oficial, e dê o veredito: aprovado (chamada aberta de fomento a OSC), atenção (serve, mas o enquadramento exige conferência) ou reprovado (com a família: resultado de edital, seleção de empresa, serviço ao órgão, qualificação como OS, órgão buscando patrocinador, parceria já celebrada).

- `op-op-aff71483f39b` — Instituto Clima e Sociedade abre edital de até R$ 500 mil para projetos de comunicação cli · falta: Objeto, Prazo de inscrição · https://climaesociedade.org/edital/comunicacao-para-acao-climatica-no-brasil/
- `rec-r30milporprojeto` — Instituto chamex lanca edital educacao com cidadania com investimento de ate r 30 mil por  · falta: Objeto, Prazo de inscrição · https://www.idis.org.br/instituto-chamex-lanca-edital-educacao-com-cidadania-com-investimento-de-ate-r-30-mil-por-projeto/
- `op-58c0cce00fd4` — Edital 012/2026 – Seleção de Associações e/ou Cooperativas de Catadores de Materiais Recic · falta: Objeto, Prazo de inscrição · https://ifrs.edu.br/restinga/wp-content/uploads/sites/5/2026/05/Edital_012_2026_Programa_Coleta_Seletiva_Cidada_assinado.pdf
- `op-c80321f33e60` — EDITAL DE PREMIAÇÃO DE PONTOS E PONTÕES DE CULTURA DE SOBRAL/CE - PNAB - SOBRAL -CE · falta: Objeto, Prazo de inscrição · https://mapacultural.secult.ce.gov.br/files/opportunity/6583/edital-ch25002-sejuc.pdf
- `rec-ditcjpsqdt8zview` — 10ª Edição do Edital Programa Municipal de Fomento à Cultura da Periferia · falta: Objeto, Prazo de inscrição · https://drive.google.com/file/d/1uUAD4g9pG1-wD5VM_tediTCjpS_QdT8z/view
- `op-81991a04c231` — O presente procedimento tem por objeto subsidiar o Chamamento Público para a seleção de as · falta: Objeto, Prazo de inscrição, Página oficial do edital
- `76a87f11d38a7c21ba62` — Chamada pública para selecionar Organização da Sociedade Civil para a execução de ações de · falta: Objeto, Prazo de inscrição · https://aderes.es.gov.br/edital-de-chamamento-publico-no-109-2026-selecao-de-organizacao-da-sociedade-civil-osc-especializada-na-prestacao-de-servicos-de-capacitacao-e-qualificacao-empreendedora-de-impacto-social-presencial-para-a-execucao-do-projeto-empreendendo-para-a-vida
- `0f67c214178145466a7d` — SECULT-GO (cultura) — Edital nº 10/2026 · falta: Objeto, Prazo de inscrição · https://diariooficial.abc.go.gov.br/portal/visualizacoes/pdf/7410/#e:7410
- `d84e27976008e47847ad` — SECTI-GO (ciência e tecnologia) — Edital nº 593/2026 · falta: Objeto, Prazo de inscrição · https://diariooficial.abc.go.gov.br/portal/visualizacoes/pdf/7386/#e:7386
- `3d168a558e5a45b1d675` — Participe do edital Projeto Coletivos da Fundação Abrinq · falta: Objeto, Prazo de inscrição · https://edital.fadc.org.br/coletivos/formulario/
- `rec-eincentivofiscal` — Zurich abre edital nacional para apoiar projetos sociais via leis de ... · falta: Objeto, Prazo de inscrição · https://esginside.com.br/2026/09/28/zurich-abre-edital-nacional-para-apoiar-projetos-sociais-via-leis-de-incentivo-fiscal/
- `cat-a401d40f2a7f` — Dia de doar lanca edital para apoiar campanhas comunitarias · falta: Objeto, Prazo de inscrição · https://observatorio3setor.org.br/dia-de-doar-lanca-edital-para-apoiar-campanhas-comunitarias/
- `op-op-fc3e32dc23e5` — Edital Itagibá 2026: Guia de Captação e Inscrições · Capitaai — Brasil · falta: Objeto, Prazo de inscrição · https://www.planalto.gov.br/ccivil_03/leis/L12305.htm
- `eee1b942ec6a81293e7f` — Prefeitura de Goiânia — Referência: Processo Nº 26.39.000001033-9 SEI Nº 11780957v1 Prefei · falta: Objeto, Prazo de inscrição · https://www.goiania.go.gov.br/Download/legislacao/diariooficial/2026/do_20261015_000008884.pdf
- `c66211b5916da0e9fbbd` — Prefeitura de Goiânia — Secretaria Municipal de Governo – SEGOV. A SECRETÁRIA MUNICIPAL DE · falta: Objeto, Prazo de inscrição · https://goiania.go.gov.br/
- `1033b090cd9af719f839` — SEDHS (desenvolvimento humano e social) — Edital nº 214/2026 · falta: Objeto, Prazo de inscrição · https://goiania.go.gov.br/
- `cat-af40956a098a` — Itau viver mais abre inscricoes para a 7a edicao do edital de projetos voltados a longevid · falta: Objeto, Prazo de inscrição · https://captadores.org.br/editais/itau-viver-mais-abre-inscricoes-para-a-7a-edicao-do-edital-de-projetos-voltados-a-longevidade/
- `04ce18e532fff5b6d4b2` — Prefeitura de Goiânia — âmbito da Secretaria Municipal de Governo – SEGOV. A SECRETÁRIA MU · falta: Objeto, Prazo de inscrição · https://goiania.go.gov.br/
- `cat-0afd299c9a0b` — Fundo Brasil de Direitos Humanos Abre Edital Geral 2026: Até R$ 50 Mil ... · falta: Objeto, Prazo de inscrição · https://www.editalong.com/blog/fundo-brasil-direitos-humanos-edital-geral-2026-osc
- `rec-dtreinamento1256` — 01_inscricao.php · falta: Objeto, Prazo de inscrição · https://app.filantropia.ong/treinamentos/01_inscricao.php?Id_Turma=3133&Id_Treinamento=1256
- `op-op-db8328a79d07` — SES-GO (saúde) — Edital nº 01/2026 — Goiás — Goiás · falta: Objeto, Prazo de inscrição · https://diariooficial.abc.go.gov.br/portal/visualizacoes/pdf/7394/#e:7394
- `cat-6cce0a52a07c` — SIM para Cuidar do Futuro 2026: inscrições abertas para projetos ... · falta: Objeto, Prazo de inscrição · https://sindienergia.org.br/2026/07/31/sim-para-cuidar-do-futuro-2026-inscricoes-abertas-para-projetos-sociais-culturais-e-esportivos/
- `a8ce216e714dcb410ca7` — Prefeitura de Goiânia — KENIA HABERL DE LIMA Gerente da I mprensa Oficial Prefeitura de Go · falta: Objeto, Prazo de inscrição · https://www.goiania.go.gov.br/Download/legislacao/diariooficial/2026/do_20261002_000008876.pdf
- `cat-413a4537ce58` — Comarca de Serranópolis abre seleção de projetos sociais ... - Jusbrasil · falta: Objeto, Prazo de inscrição · https://www.jusbrasil.com.br/noticias/comarca-de-serranopolis-abre-selecao-de-projetos-sociais-para-receber-recursos-de-penas-pecuniarias/6662850176
- `op-op-f6c04b6e4409` — Chamamento público para qualificação de pessoas jurídicas dedireito privado, sem fins lucr · falta: Objeto, Prazo de inscrição · https://www.porangatu.go.gov.br/
- `rec-arargo0012026pdf` — 📄 Edital nº 001/2026 – Doação de Bens Móveis SENAR/AR-GO · falta: Objeto, Prazo de inscrição · https://www.sistemafaeg.com.br/storage/arquivos/EDITAL-DE-DOA%C3%87%C3%83O-DO-SENAR_AR-GO-001_2026.pdf
- `ab0b0a6a2aca2f4d302a` — Prefeitura de Goiânia — transitório, sobre a coordenação e administrativa da operacionaliz · falta: Objeto, Prazo de inscrição · https://goiania.go.gov.br/
- `rec-sascombrempresas` — Otimize o processo de seleção de projetos sociais da sua empresa. · falta: Objeto, Prazo de inscrição · https://prosas.com.br/empresas
- `rec-tivoseambientais` — Volvo apoia projetos culturais, sociais, esportivos e ambientais · falta: Objeto, Prazo de inscrição · https://www.volvogroup.com/content/dam/volvo-group/markets/brazil/sustentabilidade/patrocinios-e-apoios/VOLVO_politica_de_patrocinios_e_apoios_lagon_140119_2019.pdf
- `8c36684df22eacb1614f` — CMAS/FMAS — Edital nº 37/2026 — DA CONTRATAÇÃO DIRETA 1.1 · falta: Objeto, Prazo de inscrição, Página oficial do edital
- `cat-e311d40d4596` — EDP abre inscrições para seleção de projetos incentivados e prevê ... · falta: Objeto, Prazo de inscrição · https://esginside.com.br/2026/07/24/edp-abre-inscricoes-para-selecao-de-projetos-incentivados-e-preve-destinar-ate-r-12-milhoes-a-iniciativas-sociais-esportivas-e-de-saude/
- `op-op-0f80746cf4b3` — COMPANHIA NACIONAL DE ABASTECIMENTO — Contratação de entidade sem fins lucrativos, inscrit · falta: Objeto, Prazo de inscrição · https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra?compra=13510005000192026
- `cat-18a981b5b36d` — EDP abre inscrições para projetos sociais em 13 estados · falta: Objeto, Prazo de inscrição · https://afinamenina.com.br/2026/07/23/edp-abre-inscricoes-para-projetos-sociais-em-13-estados/
- `69ad5e784807c33b8ebe` — Câmara Municipal (emendas) — Parlamentares Impositivas Municipais. 2 A medida fundamenta-s · falta: Objeto, Prazo de inscrição · https://goiania.go.gov.br/
- `rec-aculturadedoacao` — Premio mol reconhece reportagens que inspiram solidariedade e a cultura de doacao · falta: Objeto, Prazo de inscrição · https://observatorio3setor.org.br/premio-mol-reconhece-reportagens-que-inspiram-solidariedade-e-a-cultura-de-doacao/
- `op-op-f2026a409e7c` — Goiânia — Diário Oficial de Goiânia — edição 8874 (2026-09-30) — chamamento público — Goiá · falta: Objeto, Prazo de inscrição, Página oficial do edital
- `e45d79fd575e7887b45e` — Para mais informações, basta acessar o Edital do Programa de Pagamento por Serviços Ambien · falta: Objeto, Prazo de inscrição · https://www.semadesc.ms.gov.br/wp-content/uploads/2025/04/EDITAL-CHAMAMENTO-FUNDO-CLIMA-PANTANAL-003.2025.pdf
- `a0edd9ea12669fec69cc` — Prefeitura de Goiânia — administrativa da operacionalização de emendas impositivas municip · falta: Objeto, Prazo de inscrição · https://goiania.go.gov.br/
- `op-nova-2a700cb1173c` — LUPPA abre inscrições para selecionar dez cidades e fortalecer políticas públicas alimenta · falta: Objeto, Prazo de inscrição · https://conjunta.org/
- `op-op-786e5f51f56a` — Edital Rouanet nas Favelas 2 (2026): Guia de Captação · Capitaai — Brasil · falta: Objeto, Prazo de inscrição · https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14535.htm

## Etapa 4½ — IA local (organização automática, sem gastar Claude)

Se a pasta `ia_local/` ainda não existe: `python scripts/ia_local_instalar.py` (uma vez, ~2 GB; `--leve` para 1 GB).
Suba o servidor local (`ia_local/iniciar.bat` ou `.sh`, deixe a janela aberta) e rode:

```
python -m src.ia_local ciclo      # classifica os incompletos, extrai objeto/prazo com trecho literal, propõe léxico, diagnostica motores 'lendo sem achar'
python -m src.ia_local aplicar    # grava só o que passou na validação — como PROPOSTA, nunca sobrescrevendo dado confirmado
```

As sugestões de rota ficam em `estado/rotas_sugeridas_ia.json` com status 'a confirmar pelo titular'; as extrações entram em `proposta_ia` no registro para o Opus 5 validar na Etapa 4.

## Etapa 5 — fechar o ciclo

```
python -m src.enquadramento ingerir_navegador
python -m src.enquadramento
python -m src.enquadramento fila
python -m src.alerta_motores
python -m src.auditoria_motores
python -m src.dashboard_dados
python scripts/testar.py -- tests/test_system.py  # só siga com tudo verde
python scripts/verificar_privacidade.py
git add -A && git commit -m "desktop: complementacao <data>" && git pull --rebase origin main && git push
```

## Resumo final que você deve me dar

Quantos motores voltaram a ler, quantas oportunidades foram completadas, quantas não eram editais, quais sites não abriram — e o que ficou para o titular decidir.