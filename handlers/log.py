from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 這是你的語靈學習紀錄，目前尚未接入紀錄資料。")

log_handler = CommandHandler("log", log)