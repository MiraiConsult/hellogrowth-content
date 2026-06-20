#!/usr/bin/env python3
"""Generate layered PSDs for all 3 cards of Nota Alta carousel."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
from build_psd import build_layered_psd, render_html, create_layer_html

BASE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H = 1080, 1350
PSD_DIR = os.path.join(BASE, "psd")
os.makedirs(PSD_DIR, exist_ok=True)

def render_layer(name, css, html, bg="transparent"):
    """Render a single layer as PNG with optional transparent bg."""
    html_path = create_layer_html(BASE, name, css, html, bg)
    png_path = os.path.join(BASE, f"_layer_{name}.png")
    render_html(html_path, png_path)
    img = Image.open(png_path).convert("RGBA")
    # Clean up temp files
    os.remove(html_path)
    os.remove(png_path)
    return img

# ============================================================
# CARD 1 — Capa
# ============================================================
print("Building Card 1 PSD...")

# Layer: Background
bg1 = render_layer("c1_bg", "", "", bg="#004d40")

# Layer: Glass panel
glass1 = render_layer("c1_glass", """
.glass {
  position: absolute;
  top: 300px; left: 50px; right: 50px;
  height: 580px;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 32px;
}
""", '<div class="glass"></div>', bg="transparent")

# Layer: Text "tem 4,9 estrelas"
t1_line1 = render_layer("c1_line1", """
.t { position: absolute; left: 80px; top: 352px;
  font-size: 115px; font-weight: 900; color: #bfff00;
  line-height: 1; letter-spacing: -0.055em;
  font-family: 'Inter', sans-serif; }
""", '<div class="t">tem 4,9 estrelas</div>', bg="transparent")

# Layer: Text "e mesmo assim perdendo"
t1_line2 = render_layer("c1_line2", """
.t { position: absolute; left: 80px; top: 490px;
  font-size: 58px; font-weight: 600; color: rgba(237,240,238,0.65);
  letter-spacing: -0.03em;
  font-family: 'Inter', sans-serif; }
""", '<div class="t">e mesmo assim perdendo</div>', bg="transparent")

# Layer: Text "PRA QUEM TEM 4,6?"
t1_line3 = render_layer("c1_line3", """
.t { position: absolute; left: 80px; top: 560px;
  font-size: 118px; font-weight: 900; color: #edf0ee;
  line-height: 1.05; letter-spacing: -0.05em;
  text-transform: uppercase;
  font-family: 'Inter', sans-serif; }
.t .num { color: #bfff00; }
""", '<div class="t">PRA QUEM<br>TEM <span class="num">4,6?</span></div>', bg="transparent")

# Layer: Logo
logo1 = render_layer("c1_logo", """
.logo { position: absolute; left: 33px; top: 1074px; }
.logo img { height: 164px; }
""", '<div class="logo"><img src="assets/logo-symbol-light.svg"></div>', bg="transparent")

# Layer: Arrow
arrow1 = render_layer("c1_arrow", """
.a { position: absolute; right: 80px; top: 1100px;
  width: 84px; height: 84px; background: #28ae61;
  border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.a svg { width: 36px; height: 36px; }
""", '''<div class="a"><svg viewBox="0 0 24 24" fill="none" stroke="#edf0ee" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>''', bg="transparent")

layers1 = [
    ("Background", bg1),
    ("Glass Panel", glass1),
    ("tem 4,9 estrelas", t1_line1),
    ("e mesmo assim perdendo", t1_line2),
    ("PRA QUEM TEM 4,6?", t1_line3),
    ("Logo Symbol", logo1),
    ("Arrow Next", arrow1),
]
psd1_path = os.path.join(PSD_DIR, "card-01-capa.psd")
build_layered_psd(layers1, psd1_path)
print(f"  → {psd1_path} ({os.path.getsize(psd1_path):,} bytes)")

# ============================================================
# CARD 2 — Corpo
# ============================================================
print("Building Card 2 PSD...")

bg2 = render_layer("c2_bg", "", "", bg="#edf0ee")

glass2a = render_layer("c2_glass_text", """
.g { position: absolute; top: 268px; left: 60px; right: 60px; height: 280px;
  background: rgba(255,255,255,0.55); border: 1px solid rgba(255,255,255,0.6);
  border-radius: 28px; }
""", '<div class="g"></div>', bg="transparent")

glass2b = render_layer("c2_glass_compare", """
.g { position: absolute; top: 530px; left: 60px; right: 60px; height: 410px;
  background: rgba(255,255,255,0.45); border: 1px solid rgba(255,255,255,0.5);
  border-radius: 28px; }
""", '<div class="g"></div>', bg="transparent")

# Full card 2 content as one text layer (complex formatting)
card2_full = Image.open(os.path.join(BASE, "slide-02.png")).convert("RGBA")
# Make bg transparent by removing the base color
# Actually easier: render just the content elements
t2_content = render_layer("c2_content", """
.g-logo { font-weight: 700; display: inline; }
.g-logo .b { color: #4285F4; } .g-logo .r { color: #EA4335; }
.g-logo .y { color: #FBBC04; } .g-logo .g { color: #34A853; }
.intro { position: absolute; left: 92px; top: 308px;
  font-size: 52px; font-weight: 800; color: #004d40;
  letter-spacing: -0.035em; font-family: 'Inter', sans-serif; }
.body { position: absolute; left: 92px; top: 406px; width: 880px;
  font-size: 38px; font-weight: 500; color: #1b6b5b; line-height: 1.5;
  font-family: 'Inter', sans-serif; }
.body .accent { font-weight: 800; color: #004d40; }
""", '''
<div class="intro">O <span class="g-logo"><span class="b">G</span><span class="r">o</span><span class="y">o</span><span class="b">g</span><span class="g">l</span><span class="r">e</span></span> não olha só a nota.</div>
<div class="body">Olha <span class="accent">quantas avaliações</span> você tem, se são <span class="accent">recentes</span> e se chegam <span class="accent">toda semana</span>.</div>
''', bg="transparent")

t2_compare = render_layer("c2_compare", """
.row { position: absolute; left: 92px; top: 562px; display: flex; gap: 24px; }
.box { width: 436px; height: 354px; border-radius: 24px; padding: 37px 24px; text-align: center;
  font-family: 'Inter', sans-serif; }
.loser { background: rgba(0,77,64,0.06); border: 2px solid rgba(0,77,64,0.12); color: #004d40; }
.winner { background: #004d40; color: #edf0ee; }
.rating { font-size: 103px; font-weight: 900; line-height: 1; margin-bottom: 10px; }
.winner .rating { color: #bfff00; }
.reviews { font-size: 22px; font-weight: 600; line-height: 1.5; }
.badge { display: inline-block; margin-top: 14px; font-size: 18px; font-weight: 800;
  padding: 5px 24px; border-radius: 50px; text-transform: uppercase; letter-spacing: 0.12em; }
.loser .badge { background: #edf0ee; color: #004d40; }
.winner .badge { background: #bfff00; color: #004d40; }
""", '''
<div class="row">
  <div class="box loser"><div class="rating">4,9</div><div class="reviews">12 avaliações<br>paradas há meses</div><div class="badge">NÃO APARECE</div></div>
  <div class="box winner"><div class="rating">4,6</div><div class="reviews">300 avaliações<br>atualizadas sempre</div><div class="badge">TOPO DO GOOGLE</div></div>
</div>
''', bg="transparent")

logo2 = render_layer("c2_logo", """
.logo { position: absolute; left: 44px; top: 1075px; }
.logo img { height: 165px; }
""", '<div class="logo"><img src="assets/logo-symbol.svg"></div>', bg="transparent")

arrow2 = render_layer("c2_arrow", """
.a { position: absolute; right: 80px; top: 1108px;
  width: 84px; height: 84px; background: #28ae61;
  border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.a svg { width: 36px; height: 36px; }
""", '''<div class="a"><svg viewBox="0 0 24 24" fill="none" stroke="#edf0ee" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>''', bg="transparent")

layers2 = [
    ("Background", bg2),
    ("Glass - Text Area", glass2a),
    ("Glass - Compare Area", glass2b),
    ("Headline + Body Text", t2_content),
    ("Compare 4,9 vs 4,6", t2_compare),
    ("Logo Symbol", logo2),
    ("Arrow Next", arrow2),
]
psd2_path = os.path.join(PSD_DIR, "card-02-corpo.psd")
build_layered_psd(layers2, psd2_path)
print(f"  → {psd2_path} ({os.path.getsize(psd2_path):,} bytes)")

# ============================================================
# CARD 3 — CTA
# ============================================================
print("Building Card 3 PSD...")

bg3 = render_layer("c3_bg", "", "", bg="#004d40")

glass3a = render_layer("c3_glass_main", """
.g { position: absolute; left: 86px; top: 236px; width: 908px; height: 371px;
  background: rgba(255,255,255,0.10); border: 1px solid rgba(255,255,255,0.12);
  border-radius: 32px; }
""", '<div class="g"></div>', bg="transparent")

glass3b = render_layer("c3_glass_cta", """
.g { position: absolute; left: 86px; top: 630px; width: 908px; height: 240px;
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.06);
  border-radius: 28px; }
""", '<div class="g"></div>', bg="transparent")

t3_headline = render_layer("c3_headline", """
.g-pill { position: absolute; left: 203px; top: 368px; width: 202px; height: 64px;
  background: rgba(255,255,255,0.92); border-radius: 50px;
  display: flex; align-items: center; justify-content: center; }
.g-pill span { font-size: 49px; font-weight: 700; font-family: 'Inter', sans-serif; }
.g-pill .b { color: #4285F4; } .g-pill .r { color: #EA4335; }
.g-pill .y { color: #FBBC04; } .g-pill .g { color: #34A853; }
.l1 { position: absolute; left: 128px; top: 296px;
  font-size: 54px; font-weight: 900; color: #edf0ee;
  letter-spacing: -0.035em; font-family: 'Inter', sans-serif; }
.l2 { position: absolute; left: 128px; top: 364px;
  font-size: 54px; font-weight: 900; color: #edf0ee;
  letter-spacing: -0.035em; font-family: 'Inter', sans-serif; }
.hl { position: absolute; left: 128px; top: 455px;
  background: #bfff00; border-radius: 4px; padding: 13px 23px; }
.hl span { font-size: 54px; font-weight: 900; color: #004d40;
  letter-spacing: -0.035em; font-family: 'Inter', sans-serif; }
""", '''
<div class="l1">Sua qualidade não aparece</div>
<div class="l2">no &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; porque ela</div>
<div class="g-pill"><span><span class="b">G</span><span class="r">o</span><span class="y">o</span><span class="b">g</span><span class="g">l</span><span class="r">e</span></span></div>
<div class="hl"><span>não está virando avaliação.</span></div>
''', bg="transparent")

t3_cta = render_layer("c3_cta", """
.closer { position: absolute; left: 130px; top: 654px;
  font-size: 44px; font-weight: 700; color: #bfff00;
  letter-spacing: -0.03em; font-family: 'Inter', sans-serif; }
.cta { position: absolute; left: 130px; top: 723px; width: 820px;
  font-size: 30px; font-weight: 500; color: rgba(237,240,238,0.7);
  line-height: 1.5; font-family: 'Inter', sans-serif; }
.cta strong { color: #edf0ee; font-weight: 800; }
""", '''
<div class="closer">É esse processo que falta.</div>
<div class="cta">Coleta automática. Recência. Frequência.<br><strong>A gente monta esse processo pra você.</strong></div>
''', bg="transparent")

logo3 = render_layer("c3_logo", """
.logo { position: absolute; left: 364px; top: 1129px; }
.logo img { height: 72px; }
""", '<div class="logo"><img src="assets/logo-full-light.svg"></div>', bg="transparent")

layers3 = [
    ("Background", bg3),
    ("Glass - Main Card", glass3a),
    ("Glass - CTA Area", glass3b),
    ("Headline + Google Pill", t3_headline),
    ("CTA Text", t3_cta),
    ("Logo Full Light", logo3),
]
psd3_path = os.path.join(PSD_DIR, "card-03-cta.psd")
build_layered_psd(layers3, psd3_path)
print(f"  → {psd3_path} ({os.path.getsize(psd3_path):,} bytes)")

print("\nDone! All PSDs in:", PSD_DIR)
