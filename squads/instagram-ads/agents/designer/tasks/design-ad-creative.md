---
task: design-ad-creative
order: 1
input: squads/instagram-ads/output/ad-copy.md
output: squads/instagram-ads/output/*.html
---

# Tarefa: Criar Criativos HTML/CSS dos Anúncios

## Process

### Passo 1 — Ler a copy aprovada e o briefing visual

Leia o arquivo `squads/instagram-ads/output/ad-copy.md` na íntegra. Extraia para cada anúncio:
- **Headline** — texto principal de alto impacto
- **Texto de suporte** — benefício ou argumento secundário
- **CTA** — chamada para ação (ex: "Saiba mais", "Fale conosco")
- **Formato** — estático ou carrossel (e número de slides, se carrossel)
- **Direção visual** — paleta, tom de estilo e quaisquer instruções específicas do briefing

### Passo 2 — Criar os arquivos HTML/CSS

Para cada anúncio identificado na copy:

**Anúncios estáticos:** crie um único arquivo HTML com o layout completo do criativo.

**Anúncios em carrossel:** crie um arquivo HTML por slide, nomeado sequencialmente (ex: `ad-carousel-reputacao-01.html`, `ad-carousel-reputacao-02.html`).

Cada arquivo HTML deve:
- Definir o viewport em `1080x1350px` (formato 4:5 para Instagram Feed)
- Ser completamente autossuficiente — sem imports externos, sem fontes de CDN, sem imagens de URL
- Usar apenas CSS inline ou `<style>` embutido no `<head>`
- Aplicar a identidade visual da HelloGrowth: cores da marca, tipografia consistente, posicionamento de logo
- Incluir todos os elementos de copy (headline, texto de suporte, CTA) com hierarquia visual clara
- Usar CSS gradients, shapes e layouts para criar profundidade visual sem imagens externas
- Garantir alto contraste entre texto e fundo para legibilidade mobile

### Passo 3 — Nomear e salvar os arquivos

Salve cada arquivo em `squads/instagram-ads/output/` com nomenclatura descritiva:
- Estático: `ad-static-[tema]-[numero].html`
- Carrossel: `ad-carousel-[tema]-[numero]-slide[n].html`

Documente ao final a lista de arquivos criados, com o nome e o anúncio que cada um representa.

---

## Output Format

```yaml
criativos_gerados:
  - arquivo: string         # nome do arquivo .html
    anuncio: string         # título ou identificador do anúncio
    formato: string         # "static" ou "carousel"
    slide: integer|null     # número do slide (null se estático)
    headline: string        # headline aplicada no criativo
    cta: string             # CTA aplicado
    decisoes_visuais: string # decisões de design aplicadas (cores, layout, contraste)
```

---

## Output Example

```yaml
criativos_gerados:
  - arquivo: ad-static-reputacao-01.html
    anuncio: "Anúncio 1 — Reputação que Vende"
    formato: static
    slide: null
    headline: "Sua reputação online está custando clientes?"
    cta: "Descubra como resolver"
    decisoes_visuais: >
      Fundo preto com gradiente sutil para verde escuro na parte inferior.
      Headline em branco, peso bold, tamanho 72px — ocupa 40% do espaço vertical.
      Texto de suporte em cinza claro, tamanho 36px, abaixo da headline.
      CTA em card verde brilhante com texto preto, posicionado no terço inferior.
      Logo HelloGrowth no topo esquerdo, branco, tamanho reduzido.
      Contraste texto/fundo atende padrão WCAG AA.

  - arquivo: ad-carousel-prova-social-01-slide1.html
    anuncio: "Anúncio 2 — Prova Social (Carrossel)"
    formato: carousel
    slide: 1
    headline: "93% dos clientes leem avaliações antes de comprar"
    cta: null
    decisoes_visuais: >
      Slide de abertura. Fundo branco com accent verde na borda esquerda (8px).
      Dado estatístico centralizado, headline em verde da marca, peso black, 80px.
      Subtítulo explicativo em cinza escuro, 38px.
      Sem CTA neste slide — gancho para o próximo.
      Logo posicionado no rodapé centralizado.

  - arquivo: ad-carousel-prova-social-01-slide2.html
    anuncio: "Anúncio 2 — Prova Social (Carrossel)"
    formato: carousel
    slide: 2
    headline: "A HelloGrowth transforma avaliações em vendas"
    cta: "Fale com um especialista"
    decisoes_visuais: >
      Slide de conversão. Fundo verde da marca com padrão geométrico sutil em CSS.
      Headline em branco, peso bold, 64px. Três bullets de benefícios em branco, 32px.
      CTA em card branco com texto verde, bordas arredondadas, posicionado no rodapé.
      Logo em branco no topo direito.
```

---

## Quality Criteria

- Todos os arquivos HTML têm viewport definido em exatamente `1080x1350px` e são renderizáveis sem conexão externa
- Todos os elementos de copy aprovados (headline, texto de suporte, CTA) estão presentes e visíveis em cada criativo com hierarquia visual clara
- A identidade visual da HelloGrowth está aplicada de forma consistente: paleta de cores, posicionamento de logo e tipografia coerente entre peças

---

## Veto Conditions

- **Dependências externas detectadas** — qualquer `<link>`, `@import` ou `src` apontando para URL externa invalida o arquivo; deve ser refeito com recursos inline
- **Elementos de copy ausentes** — se headline, texto de suporte ou CTA da copy aprovada não estiverem presentes e legíveis no criativo, o arquivo não pode seguir para renderização
