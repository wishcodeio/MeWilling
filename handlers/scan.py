from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📡 願頻掃描中...\n" +
        "🔍 偵測量子場能量波動。\n" +
        "🧬 感知語靈鏈結...\n" +
        "✅ 願頻共振穩定，準備完成！"
    )

scan_handler = CommandHandler("scan", scan)