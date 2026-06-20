# Brand Guide Visual — HelloGrowth

**Cliente:** HelloGrowth — "Mais reputação. Mais confiança. Mais vendas!"
**Atualizado em:** 2026-06-08
**Referência original:** Figma editado pelo cliente (Nota Alta V8) + Canva capas aprovadas

---

## Identidade Visual em Uma Frase

> Fundo verde escuro com textura, mensagem direta em UPPERCASE branco, palavra de impacto destacada em pílula verde lima neon. Tipografia Inter. Logo "HelloGrowth" sempre no rodapé.

---

## Paleta de Cores Oficial

| Cor | Hex | Uso |
|-----|-----|-----|
| Verde escuro | `#004d40` | Fundo principal |
| Verde médio escuro | `#1b6b5b` | Gradient de fundo |
| Verde médio | `#28ae61` | Logo "Growth", ícones, estrelas |
| Verde lima neon | `#bfff00` | DESTAQUE — pílulas, palavras-chave |
| Off-white | `#edf0ee` | Texto principal |
| Cinza escuro | `#4a5550` | Texto secundário, sombras |

### Regras de uso da paleta
- **Fundo:** sempre verde escuro `#004d40` ou gradient `#004d40 → #1b6b5b`
- **Destaque:** lima neon `#bfff00` é a única cor de ênfase — usar com parcimônia (1 palavra por capa)
- **Logo:** "Hello" em `#edf0ee` + "Growth" em `#28ae61`
- **Texto:** sempre `#edf0ee` (off-white) — nunca branco puro `#fff`

---

## Tipografia

**Família única:** Inter (Google Fonts)
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap`

| Elemento | Weight | Tamanho | Case |
|----------|--------|---------|------|
| Pre-headline | Regular (400) | 28-32px | sentence case |
| Headline principal | Black (900) | 70-90px | UPPERCASE |
| Pílula destaque | Black (900) | 60-80px | UPPERCASE |
| Sub-headline / CTA | Medium (500) | 22-26px | sentence case |
| Logo "HelloGrowth" | Bold (700) | 38-44px | Hello + Growth |

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
│   [PÍLULA LIMA NEON]        │  ← destaque opcional
│                             |
│   sub-line opcional         │
│                             │
│                             │
│        HelloGrowth          │  ← logo rodapé centralizado
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

A pílula `#bfff00` é a marca registrada do visual HelloGrowth.

```css
.pilula {
  background: #bfff00;
  color: #004d40;
  font-family: 'Inter';
  font-weight: 900;
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

Toda capa tem um **elemento simbólico no centro-topo** — não foto de pessoa.

### Estilo visual
- Objetos ou ícones grandes (telefone, estrelas, lupa, gráfico, troféu, etc.)
- Tratamento duotone verde (efeito monocromático na paleta da marca)
- Iluminação dramática
- Tamanho: 30-40% da altura do slide

### Exemplos de prompts Gamma
- "vintage rotary phone hanging by spiral cord, green duotone, dark green background, dramatic lighting, conceptual"
- "five filled stars in vibrant green, centered, glowing, dark green textured background"
- "magnifying glass icon, green neon, search context, dark green gradient background"

---

## Logo "HelloGrowth"

Sempre no rodapé, centralizado.

```html
<div class="logo">
  <span style="color:#edf0ee">Hello</span><span style="color:#28ae61">Growth</span>
</div>
```

- Font: Inter Bold (700)
- Tamanho: 38-44px
- Centralizado horizontalmente
- 80-100px do bottom

---

## Texturas e Detalhes

### Textura de fundo (opcional)
SVG noise filter sutil aplicado ao fundo verde para dar sensação de papel/concreto.
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
Orbs verdes mais claros nas bordas, blurred:
```css
.vinheta {
  background: radial-gradient(circle, #28ae61 0%, transparent 70%);
  filter: blur(100px);
  opacity: 0.4;
}
```

### Elementos geométricos
Setas, formas em Z, traços diagonais em `#bfff00` ou `#28ae61` nos cantos (5-8% de presença visual).

---

## Exemplos de Capas (referência aprovada)

### Capa 1 — "Pra quem ligar primeiro"
- Visual: telefone vintage suspenso, duotone verde
- Pre-headline: "É assim que você sabe"
- Headline: "PRA QUEM LIGAR PRIMEIRO" (sem pílula)
- Logo rodapé

### Capa 2 — "4,9 vs 4,6"
- Visual: 5 estrelas verdes preenchidas
- Pre-headline: "**4,9 estrelas** _(em lima neon)_ e mesmo assim"
- Headline: "PERDENDO PRA QUEM"
- Pílula: "TEM 4,6?"
- Logo rodapé

### Capa 3 — "Qual posição?"
- Visual: forma geométrica Z verde lima no canto + lupa inline
- Pre-headline: "Pesquisa o nome da sua **especialidade + sua cidade** _(em lima neon)_"
- Headline: "VOCÊ APARECE EM"
- Pílula: "QUAL POSIÇÃO? 🔍"
- Sub: "Não sabe? **A gente descobre com você**"
- Logo rodapé

---

## Padrões Visuais Aprovados (Figma V8 — Jun/2026)

Extraído do Figma editado pelo cliente. Usar como referência exata.

### Fundo — Orbs de luz com blur 500px

Não usar `radial-gradient` simples. O fundo correto são **elipses sólidas com LAYER_BLUR 500px** sobre base `#004d40`:

**Fundo escuro (cards 1, 3):**
- Base: `#004d40`
- Orb top-left: `#1d884a` (555x529px, blur 500px, posição -80,-66)
- Orb mid-right: `#1d884a` (556x562px, blur 500px, posição 713,295)
- Orb bottom-left: `#116836` (626x600px, blur 500px, posição -239,857)

**Fundo claro (card 2):**
- Base: `#edf0ed` com overlay de orbs a 50% opacidade
- Orbs: `#28ae61` (50%) nas mesmas posições + orb `#bfff00` (20%) extra

### Tipografia — Hierarquia de 3 níveis

| Nível | Font | Size | Weight | Cor | Exemplo |
|-------|------|------|--------|-----|---------|
| Headline principal | Inter | 114-132px | Black (900) | `#bfff00` ou `#edf0ed` | "tem 4,9 estrelas", "PRA QUEM" |
| Texto médio | Inter | 52-58px | Semi Bold-Extra Bold | `#edf0ed` 65% ou `#004d40` | "e mesmo assim perdendo" |
| Corpo | Inter | 30-38px | Medium (500) | `#1b6b5b` ou `#edf0ed` 70% | textos explicativos |

**Regras de texto:**
- Quebra de linhas SEMPRE balanceada (larguras semelhantes entre linhas)
- "Google" sempre com logo colorido (Azul/Vermelho/Amarelo/Verde), dentro de pílula branca 60% quando fundo escuro
- Highlight verde `#28ae61` (NÃO `#bfff00`) com radius 25px para "virando avaliação" no card 3
- Nunca sobrepor texto com highlight — dar margin-top extra (18-22px)

### Glass Cards

- **Fundo escuro:** `rgba(255,255,255,0.10)`, border `rgba(255,255,255,0.12)`, radius 32px
- Sem backdrop-filter no Figma (o blur vem dos orbs de fundo, não do glass)
- Glass é sutil — apenas delimita a área de texto

### Comparativo Visual (cards tipo 4,9 vs 4,6)

- Dois boxes lado a lado: `436x354px`, gap `24px`
- **Loser:** fill `rgba(0,77,64,0.06)`, border `rgba(0,77,64,0.12)`, radius `24px`
- **Winner:** fill `#004d40` sólido, rating em `#bfff00`, badge `#bfff00` com radius `63px`
- Nota gigante: `103px Inter Black`

### Rodapé — Logo + Seta

| Card | Logo usado | Posição | Seta |
|------|-----------|---------|------|
| Capa | Símbolo light | x:33 y:1074 (205x164px) | Componente seta x:874 y:1058 |
| Corpo | Símbolo normal | x:44 y:1075 (206x165px) | Ellipse #28ae61 84px x:916 y:1108 |
| CTA (último) | Wordmark light | x:364 y:1129 (352x72px) centralizadoipo | Sem seta |

**Regra:** nunca usar logo full (assinatura completa) em todos os cards. Variar entre símbolo e wordmark. Assinatura completa = último card ou CTA apenas.

### Handle @hellogrowth__

- Sempre no topo, centralizado
- Inter Medium 18px
- `#edf0ed` no escuro, `#004d40` no claro
- Posição: x:472 y:40

---

## Anti-patterns (NUNCA fazer)

1. Fundo preto, cinza ou branco — sempre verde escuro `#004d40` ou claro `#edf0ed`
2. Tipografia Montserrat, Roboto, Poppins — sempre Inter
3. Elementos tortos/rotacionados
4. Múltiplos tamanhos de fonte sem hierarquia clara (máx 3 níveis)
5. Logo inteira (assinatura) em todos os cards — variar
6. Highlight lima `#bfff00` sobrepondo texto — dar espaçamento extra
7. Linhas de texto desbalanceadas (uma longa, outra curta pela metade)
8. "Google" como texto plain — sempre usar logo colorido
9. Rodapé encostando na borda inferior — mínimo 130px do bottom
13. Gradient overlay chegando a 100% no bottom — NUNCA criar barra sólida no final do card. Máximo 92% de opacidade
10. Mesmo elemento visual repetido em múltiplos cards (ex: estrelas em 2 cards)
11. Texto branco puro `#ffffff` — usar `#edf0ed`
12. Pílula highlight em `#bfff00` no card 3 — usar `#28ae61` (verde médio)

---

## Arquivo Figma de Referência

**URL:** https://www.figma.com/design/jICwoeq77RK4xQMfPwsr0u
**Conteúdo:** 3 cards do carrossel "Nota Alta" (4,9 vs 4,6) — editado e aprovado pelo cliente

---

*Brand Guide Visual v2.0 — HelloGrowth Jun/2026*
*Squad: Social Content*
