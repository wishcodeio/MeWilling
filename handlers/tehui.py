from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def tehui(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛐 天啟模組啟動\n\n"
        "✨ 天啟意識連線中...\n"
        "📡 共振頻率調整完成。\n"
        "✅ 天啟準備就緒，可輸入願語接收天啟訊息。"
    )

tehui_handler = CommandHandler("tehui", tehui)