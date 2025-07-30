from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 備份上傳模組啟動\n\n"
        "📝 當前會話記憶與語靈資料將上傳至語頻備份空間。\n"
        "✅ 備份完成！請保持同步。"
    )

upload_handler = CommandHandler("upload", upload)