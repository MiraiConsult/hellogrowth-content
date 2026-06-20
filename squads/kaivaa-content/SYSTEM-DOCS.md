# HelloGrowth Content System — Documentação Técnica Completa

**Objetivo:** Replicar o sistema de produção de conteúdo social que foi construído nesta sessão.
**Data:** Junho 2026
**Autor:** Claude Code (sessão cse_01RXRUyw64HWp6pgoosUTsE4)

---

## 1. O QUE O SISTEMA FAZ

Produz carrosséis Instagram, cards WhatsApp, capas de Reels e templates de email marketing para a HelloGrowth, uma empresa de gestão de reputação digital focada em clínicas odontológicas.

### Fluxo completo:
```
Pesquisa → Copy → Design → Renderização → Upload → Distribuição (Slack/Figma)
```

### Entregas desta sessão:
- 4 carrosséis Instagram ("+R$45K Harvard", "Nota Alta 4,9 vs 4,6", "3 Sinais", "Tráfego vs Indicação", "96% te julgam")
- 3 cards WhatsApp (Persona Solo, Copa ranking, 4 Fases)
- 1 template email marketing
- 1 capa de Reels
- 9 fotos IA (clínica odontológica, estádio, celular)
- 2 vetores SVG (ranking Google, clínica comparativo)
- Brand guide v2 documentado
- Arquivos Figma editáveis

---

## 2. STACK TÉCNICA

### Ferramentas usadas:
| Ferramenta | Uso | Como acessar |
|-----------|-----|-------------|
| **HTML/CSS** | Montar cada slide como página web | Arquivo local `.html` |
| **Chrome Headless** | Renderizar HTML → PNG (1080x1350px) | `/opt/pw-browsers/chromium-1194/chrome-linux/chrome` |
| **Gamma AI (Flux-2-Pro)** | Gerar fotos de IA | MCP tool `mcp__6445ae58__generate` |
| **Figma MCP** | Criar/editar designs no Figma | MCP tool `mcp__a35b53ef__use_figma` |
| **Supabase Storage** | Hospedar imagens com URLs públicas | Bucket `instagram-carousels` |
| **Slack MCP** | Enviar artes pro canal #marketing | MCP tool `mcp__e1ed6fcb__slack_send_message` |
| **Gmail MCP** | Ler emails (logos, assets) | MCP tool `mcp__4e5963fd__search_threads` |
| **Google Drive (gdown)** | Baixar assets do Drive | `pip install gdown` |

### Comando de renderização:
```bash
chrome --headless=new --no-sandbox --disable-gpu \
  --disable-software-rasterizer --hide-scrollbars \
  --force-device-scale-factor=1 \
  --screenshot=output.png \
  --window-size=1080,1350 \
  file:///path/to/slide.html
```

### Dimensões:
| Formato | Tamanho |
|---------|---------|
| Instagram Feed (carrossel) | 1080x1350px (4:5) |
| Instagram Reels (capa) | 1080x1920px (9:16) |
| WhatsApp card | 1080x1080px (1:1) |
| Email marketing | 600px largura |
| Preview strip | 7700x1400px (todos lado a lado) |

---

## 3. DESIGN SYSTEM — BRAND HELLOGROWTH

### 3.1 Paleta de Cores

| Cor | Hex | Uso |
|-----|-----|-----|
| Verde escuro (fundo) | `#004d40` | Background principal dos cards escuros |
| Verde médio escuro | `#1b6b5b` | Gradientes, logo "Growth" |
| Verde médio | `#28ae61` | Ícones, highlights, seta, logo "Growth" |
| Verde lima neon | `#bfff00` | DESTAQUE — números, pílulas, dados-chave |
| Off-white | `#edf0ed` | Texto principal em fundo escuro |
| Body bg escuro | `#0a5e4d` | Body dos HTMLs escuros (evita barra no bottom) |
| Body bg claro | `#e0eadb` | Body dos HTMLs claros |
| Crimson (Harvard) | `#A41E22` | Badge Harvard |

### 3.2 Tipografia

- **Font:** Inter (Google Fonts)
- **URL:** `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap`

| Elemento | Weight | Size | Case |
|----------|--------|------|------|
| Headline principal | Black (900) | 86-132px | UPPERCASE ou sentence |
| Números grandes | Black (900) | 160-260px | — |
| Texto médio | Semi Bold (600) | 44-58px | sentence |
| Corpo | Medium (500) | 30-38px | sentence |
| Handle @hellogrowth__ | Medium (500) | 18px | lowercase |

### 3.3 Fundo — Orbs com blur

**NÃO usar** `radial-gradient` CSS simples. O fundo correto são **elipses sólidas com filter: blur(250px)**:

```html
<!-- Fundo escuro -->
<div class="orb" style="width:555px;height:529px;left:-80px;top:-66px;
  background:#1d884a;filter:blur(250px);border-radius:50%;position:absolute;"></div>
<div class="orb" style="width:556px;height:562px;left:713px;top:295px;
  background:#1d884a;filter:blur(250px);border-radius:50%;position:absolute;"></div>
<div class="orb" style="width:626px;height:600px;left:-239px;top:857px;
  background:#116836;filter:blur(250px);border-radius:50%;position:absolute;"></div>
```

**Body bg deve bater com o gradient:** `#0a5e4d` para escuro, `#e0eadb` para claro. Senão cria barra visível no bottom.

### 3.4 Glass Cards

```css
.glass {
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 32px;
}
```

### 3.5 Highlight Block (verde, NÃO lima)

```css
.hl-block {
  background: #28ae61;  /* verde médio, NÃO #bfff00 */
  padding: 8px 18px;
  border-radius: 25px;
}
```

### 3.6 Logos

3 variantes oficiais (SVGs no Google Drive):
- `logo-symbol.svg` / `logo-symbol-light.svg` — símbolo HG
- `logo-wordmark.svg` / `logo-wordmark-light.svg` — texto "HelloGrowth"
- `logo-full.svg` / `logo-full-light.svg` — assinatura completa

**Regras:**
- Cards escuros → versão `-light`
- Cards claros → versão normal
- Variar entre símbolo (cards internos) e wordmark/full (capa e CTA)
- Nunca usar assinatura completa em todos os cards

### 3.7 Rodapé

- Logo: posição absoluta, `bottom: 130px` mínimo
- Seta next: ellipse 84x84px, `#28ae61` (claro) ou `#bfff00` (escuro)
- Handle `@hellogrowth__`: centralizado, topo, 18px, opacidade 0.4

---

## 4. ANTI-PATTERNS (NUNCA FAZER)

1. Fundo preto ou branco puro — sempre verde escuro ou off-white
2. Tipografia que não seja Inter
3. Elementos tortos/rotacionados
4. Mais de 3 níveis de tamanho de fonte por card
5. Logo inteira em todos os cards
6. Highlight lima sobrepondo texto — dar margin-top extra
7. Linhas de texto desbalanceadas
8. "Google" como texto plain — sempre logo colorido
9. Rodapé encostando na borda — mínimo 130px
10. Mesmo elemento visual em múltiplos cards (ex: estrelas em 2 cards)
11. Texto `#ffffff` — usar `#edf0ed`
12. Gradient overlay chegando a 100% no bottom — máximo 92%
13. `body { background }` diferente do gradient end — causa barra visível

---

## 5. ESTRUTURA DE ARQUIVOS

```
squads/social-content/
├── squad.yaml                    # Config do squad
├── agents/
│   └── designer.agent.md         # Persona Dani Design
├── pipeline/
│   ├── pipeline.yaml             # Steps do pipeline
│   ├── steps/                    # Instruções por step
│   └── data/
│       ├── brand-guide.md        # Design system completo
│       ├── tone-of-voice.md      # Tom de voz
│       ├── quality-criteria.md   # Critérios de qualidade
│       └── research-focus.md     # Foco da pesquisa atual
└── output/
    ├── 2026-06-03-195535/        # Run +R$45K Harvard
    │   └── slides-brand/
    │       ├── assets/           # SVGs dos logos
    │       ├── slide-01.html     # Fonte HTML
    │       ├── slide-01.png      # Imagem renderizada
    │       └── preview-strip.png # Todos lado a lado
    ├── 2026-06-05-nota-alta/     # Run Nota Alta
    ├── 2026-06-08-3sinais/       # Run 3 Sinais
    ├── 2026-06-18-96pct/         # Run 96% te julgam
    └── photo-pack/               # Fotos IA geradas
```

---

## 6. PIPELINE DE PRODUÇÃO (12 steps)

```yaml
1. checkpoint: Foco da Pesquisa (tema, período, keywords)
2. agent/subagent: Pesquisa de Tendências (web search)
3. checkpoint: Seleção de Notícia (top 3)
4. agent/inline: Geração de Ângulos (3 opções)
5. checkpoint: Seleção de Ângulo
6. agent/inline: Criação Conteúdo Instagram (copy dos slides)
7. agent/subagent: Criação Conteúdo LinkedIn
8. agent/inline: Design Visual (HTML/CSS → PNG)
9. checkpoint: Aprovação do Conteúdo
10. agent/inline: Revisão de Qualidade
11. checkpoint: Aprovação Final
12. agent/inline: Publicação no Instagram
```

---

## 7. TEMPLATE HTML DE UM SLIDE (exemplo card escuro)

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>
@page { size: 1080px 1350px; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body {
  width: 1080px; height: 1350px;
  background: #0a5e4d;
  font-family: 'Inter', sans-serif;
  color: #edf0ed;
  overflow: hidden;
  letter-spacing: -0.02em;
}
.card { width: 1080px; height: 1350px; position: relative; }
.orb { position: absolute; border-radius: 50%; }
.orb1 { width: 555px; height: 529px; left: -80px; top: -66px;
  background: #1d884a; filter: blur(250px); }
.orb2 { width: 556px; height: 562px; left: 713px; top: 295px;
  background: #1d884a; filter: blur(250px); }
.orb3 { width: 626px; height: 600px; left: -239px; top: 857px;
  background: #116836; filter: blur(250px); }
.handle { position: absolute; top: 40px; left: 50%;
  transform: translateX(-50%); font-size: 18px;
  font-weight: 500; color: rgba(237,240,237,0.4); }

/* Conteúdo */
.headline { /* seus estilos */ }

/* Rodapé */
.logo-wrap { position: absolute; left: 33px; top: 1060px; }
.logo-wrap img { height: 164px; }
.arrow-wrap { position: absolute; right: 80px; bottom: 130px; }
.arrow-circle { width: 84px; height: 84px; background: #bfff00;
  border-radius: 50%; display: flex; align-items: center;
  justify-content: center; }
</style>
</head>
<body>
<div class="card">
  <div class="orb orb1"></div>
  <div class="orb orb2"></div>
  <div class="orb orb3"></div>
  <div class="handle">@hellogrowth__</div>

  <!-- CONTEÚDO AQUI -->

  <div class="logo-wrap">
    <img src="assets/logo-symbol-light.svg" alt="HG">
  </div>
  <div class="arrow-wrap">
    <div class="arrow-circle">
      <svg viewBox="0 0 24 24" fill="none" stroke="#004d40"
        stroke-width="3" stroke-linecap="round"
        stroke-linejoin="round">
        <line x1="5" y1="12" x2="19" y2="12"/>
        <polyline points="12 5 19 12 12 19"/>
      </svg>
    </div>
  </div>
</div>
</body>
</html>
```

---

## 8. GERAÇÃO DE FOTOS IA

### Ferramenta: Gamma MCP com modelo flux-2-pro

```javascript
// Exemplo de chamada
mcp__6445ae58__generate({
  format: "social",
  cardOptions: { dimensions: "4x5" },
  exportAs: "png",
  imageOptions: {
    model: "flux-2-pro",
    style: "cinematic photography, dark moody green lighting, shallow depth of field, dramatic shadows, dark green color grade, 35mm film grain",
    stylePreset: "custom"
  },
  inputText: "Photo: [descrição detalhada da foto]"
})
```

### Prompt pattern que funciona:
```
Photo: [objeto/cena]. [Iluminação]. [Cor dominante].
[Depth of field]. [Ângulo]. [Atmosfera].
Portrait orientation.
```

### Fotos geradas nesta sessão:
- Cadeira odontológica vazia (dark green)
- Recepção de clínica vazia à noite
- Instrumentos odontológicos (close-up)
- WhatsApp chat (close-up celular)
- Panfleto "PROMOÇÃO" amassado
- Split screen: clínica 4,9 vazia vs 4,6 lotada
- Dona de clínica preocupada com celular
- Mão segurando celular com lista de clínicas (2 versões)
- Dentista no estádio com bandeira do Brasil

---

## 9. FIGMA INTEGRATION

### Criar arquivo:
```javascript
mcp__a35b53ef__create_new_file({
  editorType: "design",
  fileName: "Nome do arquivo",
  planKey: "team::1304984265611378863"
})
```

### Montar cards no Figma:
```javascript
mcp__a35b53ef__use_figma({
  fileKey: "FILE_KEY",
  code: `
    // Carregar fontes
    await figma.loadFontAsync({family: "Inter", style: "Black"});
    // ... criar frames, textos, retângulos
  `,
  description: "Descrição do que o código faz"
})
```

### Padrão de helper functions:
```javascript
function txt(parent, chars, x, y, size, style, color, opts) {
  const t = figma.createText();
  t.characters = chars;
  t.fontSize = size;
  t.fontName = {family: "Inter", style: style};
  t.fills = [{type: 'SOLID', color: color}];
  if (opts?.ls) t.letterSpacing = {value: opts.ls, unit: "PERCENT"};
  if (opts?.lh) t.lineHeight = {value: opts.lh, unit: "PIXELS"};
  if (opts?.op) t.opacity = opts.op;
  t.x = x; t.y = y;
  parent.appendChild(t);
  return t;
}
```

### Limitações:
- Figma Starter: limite baixo de MCP calls (esgota rápido)
- Figma Pro: mais chamadas, usado nesta sessão
- Inter font styles: "Semi Bold" (com espaço), "Extra Bold" (com espaço)
- Logos: placeholder retângulo → usuário arrasta SVG por cima

---

## 10. SUPABASE STORAGE (hosting de imagens)

### Projeto: Hello Growth Staging
- **ID:** `aevhjbvfxehghoekibjl`
- **URL:** `https://aevhjbvfxehghoekibjl.supabase.co`
- **Bucket:** `instagram-carousels` (público)

### Upload:
```bash
curl -X POST \
  "${SUPABASE_URL}/storage/v1/object/instagram-carousels/${FOLDER}/${FILE}" \
  -H "Authorization: Bearer ${ANON_KEY}" \
  -H "apikey: ${ANON_KEY}" \
  -H "Content-Type: image/png" \
  --data-binary "@local-file.png"
```

### URL pública:
```
https://aevhjbvfxehghoekibjl.supabase.co/storage/v1/object/public/instagram-carousels/{folder}/{file}
```

---

## 11. SLACK DISTRIBUTION

- **Canal:** #marketing (`C08PBK8QNBE`)
- **Workspace:** nexlexworkspace
- **Limitação:** MCP Slack não suporta upload de arquivos, só texto + URLs
- **Workaround:** sobe imagem no Supabase → manda URL no Slack → Slack faz unfurl

---

## 12. OPENSQUAD FRAMEWORK

O sistema usa o Opensquad como orquestrador multi-agente:

### Agentes do squad social-content:
- **Fábio Fonte** (researcher) — pesquisa tendências via web search
- **Iago Insta** (instagram-creator) — cria copy dos slides
- **Luna LinkedIn** (linkedin-creator) — cria post LinkedIn
- **Dani Design** (designer) — monta HTML/CSS e renderiza PNG
- **Revisor** (reviewer) — revisão de qualidade

### Execução:
- `inline` — agente roda na mesma conversa (persona switching)
- `subagent` — agente roda em background (Agent tool)
- `checkpoint` — pausa pra input do usuário (AskUserQuestion)

---

## 13. PERSONAS DA CARTEIRA

O sistema leva em conta 3 personas de clientes:

1. **Clínico-Solo** — dentista que faz tudo sozinho. Dor: tempo. Quer resultado sem virar gestor.
2. **Dentista + Braço-Direito** (ICP) — dono + secretária. Dor: empoderar o braço. Quer crescer como empresa.
3. **Clínica-Empresa** — processo e gestão. Dor: escala. Quer automação.

Cards de WhatsApp são segmentados por persona.

---

## 14. LIÇÕES APRENDIDAS (do feedback do usuário)

1. **Capa tem que ser chamativa** — fontes grandes, menos variação de tamanhos
2. **Nunca repetir elementos** entre cards (ex: estrelas em 2 cards)
3. **Alternar fundos** escuro/claro entre cards pra criar ritmo
4. **Logo variado** — símbolo nos internos, assinatura no CTA
5. **"Google" sempre com logo colorido** — nunca plain text
6. **Linhas de texto balanceadas** — larguras semelhantes entre linhas
7. **Highlight block com margin-top extra** — nunca sobrepor texto
8. **Sem barra no bottom** — body bg deve bater com gradient end
9. **Sem elementos tortos** — nada rotacionado
10. **Legendas curtas** — não repetir o que está no post
11. **Fotos reais > ilustrações** — quando usar imagem IA
12. **Cards WhatsApp precisam de imagem** — texto puro não engaja
13. **Email marketing = HTML inline** — não imagem pura

---

## 15. ARQUIVOS FIGMA CRIADOS

| Arquivo | URL | Conteúdo |
|---------|-----|----------|
| Nota Alta (4,9 vs 4,6) | `jICwoeq77RK4xQMfPwsr0u` | 3 cards + mockup Google + email + reels cover + whatsapp copa |
| +R$45K Harvard | `Cb7sV9ZRf2i6HQiQlsXO5B` | 7 cards |
| 3 Sinais | `R8fnBUILh48VCWpiPD32Qw` | 5 cards + mockup Google |
| Tráfego vs Indicação | `xPkyCl2Jy4IP0o1rJ7IjzZ` | 3 cards |

---

*Documentação gerada em 18/06/2026 — sessão Claude Code cse_01RXRUyw64HWp6pgoosUTsE4*
