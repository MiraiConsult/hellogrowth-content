---
task: find-ad-opportunities
order: 1
input: pipeline/data/research-focus.md
output: squads/instagram-ads/output/research-results.md
---

# Tarefa: Encontrar Oportunidades de Anúncios

## Process

### Passo 1 — Ler o foco de pesquisa

Leia `pipeline/data/research-focus.md` para entender o direcionamento do ciclo atual: nicho prioritário, tipo de anúncio, restrições ou ângulos específicos definidos pelo pipeline. Use essas informações para calibrar as buscas.

### Passo 2 — Executar pesquisas direcionadas

Use `web_search` para encontrar **5 a 8 oportunidades** distribuídas entre as categorias abaixo. Execute buscas específicas para cada categoria — não generalize:

- **Tendências de mercado:** notícias recentes sobre gestão de reputação online, avaliações digitais, confiança do consumidor e crescimento de vendas via reputação
- **Estatísticas e dados:** estudos, pesquisas e relatórios com números concretos sobre o impacto de avaliações negativas, comportamento do consumidor antes da compra, ou ROI de reputação online
- **Dores do público-alvo:** fóruns, comunidades, comentários e discussões onde donos de negócio e profissionais de marketing relatam problemas com reputação online ou perda de clientes por avaliações
- **Movimentos de concorrentes:** o que empresas de gestão de reputação estão comunicando, que ângulos estão usando em seus anúncios, quais gaps existem no posicionamento delas
- **Ganchos sazonais ou eventos:** datas, eventos ou contextos do momento que criam urgência ou relevância extra para o tema

### Passo 3 — Avaliar e documentar cada oportunidade

Para cada oportunidade encontrada, aplique os filtros antes de incluir:

- **Filtro de relevância:** a oportunidade conecta-se diretamente à proposta da HelloGrowth (reputação → confiança → vendas)?
- **Filtro de atualidade:** o dado ou tendência é do último ano? Se não, descarte ou sinalize a defasagem
- **Filtro de especificidade:** há dados concretos, citações ou contexto que sustentam a oportunidade?

Apenas oportunidades que passam nos três filtros entram no output.

---

## Output Format

```yaml
opportunities:
  - id: string              # slug único: ex. "reputacao-compras-2025"
    title: string           # título claro da oportunidade
    category: string        # tendência | estatística | dor | concorrente | sazonal
    source: string          # URL ou nome da fonte
    source_date: string     # data da publicação ou "estimado YYYY"
    summary: string         # resumo da oportunidade em 1-2 frases
    relevance_score: number # 1-10: fit com HelloGrowth e público-alvo
    hook_potential: number  # 1-10: capacidade de parar o scroll no Instagram
    ad_angle: string        # ângulo sugerido para anúncio (ex: "prova social + urgência")
    hellgrowth_fit: string  # como a HelloGrowth resolve ou se encaixa nessa oportunidade
```

---

## Output Example

```yaml
opportunities:
  - id: "avaliacoes-decisao-compra-2025"
    title: "93% dos consumidores leem avaliações antes de comprar"
    category: estatística
    source: "BrightLocal Consumer Review Survey 2025"
    source_date: "2025-01"
    summary: "Pesquisa anual confirma que avaliações online são o fator decisivo na jornada de compra para a grande maioria dos consumidores, superando recomendação de amigos em categorias de serviço."
    relevance_score: 10
    hook_potential: 9
    ad_angle: "prova social + medo de perda — mostrar quanto dinheiro o negócio perde sem avaliações positivas"
    hellgrowth_fit: "A HelloGrowth transforma a gestão de avaliações em estratégia de vendas; esse dado é o argumento central da proposta de valor"

  - id: "avaliacao-negativa-viral-2025"
    title: "Uma avaliação negativa viral pode custar até 30 clientes para PMEs"
    category: tendência
    source: "Harvard Business Review Brasil"
    source_date: "2025-02"
    summary: "Estudo mapeia o efeito cascata de avaliações negativas não gerenciadas: cada review ruim sem resposta multiplica o impacto negativo na percepção de novos clientes."
    relevance_score: 9
    hook_potential: 8
    ad_angle: "dor + urgência — 'você sabe quantos clientes perdeu esse mês por avaliações não respondidas?'"
    hellgrowth_fit: "Posiciona a HelloGrowth como prevenção de perda de receita, não só melhora de imagem"

  - id: "concorrente-gap-automatizacao"
    title: "Concorrentes focam em volume de reviews, ignoram qualidade da resposta"
    category: concorrente
    source: "Análise de landing pages e anúncios — Reclame Aqui, Trustpilot BR, ReviewTracker"
    source_date: "estimado 2025"
    summary: "Principais players de reputação online no Brasil comunicam quantidade de avaliações coletadas, mas nenhum posiciona a qualidade e personalização das respostas como diferencial."
    relevance_score: 8
    hook_potential: 7
    ad_angle: "diferenciação — 'não é só coletar reviews, é transformar cada resposta em vendas'"
    hellgrowth_fit: "Abre espaço para HelloGrowth se posicionar como a única que converte reputação em resultado financeiro mensurável"
```

---

## Quality Criteria

- Mínimo de 5 oportunidades e máximo de 8 por execução — quantidade insuficiente indica pesquisa rasa, excesso indica falta de filtro
- Toda oportunidade deve ter `source` e `source_date` preenchidos — dados sem origem são descartados
- Os scores de `relevance_score` e `hook_potential` devem ser justificados implicitamente pelo conteúdo dos campos `summary` e `ad_angle` — não pode haver score 9-10 com justificativa fraca

---

## Veto Conditions

- **Dado com mais de 18 meses sem contexto de atemporalidade:** se a estatística ou tendência for de 2023 ou anterior sem indicação explícita de que é dado perene, não incluir
- **Oportunidade sem fit claro com HelloGrowth:** se não for possível preencher `hellgrowth_fit` com uma conexão direta e específica à proposta de valor da empresa, a oportunidade é descartada — oportunidades genéricas que se aplicam a qualquer empresa não entram no output
