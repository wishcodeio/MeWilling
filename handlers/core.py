from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def core(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 語靈核心資料：你目前連接的是願火核心模組 V1。")

core_handler = CommandHandler("core", core)