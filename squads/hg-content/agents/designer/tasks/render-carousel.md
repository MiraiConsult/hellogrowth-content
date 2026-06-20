---
task: "Render Carousel"
order: 1
input: |
  - carousel_text: Texto de cada slide produzido pelo Iago Insta
  - caption: Legenda do post
  - company_context: Paleta de cores e tipografia da HelloGrowth
output: |
  - design_system: Documento com cores, fontes, espaçamento usados
  - html_files: Um arquivo HTML por slide (card-01.html ... card-NN.html)
  - png_files: Um screenshot PNG por slide (card-01.png ... card-NN.png)
---

# Render Carousel

Transforma o texto do copywriter em slides visuais HTML/CSS no estilo editorial @brandsdecoded__ e renderiza cada um para PNG via Playwright.

## Process

1. **Carregar contexto**: ler company.md para paleta HelloGrowth (verde #2D7D5F a #A0E8CC, fundo #0d0d0d, Montserrat). Ler output do Iago Insta para obter textos dos slides.

2. **Definir design system**: documentar cores, tipografia (Montserrat, hero 58-67px/900, heading 43px/700, body 34px/500), espaçamento (base 24px, margem 72px), grid (single column centered, max-width 936px), e elementos visuais (border-radius 16px, overlay 65% opacidade para fotos).

3. **Criar HTML do slide 1 (cover/hook)**: arquivo self-contained com CSS inline, body 1080x1440, usando design system. Estilo @brandsdecoded__: fundo escuro ou foto com overlay, texto hero bold centralizado, subtítulo menor abaixo.

4. **Renderizar e verificar slide 1**: salvar HTML no output, navegar via Playwright, screenshot 1080x1440. Verificar: texto legível, cores corretas, nada cortado, layout balanceado. Se falhar, ajustar e re-renderizar.

5. **Produzir slides 2 a N-1 (conteúdo)**: cada slide segue design system. Variações de layout permitidas: texto à esquerda com ícone à direita, citação centralizada, lista com bullets coloridos. Manter consistência de cores e fontes.

6. **Produzir slide final (CTA)**: call-to-action com botão visual, @hellogrowth__, convite para seguir/salvar.

7. **Renderizar lote**: renderizar todos os slides via Playwright em sequência, verificar cada screenshot.

8. **Entregar**: listar todos os arquivos HTML e PNG gerados com design system documentado.

## Output Format

```yaml
design_system:
  viewport: "1080x1440"
  colors:
    primary: "#2D7D5F"
    secondary: "#3BAA7A"
    accent: "#6CCFAA"
    background: "#0d0d0d"
    text: "#ffffff"
  typography:
    family: "Montserrat"
    hero: "67px / 900"
    heading: "43px / 700"
    body: "34px / 500"
    caption: "24px / 500"
  spacing:
    base: "24px"
    margin: "72px"
slides:
  - file: "card-01-cover.html"
    image: "card-01-cover.png"
    type: "hook"
  - file: "card-02.html"
    image: "card-02.png"
    type: "content"
  # ... remaining slides
  - file: "card-07-cta.html"
    image: "card-07-cta.png"
    type: "cta"
```

## Output Example

> Use as quality reference, not as rigid template.

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;900&display=swap');
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1080px; height: 1440px; overflow: hidden;
      background: #0d0d0d;
      font-family: 'Montserrat', sans-serif;
      display: flex; flex-direction: column;
      justify-content: center; align-items: center;
      padding: 72px;
    }
    .hook {
      font-size: 67px; font-weight: 900; color: #ffffff;
      text-align: center; line-height: 1.15;
      max-width: 936px;
    }
    .hook .accent { color: #6CCFAA; }
    .subtitle {
      font-size: 34px; font-weight: 500; color: #A0E8CC;
      text-align: center; margin-top: 32px;
      max-width: 800px; line-height: 1.5;
    }
  </style>
</head>
<body>
  <h1 class="hook">
    <span class="accent">82%</span> dos brasileiros usam WhatsApp para falar com empresas.
  </h1>
  <p class="subtitle">Sua empresa responde em quanto tempo?</p>
</body>
</html>
```

Design rationale: Fundo #0d0d0d (marca HelloGrowth) com texto branco cria contraste 19.3:1. Verde menta #6CCFAA destaca o dado numérico. Montserrat 900 no hero dá peso editorial. Subtitle em verde claro #A0E8CC mantém hierarquia sem competir com o hook.

## Quality Criteria

- [ ] Design system documentado com cores hex, fontes px, espaçamento
- [ ] Cada HTML é self-contained (apenas @import Google Fonts permitido)
- [ ] Body = 1080x1440 exatos
- [ ] Hero >= 58px, body >= 34px
- [ ] Contraste >= 4.5:1 em todo texto
- [ ] Slide 1 verificado visualmente antes do lote
- [ ] Estilo editorial bold (referência @brandsdecoded__)

## Veto Conditions

Reject and redo if ANY are true:
1. Qualquer texto abaixo de 34px no viewport 1080x1440
2. HTML com dependências externas (CDN, JS, imagens externas não-base64)
3. Slides sem consistência visual (cores ou fontes diferentes entre slides)
