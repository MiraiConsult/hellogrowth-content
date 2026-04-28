# Squad Memory — social-content

> Este arquivo é atualizado automaticamente após cada execução do pipeline.
> Contém aprendizados, preferências do usuário e padrões identificados.

## Execuções

### Run 2026-03-25-015617

- **Tema:** Reputação digital
- **Notícia escolhida:** #1 — "97% dos consumidores são influenciados por avaliações online, mas só 17% têm plano ativo"
- **Ângulo escolhido:** #2 — Polêmico/Opinativo — "Sua Empresa Está Nua na Internet"
- **Peças produzidas:** Carrossel Feed (7 slides), Reels (30s), Stories (5 frames), LinkedIn Post
- **Score revisão:** 4.3/5.0 — APROVADO
- **Ciclos de revisão:** 0 (aprovado na primeira tentativa)
- **Aprovação do usuário:** Aprovado em todas as etapas sem ajustes

### Run 2026-03-25-023004

- **Tema:** Reputação digital (reutilizou pesquisa do run anterior)
- **Notícia:** Mesma do run anterior (#1)
- **Ângulo:** Mesmo (#2 — "Sua Empresa Está Nua na Internet")
- **Foco:** Testar novo agente Designer (Dani Design) + geração de imagens com IA
- **Peças produzidas:** Carrossel Feed (7 cards com fotos IA via Gamma Flux Pro), LinkedIn Post
- **Design:** Gamma com tema dark, fotos AI-generated, acento verde #6CCFAA
- **Link Gamma:** https://gamma.app/docs/49r08ajja4airhp
- **Créditos Gamma usados:** 108 (restam 4.292)
- **Status:** Aprovado pelo usuário para ajustes finais no Gamma

### Run 2026-04-28-204139

- **Tema:** Growth / Crescimento — estratégias de aquisição, retenção, vendas
- **Notícia escolhida:** #1 — "Retenção como motor de lucro" (score 9.5, Bain/E-Commerce Brasil)
- **Ângulo escolhido:** #4 — Dica Prática — "5 Ações de Retenção Que Custam R$0"
- **Peças produzidas:** Carrossel Feed (7 cards), Stories (4 frames planejados)
- **Design:** HTML/CSS → Chrome headless, estilo Dashboard/Bloomberg, Montserrat
- **Publicação:** Via Supabase Edge Function → Instagram Graph API
- **Post:** https://www.instagram.com/p/DXsKcSojIr9/
- **Ciclos de revisão:** 0 (aprovado na primeira tentativa)
- **Catbox offline:** Usou Supabase Storage como CDN alternativo
- **Token IG:** Short-lived, expirou em horas. Precisa trocar por long-lived.

### Preferências identificadas

- Diego tende a escolher ângulos provocativos/polêmicos
- Prefere dados concretos com contraste forte (97% vs 17%)
- Aprova conteúdo rápido quando qualidade é boa — confia no processo
- Referência visual: @brandsdecoded__ — editorial com fotos de pessoas, copys grandes
- Prefere fotos full-bleed com texto sobreposto (não layout split)
- Ferramenta de design preferida: Gamma com Flux Pro (AI images)
- Cores da marca: verde gradiente #2D7D5F → #6CCFAA
- Planeja criar carrossel diariamente
- Tem Gamma Pro (créditos ilimitados)
- Tema core: reputação digital (alinhado com HelloGrowth)
- Também aceita temas de Growth/Crescimento (retenção, vendas, CAC)
- Gostou do ângulo "Dica Prática" com ações gratuitas — conteúdo acionável
- Estilo Dashboard/Bloomberg com Montserrat é o padrão visual atual (não mais Gamma)
- Publicação automatizada funciona via Supabase Edge Function (ig-publish) quando graph.facebook.com bloqueado pelo egress
- Supabase Storage como CDN alternativo quando catbox.moe está offline
- IG Business Account ID correto: 17841448421441860 (não o Page ID)
- Precisa gerar long-lived token pra evitar expiração frequente
