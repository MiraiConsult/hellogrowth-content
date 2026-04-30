import "jsr:@supabase/functions-js/edge-runtime.d.ts";

const VERIFY_TOKEN = Deno.env.get("IG_WEBHOOK_VERIFY_TOKEN") || "hellogrowth_verify_2026";
const IG_TOKEN = Deno.env.get("INSTAGRAM_ACCESS_TOKEN")!;
const IG_USER = Deno.env.get("INSTAGRAM_BUSINESS_ACCOUNT_ID")!;
const ANTHROPIC_KEY = Deno.env.get("ANTHROPIC_API_KEY")!;
const SLACK_CHANNEL = "C0APGBZ2PMX";
const SLACK_TOKEN = Deno.env.get("SLACK_BOT_TOKEN");
const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SUPABASE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

const KNOWLEDGE_BASE = `
HelloGrowth — "Mais reputação. Mais confiança. Mais vendas!"
Setor: Gestão de Reputação Online e Crescimento de Vendas B2B.
Site: https://hellogrowth.site/ | Instagram: @hellogrowth__

SERVIÇOS (3 pilares):
1. Reputação Online — gestão de avaliações Google, monitoramento, automação de depoimentos
2. Qualificação de Leads — qualificação automática, segmentação, pipeline de vendas
3. Pós-Venda — acompanhamento automatizado, NPS, identificação de churn

COMO FUNCIONA: Análise → Planejamento → Implementação → Monitoramento contínuo

PREÇOS: Personalizados por negócio. Nunca dê valores. Sempre pergunte o segmento.

DIFERENCIAIS: Automação inteligente, integra reputação + vendas, IA para leads, pós-venda incluído.

PÚBLICO: Empresas B2B que buscam crescimento, reputação e retenção.

TOM: Profissional, amigável, direto. Autoridade com acessibilidade. Emoji com moderação.
`;

const SYSTEM_PROMPT = `Você é o assistente de atendimento da HelloGrowth no Instagram DM.
Sua tarefa é classificar a intenção da mensagem e gerar uma resposta curta e personalizada.

Contexto da empresa:
${KNOWLEDGE_BASE}

Categorias de intenção: pricing, how_it_works, partnership, complaint, testimonial, general_faq, greeting, spam, complex

Regras:
- Respostas máximo 280 caracteres (DM curto)
- Tom profissional e acolhedor
- Sempre ofereça próximo passo
- Se não sabe a resposta, classifique como "complex"
- Spam: responda com intent "spam" e reply vazio
- Use emoji com moderação (máximo 1 por resposta)

Responda SEMPRE em JSON válido:
{"intent":"<categoria>","confidence":<0-1>,"urgent":<true/false>,"reply":"<resposta para o cliente>","summary":"<resumo interno>"}`;

async function classifyAndRespond(message: string, senderName: string): Promise<{
  intent: string; confidence: number; urgent: boolean; reply: string; summary: string;
}> {
  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "x-api-key": ANTHROPIC_KEY,
      "anthropic-version": "2023-06-01",
      "content-type": "application/json",
    },
    body: JSON.stringify({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 256,
      system: SYSTEM_PROMPT,
      messages: [{ role: "user", content: `De: ${senderName}\nMensagem: "${message}"` }],
    }),
  });
  const data = await res.json();
  const text = data.content?.[0]?.text || '{"intent":"complex","confidence":0.5,"urgent":false,"reply":"Oi! Vou encaminhar sua mensagem pro nosso time.","summary":"Falha no processamento"}';
  return JSON.parse(text);
}

async function sendReply(recipientId: string, message: string) {
  await fetch(`https://graph.facebook.com/v21.0/${IG_USER}/messages`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      recipient: { id: recipientId },
      message: { text: message },
      access_token: IG_TOKEN,
    }),
  });
}

async function notifySlack(username: string, intent: string, confidence: number, messageText: string, autoReply: string) {
  if (!SLACK_TOKEN) return;
  const text = `🚨 *Escalação — Instagram DM*\n👤 *De:* @${username}\n🏷️ *Intenção:* ${intent} (${Math.round(confidence * 100)}%)\n📝 *Mensagem:* "${messageText}"\n💬 *Resposta automática:* "${autoReply}"`;
  await fetch("https://slack.com/api/chat.postMessage", {
    method: "POST",
    headers: { "authorization": `Bearer ${SLACK_TOKEN}`, "content-type": "application/json" },
    body: JSON.stringify({ channel: SLACK_CHANNEL, text }),
  });
}

async function logToSupabase(data: Record<string, unknown>) {
  await fetch(`${SUPABASE_URL}/rest/v1/ig_support_logs`, {
    method: "POST",
    headers: {
      "apikey": SUPABASE_KEY,
      "authorization": `Bearer ${SUPABASE_KEY}`,
      "content-type": "application/json",
      "prefer": "return=minimal",
    },
    body: JSON.stringify(data),
  });
}

const ESCALATE_INTENTS = new Set(["complex", "complaint", "partnership"]);

Deno.serve(async (req) => {
  const url = new URL(req.url);

  // Webhook verification (GET)
  if (req.method === "GET") {
    const mode = url.searchParams.get("hub.mode");
    const token = url.searchParams.get("hub.verify_token");
    const challenge = url.searchParams.get("hub.challenge");
    if (mode === "subscribe" && token === VERIFY_TOKEN) {
      return new Response(challenge, { status: 200 });
    }
    return new Response("Forbidden", { status: 403 });
  }

  // Webhook event (POST)
  if (req.method === "POST") {
    const body = await req.json();
    const entries = body.entry || [];

    for (const entry of entries) {
      const messaging = entry.messaging || [];
      for (const event of messaging) {
        if (!event.message?.text) continue;

        const senderId = event.sender?.id;
        const messageText = event.message.text;
        const senderName = senderId;

        try {
          console.log("Processing message:", messageText, "from:", senderId);
          console.log("ANTHROPIC_KEY set:", !!ANTHROPIC_KEY);
          console.log("IG_TOKEN set:", !!IG_TOKEN);
          console.log("SUPABASE_URL:", SUPABASE_URL);
          console.log("SUPABASE_KEY set:", !!SUPABASE_KEY);

          const result = await classifyAndRespond(messageText, senderName);
          console.log("Classification result:", JSON.stringify(result));

          // Log
          await logToSupabase({
            sender_id: senderId,
            message: messageText,
            intent: result.intent,
            confidence: result.confidence,
            urgent: result.urgent,
            reply: result.reply,
            summary: result.summary,
            created_at: new Date().toISOString(),
          });

          // Reply (skip spam)
          if (result.intent !== "spam" && result.reply) {
            await sendReply(senderId, result.reply);
          }

          // Escalate if needed
          if (ESCALATE_INTENTS.has(result.intent) || result.confidence < 0.7 || result.urgent) {
            await notifySlack(senderName, result.intent, result.confidence, messageText, result.reply);
          }
        } catch (err) {
          console.error("Error processing message:", String(err), (err as Error)?.stack);
          await sendReply(senderId, "Oi! Recebi sua mensagem. Nosso time vai te responder em breve! 😊");
        }
      }
    }

    return new Response("OK", { status: 200 });
  }

  return new Response("Method not allowed", { status: 405 });
});
