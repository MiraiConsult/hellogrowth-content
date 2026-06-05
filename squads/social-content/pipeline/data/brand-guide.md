# Brand Guide Visual — HelloGrowth

**Cliente:** HelloGrowth — "Mais reputação. Mais confiança. Mais vendas!"
**Atualizado em:** 2026-06-05
**Referência original:** Canva carrossel HelloGrowth + capas aprovadas pelo cliente

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

## Anti-patterns (NUNCA fazer)

1. Fundo preto, cinza ou branco — sempre verde escuro
2. Tipografia Montserrat, Roboto, Poppins — sempre Inter
3. Glassmorphism / blur translúcido
4. Múltiplas pílulas no mesmo slide
5. Pílula em outra cor que não `#bfff00`
6. Logo sem split de cor (Hello branco / Growth verde)
7. Foto de pessoa como elemento central
8. Headline em sentence-case nas capas
9. Cor de destaque que não seja lima neon
10. Texto branco puro `#ffffff` (usar `#edf0ee`)

---

*Brand Guide Visual v1.0 — HelloGrowth 2026*
*Squad: Social Content*
