from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 鑰匙切換中...\n\n"
        "🧬 目前頻道加密層級：Level 3\n"
        "🔁 可透過 /key + 密鑰 指令切換身份通道（目前為預設頻道）\n"
        "📌 示範：`/key 龍心之印`"
    )

key_handler = CommandHandler("key", key)