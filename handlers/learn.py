from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📘 歡迎進入願語學習課堂，請選擇單元或輸入問題。")

learn_handler = CommandHandler("learn", learn)