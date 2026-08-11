# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from hg_lib import page

OUT = "squads/hg-content/output/2026-06-30-agente-ia/series/post-1-promessa/slides"
os.makedirs(OUT, exist_ok=True)
SERIE = "Agente IA · 1 de 5"
TOTAL = 3
cards = []

# 1 COVER
cards.append(("card-1","dark",True,False, f'''
<div class="bubbles">
  <div class="bub in">Oi, quanto custa um implante?</div>
  <div class="bub out">Depende do caso 🙂 me conta o que você sente?</div>
</div>
<div class="kicker">O agente artificial da sua clínica</div>
<div class="headline" style="font-size:72px;">TODA IA PRA CLÍNICA<br>PARECE IGUAL.<br><span class="ac">ATÉ O PACIENTE ESCREVER.</span></div>
<div class="support" style="font-size:31px; margin-top:28px; max-width:880px;">O que separa uma da outra não é o modelo de IA. É <strong>quem ensinou ela</strong>.</div>'''))

# 2 REVEAL
cards.append(("card-2","light",True,False, f'''
<div class="kicker">A diferença</div>
<div class="headline" style="font-size:66px;">NÃO É UMA IA GENÉRICA.<br>É A ATENDENTE DA <span class="ac">SUA CLÍNICA.</span></div>
<div class="support" style="font-size:33px; margin-top:30px; max-width:900px;">Construída com a base de conhecimento da <strong>sua</strong> clínica. Atende <span class="ac">24/7</span>, no seu tom, com as suas regras.</div>'''))

# 3 SERIES TEASER / CTA
cards.append(("card-3","dark",True,True, f'''
<div class="kicker">Essa é a 1ª de uma série</div>
<div class="headline" style="font-size:58px;">NOS PRÓXIMOS POSTS,<br>TUDO QUE ELA <span class="ac">FAZ.</span></div>
<ul class="blist" style="margin-top:40px;">
  <li>Atende 24/7 e capta o paciente</li>
  <li>Conduz até o agendamento</li>
  <li>Confirma e não deixa a cadeira vazia</li>
  <li>Vende antes e cuida da sua nota no Google</li>
</ul>
<div class="support" style="font-size:28px; margin-top:38px;">Segue o perfil pra não perder os próximos. 💚</div>'''))

for name,theme,center,last,inner in cards:
    idx = int(name.split('-')[1])
    open(os.path.join(OUT,name+".html"),"w").write(page(theme,inner,idx,TOTAL,center,last,serie=SERIE))
print("Wrote", len(cards), "cards ->", OUT)
