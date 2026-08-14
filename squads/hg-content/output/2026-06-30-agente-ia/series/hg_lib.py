# -*- coding: utf-8 -*-
# HelloGrowth — biblioteca de estilo dos carrosséis (Agente IA)
STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:1080px; height:1350px; overflow:hidden; font-family:'Inter',sans-serif; letter-spacing:-0.02em; background:#004d40; }
.card { width:1080px; height:1350px; position:relative; padding:104px 86px 200px; display:flex; flex-direction:column; }
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
.kicker { font-size:25px; font-weight:600; text-transform:uppercase; letter-spacing:0.15em; margin-bottom:28px; }
.dark .kicker { color:#bfff00; } .light .kicker { color:rgba(0,77,64,0.55); }
.headline { font-weight:900; line-height:1.03; letter-spacing:-0.035em; text-transform:uppercase; }
.dark .headline { color:#edf0ee; } .light .headline { color:#004d40; }
.headline .ac { color:#bfff00; } .light .headline .ac { color:#28ae61; }
.support { font-weight:500; line-height:1.48; }
.dark .support { color:rgba(237,240,238,0.86); } .light .support { color:#1b6b5b; }
.support strong { font-weight:800; } .dark .support strong { color:#edf0ee; } .light .support strong { color:#004d40; }
.support .ac { font-weight:800; } .dark .support .ac { color:#bfff00; } .light .support .ac { color:#28ae61; }
/* pergunta do paciente */
.question { font-size:38px; font-weight:800; line-height:1.25; margin-bottom:34px; }
.dark .question { color:#edf0ee; } .light .question { color:#004d40; }
/* espaço reservado para print */
.printbox { border-radius:24px; display:flex; align-items:center; justify-content:center;
   border:3px dashed; position:relative; }
.dark .printbox { border-color:rgba(237,240,238,0.32); background:rgba(255,255,255,0.05); }
.light .printbox { border-color:rgba(0,77,64,0.25); background:rgba(255,255,255,0.5); }
.printbox .plabel { font-size:22px; font-weight:800; text-transform:uppercase; letter-spacing:0.1em; }
.dark .printbox .plabel { color:rgba(237,240,238,0.5); } .light .printbox .plabel { color:rgba(0,77,64,0.42); }
.ptag { position:absolute; top:-16px; left:28px; font-size:19px; font-weight:800; text-transform:uppercase;
   letter-spacing:0.08em; padding:6px 18px; border-radius:100px; }
.ptag.bad { background:#e8d5d5; color:#a83232; }
.ptag.good { background:#bfff00; color:#004d40; }
.dark .ptag.bad { background:#5c3535; color:#ffc9c9; }
/* etapas */
.stagenum { font-size:150px; font-weight:900; line-height:0.8; letter-spacing:-0.05em; }
.dark .stagenum { color:#bfff00; } .light .stagenum { color:#28ae61; }
.pill { display:inline-block; font-size:22px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em;
   border-radius:100px; padding:11px 26px; margin:24px 0 22px; }
.dark .pill { background:rgba(191,255,0,0.16); color:#bfff00; } .light .pill { background:rgba(0,77,64,0.10); color:#004d40; }
.stagetitle { font-size:56px; font-weight:900; line-height:1.02; letter-spacing:-0.035em; text-transform:uppercase; margin-bottom:30px; }
.dark .stagetitle { color:#edf0ee; } .light .stagetitle { color:#004d40; }
ul.blist { list-style:none; display:flex; flex-direction:column; gap:18px; }
ul.blist li { font-size:29px; font-weight:500; line-height:1.4; padding-left:44px; position:relative; }
.dark ul.blist li { color:rgba(237,240,238,0.9); } .light ul.blist li { color:#1b6b5b; }
ul.blist li::before { content:''; position:absolute; left:0; top:15px; width:26px; height:5px; border-radius:3px; }
.dark ul.blist li::before { background:#bfff00; } .light ul.blist li::before { background:#28ae61; }
.blockttl { font-size:26px; font-weight:800; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:16px; }
.dark .blockttl { color:#bfff00; } .light .blockttl { color:#28ae61; }
.footnote { font-size:27px; font-weight:600; line-height:1.4; margin-top:34px; }
.dark .footnote { color:rgba(237,240,238,0.75); } .light .footnote { color:rgba(0,77,64,0.7); }
.cta-pill { display:inline-block; background:#bfff00; color:#004d40; font-weight:900; font-size:30px;
   text-transform:uppercase; border-radius:100px; padding:18px 40px; margin-top:26px; box-shadow:0 12px 50px rgba(191,255,0,0.30); }
.light .cta-pill { background:#28ae61; color:#ffffff; box-shadow:0 12px 40px rgba(40,174,97,0.35); }
.cycle { font-size:130px; line-height:1; margin-bottom:18px; }
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

def printbox(height=300, label="Espaço para o print", tag=None, tagclass="good", mt=0, grow=False):
    t = f'<div class="ptag {tagclass}">{tag}</div>' if tag else ''
    size = f'flex:1; min-height:{height}px;' if grow else f'height:{height}px;'
    return (f'<div class="printbox" style="{size} margin-top:{mt}px;">'
            f'{t}<div class="plabel">{label}</div></div>')

def page(theme, inner, idx, total, center=True, last=False):
    right = arrow(theme) if not last else f'<div class="pageidx">{idx}/{total}</div>'
    c = " center" if center else ""
    return f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><style>{STYLE}</style></head>
<body><div class="card {theme}{c}"><div class="handle">@hellogrowth__</div>
{inner}
<div class="bottom">{logo(theme)}{right}</div></div></body></html>'''
