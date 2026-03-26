---
task: rank-opportunities
order: 2
input: squads/instagram-ads/output/research-results.md
output: squads/instagram-ads/output/research-results.md
---

# Tarefa: Ranquear Oportunidades

## Process

### Passo 1 — Carregar e revisar as oportunidades encontradas

Leia o output da tarefa anterior em `squads/instagram-ads/output/research-results.md`. Certifique-se de que todas as oportunidades listadas passaram pelos filtros de relevância, atualidade e especificidade. Se alguma oportunidade não tiver `source`, `source_date` ou `hellgrowth_fit` preenchidos, sinalize e exclua do ranking.

### Passo 2 — Pontuar cada oportunidade com os 5 critérios

Para cada oportunidade, aplique os cinco critérios de avaliação e atribua uma nota de 1 a 10 para cada:

1. **Relevância para o público da HelloGrowth** (peso 2x): o tema ressoa diretamente com donos de negócio e profissionais de marketing que precisam melhorar reputação online? Quanto mais específico o problema para esse público, maior a nota.

2. **Potencial de hook para Instagram** (peso 2x): o conteúdo tem capacidade de parar o scroll? Considere impacto emocional, surpresa, dado chocante, identificação imediata com uma dor ou desejo do público.

3. **Potencial de conversão** (peso 2x): a oportunidade cria condições para uma chamada à ação convincente? Avalie se há urgência, escassez, prova social ou medo de perda que sustente uma conversão.

4. **Atualidade e relevância temporal** (peso 1x): o dado ou tendência é recente e percebido como atual pelo público? Oportunidades sazonais ou ligadas a eventos do momento ganham pontuação extra.

5. **Disponibilidade de dados e prova** (peso 1x): há estatísticas, estudos, casos reais ou fontes confiáveis que sustentem o ângulo? Quanto mais sólida a prova, mais fácil criar um anúncio persuasivo.

**Score final** = (critério 1 × 2) + (critério 2 × 2) + (critério 3 × 2) + (critério 4 × 1) + (critério 5 × 1) ÷ 8

### Passo 3 — Montar o ranking e definir ângulos de anúncio

Ordene as oportunidades do maior para o menor score final. Selecione as **top 3 a 5** para o ranking definitivo. Para cada uma, elabore:

- Justificativa detalhada da posição no ranking
- Ângulo de anúncio refinado (mais específico que o `ad_angle` da tarefa anterior)
- Sugestão de formato de anúncio (carrossel, reels, stories, imagem estática)
- Um possível headline de abertura do anúncio

Atualize o arquivo de output adicionando a seção `ranked_opportunities` ao YAML existente.

---

## Output Format

```yaml
ranked_opportunities:
  - rank: number            # posição no ranking (1 = maior prioridade)
    id: string              # referência ao id da oportunidade original
    title: string           # título da oportunidade
    scores:
      relevancia_publico: number    # 1-10
      hook_instagram: number        # 1-10
      potencial_conversao: number   # 1-10
      atualidade: number            # 1-10
      disponibilidade_prova: number # 1-10
      final: number                 # score ponderado calculado
    ranking_rationale: string  # justificativa clara para a posição no ranking
    refined_ad_angle: string   # ângulo de anúncio refinado e específico
    suggested_format: string   # carrossel | reels | stories | imagem estática
    headline_suggestion: string # possível headline de abertura do anúncio
```

---

## Output Example

```yaml
ranked_opportunities:
  - rank: 1
    id: "avaliacoes-decisao-compra-2025"
    title: "93% dos consumidores leem avaliações antes de comprar"
    scores:
      relevancia_publico: 10
      hook_instagram: 9
      potencial_conversao: 10
      atualidade: 9
      disponibilidade_prova: 10
      final: 9.75
    ranking_rationale: "Combina o maior score de relevância com prova irrefutável (dado de pesquisa anual reconhecida) e potencial de conversão máximo. O número concreto (93%) é um hook natural para Instagram — para o scroll imediatamente. Cria urgência sem precisar de artifício: o custo de não agir é implícito no dado."
    refined_ad_angle: "Prova social quantificada + custo de inação — 'Antes de comprar qualquer produto ou contratar qualquer serviço, 93% das pessoas leem avaliações. O que elas estão lendo sobre o seu negócio?'"
    suggested_format: "carrossel"
    headline_suggestion: "93% dos seus futuros clientes já pesquisaram o que falam de você."

  - rank: 2
    id: "avaliacao-negativa-viral-2025"
    title: "Uma avaliação negativa viral pode custar até 30 clientes para PMEs"
    scores:
      relevancia_publico: 9
      hook_instagram: 8
      potencial_conversao: 9
      atualidade: 8
      disponibilidade_prova: 8
      final: 8.63
    ranking_rationale: "O número '30 clientes perdidos' é um hook de alto impacto emocional — transforma reputação abstrata em receita concreta perdida. Ligeiramente abaixo do primeiro por exigir mais contexto para que o público entenda o mecanismo causa-efeito, mas compensa com alto potencial de identificação: todo dono de negócio já teve ou teme ter uma avaliação negativa."
    refined_ad_angle: "Medo de perda + custo invisível — mostrar o cálculo financeiro real de avaliações não gerenciadas; posicionar a HelloGrowth como o 'seguro' que todo negócio deveria ter"
    suggested_format: "reels"
    headline_suggestion: "Você sabe quanto custou a última avaliação negativa que você ignorou?"

  - rank: 3
    id: "concorrente-gap-automatizacao"
    title: "Concorrentes focam em volume de reviews, ignoram qualidade da resposta"
    scores:
      relevancia_publico: 7
      hook_instagram: 7
      potencial_conversao: 8
      atualidade: 7
      disponibilidade_prova: 6
      final: 7.25
    ranking_rationale: "Oportunidade de posicionamento estratégico com boa janela de diferenciação — nenhum concorrente está comunicando qualidade de resposta como gerador de vendas. Score menor porque depende de um público já consciente do problema (não funciona para audiências frias) e a prova é baseada em análise qualitativa, não dado quantitativo."
    refined_ad_angle: "Diferenciação por resultado — 'Qualquer ferramenta coleta reviews. A HelloGrowth transforma cada resposta em uma oportunidade de venda'"
    suggested_format: "imagem estática"
    headline_suggestion: "Seus concorrentes coletam avaliações. Você converte avaliações em clientes."
```

---

## Quality Criteria

- O ranking deve conter entre 3 e 5 oportunidades — um ranking com mais itens dilui o foco; com menos, indica pesquisa insuficiente na tarefa anterior
- O `ranking_rationale` de cada posição deve explicitar por que aquela oportunidade está acima ou abaixo das adjacentes — justificativas genéricas são inaceitáveis
- O `headline_suggestion` deve ser uma frase de impacto real, pronta para teste — não um esboço vago

---

## Veto Conditions

- **Oportunidades com score final abaixo de 6.0 não entram no ranking:** scores baixos indicam fit fraco com o objetivo de conversão via Instagram; é preferível ter um ranking menor e mais qualificado
- **Dois itens com `refined_ad_angle` equivalente não podem coexistir no ranking:** se duas oportunidades geram o mesmo ângulo de anúncio, a de menor score é eliminada — o ranking deve representar vetores distintos de abordagem para diversificar as campanhas
