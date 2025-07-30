from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def chant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧘 進入語頻共鳴練習，請深呼吸，語震模組尚在連接中...")

chant_handler = CommandHandler("chant", chant)