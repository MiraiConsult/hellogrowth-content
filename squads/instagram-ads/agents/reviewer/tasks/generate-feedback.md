---
task: generate-feedback
order: 2
input: squads/instagram-ads/output/review-result.md (seção: scoring)
output: squads/instagram-ads/output/review-result.md (seção: feedback)
---

# Tarefa: Gerar Feedback Detalhado

## Process

### Passo 1 — Analisar scores e classificar critérios

Leia a seção `scoring` do `review-result.md` gerada pela tarefa anterior. Classifique cada critério em três grupos:
- **Pontos fortes** (score ≥ 8): merecem elogio específico com referência ao elemento que funcionou
- **Melhorias sugeridas** (score entre 6 e 7): não bloqueiam aprovação, mas impactam performance — feedback não-bloqueante
- **Correções obrigatórias** (score < 6 ou flags VETO/ATENÇÃO): devem ser corrigidas antes de publicação — feedback bloqueante com ação clara

### Passo 2 — Escrever feedback específico e acionável

Para cada critério que não atingiu 8/10, escreva feedback no seguinte formato:
- **Localização exata**: referencie o trecho da copy ou o elemento visual específico
- **O que está errado e por quê**: diagnóstico técnico baseado no critério, não em opinião
- **Como corrigir**: instrução direta e executável — não "melhore o hook" mas "substitua os primeiros 125 caracteres por [abordagem específica]"

Para critérios com score ≥ 8, escreva um elogio específico que destaque o que funcionou e por quê — evita que o agente de criação abandone o que está funcionando na próxima iteração.

### Passo 3 — Compilar o documento de revisão final

Monte o documento completo de revisão com as seguintes seções em ordem:
1. **Veredicto**: APROVADO / APROVADO COM RESSALVAS / REJEITADO, com a regra de decisão aplicada
2. **Tabela de Scores**: todos os 10 critérios com nota, peso e média ponderada
3. **Pontos Fortes**: elogios específicos aos critérios com score ≥ 8
4. **Correções Obrigatórias** `[BLOQUEANTE]`: lista numerada do que deve ser corrigido antes de publicar
5. **Sugestões** `[NÃO-BLOQUEANTE]`: melhorias que elevam performance mas não impedem aprovação
6. **Caminho para Aprovação**: se veredicto for REJEITADO, lista numerada e ordenada de todas as correções obrigatórias com descrição da ação específica — esse campo é o protocolo de retrabalho para o ad-creator

---

## Output Format

```yaml
feedback:
  verdict: string                    # APROVADO | APROVADO COM RESSALVAS | REJEITADO
  verdict_reason: string             # regra de decisão aplicada
  weighted_average: number           # média ponderada do scoring

  scoring_table:
    - criterion: string              # nome do critério
      weight: string                 # peso formatado: ex. "15%"
      score: number                  # nota de 1 a 10
      status: string                 # FORTE | OK | ATENÇÃO | BLOQUEANTE

  strengths:
    - criterion: string              # critério com score ≥ 8
      praise: string                 # elogio específico com referência ao elemento

  required_changes:
    - id: number                     # número da correção obrigatória
      criterion: string              # critério que originou a correção
      location: string               # onde está o problema (ex: "headline", "imagem de fundo")
      diagnosis: string              # o que está errado e por quê
      action: string                 # instrução específica de como corrigir

  suggestions:
    - criterion: string              # critério com score 6-7 (não-bloqueante)
      location: string               # onde está o ponto de melhoria
      suggestion: string             # sugestão de otimização

  path_to_approval:                  # preenchido APENAS se veredicto for REJEITADO
    - step: number
      action: string                 # ação obrigatória numerada em ordem de prioridade
```

---

## Output Example

```yaml
feedback:
  verdict: APROVADO COM RESSALVAS
  verdict_reason: "Média 7,7 ≥ 7,0; critério Layout/Formato com score 6 (não-crítico) — aprovado com ressalvas conforme regra de decisão."
  weighted_average: 7.7

  scoring_table:
    - criterion: Hook / Scroll-Stop
      weight: "15%"
      score: 8
      status: FORTE
    - criterion: Proposta de Valor
      weight: "10%"
      score: 7
      status: OK
    - criterion: CTA
      weight: "10%"
      score: 9
      status: FORTE
    - criterion: Framework de Persuasão
      weight: "10%"
      score: 8
      status: FORTE
    - criterion: Brand Voice
      weight: "10%"
      score: 9
      status: FORTE
    - criterion: Técnica de Copy
      weight: "5%"
      score: 7
      status: OK
    - criterion: Layout / Formato
      weight: "10%"
      score: 6
      status: ATENÇÃO
    - criterion: Identidade Visual
      weight: "10%"
      score: 8
      status: FORTE
    - criterion: Coerência Copy-Visual
      weight: "10%"
      score: 7
      status: OK
    - criterion: Adequação à Plataforma
      weight: "10%"
      score: 9
      status: FORTE

  strengths:
    - criterion: CTA
      praise: "'Solicite um diagnóstico gratuito →' é um CTA exemplar para público frio: oferece valor sem exigir comprometimento, com verbo no imperativo e indicador visual de ação. Manter esse padrão nas próximas versões."
    - criterion: Brand Voice
      praise: "Copy totalmente alinhada ao tom HelloGrowth — direta, orientada a resultado, sem nenhuma palavra proibida. Vocabulário da marca ('estratégia', 'comprovado') integrado de forma natural, não forçada."
    - criterion: Hook / Scroll-Stop
      praise: "O dado dos 87% no hook cria parada imediata: número específico + dor direta + driver de medo. Combinação eficaz que entrega a proposta de valor nos primeiros 120 caracteres."

  required_changes: []

  suggestions:
    - criterion: Layout / Formato
      location: "Posicionamento do logo no terço superior do criativo"
      suggestion: "Reduzir o logo para ~8% da área e movê-lo para o rodapé ou canto superior direito. Elevar o headline para a posição principal, com fonte 20-30% maior que o logo. A hierarquia visual deve priorizar a mensagem, não a marca."
    - criterion: Proposta de Valor
      location: "Corpo do primary text — ausência de diferenciador competitivo"
      suggestion: "Incluir um elemento de diferenciação específico da HelloGrowth frente a concorrentes — pode ser metodologia, velocidade de resposta, integração de plataformas ou resultado mensurável. Exemplo: 'Diferente de ferramentas genéricas, o método HelloGrowth é construído para converter reputação em vendas, não só em estrelas.'"
    - criterion: Coerência Copy-Visual
      location: "Imagem de fundo — pessoa genérica no computador"
      suggestion: "Substituir por imagem que remeta diretamente ao contexto de avaliações: tela de Google Reviews, notificação de avaliação, ou dashboard de reputação. A especificidade visual reforça a copy e elimina o gap entre mensagem e imagem."

  path_to_approval: []
```

---

## Quality Criteria

- Todo critério com score abaixo de 8 tem feedback com localização exata, diagnóstico técnico e ação específica — feedback genérico sem localização não tem valor operacional
- A separação entre `required_changes` (bloqueante) e `suggestions` (não-bloqueante) é rigorosa e baseada nas regras de decisão de `quality-criteria.md` — a mistura dos dois tipos paralisa o processo de retrabalho
- O `path_to_approval` é preenchido exclusivamente quando o veredicto é REJEITADO e contém todas as correções obrigatórias em ordem de prioridade — omitir esse campo numa rejeição invalida a revisão

---

## Veto Conditions

- **Feedback sem localização específica:** toda correção obrigatória deve referenciar um elemento concreto da copy ou do visual — diagnósticos abstratos como "a copy pode melhorar" são rejeitados e a tarefa deve ser refeita
- **`path_to_approval` ausente em veredicto REJEITADO:** se o veredicto for REJEITADO e o campo `path_to_approval` estiver vazio ou ausente, o output está incompleto — o ad-creator não tem protocolo de retrabalho e o ciclo de revisão ficará em loop sem resolução
