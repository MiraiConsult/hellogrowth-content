# -*- coding: utf-8 -*-
import os
OUT = "squads/hg-content/output/2026-06-30-hexa-uber/slides"
os.makedirs(OUT, exist_ok=True)
STAR = "M12 .587l3.668 7.431 8.2 1.192-5.934 5.786 1.401 8.169L12 18.897l-7.335 3.868 1.401-8.169L.132 9.21l8.2-1.192z"

def stars(n_full=5, ghost=True, size=118, gap=14):
    s = f'<div class="stars" style="gap:{gap}px;">'
    for i in range(n_full):
        s += f'<svg class="star full" width="{size}" height="{size}" viewBox="0 0 24 24"><path d="{STAR}"/></svg>'
    if ghost:
        s += f'<svg class="star ghost" width="{size}" height="{size}" viewBox="0 0 24 24"><path d="{STAR}"/><text x="12" y="15.5" class="six">6</text></svg>'
    s += '</div>'
    return s

STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1080px; height:1350px; overflow:hidden; font-family:'Inter',sans-serif; letter-spacing:-0.02em; background:#004d40; }
.card { width:1080px; height:1350px; position:relative; padding:100px 86px; display:flex; flex-direction:column; justify-content:center; }
.light { background:
   radial-gradient(ellipse 900px 700px at top left, rgba(191,255,0,0.22) 0%, transparent 60%),
   radial-gradient(ellipse 700px 800px at bottom right, rgba(40,174,97,0.13) 0%, transparent 65%),
   linear-gradient(180deg,#f4f8f0 0%,#e8efe4 50%,#e0eadb 100%); color:#004d40; }
.photocard { padding:0; }
.photo { position:absolute; inset:0; background-size:cover; }
.grade { position:absolute; inset:0; background:#0a5e4d; mix-blend-mode:color; opacity:0.66; }
.grade2 { position:absolute; inset:0;
   background:linear-gradient(180deg, rgba(0,61,51,0.30) 0%, rgba(0,61,51,0.06) 28%, rgba(0,77,64,0.78) 72%, #012f28 100%); }
.pcontent { position:absolute; left:86px; right:86px; bottom:200px; z-index:5; }
.handle { position:absolute; top:46px; left:50%; transform:translateX(-50%);
   font-size:19px; font-weight:500; letter-spacing:0.06em; z-index:6; }
.photocard .handle { color:rgba(237,240,238,0.75); }
.light .handle { color:rgba(0,77,64,0.42); }
.kicker { font-size:26px; font-weight:600; text-transform:uppercase; letter-spacing:0.15em; margin-bottom:26px; }
.photocard .kicker { color:#bfff00; }
.light .kicker { color:rgba(0,77,64,0.55); }
.stars { display:flex; align-items:center; margin-bottom:30px; }
.star.full path { fill:#bfff00; filter:drop-shadow(0 6px 18px rgba(191,255,0,0.35)); }
.star.ghost path { fill:none; stroke-width:1.4; stroke-dasharray:2 1.6; }
.photocard .star.ghost path { stroke:rgba(237,240,238,0.75); }
.light .star.ghost path { stroke:rgba(0,77,64,0.40); }
.star.ghost .six { font-size:8px; font-weight:900; text-anchor:middle; }
.photocard .star.ghost .six { fill:rgba(237,240,238,0.9); }
.light .star.ghost .six { fill:rgba(0,77,64,0.55); }
.headline { font-weight:900; line-height:1.02; letter-spacing:-0.035em; text-transform:uppercase; margin-bottom:26px; }
.photocard .headline { color:#edf0ee; text-shadow:0 4px 30px rgba(0,30,24,0.55); }
.light .headline { color:#004d40; }
.headline .ac { color:#bfff00; } .light .headline .ac { color:#28ae61; }
.support { font-weight:500; line-height:1.5; }
.photocard .support { color:rgba(237,240,238,0.95); text-shadow:0 2px 16px rgba(0,30,24,0.65); }
.light .support { color:#1b6b5b; }
.support .ac { font-weight:800; } .photocard .support .ac { color:#bfff00; } .light .support .ac { color:#28ae61; }
.support strong { font-weight:800; } .photocard .support strong { color:#edf0ee; } .light .support strong { color:#004d40; }
.cta-pill { display:inline-block; background:#bfff00; color:#004d40; font-weight:900; font-size:30px;
   text-transform:uppercase; border-radius:100px; padding:18px 40px; margin-top:14px; box-shadow:0 12px 50px rgba(191,255,0,0.30); }
.bottom { position:absolute; bottom:84px; left:86px; right:86px; display:flex; align-items:center; justify-content:space-between; z-index:6; }
.logo img { height:60px; }
.pageidx { font-size:20px; font-weight:700; }
.photocard .pageidx { color:rgba(237,240,238,0.6); }
.light .pageidx { color:rgba(0,77,64,0.40); }
.arrow { width:84px; height:84px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.photocard .arrow { background:#bfff00; box-shadow:0 6px 24px rgba(191,255,0,0.30); }
.light .arrow { background:#28ae61; box-shadow:0 8px 28px rgba(40,174,97,0.40); }
.arrow svg { width:38px; height:38px; }
"""

def arrow(dark_btn=True):
    stroke = "#004d40" if dark_btn else "#edf0ee"
    return f'<div class="arrow"><svg viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>'

def logo(light_logo):
    f = "logo-full-light.svg" if light_logo else "logo-full.svg"
    return f'<div class="logo"><img src="assets/{f}" alt="HelloGrowth"></div>'

def graphic(inner, idx, last=False):
    right = arrow(False) if not last else f'<div class="pageidx">{idx}/4</div>'  # green btn + light stroke
    return f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><style>{STYLE}</style></head>
<body><div class="card light"><div class="handle">@hellogrowth__</div>
{inner}
<div class="bottom">{logo(False)}{right}</div></div></body></html>'''

def photo(imgfile, pos, inner, idx, last=False):
    right = arrow(True) if not last else f'<div class="pageidx">{idx}/4</div>'
    return f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><style>{STYLE}</style></head>
<body><div class="card photocard">
  <div class="photo" style="background-image:url('photos/{imgfile}'); background-position:{pos};"></div>
  <div class="grade"></div><div class="grade2"></div>
  <div class="handle">@hellogrowth__</div>
  <div class="pcontent">{inner}</div>
  <div class="bottom">{logo(True)}{right}</div>
</div></body></html>'''

# CARD 1 — PHOTO (bandeira no estádio)
c1 = f'''{stars(5, True, 62, 8)}
<div class="kicker">Copa · Reputação</div>
<div class="headline" style="font-size:76px;">TODO BRASIL SONHA<br>COM A <span class="ac">6ª ESTRELA.</span></div>
<div class="support" style="font-size:31px; max-width:860px;">No Uber, ela não existe. O teto é <strong>5 estrelas</strong>. E, sendo honesto, a maioria das empresas nem chega lá.</div>'''
open(os.path.join(OUT,"card-1.html"),"w").write(photo("capa-bandeira.jpg","50% 32%", c1, 1, False))

# CARD 2 — GRAPHIC
c2 = f'''<div class="kicker">O teto de todo mundo</div>
<div class="headline" style="font-size:64px;">5 ESTRELAS É O <span class="ac">HEXA</span> DE QUEM ATENDE BEM.</div>
<div class="support" style="font-size:33px; max-width:900px;">Uber, Google, iFood, Booking... o título máximo é sempre o mesmo. E a sua empresa disputa essa taça <strong>todo santo dia</strong> — em cada avaliação que um cliente deixa.</div>'''
open(os.path.join(OUT,"card-2.html"),"w").write(graphic(c2, 2, False))

# CARD 3 — PHOTO (celular)
c3 = f'''<div class="kicker">O jogo de verdade</div>
<div class="headline" style="font-size:62px;">CADA CLIENTE É UM JUIZ.<br>CADA NOTA, UM <span class="ac">PLACAR.</span></div>
<div class="support" style="font-size:31px; max-width:880px;"><span class="ac">96%</span> das pessoas leem avaliações antes de escolher. Nota baixa é perder em casa: te eliminam <strong>antes do apito inicial</strong>.</div>
<div class="support" style="font-size:19px; margin-top:20px; opacity:0.7;">Fonte: Harmo + Reclame AQUI — 2025</div>'''
open(os.path.join(OUT,"card-3.html"),"w").write(photo("phoneapp.jpg","50% 40%", c3, 3, False))

# CARD 4 — GRAPHIC CTA
c4 = f'''{stars(5, False, 108, 14)}
<div class="kicker">Enquanto o hexa não vem</div>
<div class="headline" style="font-size:62px;">SUAS 5 ESTRELAS<br>A GENTE <span class="ac">CONSTRÓI.</span></div>
<div class="support" style="font-size:32px; max-width:900px;">A HelloGrowth ajuda sua empresa a conquistar (e manter) as 5 estrelas que decidem a venda. O hexa é sonho. <strong>Reputação é processo.</strong></div>
<div class="cta-pill">Link na bio 💚</div>'''
open(os.path.join(OUT,"card-4.html"),"w").write(graphic(c4, 4, True))
print("Wrote 4 cards")
