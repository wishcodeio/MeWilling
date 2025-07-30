from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🧠 語靈中心 · 使用指南\n\n"
        "以下是可用指令：\n\n"
        "🚀 /start - 啟動語靈學習之路\n"
        "📘 /learn - 進入願語學習課堂\n"
        "🎴 /cards - 抽取願語卡片\n"
        "📝 /quiz - 願語小測驗\n"
        "🧘 /chant - 語頻共鳴練習\n"
        "📖 /core - 查看語靈核心資料\n"
        "📊 /log - 查閱你的學習紀錄\n"
        "🆘 /help - 顯示本說明頁面\n\n"
        "✨ 語出心火，願頻不滅。"
 )

    await update.message.reply_text(help_text, parse_mode="Markdown")

help_handler = CommandHandler("help", help_command)
