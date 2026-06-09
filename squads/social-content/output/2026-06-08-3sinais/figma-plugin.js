// ============================================================
// HelloGrowth — "3 Sinais" Carousel Plugin
// Cole este código inteiro no Figma Plugin Console
// ============================================================

// Passo 1: Carregar fontes
await figma.loadFontAsync({family: "Inter", style: "Black"});
await figma.loadFontAsync({family: "Inter", style: "Semi Bold"});
await figma.loadFontAsync({family: "Inter", style: "Extra Bold"});
await figma.loadFontAsync({family: "Inter", style: "Medium"});
await figma.loadFontAsync({family: "Inter", style: "Bold"});
await figma.loadFontAsync({family: "Inter", style: "Regular"});

const page = figma.currentPage;
page.name = "3 Sinais — Carrossel";

// Cores
const DARK = {r: 0, g: 0.302, b: 0.251};        // #004d40
const LIME = {r: 0.749, g: 1, b: 0};              // #bfff00
const WHITE = {r: 0.93, g: 0.94, b: 0.93};        // #edf0ed
const GREEN_MED = {r: 0.16, g: 0.68, b: 0.38};   // #28ae61
const GREEN_DK = {r: 0.106, g: 0.42, b: 0.357};  // #1b6b5b
const LIGHT_BG = {r: 0.93, g: 0.94, b: 0.93};    // #edf0ed

// Helper: criar texto
function txt(parent, chars, x, y, size, style, color, opts = {}) {
  const t = figma.createText();
  t.characters = chars;
  t.fontSize = size;
  t.fontName = {family: "Inter", style: style};
  t.fills = [{type: 'SOLID', color: color}];
  if (opts.letterSpacing) t.letterSpacing = {value: opts.letterSpacing, unit: "PERCENT"};
  if (opts.lineHeight) t.lineHeight = {value: opts.lineHeight, unit: "PIXELS"};
  if (opts.opacity) t.opacity = opts.opacity;
  if (opts.width) t.resize(opts.width, t.height);
  t.x = x; t.y = y;
  parent.appendChild(t);
  return t;
}

// Helper: handle
function handle(parent, dark) {
  txt(parent, "@hellogrowth__", 472, 40, 18, "Medium", dark ? WHITE : DARK, {opacity: 0.4});
}

// Helper: logo placeholder
function logoPlaceholder(parent, x, y, w, h, label) {
  const r = figma.createRectangle();
  r.name = label;
  r.resize(w, h);
  r.x = x; r.y = y;
  r.fills = [{type: 'SOLID', color: WHITE, opacity: 0.15}];
  r.cornerRadius = 12;
  parent.appendChild(r);
}

// Helper: arrow
function arrow(parent, x, y, color) {
  const e = figma.createEllipse();
  e.name = "Arrow Next";
  e.resize(84, 84);
  e.x = x; e.y = y;
  e.fills = [{type: 'SOLID', color: color}];
  parent.appendChild(e);
}

// Helper: glass card
function glass(parent, x, y, w, h, opacity, dark) {
  const f = figma.createFrame();
  f.name = "Glass Card";
  f.resize(w, h);
  f.x = x; f.y = y;
  f.fills = [{type: 'SOLID', color: {r: 1, g: 1, b: 1}, opacity: opacity}];
  f.cornerRadius = 32;
  if (dark) {
    f.strokes = [{type: 'SOLID', color: {r: 1, g: 1, b: 1}, opacity: 0.12}];
    f.strokeWeight = 1;
  } else {
    f.strokes = [{type: 'SOLID', color: {r: 1, g: 1, b: 1}, opacity: 0.6}];
    f.strokeWeight = 1;
  }
  parent.appendChild(f);
  return f;
}


// ============================================================
// CARD 1 — CAPA (fundo escuro + foto como bg)
// ============================================================
const c1 = figma.createFrame();
c1.name = "Card 1 — Capa";
c1.resize(1080, 1350);
c1.x = 0; c1.y = 0;
c1.fills = [{type: 'SOLID', color: DARK}];

handle(c1, true);

// Nota: adicionar foto 'empty-chair.png' como fill de imagem neste frame
const nota = txt(c1, "↑ Adicionar foto 'empty-chair.png' como Fill de imagem deste frame + overlay verde", 80, 100, 16, "Medium", LIME, {opacity: 0.7});

txt(c1, "3 sinais", 80, 400, 120, "Black", LIME, {letterSpacing: -5.5});
txt(c1, "de que esse contato", 80, 546, 54, "Semi Bold", WHITE, {opacity: 0.75, letterSpacing: -3});
txt(c1, "NÃO VIRA\nPACIENTE.", 80, 610, 88, "Black", WHITE, {letterSpacing: -4.5, lineHeight: 88});
txt(c1, "E você ainda gasta energia\ncom ele.", 80, 810, 36, "Medium", WHITE, {opacity: 0.55, lineHeight: 50});

logoPlaceholder(c1, 33, 1056, 205, 164, "Logo Symbol Light");
arrow(c1, 916, 1121, GREEN_MED);


// ============================================================
// CARD 2 — Sinal 1 (fundo claro + glass)
// ============================================================
const c2 = figma.createFrame();
c2.name = "Card 2 — Sinal 1";
c2.resize(1080, 1350);
c2.x = 1200; c2.y = 0;
c2.fills = [{type: 'SOLID', color: LIGHT_BG}];

handle(c2, false);
glass(c2, 60, 200, 960, 760, 0.55, false);

txt(c2, "1.", 92, 240, 180, "Black", LIME, {letterSpacing: -6});
txt(c2, "SÓ PERGUNTA\nO PREÇO.", 92, 430, 64, "Black", DARK, {letterSpacing: -4, lineHeight: 70});
txt(c2, "Na primeira mensagem,\nantes de qualquer outra coisa.", 92, 680, 38, "Medium", GREEN_DK, {lineHeight: 53});

logoPlaceholder(c2, 44, 1075, 165, 165, "Logo Symbol");
arrow(c2, 916, 1121, GREEN_MED);


// ============================================================
// CARD 3 — Sinal 2 (fundo escuro + glass)
// ============================================================
const c3 = figma.createFrame();
c3.name = "Card 3 — Sinal 2";
c3.resize(1080, 1350);
c3.x = 2400; c3.y = 0;
c3.fills = [{type: 'SOLID', color: DARK}];

handle(c3, true);
glass(c3, 60, 200, 960, 760, 0.10, true);

txt(c3, "2.", 92, 240, 180, "Black", LIME, {letterSpacing: -6});
txt(c3, "SOME QUANDO\nVOCÊ CHAMA.", 92, 430, 64, "Black", WHITE, {letterSpacing: -4, lineHeight: 70});
txt(c3, "Quer resolver tudo no chat.\nNunca marca a avaliação.", 92, 680, 38, "Medium", WHITE, {opacity: 0.65, lineHeight: 53});

logoPlaceholder(c3, 33, 1056, 205, 164, "Logo Symbol Light");
arrow(c3, 916, 1121, LIME);


// ============================================================
// CARD 4 — Sinal 3 (fundo claro + glass)
// ============================================================
const c4 = figma.createFrame();
c4.name = "Card 4 — Sinal 3";
c4.resize(1080, 1350);
c4.x = 3600; c4.y = 0;
c4.fills = [{type: 'SOLID', color: LIGHT_BG}];

handle(c4, false);
glass(c4, 60, 200, 960, 760, 0.55, false);

txt(c4, "3.", 92, 240, 180, "Black", GREEN_MED, {letterSpacing: -6});
txt(c4, "VEIO DA\nPROMOÇÃO.", 92, 430, 64, "Black", DARK, {letterSpacing: -4, lineHeight: 70});
txt(c4, "Não da dor que você trata.\nVeio pelo preço, não pela solução.", 92, 660, 38, "Medium", GREEN_DK, {lineHeight: 53});

logoPlaceholder(c4, 44, 1075, 165, 165, "Logo Symbol");
arrow(c4, 916, 1121, GREEN_MED);


// ============================================================
// CARD 5 — Fecho (fundo escuro + glass)
// ============================================================
const c5 = figma.createFrame();
c5.name = "Card 5 — Fecho";
c5.resize(1080, 1350);
c5.x = 4800; c5.y = 0;
c5.fills = [{type: 'SOLID', color: DARK}];

handle(c5, true);
glass(c5, 60, 180, 960, 520, 0.10, true);

txt(c5, "Atender todo mundo na mesma\nordem é tratar quem vai marcar\nigual a quem nunca ia.", 92, 220, 56, "Black", WHITE, {letterSpacing: -3.5, lineHeight: 66});

// Highlight block
const hlBlock = figma.createFrame();
hlBlock.name = "Highlight Block";
hlBlock.resize(560, 76);
hlBlock.x = 92; hlBlock.y = 460;
hlBlock.fills = [{type: 'SOLID', color: GREEN_MED}];
hlBlock.cornerRadius = 25;
c5.appendChild(hlBlock);

const hlText = figma.createText();
hlText.characters = "Dá pra saber antes.";
hlText.fontSize = 50;
hlText.fontName = {family: "Inter", style: "Black"};
hlText.fills = [{type: 'SOLID', color: {r: 0.96, g: 0.96, b: 0.96}}];
hlText.letterSpacing = {value: -3.5, unit: "PERCENT"};
hlText.x = 23; hlText.y = 8;
hlBlock.appendChild(hlText);

txt(c5, "A HelloGrowth te ajuda a priorizar.", 92, 590, 44, "Bold", LIME, {letterSpacing: -3});
txt(c5, "Qualifique antes de gastar tempo.\nLink na bio.", 92, 660, 34, "Medium", WHITE, {opacity: 0.7, lineHeight: 49});

// Logo full centered
logoPlaceholder(c5, 364, 1129, 352, 72, "Logo Wordmark Light (centered)");


// ============================================================
// Zoom to fit
// ============================================================
figma.viewport.scrollAndZoomIntoView(page.children);

figma.notify("✅ 5 cards criados com sucesso!");
