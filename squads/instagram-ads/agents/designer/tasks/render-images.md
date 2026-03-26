---
task: render-images
order: 2
input: squads/instagram-ads/output/*.html
output: squads/instagram-ads/output/*.png
---

# Tarefa: Renderizar Criativos HTML em Imagens PNG

## Process

### Passo 1 — Iniciar servidor HTTP local

Inicie um servidor HTTP local apontando para o diretório de output, para que o Playwright consiga servir os arquivos HTML corretamente:

```bash
python -m http.server 8765 --directory "squads/instagram-ads/output" &
```

Aguarde 1-2 segundos para o servidor iniciar antes de prosseguir com as navegações.

### Passo 2 — Renderizar cada arquivo HTML em PNG

Para cada arquivo `.html` gerado na tarefa anterior (`design-ad-creative`), execute a seguinte sequência via skill `image-creator` (Playwright):

1. **Navegar até o arquivo:**
   ```
   browser_navigate → http://localhost:8765/{nome-do-arquivo}.html
   ```

2. **Redimensionar o viewport:**
   ```
   browser_resize → largura: 1080, altura: 1350
   ```

3. **Capturar o screenshot e salvar como PNG:**
   ```
   browser_take_screenshot → squads/instagram-ads/output/{nome-do-arquivo}.png
   ```

Repita para cada arquivo HTML, em ordem sequencial.

### Passo 3 — Verificar e encerrar

Após renderizar todos os arquivos:
- Verifique que cada `.png` foi criado no diretório `squads/instagram-ads/output/`
- Confirme que o número de PNGs corresponde ao número de HTMLs processados
- Encerre o servidor HTTP:

```bash
kill $(lsof -ti:8765) 2>/dev/null || true
```

Documente o resultado: lista de imagens geradas com caminho completo e status de verificação.

---

## Output Format

```yaml
renderizacoes:
  - html: string          # nome do arquivo HTML de origem
    png: string           # caminho completo do PNG gerado
    status: string        # "sucesso" ou "erro"
    erro: string|null     # descrição do erro, se houver (null se sucesso)

resumo:
  total_htmls: integer    # número de arquivos HTML processados
  total_pngs: integer     # número de PNGs criados com sucesso
  falhas: integer         # número de falhas, se houver
```

---

## Output Example

```yaml
renderizacoes:
  - html: ad-static-reputacao-01.html
    png: squads/instagram-ads/output/ad-static-reputacao-01.png
    status: sucesso
    erro: null

  - html: ad-carousel-prova-social-01-slide1.html
    png: squads/instagram-ads/output/ad-carousel-prova-social-01-slide1.png
    status: sucesso
    erro: null

  - html: ad-carousel-prova-social-01-slide2.html
    png: squads/instagram-ads/output/ad-carousel-prova-social-01-slide2.png
    status: sucesso
    erro: null

  - html: ad-static-urgencia-01.html
    png: squads/instagram-ads/output/ad-static-urgencia-01.png
    status: sucesso
    erro: null

resumo:
  total_htmls: 4
  total_pngs: 4
  falhas: 0
```

---

## Quality Criteria

- Cada arquivo HTML produzido em `design-ad-creative` deve ter um PNG correspondente gerado em `squads/instagram-ads/output/`
- O viewport de cada captura é exatamente 1080x1350px — screenshots fora dessas dimensões são inválidos e devem ser refeitos
- O servidor HTTP é sempre encerrado ao final da tarefa, evitando conflito de porta em execuções futuras

---

## Veto Conditions

- **PNG não gerado para algum HTML** — se qualquer arquivo HTML não tiver um PNG correspondente verificado no diretório de output, a tarefa não está concluída; reprocessar o arquivo com falha antes de encerrar
- **Dimensões incorretas** — se o screenshot não corresponder a 1080x1350px (ex: viewport não foi redimensionado corretamente), o PNG deve ser descartado e a captura refeita com `browser_resize` antes de `browser_take_screenshot`
