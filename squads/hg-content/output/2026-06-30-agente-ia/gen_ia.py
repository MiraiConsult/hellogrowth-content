# -*- coding: utf-8 -*-
import os
OUT = "squads/hg-content/output/2026-06-30-agente-ia/slides"
os.makedirs(OUT, exist_ok=True)

STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1080px; height:1350px; overflow:hidden; font-family:'Inter',sans-serif; letter-spacing:-0.02em; background:#004d40; }
.card { width:1080px; height:1350px; position:relative; padding:104px 86px; display:flex; flex-direction:column; }
.center { justify-content:center; }
.dark { background:
   radial-gradient(ellipse at top right, rgba(40,174,97,0.22) 0%, transparent 55%),
   radial-gradient(ellipse at bottom left, rgba(191,255,0,0.10) 0%, transparent 55%),
   linear-gradient(160deg,#0f6652 0%,#1b6b5b 42%,#004d40 100%); color:#edf0ee; }
.light { background:
   radial-gradient(ellipse 900px 700px at top left, rgba(191,255,0,0.22) 0%, transparent 60%),
   radial-gradient(ellipse 700px 800px at bottom right, rgba(40,174,97,0.13) 0%, transparent 65%),
   linear-gradient(180deg,#f4f8f0 0%,#e8efe4 50%,#e0eadb 100%); color:#004d40; }
.handle { position:absolute; top:46px; left:50%; transform:translateX(-50%);
   font-size:19px; font-weight:500; letter-spacing:0.06em; z-index:6; }
.dark .handle { color:rgba(237,240,238,0.5); } .light .handle { color:rgba(0,77,64,0.42); }
.kicker { font-size:25px; font-weight:600; text-transform:uppercase; letter-spacing:0.15em; margin-bottom:30px; }
.dark .kicker { color:#bfff00; } .light .kicker { color:rgba(0,77,64,0.55); }
.headline { font-weight:900; line-height:1.03; letter-spacing:-0.035em; text-transform:uppercase; }
.dark .headline { color:#edf0ee; } .light .headline { color:#004d40; }
.headline .ac { color:#bfff00; } .light .headline .ac { color:#28ae61; }
.support { font-weight:500; line-height:1.48; }
.dark .support { color:rgba(237,240,238,0.86); } .light .support { color:#1b6b5b; }
.support strong { font-weight:800; } .dark .support strong { color:#edf0ee; } .light .support strong { color:#004d40; }
.support .ac { font-weight:800; } .dark .support .ac { color:#bfff00; } .light .support .ac { color:#28ae61; }
/* chat bubble motif */
.bubbles { display:flex; flex-direction:column; gap:16px; margin-bottom:44px; }
.bub { max-width:640px; padding:22px 30px; font-size:27px; font-weight:600; border-radius:26px; }
.bub.in { align-self:flex-start; border-bottom-left-radius:6px; }
.dark .bub.in { background:rgba(255,255,255,0.12); color:#edf0ee; }
.light .bub.in { background:#ffffff; color:#004d40; box-shadow:0 8px 24px rgba(0,77,64,0.08); }
.bub.out { align-self:flex-end; border-bottom-right-radius:6px; background:#bfff00; color:#004d40; }
/* stage system */
.dots { display:flex; gap:10px; margin-bottom:54px; }
.dot { height:9px; border-radius:6px; width:44px; }
.dark .dot { background:rgba(237,240,238,0.2); } .light .dot { background:rgba(0,77,64,0.15); }
.dot.on { width:96px; }
.dark .dot.on { background:#bfff00; } .light .dot.on { background:#28ae61; }
.stagenum { font-size:190px; font-weight:900; line-height:0.8; letter-spacing:-0.05em; }
.dark .stagenum { color:#bfff00; } .light .stagenum { color:#28ae61; }
.pill { display:inline-block; font-size:22px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em;
   border-radius:100px; padding:11px 26px; margin:26px 0 26px; }
.dark .pill { background:rgba(191,255,0,0.16); color:#bfff00; } .light .pill { background:rgba(0,77,64,0.10); color:#004d40; }
.stagetitle { font-size:60px; font-weight:900; line-height:1.02; letter-spacing:-0.035em; text-transform:uppercase; margin-bottom:34px; }
.dark .stagetitle { color:#edf0ee; } .light .stagetitle { color:#004d40; }
ul.blist { list-style:none; display:flex; flex-direction:column; gap:20px; }
ul.blist li { font-size:30px; font-weight:500; line-height:1.4; padding-left:44px; position:relative; }
.dark ul.blist li { color:rgba(237,240,238,0.9); } .light ul.blist li { color:#1b6b5b; }
ul.blist li::before { content:''; position:absolute; left:0; top:15px; width:26px; height:5px; border-radius:3px; }
.dark ul.blist li::before { background:#bfff00; } .light ul.blist li::before { background:#28ae61; }
.cta-pill { display:inline-block; background:#bfff00; color:#004d40; font-weight:900; font-size:30px;
   text-transform:uppercase; border-radius:100px; padding:18px 40px; margin-top:20px; box-shadow:0 12px 50px rgba(191,255,0,0.30); }
.cycle { font-size:150px; line-height:1; margin-bottom:20px; }
.dark .cycle { color:#bfff00; } .light .cycle { color:#28ae61; }
.bottom { position:absolute; bottom:80px; left:86px; right:86px; display:flex; align-items:center; justify-content:space-between; z-index:6; }
.logo img { height:58px; }
.pageidx { font-size:20px; font-weight:700; }
.dark .pageidx { color:rgba(237,240,238,0.5); } .light .pageidx { color:rgba(0,77,64,0.4); }
.arrow { width:82px; height:82px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.dark .arrow { background:#bfff00; } .light .arrow { background:#28ae61; }
.arrow svg { width:36px; height:36px; }
"""

def arrow(theme):
    stroke = "#004d40" if theme=="dark" else "#edf0ee"
    return f'<div class="arrow"><svg viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>'
def logo(theme):
    f = "logo-full-light.svg" if theme=="dark" else "logo-full.svg"
    return f'<div class="logo"><img src="assets/{f}" alt="HelloGrowth"></div>'
def dots(active):
    return '<div class="dots">' + ''.join(f'<div class="dot{" on" if i==active else ""}"></div>' for i in range(1,6)) + '</div>'
def page(theme, inner, idx, total, center=True, last=False):
    right = arrow(theme) if not last else f'<div class="pageidx">{idx}/{total}</div>'
    c = " center" if center else ""
    return f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><style>{STYLE}</style></head>
<body><div class="card {theme}{c}"><div class="handle">@hellogrowth__</div>
{inner}
<div class="bottom">{logo(theme)}{right}</div></div></body></html>'''

def stage(theme, num, active, timing, title, bullets):
    lis = ''.join(f'<li>{b}</li>' for b in bullets)
    return f'''{dots(active)}
<div class="stagenum">{num}</div>
<div class="pill">{timing}</div>
<div class="stagetitle">{title}</div>
<ul class="blist">{lis}</ul>'''

TOTAL = 9
cards = []

# 1 COVER (dark) — problema
cards.append(("card-1","dark",True,False, f'''
<div class="bubbles">
  <div class="bub in">Oi, quanto custa um implante?</div>
  <div class="bub out">Depende do caso 🙂 me conta...</div>
</div>
<div class="kicker">Agente Artificial · Clínicas</div>
<div class="headline" style="font-size:72px;">TODA IA PRA CLÍNICA<br>PARECE IGUAL.<br><span class="ac">ATÉ O PACIENTE ESCREVER.</span></div>
<div class="support" style="font-size:31px; margin-top:28px; max-width:880px;">O que separa uma da outra não é o modelo de IA. É <strong>quem ensinou ela</strong>.</div>'''))

# 2 REVEAL (light)
cards.append(("card-2","light",True,False, f'''
<div class="kicker">A diferença</div>
<div class="headline" style="font-size:66px;">NÃO É UMA IA GENÉRICA.<br>É A ATENDENTE DA <span class="ac">SUA CLÍNICA.</span></div>
<div class="support" style="font-size:33px; margin-top:30px; max-width:900px;">Construída com a base de conhecimento da <strong>sua</strong> clínica. Atende <span class="ac">24/7</span>, no seu tom, com as suas regras.</div>'''))

# 3 CYCLE INTRO (dark)
cards.append(("card-3","dark",True,False, f'''
<div class="kicker">O ciclo do paciente</div>
<div class="headline" style="font-size:64px;">ELA NÃO ATENDE.<br>ELA <span class="ac">ACOMPANHA</span> O PACIENTE INTEIRO.</div>
<div class="support" style="font-size:31px; margin-top:30px; max-width:900px;">Do primeiro "bom dia" até a avaliação no Google. Estes são os <strong>5 momentos</strong> em que ela entra sozinha — sem ninguém da equipe apertar nada.</div>'''))

# 4-8 STAGES
stages = [
 ("dark","01",1,"Responde a qualquer hora","PRIMEIRO CONTATO",
   ["Atende inclusive fora do expediente","Levanta a queixa, a urgência e a origem do contato"]),
 ("light","02",2,"Enquanto o interesse está quente","CONDUÇÃO ATÉ O AGENDAMENTO",
   ["Explica o procedimento e trata o valor pela regra da clínica","Entrega pra equipe fechar o horário na agenda real"]),
 ("dark","03",3,"Um dia antes da consulta","CONFIRMAÇÃO DE CONSULTA",
   ["Confirma a presença e libera o horário se o paciente não vier","Avisa a equipe a tempo de reocupar a cadeira"]),
 ("light","04",4,"Logo após a confirmação","FORMULÁRIO DE PRÉ-VENDA",
   ["Identifica oportunidades de venda antes da consulta","Prepara o dentista pra vender mais e melhor"]),
 ("dark","05",5,"Depois do atendimento","FORMULÁRIO DE PÓS-VENDA",
   ["Mede a satisfação do paciente","Direciona quem gostou pro Google","Aciona a equipe quando a nota vem baixa"]),
]
for i,(th,num,act,timing,title,bullets) in enumerate(stages):
    cards.append((f"card-{i+4}",th,False,False, stage(th,num,act,timing,title,bullets)))

# 9 CTA (light)
cards.append(("card-9","light",True,True, f'''
<div class="cycle">↻</div>
<div class="headline" style="font-size:60px;">E O CICLO <span class="ac">RECOMEÇA</span> A CADA NOVA CONSULTA.</div>
<div class="support" style="font-size:32px; margin-top:28px; max-width:900px;">Uma IA que não só responde — ela capta, agenda, confirma, vende e cuida da sua reputação. No tom da sua clínica.</div>
<div class="cta-pill">Conhecer o agente 💚</div>'''))

for name,theme,center,last,inner in cards:
    open(os.path.join(OUT,name+".html"),"w").write(page(theme,inner,int(name.split('-')[1]),TOTAL,center,last))
print("Wrote", len(cards), "cards")
