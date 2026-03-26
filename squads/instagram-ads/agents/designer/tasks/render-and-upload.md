---
task: "Renderizar PNG e Hospedar no Supabase"
order: 3
input:
  - html_files: "Arquivos HTML dos criativos em squads/instagram-ads/output/"
output:
  - png_files: "Imagens PNG renderizadas localmente"
  - supabase_urls: "URLs públicas das imagens no Supabase Storage"
---

# Renderizar PNG e Hospedar no Supabase

Renderiza cada arquivo HTML em imagem PNG via Playwright (Chrome headless) e faz upload para o Supabase Storage, gerando URLs públicas para uso no Meta Ads Manager.

## Process

### Passo 1 — Renderizar HTML em PNG via Playwright

1. Iniciar servidor HTTP local:
   ```bash
   python -m http.server 8765 --directory "squads/instagram-ads/output" &
   for i in $(seq 1 30); do curl -s http://localhost:8765 > /dev/null 2>&1 && break || sleep 0.1; done
   ```

2. Para cada arquivo `.html` em `squads/instagram-ads/output/`:
   - `browser_navigate` → `http://localhost:8765/{nome}.html`
   - `browser_resize` → largura: 1080, altura: 1350
   - `browser_take_screenshot` → salvar como `squads/instagram-ads/output/{nome}.png`

3. Verificar que cada PNG foi criado e tem resolução correta.

4. Encerrar o servidor HTTP:
   ```bash
   kill %1 2>/dev/null || true
   ```

### Passo 2 — Upload para Supabase Storage

1. Para cada arquivo PNG gerado, fazer upload para o Supabase Storage usando a ferramenta MCP do Supabase:
   - Bucket: `ad-creatives` (criar se não existir)
   - Path: `instagram-ads/{data}/{nome}.png`
   - Tornar o arquivo público para acesso direto

2. Coletar a URL pública de cada imagem hospedada.

3. Compilar um manifesto com todas as URLs.

### Passo 3 — Gerar manifesto final

Criar o arquivo `squads/instagram-ads/output/creative-manifest.md` com todas as informações dos criativos produzidos.

## Output Format

```yaml
manifest:
  squad: instagram-ads
  date: "YYYY-MM-DD"
  creatives:
    - name: "Nome do criativo"
      html: "squads/instagram-ads/output/{nome}.html"
      png_local: "squads/instagram-ads/output/{nome}.png"
      png_url: "https://{project}.supabase.co/storage/v1/object/public/ad-creatives/{path}.png"
      dimensions: "1080x1350"
      format: "4:5"
    # ... para cada criativo
  total_files: N
  storage_bucket: "ad-creatives"
```

## Output Example

```yaml
manifest:
  squad: instagram-ads
  date: "2026-03-26"
  creatives:
    - name: "Anúncio Estático — Reputação Medo"
      html: "squads/instagram-ads/output/ad-reputacao-medo.html"
      png_local: "squads/instagram-ads/output/ad-reputacao-medo.png"
      png_url: "https://abcdef.supabase.co/storage/v1/object/public/ad-creatives/instagram-ads/2026-03-26/ad-reputacao-medo.png"
      dimensions: "1080x1350"
      format: "4:5"
    - name: "Carousel Slide 1 — Cover"
      html: "squads/instagram-ads/output/ad-carousel-cover.html"
      png_local: "squads/instagram-ads/output/ad-carousel-cover.png"
      png_url: "https://abcdef.supabase.co/storage/v1/object/public/ad-creatives/instagram-ads/2026-03-26/ad-carousel-cover.png"
      dimensions: "1080x1350"
      format: "4:5"
    - name: "Carousel Slide 2 — Problema"
      html: "squads/instagram-ads/output/ad-carousel-problema.html"
      png_local: "squads/instagram-ads/output/ad-carousel-problema.png"
      png_url: "https://abcdef.supabase.co/storage/v1/object/public/ad-creatives/instagram-ads/2026-03-26/ad-carousel-problema.png"
      dimensions: "1080x1350"
      format: "4:5"
    - name: "Carousel Slide 3 — Prova"
      html: "squads/instagram-ads/output/ad-carousel-prova.html"
      png_local: "squads/instagram-ads/output/ad-carousel-prova.png"
      png_url: "https://abcdef.supabase.co/storage/v1/object/public/ad-creatives/instagram-ads/2026-03-26/ad-carousel-prova.png"
      dimensions: "1080x1350"
      format: "4:5"
    - name: "Carousel Slide 4 — CTA"
      html: "squads/instagram-ads/output/ad-carousel-cta.html"
      png_local: "squads/instagram-ads/output/ad-carousel-cta.png"
      png_url: "https://abcdef.supabase.co/storage/v1/object/public/ad-creatives/instagram-ads/2026-03-26/ad-carousel-cta.png"
      dimensions: "1080x1350"
      format: "4:5"
  total_files: 5
  storage_bucket: "ad-creatives"
```

## Quality Criteria

- [ ] Cada PNG tem resolução exata de 1080x1350px (formato 4:5)
- [ ] Todas as imagens foram uploadadas com sucesso para o Supabase Storage
- [ ] URLs públicas estão acessíveis (testáveis via browser_navigate)
- [ ] Manifesto criado com todos os criativos e suas URLs

## Veto Conditions

Rejeitar e refazer se:
1. Qualquer PNG tem dimensões diferentes de 1080x1350px
2. Upload para Supabase falhou e não há URL pública disponível para algum criativo
