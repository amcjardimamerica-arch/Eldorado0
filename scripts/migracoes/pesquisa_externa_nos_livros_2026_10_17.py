"""Migração única (titular, 17/10/2026): o livro especial da pesquisa externa vai para os livros; identidades recuperadas;
livro com identidade a completar; duplicados unidos; monitoramento remapeado; vistas refeitas. Idempotente: se a pasta
do livro especial não existe mais, não faz nada."""
import sys,json,collections,re,os; sys.path.insert(0,'.')
if not os.path.exists('biblioteca_alexandria/livros/especiais/pesquisa_externa'):
    print(json.dumps({'migracao':'já aplicada'})); sys.exit(0)
from src import pesquisa_externa as P, banco_livros as B, livros_monitoramento as M, trava_livros as TR, fluxo_oportunidades as F, cartorio as C
from src import livros_regra as LR, selo_livros as S, indexacao_livros as IX, livros_leis as LL
out={}
esp='biblioteca_alexandria/livros/especiais/pesquisa_externa/livro.json'
info=json.load(open('scripts/migracoes/identidades_recuperadas_2026_10_17.json'))
E_=json.load(open(esp))['resultados'] if __import__('os').path.exists(esp) else {}
por=collections.defaultdict(list)
for v in E_.values(): por[v.get('origem') or 'revisao'].append({**v,**{k:x for k,x in (info.get(v['id']) or {}).items() if not v.get(k)}})
st=collections.Counter()
for o,rr in por.items(): st.update(P.gravar(rr,o))
out['especial_para_livros']=dict(st)
v=json.load(open('biblioteca_alexandria/livros/_acervo/editais/vereditos_revisao.json'))['vereditos'].get('e9c73094a796b7fc98ef') or {}
out['identidade']=P.livro_a_identificar('e9c73094a796b7fc98ef', v.get('veredito'),'programa de apoio da GM (General Motors) com inscrição por formulário Qualtrics; citado por ABCR e GIFE', v.get('aprendizado'), v.get('origem') or 'chrome_2026_10_17')
c=json.load(open('estado/pesquisa_externa_resolvidos.json')); c['ids'].pop('e9c73094a796b7fc98ef',None); json.dump(c,open('estado/pesquisa_externa_resolvidos.json','w'),ensure_ascii=False,indent=1)
out['uniao']={k:x for k,x in B.unir_duplicados().items() if not isinstance(x,(list,dict))}
cat=json.load(open('biblioteca_alexandria/fontes/motores.json')); L=cat['motores']
g=collections.defaultdict(list)
for x in L: g[re.sub(r"[^a-z0-9]","",f"{x.get('programa')}{x.get('orgao')}".lower())[:80]].append(x)
sai=set()
for grupo in [gg for gg in g.values() if len(gg)>1]:
    grupo=sorted(grupo,key=lambda y:-len(y.get('juntados') or []))
    for y in grupo[1:]: B.juntar_em(grupo[0],y,"mesmo programa e órgão (endereços diferentes)"); sai.add(y['id'])
cat['motores']=[x for x in L if x['id'] not in sai]; open('biblioteca_alexandria/fontes/motores.json','w').write(json.dumps(cat,ensure_ascii=False,separators=(',',':')))
out['pares_explicitos']=len(sai)
out['trava1']=TR.aplicar(); out['monitoramento']=M.remapear_unidos()
for f in (LR.aplicar_motores, S.aplicar, IX.indexar, LL.montar): f()
out['vistas']={**P.vista_vereditos(),**P.vista_aprendizado()}
out['trava2']=TR.aplicar(); out['bussola']=F.sincronizar_catalogo()
out['pendencias']=C.pendencias(lote_chrome=False).get('para_o_chrome_por_grupo')
print(json.dumps(out,ensure_ascii=False))

import shutil; shutil.rmtree('biblioteca_alexandria/livros/especiais/pesquisa_externa', ignore_errors=True)
