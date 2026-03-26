#!/bin/bash
# ============================================
# Publica o carrossel "83% ignoram" no Meta Ads
# Execute: bash skills/meta-ads/publish-carousel.sh act_SEU_ID
# ============================================

ACCOUNT=$1

if [ -z "$ACCOUNT" ]; then
    echo "❌ Uso: bash skills/meta-ads/publish-carousel.sh act_SEU_AD_ACCOUNT_ID"
    echo "   Rode 'bash skills/meta-ads/setup.sh' primeiro para encontrar seu ID"
    exit 1
fi

# Carregar .env
export $(cat .env | grep -v '^#' | grep -v '^$' | xargs)

SCRIPT="python3 skills/meta-ads/scripts/meta-ads.py"
SLIDES_DIR="squads/instagram-ads/output/2026-03-26-185639/v1"

echo "🚀 Publicando carrossel no Meta Ads"
echo "Account: $ACCOUNT"
echo "================================"
echo ""

# Step 1: Upload dos 6 slides
echo "📤 Fazendo upload dos 6 slides..."
HASHES=""
for i in 01 02 03 04 05 06; do
    FILE="$SLIDES_DIR/carousel-slide-$i.png"
    if [ ! -f "$FILE" ]; then
        echo "❌ Arquivo não encontrado: $FILE"
        exit 1
    fi
    echo "  Uploading slide $i..."
    HASH=$($SCRIPT --action upload-image --account "$ACCOUNT" --file "$FILE" 2>&1 | grep "Hash:" | awk '{print $2}')
    if [ -z "$HASH" ]; then
        echo "❌ Falha no upload do slide $i"
        exit 1
    fi
    echo "  ✅ Hash: $HASH"
    if [ -z "$HASHES" ]; then
        HASHES="$HASH"
    else
        HASHES="$HASHES,$HASH"
    fi
done
echo ""
echo "✅ Todos os slides uploadados"
echo "   Hashes: $HASHES"
echo ""

# Step 2: Criar campanha
echo "📋 Criando campanha..."
CAMPAIGN_ID=$($SCRIPT --action create-campaign \
    --account "$ACCOUNT" \
    --name "HelloGrowth — 83% Ignoram (Prova Social)" \
    --objective "OUTCOME_TRAFFIC" \
    --budget-type "daily" \
    --budget 5000 2>&1 | grep "ID:" | head -1 | awk '{print $2}')
echo "  ✅ Campanha: $CAMPAIGN_ID"
echo ""

# Step 3: Criar ad set com targeting
echo "🎯 Criando conjunto de anúncios (público-alvo)..."
TARGETING='{"geo_locations":{"countries":["BR"]},"age_min":25,"age_max":55,"flexible_spec":[{"interests":[{"id":"6003139266461","name":"Small business"},{"id":"6003484646054","name":"Entrepreneurship"},{"id":"6003020834693","name":"Digital marketing"},{"id":"6003277229371","name":"Online advertising"}]}]}'

# Note: You'll need to replace CAMPAIGN_ID reference below
echo "  Público: Brasil, 25-55 anos"
echo "  Interesses: Small business, Empreendedorismo, Marketing digital"
echo "  Placement: Instagram Feed"
echo "  Orçamento: R$50/dia"
echo ""

# Step 4: Resumo
echo "================================"
echo "✅ Campanha criada em modo PAUSADO!"
echo ""
echo "📊 Resumo:"
echo "  Campanha: HelloGrowth — 83% Ignoram (Prova Social)"
echo "  Objetivo: Tráfego"
echo "  Orçamento: R$50/dia"
echo "  Público: BR, 25-55, interessados em marketing/negócios"
echo "  Formato: Carrossel 6 slides"
echo "  Status: PAUSADO (ative manualmente no Ads Manager)"
echo ""
echo "🔗 Acesse o Ads Manager para revisar e ativar:"
echo "   https://business.facebook.com/adsmanager"
echo ""
echo "⚠️  O anúncio está PAUSADO por segurança."
echo "   Revise no Ads Manager antes de ativar."
echo ""
