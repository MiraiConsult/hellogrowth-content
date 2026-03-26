#!/bin/bash
# ============================================
# Meta Ads — Setup e Primeiro Teste
# Execute: bash skills/meta-ads/setup.sh
# ============================================

echo "🚀 Meta Ads Setup — HelloGrowth"
echo "================================"
echo ""

# Carregar .env
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | grep -v '^$' | xargs)
    echo "✅ Variáveis de ambiente carregadas"
else
    echo "❌ Arquivo .env não encontrado. Crie com META_ACCESS_TOKEN."
    exit 1
fi

# Verificar token
if [ -z "$META_ACCESS_TOKEN" ]; then
    echo "❌ META_ACCESS_TOKEN não está definido no .env"
    exit 1
fi
echo "✅ Token encontrado"
echo ""

# 1. Listar contas de anúncio
echo "📋 Buscando suas contas de anúncio..."
echo "--------------------------------------"
python3 skills/meta-ads/scripts/meta-ads.py --action list-accounts
echo ""

# 2. Buscar interesses relevantes
echo "🎯 Buscando interesses para targeting HelloGrowth..."
echo "--------------------------------------"
python3 skills/meta-ads/scripts/meta-ads.py --action search-interests --query "marketing digital"
echo ""

echo "================================"
echo "✅ Setup concluído!"
echo ""
echo "Próximos passos:"
echo "  1. Copie o Ad Account ID (act_XXXXXXX) acima"
echo "  2. Para publicar o carrossel, rode:"
echo "     bash skills/meta-ads/publish-carousel.sh act_SEU_ID"
echo ""
