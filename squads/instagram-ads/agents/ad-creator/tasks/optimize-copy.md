---
task: "Otimizar Copy do Anúncio"
order: 3
input:
  description: "Copy completa do anúncio gerada na task create-ad-copy.md (primary text, headline, description, CTA, slides do carousel, direção visual e hashtags)"
output:
  description: "Versão final otimizada da copy com relatório de cada passe de otimização e copy aprovada pronta para subir na plataforma"
---

# Otimizar Copy do Anúncio

## Objetivo

Aplicar passes sequenciais de otimização na copy rascunhada para maximizar CTR, qualidade do lead e conformidade com a plataforma. A otimização não é revisão gramatical — é cirurgia de conversão. Cada passe tem critério específico e resultado documentado.

## Processo

1. **Copy Stress Test** — Submeter a copy a 4 testes adversariais:
   - **Teste do cético**: um prospect desconfiado leria isso e acreditaria? Onde estão os pontos de resistência?
   - **Prova check**: cada afirmação tem suporte (dado, caso, garantia)? Identificar afirmações sem âncora
   - **Inflation check**: há superlativo sem evidência ("o melhor", "revolucionário", "único")? Substituir por específico
   - **Friction check**: há palavra ou frase que gera fricção desnecessária antes do CTA? Remover ou suavizar
2. **Scroll-stop test** — Avaliar o hook em isolamento: se essa primeira linha aparecesse no feed de alguém que não conhece a HelloGrowth, ela pararia de rolar? Se a resposta for "talvez", o hook não passou. Reescrever até passar com "sim"
3. **Anti-commodity check** — Substituir nome e logo pelo de um concorrente direto. Se o anúncio ainda funcionar perfeitamente, a copy é genérica. Identificar o elemento único da HelloGrowth que deve estar presente e inserir
4. **Redução de palavras** — Cortar 15-25% do volume de texto sem perder significado ou punch. Prioridade: eliminar adjuntos adverbiais desnecessários, repetições e frases de transição que não adicionam valor
5. **Conformidade com a plataforma** — Verificar truncamento do Instagram (primary text: primeiros 125 chars são os visíveis sem "ver mais"), regras de texto do Meta Ads (claims de saúde/financeiro, políticas de conteúdo), limites de caracteres de headline e description
6. **Verificação de voz HelloGrowth** — Checar presença de vocabulário proibido (hack, truque, segredo, guru, infalível) e vocabulário preferido (estratégia, resultado, dado, comprovado). Tom direto e orientado a resultado está presente do início ao fim?
7. **Entregar versão final** — Compilar a copy otimizada em formato final, com sumário das alterações aplicadas em cada passe

## Formato de Saída

```yaml
optimization_report:
  original_word_count: 0
  final_word_count: 0
  reduction_percentage: "0%"

  stress_test:
    skeptic_test:
      status: "pass | fail"
      friction_points: []
      fix_applied: ""
    proof_check:
      status: "pass | fail"
      unanchored_claims: []
      fix_applied: ""
    inflation_check:
      status: "pass | fail"
      inflated_terms: []
      fix_applied: ""
    friction_check:
      status: "pass | fail"
      friction_phrases: []
      fix_applied: ""

  scroll_stop_test:
    status: "pass | fail"
    verdict: "Sim / Talvez / Não"
    hook_rewrite: "Nova versão do hook se reescrito"

  anti_commodity_check:
    status: "pass | fail"
    generic_elements: []
    differentiator_added: ""

  platform_compliance:
    primary_text_truncation: "pass | fail"
    headline_chars: 0
    description_chars: 0
    meta_policy_issues: []
    fix_applied: ""

  brand_voice_check:
    prohibited_words_found: []
    preferred_words_present: []
    tone_verdict: "alinhado | ajuste necessário"
    fix_applied: ""

final_copy:
  primary_text: "Versão final otimizada completa"
  headline: "Headline final ≤40 chars"
  description: "Description final ≤30 chars"
  cta_button: "Botão selecionado"
  carousel_slides:
    - slide: "cover"
      headline: ""
      subtext: ""
    - slide: 2
      headline: ""
      body: ""
    - slide: "cta"
      headline: ""
      body: ""
      cta: ""
  hashtags:
    - "#hashtag"
  visual_direction: "Direção visual final (sem alteração ou com ajuste)"
```

## Exemplo de Saída (parcial)

```yaml
optimization_report:
  original_word_count: 87
  final_word_count: 68
  reduction_percentage: "22%"

  stress_test:
    skeptic_test:
      status: "fail"
      friction_points:
        - "Frase 'a causa não é o produto' pode gerar rejeição — o leitor pode discordar imediatamente"
      fix_applied: "Reformulado para 'uma das principais causas é invisível para a maioria' — menos confrontacional, mantém a provocação"
    proof_check:
      status: "pass"
      unanchored_claims: []
      fix_applied: ""
    inflation_check:
      status: "fail"
      inflated_terms:
        - "'totalmente gratuito' — redundante e suspeito"
      fix_applied: "Substituído por 'diagnóstico sem custo' — específico e crível"
    friction_check:
      status: "pass"
      friction_phrases: []
      fix_applied: ""

  scroll_stop_test:
    status: "pass"
    verdict: "Sim"
    hook_rewrite: ""

  anti_commodity_check:
    status: "fail"
    generic_elements:
      - "Frase 'gerencie sua reputação digital' pode ser de qualquer agência de marketing"
    differentiator_added: "Inserido 'HelloGrowth rastreia onde seus clientes pesquisam antes de comprar' — diferenciador de método e foco B2B"

  platform_compliance:
    primary_text_truncation: "pass"
    headline_chars: 31
    description_chars: 22
    meta_policy_issues: []
    fix_applied: ""

  brand_voice_check:
    prohibited_words_found: []
    preferred_words_present: ["resultado", "dado", "comprovado", "estratégia"]
    tone_verdict: "alinhado"
    fix_applied: ""

final_copy:
  primary_text: "Cada semana sem gestão de reputação, você perde leads que já estavam prontos para comprar. 68% dos decisores pesquisam sua empresa antes de qualquer reunião. Se não encontram confiança, somem — sem avisar. A HelloGrowth rastreia onde seus clientes pesquisam e fortalece o que eles encontram. Descubra quanto está na mesa →"
  headline: "Reputação que fecha vendas"
  description: "Diagnóstico sem custo"
  cta_button: "Saiba Mais"
```

## Critérios de Qualidade

1. Todos os 4 testes do Copy Stress Test foram executados e documentados — nenhum item marcado como "não verificado"
2. Cada "fail" tem correção específica registrada e aplicada na versão final — não basta identificar o problema
3. A redução de palavras está entre 15-25% em relação ao rascunho original — cortes abaixo de 15% indicam otimização superficial

## Condições de Veto

- **REJEITAR** se o scroll-stop test resultar em "Não" e o hook não for reescrito antes de entregar
- **REJEITAR** se o anti-commodity check falhar e nenhum diferenciador específico da HelloGrowth for inserido na copy final
