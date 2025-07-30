from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 願語小測驗尚未實作，稍後會提供題庫模組。")

quiz_handler = CommandHandler("quiz", quiz)