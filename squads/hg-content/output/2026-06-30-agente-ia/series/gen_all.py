# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hg_lib import page, printbox

ROOT = "squads/hg-content/output/2026-06-30-agente-ia/series"

# ---------------- POST 1 ----------------
P1 = []
P1.append(("dark", False, f'''
<div class="kicker">O agente artificial da sua clínica</div>
<div class="headline" style="font-size:70px;">TODA IA PRA CLÍNICA<br>PARECE IGUAL.<br><span class="ac">ATÉ O PACIENTE ESCREVER.</span></div>
<div class="support" style="font-size:30px; margin-top:26px; max-width:880px;">O que separa uma da outra não é o modelo de IA. É <strong>quem ensinou ela</strong>.</div>
{printbox(330, "Print da conversa", mt=44, grow=True)}'''))

P1.append(("light", True, f'''
<div class="kicker">A diferença</div>
<div class="headline" style="font-size:66px;">NÃO É UMA IA GENÉRICA.<br>É A ATENDENTE DA <span class="ac">SUA CLÍNICA.</span></div>
<div class="support" style="font-size:33px; margin-top:30px; max-width:900px;">Construída com a base de conhecimento da <strong>sua</strong> clínica. Atende <span class="ac">24/7</span>, no seu tom, com as suas regras.</div>'''))

P1.append(("dark", True, f'''
<div class="headline" style="font-size:60px;">ELA NÃO ATENDE.<br>ELA <span class="ac">ACOMPANHA</span> O PACIENTE INTEIRO.</div>
<ul class="blist" style="margin-top:44px;">
  <li>Responde a qualquer hora e conduz até o agendamento</li>
  <li>Confirma a consulta e não deixa a cadeira vazia</li>
  <li>Vende antes e cuida da sua nota no Google</li>
</ul>
<div class="cta-pill">Conhecer o agente 💚</div>'''))

# ---------------- POST 2 ----------------
def compare(tagtxt, question, foot):
    return f'''
<div class="kicker">{tagtxt}</div>
<div class="question">“{question}”</div>
{printbox(250, "Print da resposta", tag="IA genérica", tagclass="bad", grow=True)}
{printbox(250, "Print da resposta", tag="Agente treinado", tagclass="good", mt=46, grow=True)}
<div class="footnote">{foot}</div>'''

P2 = []
P2.append(("dark", True, f'''
<div class="kicker">Agente IA · exemplos reais</div>
<div class="headline" style="font-size:76px;">A MESMA PERGUNTA.<br><span class="ac">DUAS RESPOSTAS.</span></div>
<div class="support" style="font-size:33px; margin-top:32px; max-width:880px;">Uma faz o paciente sumir. A outra faz ele marcar.</div>'''))
P2.append(("light", False, compare("Preço", "Quanto custa um clareamento?",
   "Ela sabe o preço, a regra e a forma de pagamento — porque <strong>você ensinou</strong>.")))
P2.append(("dark", False, compare("Convênio", "Vocês atendem meu convênio?",
   "“Não sei” mata a conversa. A regra da clínica <strong>vira resposta</strong>.")))
P2.append(("light", False, compare("Urgência", "Tô com muita dor, o que eu faço?",
   "Urgência é encaixe, não protocolo. Ela sabe <strong>qual horário pode oferecer</strong>.")))
P2.append(("dark", True, f'''
<div class="kicker">Por que a diferença é tão grande</div>
<div class="headline" style="font-size:62px;">O MODELO É O MESMO.<br>A <span class="ac">BASE DE CONHECIMENTO</span> NÃO.</div>
<div class="support" style="font-size:32px; margin-top:32px; max-width:900px;">IA genérica responde sobre odontologia. A sua responde <strong>pela sua clínica</strong>: seus preços, suas regras, sua agenda, seu jeito de falar.</div>'''))
P2.append(("light", True, f'''
<div class="headline" style="font-size:62px;">A DIFERENÇA NÃO ESTÁ NA IA.<br>ESTÁ EM <span class="ac">QUEM ENSINOU.</span></div>
<div class="support" style="font-size:32px; margin-top:30px; max-width:900px;">Uma atendente treinada com a base de conhecimento da sua clínica — que responde <strong>24/7</strong> no seu tom.</div>
<div class="cta-pill">Conhecer o agente 💚</div>'''))

# ---------------- POST 3 ----------------
def stage(num, timing, title, bullets, printh=None, printlbl="Print da conversa"):
    lis = ''.join(f'<li>{b}</li>' for b in bullets)
    pb = printbox(printh, printlbl, mt=40, grow=True) if printh else ''
    return f'''
<div class="stagenum">{num}</div>
<div class="pill">{timing}</div>
<div class="stagetitle">{title}</div>
<ul class="blist">{lis}</ul>
{pb}'''

P3 = []
P3.append(("dark", False, f'''
<div class="kicker">O ciclo completo</div>
<div class="headline" style="font-size:66px;">ENQUANTO VOCÊ DORME,<br>ALGUÉM ESTÁ <span class="ac">ESCOLHENDO UMA CLÍNICA.</span></div>
<div class="support" style="font-size:31px; margin-top:28px; max-width:880px;">E escolhe a que <strong>respondeu</strong>. Não a melhor — a que respondeu.</div>
{printbox(320, "Print da conversa de madrugada", mt=44, grow=True)}'''))
P3.append(("light", False, stage("01","Responde a qualquer hora","PRIMEIRO CONTATO",
   ["Atende inclusive fora do expediente, fim de semana e feriado",
    "Levanta a queixa, a urgência e de onde veio o contato"])
   + '<div class="footnote">O paciente não espera até segunda. Ele manda pra próxima clínica.</div>'))
P3.append(("dark", False, stage("02","Enquanto o interesse está quente","CONDUÇÃO ATÉ O AGENDAMENTO",
   ["Explica o procedimento e trata o valor pela regra da clínica",
    "Entrega pra equipe fechar o horário na agenda real"], printh=260)))
P3.append(("light", False, stage("03","Um dia antes","CONFIRMAÇÃO DE CONSULTA",
   ["Confirma a presença e libera o horário se o paciente não vier",
    "Avisa a equipe a tempo de reocupar a cadeira"], printh=260, printlbl="Print da confirmação")))
P3.append(("dark", True, f'''
<div class="kicker">Antes e depois da consulta</div>
<div class="headline" style="font-size:60px;">ELA VENDE ANTES.<br>E <span class="ac">CUIDA DEPOIS.</span></div>
<div style="margin-top:52px;">
  <div class="blockttl">04 · Pré-venda</div>
  <ul class="blist">
    <li>Identifica oportunidades de venda antes da consulta</li>
    <li>Prepara o dentista pra vender mais e melhor</li>
  </ul>
</div>
<div style="margin-top:44px;">
  <div class="blockttl">05 · Pós-venda</div>
  <ul class="blist">
    <li>Mede a satisfação do paciente</li>
    <li>Direciona quem gostou pro Google</li>
    <li>Aciona a equipe quando a nota vem baixa</li>
  </ul>
</div>'''))
P3.append(("light", True, f'''
<div class="cycle">↻</div>
<div class="headline" style="font-size:60px;">E O CICLO <span class="ac">RECOMEÇA</span> A CADA NOVA CONSULTA.</div>
<div class="support" style="font-size:31px; margin-top:28px; max-width:900px;">Uma atendente que não dorme, não esquece de confirmar e não deixa uma avaliação boa se perder. No tom da sua clínica.</div>
<div class="cta-pill">Conhecer o agente 💚</div>'''))

POSTS = [("post-1-promessa", P1), ("post-2-generica-vs-treinada", P2), ("post-3-ciclo", P3)]
for folder, cards in POSTS:
    out = os.path.join(ROOT, folder, "slides")
    os.makedirs(out, exist_ok=True)
    total = len(cards)
    for i,(theme,center,inner) in enumerate(cards, start=1):
        last = (i == total)
        open(os.path.join(out, f"card-{i}.html"), "w").write(page(theme, inner, i, total, center, last))
    print(f"{folder}: {total} cards")
