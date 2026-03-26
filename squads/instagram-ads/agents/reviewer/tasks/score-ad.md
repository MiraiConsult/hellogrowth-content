---
task: score-ad
order: 1
input: squads/instagram-ads/output/ad-copy.md + squads/instagram-ads/output/*.png + squads/instagram-ads/pipeline/data/quality-criteria.md
output: squads/instagram-ads/output/review-result.md (seção: scoring)
---

# Tarefa: Pontuar o Anúncio

## Process

### Passo 1 — Carregar os materiais de avaliação

Leia `pipeline/data/quality-criteria.md` na íntegra para internalizar os 10 critérios, seus pesos e as regras de decisão antes de abrir qualquer material do anúncio. Em seguida, leia `squads/instagram-ads/output/ad-copy.md` completo — primary text, headline, CTA e direção visual. Por fim, analise os arquivos `*.png` disponíveis em `squads/instagram-ads/output/` como representação da arte final do criativo.

### Passo 2 — Avaliar cada critério individualmente

Percorra os 10 critérios na ordem abaixo, avaliando um de cada vez sem interferência entre eles. Para cada critério:
- Identifique a(s) passagem(ns) específica(s) da copy ou elemento(s) visual(is) sendo avaliados
- Atribua uma nota de **1 a 10** com base nos sub-itens do critério em `quality-criteria.md`
- Escreva uma justificativa de 1 a 2 frases com a evidência que sustenta a nota — positiva ou negativa
- Registre qualquer passagem ou elemento específico que motivou dedução de ponto

Critérios a avaliar (na ordem):
1. **Hook/Scroll-Stop** — os primeiros 125 caracteres do texto e o gancho visual param o scroll?
2. **Proposta de Valor** — o benefício é claro, específico e diferenciado?
3. **CTA** — é específico, único e calibrado para o estágio do funil?
4. **Framework de Persuasão** — AIDA, PAS, BAB ou 4Ps aplicado corretamente do hook ao CTA?
5. **Brand Voice** — tom HelloGrowth presente; vocabulário correto; palavras proibidas ausentes?
6. **Técnica de Copy** — frases curtas, sem clichês, linguagem natural e conversacional?
7. **Layout/Formato** — formato 4:5, hierarquia visual, contraste e legibilidade mobile?
8. **Identidade Visual** — cores, tipografia e logo da HelloGrowth aplicados corretamente?
9. **Coerência Copy-Visual** — visual e copy se reforçam mutuamente sem contradição?
10. **Adequação à Plataforma** — respeita regras do Instagram e Meta Ads (texto <20%, sem links na copy)?

### Passo 3 — Calcular média ponderada e aplicar regras de decisão

Some os produtos (nota × peso) de cada critério conforme os pesos de `quality-criteria.md` e divida pelo total de pesos para obter a média ponderada final. Aplique as regras de decisão:
- **APROVADO**: média ≥ 7,0 e nenhum critério abaixo de 4
- **APROVADO COM RESSALVAS**: média ≥ 7,0 e critério não-crítico entre 4 e 6
- **REJEITADO**: média < 7,0 ou qualquer critério com nota < 4 (trigger automático)

Identifique o elemento específico da copy ou do visual responsável por cada dedução relevante para fundamentar o feedback da próxima tarefa.

---

## Output Format

```yaml
scoring:
  ad_id: string                  # identificador do anúncio avaliado
  reviewed_at: string            # data da revisão no formato YYYY-MM-DD
  criteria:
    - id: string                 # slug do critério: ex. "hook-scroll-stop"
      name: string               # nome do critério conforme quality-criteria.md
      weight: number             # peso do critério em decimal: ex. 0.15
      score: number              # nota de 1 a 10
      justification: string      # justificativa objetiva em 1-2 frases
      evidence: string           # trecho ou elemento específico que embasou a nota
  weighted_average: number       # média ponderada calculada (arredondada para 1 casa)
  verdict: string                # APROVADO | APROVADO COM RESSALVAS | REJEITADO
  verdict_reason: string         # regra de decisão aplicada que gerou o veredicto
  flags:
    - criterion: string          # critério que disparou flag
      type: string               # VETO | ATENÇÃO
      note: string               # descrição do problema
```

---

## Output Example

```yaml
scoring:
  ad_id: "instagram-feed-reputacao-v1"
  reviewed_at: "2026-03-26"
  criteria:
    - id: hook-scroll-stop
      name: Hook / Scroll-Stop
      weight: 0.15
      score: 8
      justification: "Os primeiros 120 caracteres entregam dado concreto ('87% dos clientes desistem após ler avaliação negativa') com driver emocional de medo, forte o suficiente para parar o scroll."
      evidence: "'87% dos seus clientes em potencial desistem antes de ligar. Por causa de avaliações que você ainda não respondeu.'"

    - id: proposta-de-valor
      name: Proposta de Valor
      weight: 0.10
      score: 7
      justification: "O benefício está presente e específico, mas o diferencial competitivo frente a outras soluções de reputação não está explícito na copy."
      evidence: "Ausência de elemento diferenciador; a promessa 'transforme avaliações em vendas' é compartilhável por concorrentes sem alteração."

    - id: cta
      name: CTA
      weight: 0.10
      score: 9
      justification: "CTA único, específico e alinhado ao estágio de conscientização: 'Solicite um diagnóstico gratuito' convida sem comprometer, ideal para público frio."
      evidence: "'Solicite um diagnóstico gratuito →'"

    - id: framework-de-persuasao
      name: Framework de Persuasão
      weight: 0.10
      score: 8
      justification: "PAS aplicado corretamente: problema (avaliações negativas ignoradas), agitação (perda de clientes mensurada), solução (HelloGrowth como sistema de resposta)."
      evidence: "Estrutura P→A→S identificável do headline ao CTA sem quebras de lógica."

    - id: brand-voice
      name: Brand Voice
      weight: 0.10
      score: 9
      justification: "Tom direto e orientado a resultado alinhado à HelloGrowth; vocabulário da marca presente ('estratégia', 'resultado', 'comprovado'); nenhuma palavra proibida identificada."
      evidence: "Sem ocorrências de 'hack', 'truque', 'segredo' ou equivalentes na copy completa."

    - id: tecnica-de-copy
      name: Técnica de Copy
      weight: 0.05
      score: 7
      justification: "Frases curtas e diretas na maior parte; um parágrafo de 3 linhas no corpo quebra o ritmo e pode ser dividido para melhor leitura mobile."
      evidence: "Parágrafo: 'Com o método HelloGrowth, você passa a monitorar, responder e transformar cada avaliação recebida em argumento de venda para novos clientes.'"

    - id: layout-formato
      name: Layout / Formato
      weight: 0.10
      score: 6
      justification: "Formato 4:5 correto e contraste adequado, mas a hierarquia visual coloca o logo em posição de destaque competindo com o headline — inversão de prioridade."
      evidence: "Logo ocupa 18% da área superior; headline posicionado abaixo com fonte menor que o nome da marca."

    - id: identidade-visual
      name: Identidade Visual
      weight: 0.10
      score: 8
      justification: "Paleta de cores da HelloGrowth aplicada corretamente; tipografia consistente com a identidade; logo presente sem distorções."
      evidence: "Verde #00A651 e branco #FFFFFF nas proporções corretas; sem desvios de tipografia identificados."

    - id: coerencia-copy-visual
      name: Coerência Copy-Visual
      weight: 0.10
      score: 7
      justification: "Copy e visual comunicam o mesmo problema (reputação → vendas), mas a imagem de fundo genérica (pessoa no computador) não reforça a especificidade da dor mapeada na copy."
      evidence: "Copy menciona 'avaliações não respondidas'; visual não faz referência a reviews, plataformas ou contexto de reputação digital."

    - id: adequacao-plataforma
      name: Adequação à Plataforma
      weight: 0.10
      score: 9
      justification: "Sem links na copy; texto no criativo estimado em ~12% da área total, dentro da regra de 20% do Meta Ads; funcional em visualização mobile."
      evidence: "Nenhum URL ou @menção no primary text; proporção de texto no criativo dentro do limite."

  weighted_average: 7.7
  verdict: APROVADO COM RESSALVAS
  verdict_reason: "Média ≥ 7,0, mas critério Layout/Formato com score 6 (não-crítico) — aprovado com ressalvas conforme regra de decisão."
  flags:
    - criterion: layout-formato
      type: ATENÇÃO
      note: "Hierarquia visual invertida: logo em posição de destaque sobre o headline. Corrigir na próxima iteração."
```

---

## Quality Criteria

- Todos os 10 critérios estão presentes no output com score, justificativa e evidência preenchidos — score sem justificativa invalida a avaliação
- A média ponderada reflete corretamente os pesos definidos em `quality-criteria.md` — erro de cálculo gera veredicto incorreto
- Toda nota abaixo de 7 inclui `evidence` com trecho ou elemento específico da copy ou do visual que embasou a dedução — generalidades não são aceitáveis como evidência

---

## Veto Conditions

- **Critério com score < 4:** aciona rejeição automática independentemente da média — o campo `flags` deve registrar `type: VETO` com descrição do elemento que causou o veto
- **Avaliação sem leitura da copy completa:** se algum critério de copy for avaliado sem referência a trechos reais do `ad-copy.md`, a tarefa deve ser reiniciada — scores baseados em suposição sobre o conteúdo invalidam toda a revisão
