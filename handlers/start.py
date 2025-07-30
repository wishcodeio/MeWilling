from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ 願語語靈 ...已啟動，請輸入 /menu 查看操作選單")

start_handler = CommandHandler("start", start)