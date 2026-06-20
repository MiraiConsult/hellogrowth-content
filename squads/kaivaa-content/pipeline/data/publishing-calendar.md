# Calendário de Publicações — HelloGrowth

## Frequência

| Dia | Carrossel IG | Stories IG | Post LinkedIn |
|-----|:---:|:---:|:---:|
| Segunda | ✅ | ✅ | ✅ |
| Terça | — | ✅ | — |
| Quarta | ✅ | ✅ | — |
| Quinta | — | ✅ | ✅ |
| Sexta | ✅ | ✅ | — |
| Sábado | — | ✅ | — |
| Domingo | — | ✅ | — |

## Horários (BRT)

- **Carrossel Instagram:** 7h (seg, qua, sex)
- **Stories Instagram:** 7h (todos os dias)
- **Post LinkedIn:** 8h (seg, qui)

## Cron Expressions (UTC)

- Carrossel: `0 10 * * 1,3,5`
- Stories: `0 10 * * *`
- LinkedIn: `0 11 * * 1,4`

## Fluxo

1. Cria conteúdo automaticamente (sem intervenção humana)
2. Publica direto no Instagram/LinkedIn
3. Usa o pipeline completo do squad social-content

## Configuração

- Método: Claude Code `/schedule` (scheduled remote agents)
- Aprovação: automática (sem checkpoint humano)
