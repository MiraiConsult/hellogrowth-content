# Design System — Carrossel "Duas clínicas iguais, faturamentos opostos"

**Designer:** Dani Design · **Run:** 2026-06-30-162452 · **Viewport:** 1080×1350px (Instagram 4:5)

## Cores (paleta HelloGrowth)
- Verde escuro (fundo dark): `#004d40 → #1b6b5b → #0f6652` (gradiente)
- Fundo light: `#f4f8f0 → #e8efe4 → #e0eadb`
- Verde médio (logo "Growth", acento light): `#28ae61`
- Lima neon (destaque/pílula/badge): `#bfff00`
- Off-white (texto dark): `#edf0ee`
- Verde-escuro (texto light): `#004d40` / apoio `#1b6b5b`

## Tipografia
- Família: **Inter** (400/500/700/800/900) — Google Fonts
- Kicker: 26px / 600 UPPERCASE, tracking 0.15em
- Headline: 46–96px / 900 UPPERCASE, line-height ~1.04
- Support: 31–33px / 500, line-height 1.5
- Big number: 300px / 900 (slide 03 — "41%")
- Badge pilar: 34px / 900 em quadrado lima 78×78px

## Ritmo visual (alternância dark/light)
1. dark (capa) · 2. light · 3. dark (41%) · 4. light · 5. dark (Pilar 01) · 6. light (Pilar 02) · 7. dark (Pilar 03) · 8. dark (síntese) · 9. light (CTA)

## Elementos
- Header: `@hellogrowth__` centralizado no topo
- Rodapé: logo HelloGrowth (Hello off-white/escuro + Growth verde) + seta lima/verde circular
- Slides com fonte citada: linha de crédito acima do rodapé (slides 02, 06, 09)
- Sem fotos de pessoas (anti-pattern Dani) — hierarquia tipográfica + número como elemento visual

## Arquivos
- HTML self-contained: `card-01-cover.html` … `card-09-cta.html` (apenas @import Google Fonts)
- PNG 1080×1350: `card-01-cover.png` … `card-09-cta.png`
- Preview: `preview-strip.png`

## Render
`google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --screenshot=OUT.png --window-size=1080,1350 file://CARD.html`

## Quality check
- [x] 1080×1350 em todos
- [x] Inter carregada
- [x] Fundo verde (sem linha branca — html/body com bg)
- [x] Lima neon presente nos destaques
- [x] Headlines UPPERCASE
- [x] Logo com split de cor no rodapé
- [x] Preview strip gerado
- [x] Spot-check slide denso (06) sem colisão
