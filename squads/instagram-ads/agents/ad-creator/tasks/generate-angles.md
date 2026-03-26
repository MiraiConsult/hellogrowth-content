---
task: "Gerar Ângulos Criativos"
order: 1
input:
  description: "Oportunidade de mercado selecionada do research-results.md — inclui dados, contexto competitivo, público-alvo e nível de consciência estimado"
output:
  description: "5 ângulos emocionais distintos, cada um com driver psicológico, rascunho de hook, nível de consciência do público e framework de copy recomendado"
---

# Gerar Ângulos Criativos

## Objetivo

A partir da oportunidade selecionada, gerar 5 ângulos emocionais distintos para o anúncio. Cada ângulo usa um driver psicológico diferente para abordar o mesmo problema ou desejo do público. A diversidade de ângulos é a base para testes A/B eficientes no Meta Ads.

## Processo

1. **Analisar a oportunidade** — Extrair do research-results.md o dado-chave, o problema central do público, o diferencial da HelloGrowth e o nível de consciência estimado do segmento
2. **Mapear os 5 drivers psicológicos** — Criar um ângulo para cada um dos drivers abaixo, garantindo que cada abordagem explore um estado emocional genuinamente diferente:
   - 🔴 **Medo/Urgência** — "Se você não fizer X, vai perder Y"
   - 🟢 **Oportunidade** — "Essa é sua janela antes que todo mundo descubra"
   - 📚 **Educacional** — "Como fazer X em Y passos"
   - ↔️ **Contrário** — "O que ninguém te conta sobre X"
   - ⭐ **Aspiracional** — "Imagine ter X resultado em Y dias"
3. **Rascunhar hook para cada ângulo** — Escrever a primeira linha do primary text (max 125 caracteres) e um headline (max 40 caracteres), testando a força do gancho isolado
4. **Atribuir framework e nível de consciência** — Selecionar o framework de copy mais adequado (AIDA, PAS, BAB ou 4Ps) e definir o nível de consciência do público que este ângulo endereça melhor (frio, morno ou quente)
5. **Apresentar ângulos ao usuário** — Exibir os 5 ângulos estruturados e solicitar seleção antes de avançar para a criação do copy completo

## Formato de Saída

```yaml
opportunity_context:
  key_data: "Dado principal extraído do research"
  core_problem: "Problema central do público"
  awareness_level_estimate: "frio | morno | quente"

angles:
  - number: 1
    driver: "🔴 Medo/Urgência"
    title: "Nome interno do ângulo"
    hook_draft: "Primeiros 125 caracteres do primary text"
    headline_draft: "Headline com máx 40 caracteres"
    target_awareness: "frio | morno | quente"
    framework: "AIDA | PAS | BAB | 4Ps"
    emotional_logic: "Por que este driver funciona para este público"
    risk: "Ponto de atenção ou limite deste ângulo"
```

## Exemplo de Saída

```yaml
opportunity_context:
  key_data: "Empresas com gestão ativa de reputação online convertem 3x mais leads qualificados"
  core_problem: "Negócios B2B perdem vendas por falta de presença digital confiável, sem saber quantificar o impacto"
  awareness_level_estimate: "morno"

angles:
  - number: 1
    driver: "🔴 Medo/Urgência"
    title: "Hemorragia silenciosa"
    hook_draft: "Cada semana sem gestão de reputação, você perde leads que já estavam prontos para comprar."
    headline_draft: "Pare de perder vendas agora"
    target_awareness: "morno"
    framework: "PAS"
    emotional_logic: "Gestores B2B respondem a perdas tangíveis e mensuráveis — a dor de perder algo real é mais forte que a promessa de ganhar"
    risk: "Não exagerar na urgência para evitar rejeição do Meta Ads"

  - number: 2
    driver: "🟢 Oportunidade"
    title: "Janela competitiva"
    hook_draft: "Seus concorrentes ainda não descobriram isso. Empresas com reputação gerenciada convertem 3x mais."
    headline_draft: "Vantagem que poucos usam"
    target_awareness: "frio"
    framework: "BAB"
    emotional_logic: "FOMO competitivo + oportunidade exclusiva ativa o desejo de agir antes dos concorrentes"
    risk: "Validar o dado '3x' para não comprometer credibilidade"

  - number: 3
    driver: "📚 Educacional"
    title: "O método comprovado"
    hook_draft: "Como empresas B2B aumentam conversão em 3 etapas de gestão de reputação digital."
    headline_draft: "3 etapas para converter mais"
    target_awareness: "frio"
    framework: "AIDA"
    emotional_logic: "Público frio responde a educação — reduz resistência e posiciona HelloGrowth como autoridade antes de fazer oferta"
    risk: "Manter conteúdo acionável, não vago — cada etapa deve ser específica"

  - number: 4
    driver: "↔️ Contrário"
    title: "O mito do produto"
    hook_draft: "Você não perde vendas por causa do produto. Perde por causa do que falam de você online."
    headline_draft: "O erro que custa mais caro"
    target_awareness: "morno"
    framework: "PAS"
    emotional_logic: "Desafiar crença consolidada (problema é o produto/preço) cria dissonância cognitiva que força reflexão"
    risk: "Garantir que a afirmação contrária seja defensável com dados"

  - number: 5
    driver: "⭐ Aspiracional"
    title: "A empresa que você quer ser"
    hook_draft: "Imagine fechar o mês com leads qualificados chegando porque confiam na sua empresa — antes de falar com você."
    headline_draft: "Confiança que gera vendas"
    target_awareness: "quente"
    framework: "4Ps"
    emotional_logic: "Público quente já sabe do problema — quer visualizar o resultado e se identificar com a versão futura do negócio"
    risk: "Não prometer resultado específico sem base comprovável"
```

## Critérios de Qualidade

1. Os 5 ângulos exploram drivers psicológicos genuinamente distintos — nenhum repete a mesma emoção com palavras diferentes
2. Cada hook_draft tem no máximo 125 caracteres e cada headline_draft tem no máximo 40 caracteres
3. Os ângulos cobrem pelo menos 2 níveis de consciência diferentes (frio, morno, quente)

## Condições de Veto

- **REJEITAR** se dois ou mais ângulos explorarem o mesmo driver psicológico
- **REJEITAR** se qualquer hook_draft ultrapassar 125 caracteres ou headline_draft ultrapassar 40 caracteres
