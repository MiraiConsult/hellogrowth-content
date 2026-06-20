---
type: agent
agent: designer
execution: inline
outputFile: squads/social-content/output/slides/
---

# Design Visual — HTML/CSS → Imagens PNG

Dani Design, com base no conteúdo de texto criado pelo Iago Insta (instagram-content.md), você deve criar as imagens finais para cada slide do carrossel e cada frame dos Stories.

## Tarefas a executar

### 1. Carrossel Instagram (1080x1350px cada slide)
- Para cada slide do carrossel, criar um arquivo HTML/CSS standalone
- Usar o Design System da HelloGrowth (cores, tipografia, layout)
- Renderizar via Playwright: navegar para o HTML e fazer screenshot como PNG
- Salvar cada imagem como: `slide-01.png`, `slide-02.png`, etc.

### 2. Stories Instagram (1080x1920px cada frame)
- Para cada frame dos Stories, criar HTML/CSS com dimensões de Story
- Incluir elementos visuais dos stickers (enquetes, quizzes) como representação visual
- Renderizar via Playwright como PNG
- Salvar cada imagem como: `story-01.png`, `story-02.png`, etc.

## Processo de renderização

Para cada slide/frame:
1. Criar o HTML completo com CSS inline (standalone, sem dependências externas além de Google Fonts)
2. Usar Playwright para:
   a. `browser_navigate` para o arquivo HTML (usar data URI ou arquivo local)
   b. `browser_take_screenshot` para capturar como PNG
3. Salvar a imagem no diretório de output

## Orientações gerais
- Seguir o Design System definido no agent.md (cores, tipografia, layout)
- Alternar fundos escuros/claros entre slides
- Números e dados em cor de acento (#FF3B30)
- Header com @hellogrowth em todos os slides
- Último slide com CTA + identidade visual da marca
- Garantir que texto é legível em tela de celular
