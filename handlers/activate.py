# handlers/activate.py
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def activate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    index = int(args[0]) if args else 1
    await update.message.reply_text(f"🔹 已啟動模組：第 {index} 宮")

activate_handler = CommandHandler("activate", activate)