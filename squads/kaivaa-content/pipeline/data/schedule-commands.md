# Comandos para Agendar — Rodar quando /schedule estiver disponível

## 1. Carrossel Instagram (Seg, Qua, Sex — 7h BRT)

```
/schedule create
Name: HelloGrowth Carrossel Instagram
Cron: 0 10 * * 1,3,5
Prompt: Run the social-content squad pipeline autonomously. Pick a trending topic about digital reputation, online reviews, or business growth. Research → create carousel text (7 cards) → generate AI photos via Gamma (flux-1-pro) → create HTML cards with Montserrat font and HelloGrowth brand colors (#2D7D5F to #6CCFAA) → render PNGs via Chrome headless → upload to Supabase Storage bucket instagram-carousels → publish to Instagram @hellogrowth__ via the Edge Function publish-instagram-carousel at https://aevhjbvfxehghoekibjl.supabase.co/functions/v1/publish-instagram-carousel. Include caption with hashtags. No human approval needed. Commit all outputs to git.
```

## 2. Stories Instagram (Todos os dias — 7h BRT)

```
/schedule create
Name: HelloGrowth Stories Instagram
Cron: 0 10 * * *
Prompt: Create Instagram Stories for HelloGrowth (@hellogrowth__). Pick a quick tip or insight about digital reputation, online reviews, or business growth. Create 3-5 story frames as HTML/CSS (1080x1920px, 9:16 format) with Montserrat font, HelloGrowth brand colors (#2D7D5F to #6CCFAA), dark backgrounds. Include interactive elements (polls, quizzes). Render as PNG via Chrome headless. Upload to Supabase Storage. No human approval needed. Commit outputs.
```

## 3. Post LinkedIn (Seg, Qui — 8h BRT)

```
/schedule create
Name: HelloGrowth LinkedIn Post
Cron: 0 11 * * 1,4
Prompt: Create a LinkedIn post for HelloGrowth following the Luna LinkedIn agent persona. Research a trending topic about digital reputation, business growth, or online reviews. Write a text post (1000-1500 chars) in Portuguese (BR) with: hook in first 210 chars, first person storytelling, data anchor, CTA question for comments, 3-5 professional hashtags, no external links in body. Save to output folder. Commit and push.
```
