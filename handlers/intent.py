from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def intent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 已接收語意意圖，請輸入願語進行解析...")

intent_handler = CommandHandler("intent", intent)