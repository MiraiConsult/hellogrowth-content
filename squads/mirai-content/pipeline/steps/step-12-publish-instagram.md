---
type: agent
agent: instagram-publisher
execution: inline
---

# Publicação no Instagram

Pub Insta, publique o carrossel aprovado no Instagram da HelloGrowth (@hellogrowth__).

## Tarefas a executar

### 1. Upload das imagens para Supabase Storage
- Fazer upload de cada card PNG para o bucket público do Supabase
- Obter as URLs públicas de cada imagem
- Verificar que todas as URLs estão acessíveis

### 2. Criar containers no Instagram Graph API
- Para cada imagem, criar um container individual (`is_carousel_item: true`)
- Criar o container do carrossel com todos os children
- Incluir a legenda e hashtags do Iago Insta no container do carrossel

### 3. Publicar o carrossel
- Publicar via `media_publish`
- Obter o permalink do post publicado
- Apresentar o link ao usuário

## Orientações
- Verificar que o Access Token está válido antes de iniciar
- Se o token estiver expirado, informar o usuário e orientar a renovação
- Aguardar 30 segundos entre a criação dos containers e a publicação (Instagram precisa processar)
- Reportar cada etapa ao usuário com status (sucesso/erro)
