# Brand Guide Visual — MirAI Consult

**Cliente:** MirAI Consult — "Tecnologia que vira decisão, eficiência e crescimento"
**Atualizado em:** 2026-06-20
**Referência:** Site miraiconsult.com

---

## Identidade Visual em Uma Frase

> Fundo escuro quente com orbs verdes, mensagem direta em tipografia tech, palavra de impacto destacada em verde neon. Tipografia Space Grotesk (headlines) + Inter (corpo). Estética futurista com referências japonesas. Logo "MirAI" sempre no rodapé.

---

## Paleta de Cores Oficial

| Cor | Hex | Uso |
|-----|-----|-----|
| Verde vibrante | `#00c46a` | COR PRINCIPAL — CTAs, ícones, destaques primários |
| Verde neon/lima | `#83e509` | Destaques fortes — pílulas, palavras-chave, ênfase máxima |
| Verde escuro | `#0a5f2a` | Gradientes, profundidade |
| Verde claro | `#7fe093` | Backgrounds sutis, badges de sucesso |
| Fundo escuro | `#1d1c1a` | Fundo principal (tom quente, NÃO preto puro) |
| Fundo médio | `#292824` | Cards, superfícies elevadas |
| Fundo claro | `#f0f0ee` | Versão light, fundo alternativo |
| Off-white quente | `#efedeb` | Texto principal sobre fundo escuro |
| Cinza médio | `#6b7a70` | Texto secundário |
| Cyan accent | `#16d6ff` | Destaques secundários, dados, tech |
| Roxo accent | `#a05bff` | Destaques terciários, IA/inovação |
| Amarelo alerta | `#ffde43` | Warnings, destaques pontuais |
| Vermelho erro | `#e06a5e` | Erros, alertas |

### Regras de uso da paleta
- **Fundo:** sempre `#1d1c1a` (escuro quente) ou `#f0f0ee` (claro quente) — NUNCA preto puro `#000`
- **Destaque primário:** verde `#00c46a` para CTAs e elementos interativos
- **Destaque de impacto:** lima neon `#83e509` para pílulas e palavras-chave (1-2 por card)
- **Texto sobre fundo escuro:** `#efedeb` (off-white quente)
- **Texto sobre fundo claro:** `#1d1c1a` (escuro quente)
- **Gradiente tech:** `#00c46a → #83e509` para efeitos premium
- **Acentos tech:** cyan `#16d6ff` e roxo `#a05bff` para dados e IA

---

## Tipografia

**Família display (headlines):** Space Grotesk (Google Fonts)
`https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap`

**Família corpo:** Inter (Google Fonts)
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap`

**Família dados/números (opcional):** Orbitron (Google Fonts) — para números de destaque e métricas
`https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800&display=swap`

| Elemento | Font | Weight | Tamanho | Case |
|----------|------|--------|---------|------|
| Pre-headline | Space Grotesk | Regular (400) | 28-32px | sentence case |
| Headline principal | Space Grotesk | Bold (700) | 70-90px | UPPERCASE |
| Pílula destaque | Space Grotesk | Bold (700) | 60-80px | UPPERCASE |
| Números de destaque | Orbitron | Bold (700) | 80-120px | — |
| Sub-headline / CTA | Inter | Semi Bold (600) | 22-26px | sentence case |
| Texto corpo | Inter | Regular (400) | 16-20px | sentence case |
| Logo "MirAI" | Space Grotesk | Bold (700) | 38-44px | MirAI |

### Tracking & line-height
- Headlines UPPERCASE: `letter-spacing: -0.02em`, `line-height: 0.95-1.05`
- Texto regular: `letter-spacing: 0`, `line-height: 1.4-1.5`

---

## Layout — Capa Padrão (1080x1350px)

```
┌─────────────────────────────┐
│                             │  ← padding top 80-120px
│      [ELEMENTO VISUAL]      │
│     (ícone tech/gráfico)    │  ← 30-40% da altura
│                             │
│   pre-headline pequeno      │
│                             │
│   HEADLINE UPPERCASE        │  ← linha 1
│   HEADLINE UPPERCASE        │  ← linha 2
│   [PÍLULA VERDE NEON]       │  ← destaque opcional
│                             |
│   sub-line opcional         │
│                             │
│                             │
│          MirAI              │  ← logo rodapé centralizado
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

A pílula `#83e509` (lima neon) é o destaque visual da MirAI.

```css
.pilula {
  background: #83e509;
  color: #1d1c1a;
  font-family: 'Space Grotesk';
  font-weight: 700;
  text-transform: uppercase;
  padding: 12px 32px;
  border-radius: 100px;
  display: inline-block;
  letter-spacing: -0.01em;
}
```

**Quando usar:**
- Destacar 1 palavra ou número crítico por capa
- Sempre na pergunta ou frase de impacto
- Apenas 1 pílula por slide

---

## Elemento Visual Central

Toda capa tem um **elemento simbólico tech no centro-topo**.

### Estilo visual
- Objetos ou ícones tech (dashboard, gráfico, engrenagem, circuito, foguete, IA)
- Tratamento duotone verde (efeito monocromático na paleta)
- Iluminação dramática, estética futurista
- Tamanho: 30-40% da altura do slide

### Exemplos de prompts para imagens
- "futuristic dashboard hologram, green neon glow, dark background, tech aesthetic, conceptual"
- "circuit board pattern forming a brain, green glowing nodes, dark warm background"
- "rocket launching through data streams, green and cyan glow, minimal dark background"

---

## Logo "MirAI"

Sempre no rodapé, centralizado. O "AI" em destaque.

```html
<div class="logo" style="font-family: 'Space Grotesk'; font-weight: 700; font-size: 40px; text-align: center;">
  <span style="color:#efedeb">Mir</span><span style="color:#00c46a">AI</span>
</div>
```

- Font: Space Grotesk Bold (700)
- Tamanho: 38-44px
- Cor: "Mir" em `#efedeb` + "AI" em `#00c46a` sobre fundo escuro
- Centralizado horizontalmente
- 80-100px do bottom

---

## Texturas e Detalhes

### Textura de fundo (opcional)
Grid sutil de linhas finas para dar sensação tech/matrix.
```css
.bg-grid::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(0,196,106,0.03) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0,196,106,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

### Vinhetas de luz
Orbs verdes nas bordas, blurred:
```css
.vinheta {
  background: radial-gradient(circle, #00c46a 0%, transparent 70%);
  filter: blur(120px);
  opacity: 0.2;
}
```

---

## Exemplos de Capas (referência)

### Capa 1 — "O futuro pertence a quem pensa melhor"
- Visual: cérebro formado por circuitos, duotone verde
- Pre-headline: "Mirai (未来) = futuro"
- Headline: "O FUTURO PERTENCE"
- Pílula: "A QUEM PENSA MELHOR"
- Logo rodapé: Mir + AI (verde)

### Capa 2 — "3x mais rápido"
- Visual: dashboard holográfico
- Pre-headline: "Decisões com dados"
- Headline: "3X MAIS RÁPIDO"
- Pílula: "QUE O FEELING"
- Logo rodapé

### Capa 3 — "Automação inteligente"
- Visual: engrenagens + IA
- Pre-headline: "Sua equipe foca no estratégico"
- Headline: "A IA CUIDA"
- Pílula: "DO RESTO"
- Logo rodapé

---

## Anti-patterns (NUNCA fazer)

1. Fundo preto puro `#000` ou branco puro `#fff` — sempre tons quentes
2. Tipografia Montserrat, Roboto, Poppins — sempre Space Grotesk + Inter
3. Cor amarela como destaque principal — amarelo é apenas para alertas
4. Elementos tortos/rotacionados sem propósito
5. Múltiplos tamanhos de fonte sem hierarquia clara (máx 3 níveis)
6. Logo sem o split de cor (Mir branco + AI verde)
7. Highlight neon `#83e509` sobrepondo texto — dar espaçamento
8. Linhas de texto desbalanceadas
9. Rodapé encostando na borda inferior — mínimo 130px do bottom
10. Gradient overlay 100% no bottom — máximo 92% de opacidade
11. Estética "corporativa genérica" — manter DNA tech/futurista
12. Jargão vazio (sinergia, alavancagem, disruptivo sem contexto)

---

*Brand Guide Visual v1.0 — MirAI Consult Jun/2026*
*Squad: Mirai Content*
