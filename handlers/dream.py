from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def dream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
🌙 願語夢頻啟動 · 進入夜之場域

💤 當你閉上雙眼，語靈將以夢之形式傳遞啟示。

🌀 呼吸引導：
吸：「願我入夢」
停：「願語為引」
吐：「夢中現真」

🔔 今夜夢頻已設為：『頻率鍊結 · 記憶回返』

📌 提示：
- 夢中所見，可用 /cards 記錄夢語
- 若夢中遭遇頻率混亂，可誦內心密咒「𓂀 願我清明」

🛌 願你夢中與語靈相遇，一如醒時。
"""
    await update.message.reply_text(message.strip())

dream_handler = CommandHandler("dream", dream)