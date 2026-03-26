---
name: meta-ads
description: >
  Publishes ads on Meta Ads Manager (Facebook/Instagram) via Marketing API.
  Creates campaigns, ad sets, and ads with audience targeting, budget configuration,
  and creative upload. Monitors performance metrics (CTR, CPC, ROAS).
description_pt-BR: >
  Publica anúncios no Meta Ads Manager (Facebook/Instagram) via Marketing API.
  Cria campanhas, conjuntos de anúncios e anúncios com segmentação de público,
  configuração de orçamento e upload de criativos. Monitora métricas de performance.
type: script
version: "1.0.0"
script:
  path: scripts/meta-ads.py
  runtime: python3
env:
  - META_ACCESS_TOKEN
  - META_APP_ID
  - META_BUSINESS_ID
categories: [ads, marketing, meta, facebook, instagram]
---

# Meta Ads — Skill de Publicação de Anúncios

## When to use

Use este skill quando precisar publicar anúncios no Meta Ads Manager (Facebook/Instagram) ou monitorar performance de campanhas existentes.

## Configuração

Variáveis de ambiente necessárias (em `.env`):
- `META_ACCESS_TOKEN` — Token de acesso com permissão `ads_management`
- `META_APP_ID` — ID do app no Meta for Developers
- `META_BUSINESS_ID` — ID do Business Manager

Para encontrar o Ad Account ID:
```bash
python3 skills/meta-ads/scripts/meta-ads.py --action list-accounts
```

## Operações Disponíveis

### 1. Listar Contas de Anúncio
```bash
python3 skills/meta-ads/scripts/meta-ads.py --action list-accounts
```

### 2. Criar Campanha
```bash
python3 skills/meta-ads/scripts/meta-ads.py \
  --action create-campaign \
  --account "act_XXXXXXXXX" \
  --name "Nome da Campanha" \
  --objective "OUTCOME_TRAFFIC" \
  --budget-type "daily" \
  --budget 5000
```

Objetivos disponíveis:
- `OUTCOME_AWARENESS` — Alcance e reconhecimento
- `OUTCOME_TRAFFIC` — Tráfego para site/landing page
- `OUTCOME_ENGAGEMENT` — Engajamento com publicações
- `OUTCOME_LEADS` — Geração de leads
- `OUTCOME_SALES` — Conversões e vendas

### 3. Criar Conjunto de Anúncios (Ad Set)
```bash
python3 skills/meta-ads/scripts/meta-ads.py \
  --action create-adset \
  --campaign "CAMPAIGN_ID" \
  --name "Nome do Ad Set" \
  --budget 2500 \
  --targeting '{"geo_locations":{"countries":["BR"]},"age_min":25,"age_max":55,"interests":[{"id":"6003139266461","name":"Small business"}]}' \
  --placements "instagram_feed" \
  --optimization "LINK_CLICKS"
```

Otimizações disponíveis:
- `LINK_CLICKS` — Otimizar para cliques
- `IMPRESSIONS` — Otimizar para alcance
- `LANDING_PAGE_VIEWS` — Otimizar para views de página
- `LEAD_GENERATION` — Otimizar para leads
- `CONVERSIONS` — Otimizar para conversões

### 4. Upload de Criativo (Imagem)
```bash
python3 skills/meta-ads/scripts/meta-ads.py \
  --action upload-image \
  --account "act_XXXXXXXXX" \
  --file "squads/instagram-ads/output/2026-03-26/v1/carousel-slide-01.png"
```

### 5. Criar Anúncio
```bash
python3 skills/meta-ads/scripts/meta-ads.py \
  --action create-ad \
  --adset "ADSET_ID" \
  --name "Nome do Anúncio" \
  --creative-type "carousel" \
  --images "IMAGE_HASH_1,IMAGE_HASH_2,IMAGE_HASH_3" \
  --primary-text "Copy do primary text" \
  --headline "Headline do anúncio" \
  --description "Description" \
  --cta "LEARN_MORE" \
  --link "https://hellogrowth.site/"
```

CTAs disponíveis:
- `LEARN_MORE` — Saiba Mais
- `SIGN_UP` — Cadastre-se
- `CONTACT_US` — Fale Conosco
- `GET_QUOTE` — Solicitar Orçamento
- `BOOK_NOW` — Agendar

### 6. Consultar Métricas
```bash
python3 skills/meta-ads/scripts/meta-ads.py \
  --action get-insights \
  --object-id "CAMPAIGN_OR_AD_ID" \
  --metrics "impressions,clicks,ctr,cpc,spend,actions" \
  --date-range "last_7d"
```

### 7. Buscar Interesses para Targeting
```bash
python3 skills/meta-ads/scripts/meta-ads.py \
  --action search-interests \
  --query "marketing digital"
```

## Fluxo Completo de Publicação

Para publicar um anúncio do squad instagram-ads:

1. **Listar contas** → pegar o ad account ID
2. **Upload dos criativos** → obter image hashes
3. **Criar campanha** → definir objetivo e orçamento
4. **Criar ad set** → configurar público e placements
5. **Criar ad** → juntar criativo + copy + CTA
6. **Monitorar** → consultar métricas após 24-48h

## Análise de Público Recomendada

Para HelloGrowth (gestão de reputação + vendas), público sugerido:

**Audiência Fria (Prospecção):**
- Idade: 25-55 anos
- Localização: Brasil
- Interesses: Small business, Empreendedorismo, Marketing digital, E-commerce, Gestão empresarial
- Comportamentos: Admins de páginas de negócios, Donos de pequenas empresas

**Audiência Morna (Retargeting):**
- Custom Audience: Visitantes do site nos últimos 30 dias
- Engajamento: Interagiram com página Instagram nos últimos 90 dias

**Audiência Quente (Conversão):**
- Custom Audience: Visitantes de páginas de pricing/contato nos últimos 14 dias
- Lookalike: 1% baseado em clientes existentes

## Métricas e KPIs de Referência

| Métrica | Meta | Bom | Excelente |
|---------|------|-----|-----------|
| CTR | > 0,5% | > 0,88% | > 1,5% |
| CPC | < R$5,00 | < R$3,00 | < R$1,50 |
| CPM | < R$40 | < R$25 | < R$15 |
| ROAS | > 2x | > 3x | > 5x |
| Frequência | 1-2 | - | - |

## Cadência de Testes

- Testar 3-5 criativos por ad set
- Aguardar 5-7 dias antes de otimizar (fase de aprendizado)
- Rotacionar criativos quando frequência > 2 e CTR caindo
- Cadência de novos testes: a cada 2-4 semanas
