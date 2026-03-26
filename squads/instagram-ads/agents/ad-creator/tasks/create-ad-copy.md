---
task: "Criar Copy do Anúncio"
order: 2
input:
  description: "Ângulo emocional selecionado pelo usuário (da task generate-angles.md) + tone-of-voice.md da HelloGrowth"
output:
  description: "Copy completa do anúncio: primary text, headline, description, CTA button — com variantes de hook e direção visual do criativo. Para formato carousel: todos os slides completos."
---

# Criar Copy do Anúncio

## Objetivo

Criar a copy completa do anúncio Instagram Feed (Meta Ads) a partir do ângulo selecionado. Entregar primary text, headline, description, CTA button, direção visual do criativo e hashtags — tudo pronto para subir na plataforma ou passar para produção do criativo.

## Processo

1. **Diagnóstico pré-escrita** — Antes de escrever qualquer linha, definir: nível de consciência do público (frio/morno/quente), sofisticação de mercado, Big Idea central do anúncio e driver emocional dominante do ângulo selecionado
2. **Recomendar tom e confirmar com usuário** — Ler o tone-of-voice.md e recomendar o tom mais adequado para o ângulo e nível de consciência. Apresentar recomendação ao usuário para aprovação antes de escrever
3. **Redigir 3 variações de hook** — Criar 3 versões do hook inicial do primary text usando estruturas diferentes:
   - **Pergunta direta**: desafia crença ou provoca reflexão
   - **Bold claim**: afirmação forte com dado ou especificidade
   - **Data lead**: abre com número ou estatística impactante
   Apresentar os 3 hooks ao usuário para seleção (checkpoint)
4. **Escrever o anúncio completo** com o hook aprovado:
   - **Primary Text**: hook selecionado (≤125 chars visíveis) + corpo (benefício, prova, contexto) + CTA textual
   - **Headline**: ≤40 caracteres, complementa o criativo visual
   - **Description**: frase de apoio para o headline (≤30 chars)
   - **CTA Button**: selecionar o botão mais adequado (Saiba Mais / Fale Agora / Cadastre-se / Comprar)
5. **Para formato carousel**: escrever todos os slides completos:
   - Slide de capa (cover): headline + subtext de gancho
   - 3 a 5 slides de corpo: headline do slide, texto de apoio (40-80 palavras por slide), palavra-chave de destaque visual
   - Slide final de CTA: oferta + ação + identidade HelloGrowth
6. **Escrever direção visual do criativo** — Brief para o designer com: formato recomendado (estático/carousel), paleta de cores, layout, elementos visuais, tipografia e tom visual
7. **Selecionar hashtags** — Mix de 5 a 15 hashtags (nicho + médio alcance + marca)

## Formato de Saída

```yaml
ad_copy:
  angle: "Nome do ângulo selecionado"
  awareness_level: "frio | morno | quente"
  framework: "AIDA | PAS | BAB | 4Ps"
  tone_approved: "Tom aprovado pelo usuário"
  big_idea: "Frase de uma linha que resume a Big Idea"

  hooks_presented:
    - type: "pergunta"
      text: "Versão pergunta (≤125 chars)"
    - type: "bold_claim"
      text: "Versão afirmação forte (≤125 chars)"
    - type: "data_lead"
      text: "Versão dado/número (≤125 chars)"
  hook_selected: "Texto do hook aprovado"

  primary_text:
    hook: "Hook selecionado (≤125 chars visíveis)"
    body: "Corpo do texto com benefício, prova e contexto"
    cta_text: "CTA textual dentro do primary text"

  headline: "Headline ≤40 caracteres"
  description: "Description ≤30 caracteres"
  cta_button: "Saiba Mais | Fale Agora | Cadastre-se | Comprar"

  carousel_slides:
    - slide: "cover"
      headline: "Texto principal do slide de capa"
      subtext: "Texto de apoio"
      accent_keyword: "Palavra em destaque visual"
      background_direction: "Direção de fundo/cor"
    - slide: 2
      headline: "Headline do slide"
      body: "Texto de apoio (40-80 palavras)"
      accent_keyword: "Palavra em destaque"
      background_direction: "Direção de fundo"
    - slide: "cta"
      headline: "Oferta no slide final"
      body: "Reforço de benefício"
      cta: "Ação clara do slide final"

  visual_direction:
    format: "Estático | Carousel"
    colors: "Paleta com códigos hex ou descrição"
    layout: "Descrição do layout e hierarquia visual"
    elements: "Elementos visuais específicos (ícones, fotos, gráficos)"
    typography: "Tamanho, peso e estilo da tipografia principal"
    visual_tone: "Tom visual (limpo, bold, minimal, dinâmico)"

  hashtags:
    - "#hashtagniche"
    - "#hashtagmedium"
    - "#hashtagbroad"
    - "#hellogrowth"
```

## Exemplo de Saída (parcial)

```yaml
ad_copy:
  angle: "Hemorragia silenciosa (Medo/Urgência)"
  awareness_level: "morno"
  framework: "PAS"
  tone_approved: "Direto e urgente com base em dado"
  big_idea: "Você perde vendas toda semana sem saber — reputação digital é o furo invisível no balde"

  hooks_presented:
    - type: "pergunta"
      text: "Quantas vendas você perdeu essa semana porque alguém duvidou da sua empresa online?"
    - type: "bold_claim"
      text: "Cada semana sem gestão de reputação, você perde leads que já estavam prontos para comprar."
    - type: "data_lead"
      text: "3x mais conversão. Esse é o resultado de quem gerencia reputação digital ativamente."
  hook_selected: "Cada semana sem gestão de reputação, você perde leads que já estavam prontos para comprar."

  primary_text:
    hook: "Cada semana sem gestão de reputação, você perde leads que já estavam prontos para comprar."
    body: "Pesquisa com 500 empresas B2B brasileiras mostrou: 68% dos decisores pesquisam a reputação online antes de fechar qualquer negócio. Se o que encontram não inspira confiança, o lead some — e você nem sabe que perdeu. A HelloGrowth rastreia, gerencia e fortalece sua reputação digital onde seus clientes pesquisam."
    cta_text: "Descubra quanto você está deixando na mesa →"

  headline: "Reputação que fecha vendas"
  description: "Diagnóstico gratuito"
  cta_button: "Saiba Mais"

  carousel_slides:
    - slide: "cover"
      headline: "Você está perdendo vendas sem saber"
      subtext: "E a causa não é o produto nem o preço →"
      accent_keyword: "PERDENDO VENDAS"
      background_direction: "Fundo escuro (#0d0d0d), texto branco, acento vermelho no keyword"
    - slide: 2
      headline: "68% dos decisores pesquisam antes de comprar"
      body: "Antes de atender qualquer ligação ou abrir qualquer proposta, seu futuro cliente já foi no Google. Pesquisou avaliações, leu comentários, verificou sua presença. Se o que encontrou não transmitiu confiança, ele já tomou a decisão — e não foi a favor de você."
      accent_keyword: "68%"
      background_direction: "Fundo cinza escuro, número em destaque bold"
    - slide: "cta"
      headline: "Diagnóstico gratuito de reputação"
      body: "Veja exatamente onde sua empresa perde credibilidade online e o que fazer para reverter isso."
      cta: "Acesse agora — HelloGrowth.com.br"

  visual_direction:
    format: "Carousel (4 slides)"
    colors: "Paleta escura: fundo #0d0d0d, texto #ffffff, acento vermelho #e63946"
    layout: "Texto centralizado, hierarquia clara: número/dado em destaque > headline > body"
    elements: "Sem stock photos — tipografia bold como elemento visual principal, ícones minimalistas"
    typography: "Headline: 48-64px bold sans-serif | Body: 18-20px regular | Keyword accent: 72px+ bold"
    visual_tone: "Direto e bold — sem elementos decorativos desnecessários"

  hashtags:
    - "#reputacaodigital"
    - "#marketingb2b"
    - "#vendasb2b"
    - "#gestaodemarca"
    - "#hellogrowth"
    - "#empreendedorismo"
    - "#negociosdigitais"
```

## Critérios de Qualidade

1. **Hook inequívoco**: Os primeiros 125 caracteres do primary text funcionam sozinhos — sem contexto adicional, o leitor entende o problema ou promessa
2. **Limites de plataforma respeitados**: Headline ≤40 chars, description ≤30 chars, sem claims proibidos pelo Meta Ads
3. **Coerência ângulo-copy**: O driver emocional do ângulo selecionado está presente do hook ao CTA — sem desvios temáticos

## Condições de Veto

- **REJEITAR** se headline ultrapassar 40 caracteres ou description ultrapassar 30 caracteres
- **REJEITAR** se a copy entregar sem direção visual do criativo — copy e visual são inseparáveis
