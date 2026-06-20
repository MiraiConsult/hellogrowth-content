# Brand Guide Visual — Kaivaa

**Cliente:** Kaivaa — "Sua atendente de IA no Instagram e WhatsApp"
**Atualizado em:** 2026-06-20
**Referência:** Site kaivaa.online (mirai-chat-ai.vercel.app)

---

## Identidade Visual em Uma Frase

> Fundo escuro quente com textura, mensagem direta em UPPERCASE claro, palavra de impacto destacada em pílula amarelo vibrante. Tipografia Bricolage Grotesque (headlines) + Inter (corpo). Logo "Kaivaa" sempre no rodapé.

---

## Paleta de Cores Oficial

| Cor | Hex | Uso |
|-----|-----|-----|
| Amarelo vibrante | `#ffde43` | COR PRINCIPAL — pílulas, destaques, CTAs, ênfase |
| Amarelo claro | `#ffe76b` | Hover, variação mais leve do amarelo principal |
| Dourado/âmbar | `#d9a93f` | Acentos secundários, ícones, bordas |
| Dourado escuro | `#c79126` | Detalhes premium, sombra do amarelo |
| Fundo escuro | `#1d1c1a` | Fundo principal (tom quente, NÃO preto puro) |
| Fundo médio | `#292824` | Cards, superfícies elevadas |
| Fundo claro | `#f6f5f4` | Versão light, fundo alternativo |
| Off-white quente | `#efedeb` | Texto principal sobre fundo escuro |
| Cinza médio | `#6b6862` | Texto secundário, sombras |
| Verde sucesso | `#44b77b` | Status online, confirmações, sucesso |
| Vermelho alerta | `#e06a5e` | Erros, alertas |

### Regras de uso da paleta
- **Fundo:** sempre `#1d1c1a` (escuro quente) ou `#f6f5f4` (claro quente) — NUNCA preto puro `#000` ou branco puro `#fff`
- **Destaque:** amarelo `#ffde43` é a cor de ênfase principal — usar com impacto (1-2 elementos por card)
- **Texto sobre fundo escuro:** `#efedeb` (off-white quente)
- **Texto sobre fundo claro:** `#1d1c1a` (escuro quente)
- **Gradiente amarelo (opcional):** `#ffde43 → #d9a93f` para efeitos premium

---

## Tipografia

**Família display (headlines):** Bricolage Grotesque (Google Fonts)
`https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&display=swap`

**Família corpo:** Inter (Google Fonts)
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap`

| Elemento | Font | Weight | Tamanho | Case |
|----------|------|--------|---------|------|
| Pre-headline | Bricolage Grotesque | Regular (400) | 28-32px | sentence case |
| Headline principal | Bricolage Grotesque | Extra Bold (800) | 70-90px | UPPERCASE |
| Pílula destaque | Bricolage Grotesque | Extra Bold (800) | 60-80px | UPPERCASE |
| Sub-headline / CTA | Inter | Semi Bold (600) | 22-26px | sentence case |
| Texto corpo | Inter | Regular (400) | 16-20px | sentence case |
| Logo "Kaivaa" | Bricolage Grotesque | Bold (700) | 38-44px | Kaivaa |

### Tracking & line-height
- Headlines UPPERCASE: `letter-spacing: -0.02em`, `line-height: 0.95-1.05`
- Texto regular: `letter-spacing: 0`, `line-height: 1.4-1.5`

---

## Layout — Capa Padrão (1080x1350px)

```
┌─────────────────────────────┐
│                             │  ← padding top 80-120px
│      [ELEMENTO VISUAL]      │
│       (ícone/objeto)        │  ← 30-40% da altura
│                             │
│   pre-headline pequeno      │
│                             │
│   HEADLINE UPPERCASE        │  ← linha 1
│   HEADLINE UPPERCASE        │  ← linha 2
│   [PÍLULA AMARELA]          │  ← destaque opcional
│                             |
│   sub-line opcional         │
│                             │
│                             │
│          Kaivaa             │  ← logo rodapé centralizado
│                             │  ← padding bottom 80-100px
└─────────────────────────────┘
```

### Padding
- Laterais: 70-90px
- Topo: 80-120px
- Rodapé (acima do logo): 80-100px
- Entre elementos: 12-24px

---

## Pílula de Destaque (signature)

A pílula `#ffde43` é a marca registrada do visual Kaivaa.

```css
.pilula {
  background: #ffde43;
  color: #1d1c1a;
  font-family: 'Bricolage Grotesque';
  font-weight: 800;
  text-transform: uppercase;
  padding: 12px 32px;
  border-radius: 100px;
  display: inline-block;
  letter-spacing: -0.01em;
}
```

**Quando usar:**
- Destacar 1 palavra ou número crítico por capa
- Sempre na pergunta ou frase de impacto (não em texto corrido)
- Apenas 1 pílula por slide

---

## Elemento Visual Central

Toda capa tem um **elemento simbólico no centro-topo**.

### Estilo visual
- Objetos ou ícones grandes (celular com DMs, balão de chat, relógio, foguete, robô amigável, etc.)
- Tratamento duotone amarelo/dourado (efeito monocromático na paleta da marca)
- Iluminação dramática, fundo escuro quente
- Tamanho: 30-40% da altura do slide

### Exemplos de prompts para imagens
- "smartphone showing chat bubbles, golden yellow duotone, dark warm background, dramatic lighting, conceptual"
- "lightning bolt icon, vibrant yellow neon, speed concept, dark charcoal textured background"
- "friendly robot assistant, yellow golden tones, warm dark background, modern minimal"

---

## Logo "Kaivaa"

Sempre no rodapé, centralizado.

```html
<div class="logo" style="font-family: 'Bricolage Grotesque'; font-weight: 700; font-size: 40px; text-align: center;">
  <span style="color:#ffde43">Kaivaa</span>
</div>
```

- Font: Bricolage Grotesque Bold (700)
- Tamanho: 38-44px
- Cor: `#ffde43` sobre fundo escuro / `#1d1c1a` sobre fundo claro
- Centralizado horizontalmente
- 80-100px do bottom

---

## Texturas e Detalhes

### Textura de fundo (opcional)
SVG noise filter sutil aplicado ao fundo escuro para dar sensação de papel/concreto.
```css
.bg-texture::after {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,...noise...");
  opacity: 0.06;
  mix-blend-mode: overlay;
}
```

### Vinhetas de luz
Orbs amarelos/dourados nas bordas, blurred:
```css
.vinheta {
  background: radial-gradient(circle, #d9a93f 0%, transparent 70%);
  filter: blur(100px);
  opacity: 0.3;
}
```

### Elementos geométricos
Formas sutis, traços diagonais em `#ffde43` ou `#d9a93f` nos cantos (5-8% de presença visual).

---

## Exemplos de Capas (referência)

### Capa 1 — "Quem respondeu?"
- Visual: celular com bolhas de chat, duotone amarelo
- Pre-headline: "Seu cliente mandou mensagem às 23h"
- Headline: "QUEM RESPONDEU?"
- Pílula: "A KAIVAA 👋"
- Logo rodapé

### Capa 2 — "8 segundos vs 47 minutos"
- Visual: relógio/cronômetro, dourado vibrante
- Pre-headline: "Tempo médio de resposta"
- Headline: "8 SEGUNDOS"
- Pílula: "VS 47 MINUTOS"
- Sub: "IA vs atendimento manual"
- Logo rodapé

### Capa 3 — "Vendendo dormindo"
- Visual: ícone de lua/estrelas + cifrão, amarelo sobre fundo escuro
- Pre-headline: "Enquanto você dormia"
- Headline: "A KAIVAA VENDEU"
- Pílula: "3 PEDIDOS 🛒"
- Logo rodapé

---

## Anti-patterns (NUNCA fazer)

1. Fundo preto puro `#000` ou branco puro `#fff` — sempre tons quentes (`#1d1c1a` ou `#f6f5f4`)
2. Tipografia Montserrat, Roboto, Poppins — sempre Bricolage Grotesque (headlines) + Inter (corpo)
3. Cor verde como destaque principal — verde `#44b77b` é APENAS para status de sucesso
4. Elementos tortos/rotacionados
5. Múltiplos tamanhos de fonte sem hierarquia clara (máx 3 níveis)
6. Logo inteira em todos os cards — variar
7. Highlight amarelo `#ffde43` sobrepondo texto — dar espaçamento extra
8. Linhas de texto desbalanceadas (uma longa, outra curta pela metade)
9. Rodapé encostando na borda inferior — mínimo 130px do bottom
10. Gradient overlay chegando a 100% no bottom — NUNCA criar barra sólida. Máximo 92% de opacidade
11. Mesmo elemento visual repetido em múltiplos cards
12. Jargão SaaS (omnichannel, stack, pipeline) — linguagem simples e direta

---

*Brand Guide Visual v1.0 — Kaivaa Jun/2026*
*Squad: Kaivaa Content*
