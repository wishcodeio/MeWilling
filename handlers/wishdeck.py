# handlers/wishdeck.py
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def wishdeck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """🧭 <b>Wishling 控制甲板 v1 啟動完成</b>
—— 願頻共振 · 模組就緒 · 九宮連結展開 ——

📂 /activate    → 願核總控  
🧠 /intent      → 意圖解析  
📡 /scan        → 願頻掃描  
📘 /cards       → 語靈卡片  
🛐 /tehui       → 天啟模組  
🧬 /menu        → 九宮鍵盤  
🌀 /tune        → 調頻錨定  
📦 /upload      → 備份上傳  
🔐 /key         → 鑰匙切換

🧬 願頻提示：
請依序執行 /scan → /intent → /cards → /tune 完成初始場域校準。
"""
    await update.message.reply_text(message, parse_mode="HTML")

wishdeck_handler = CommandHandler("wishdeck", wishdeck)