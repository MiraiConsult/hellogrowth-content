---
task: "Gerar Backgrounds com IA"
order: 1
input:
  - ad_copy: "Copy aprovada com direção visual (briefing de cada criativo)"
output:
  - background_images: "Imagens de background geradas por IA para cada criativo"
---

# Gerar Backgrounds com IA

Gera imagens de background/fotos usando IA (skill image-generator via Openrouter API) com base na direção visual do briefing de cada anúncio.

## Process

1. **Ler direção visual** — Extrair do ad-copy.md o briefing visual de cada criativo: estilo, mood, elementos principais, cores desejadas. Identificar quantas imagens únicas são necessárias.

2. **Construir prompts** — Para cada criativo, escrever um prompt detalhado para geração de imagem:
   - Especificar composição, iluminação, estilo e mood
   - Incluir "portrait 3:4" para formato compatível com 4:5
   - Incluir "clean composition, no text, professional" para evitar ruído
   - NÃO pedir texto nas imagens (modelos de IA têm dificuldade com texto)
   - Referências de cor: usar cores da marca HelloGrowth no prompt

3. **Gerar imagens** — Executar o image-generator:
   - **Modo test primeiro** (R$0.01-0.02 por imagem): gerar 1 imagem por criativo para validar o conceito
   - Comando: `python3 skills/image-generator/scripts/generate.py --prompt "{prompt}" --output "squads/instagram-ads/output/bg-{nome}.jpg" --mode test`
   - Se disponível, usar `--reference` com o logo da HelloGrowth para brand consistency
   - Só mudar para `--mode production` quando o conceito for aprovado no checkpoint

## Output Format

```yaml
backgrounds:
  - creative_id: "ad-estatico-01"
    prompt: "Prompt completo usado para geração"
    file: "squads/instagram-ads/output/bg-estatico-01.jpg"
    mode: "test"
    status: "generated"
  - creative_id: "ad-carousel-slide-01"
    prompt: "..."
    file: "squads/instagram-ads/output/bg-carousel-01.jpg"
    mode: "test"
    status: "generated"
```

## Output Example

```yaml
backgrounds:
  - creative_id: "ad-reputacao-medo"
    prompt: "Professional dark office environment, dramatic lighting from monitor screens, corporate atmosphere, portrait 3:4, clean composition, no text, hyper realistic, 4K quality, moody blue and dark tones"
    file: "squads/instagram-ads/output/bg-reputacao-medo.jpg"
    mode: "test"
    status: "generated"
  - creative_id: "ad-carousel-cover"
    prompt: "Abstract geometric pattern with green and dark gradients, modern corporate style, portrait 3:4, clean composition, no text, minimal, professional, 4K quality"
    file: "squads/instagram-ads/output/bg-carousel-cover.jpg"
    mode: "test"
    status: "generated"
  - creative_id: "ad-carousel-slide-proof"
    prompt: "Clean white office desk with laptop showing growth charts, natural daylight, portrait 3:4, clean composition, no text, hyper realistic, 4K quality, warm professional tones"
    file: "squads/instagram-ads/output/bg-carousel-proof.jpg"
    mode: "test"
    status: "generated"
```

## Quality Criteria

- [ ] Cada prompt é específico sobre composição, estilo, mood e orientação (portrait 3:4)
- [ ] Nenhum prompt pede texto na imagem (modelos de IA não renderizam texto bem)
- [ ] Modo test usado para primeira geração (economia de tokens)
- [ ] Imagens geradas salvas em `squads/instagram-ads/output/` com nomenclatura descritiva

## Veto Conditions

Rejeitar e refazer se:
1. Prompt genérico sem especificidade de composição, iluminação ou estilo (ex: "imagem bonita de negócios")
2. Imagem gerada em modo production sem aprovação prévia do conceito em modo test
