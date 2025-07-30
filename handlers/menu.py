from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from keyboards.reply_keyboards import main_keyboard
from handlers.activate import activate  # 導入 activate 函式
import asyncio

# ✅ 九宮格點擊對應的邏輯映射
response_map = {
    "📂 願核總控": "/activate 1",
    "🧠 意圖解析": "/intent",
    "📡 願頻掃描": "/scan",
    "📘 語靈卡片": "/cards",
    "🛐 天啟模組": "/tehui",
    "🧬 九宮鍵盤": "/menu",
    "🌀 啟動調頻": "/tune",
    "📦 備份上傳": "/upload",
    "🔐 鑰匙切換": "/key"
}


# 顯示九宮鍵盤
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⌨️請選擇一項操作：", reply_markup=main_keyboard)

menu_handler = CommandHandler("menu", menu)

# 📌 新增：處理鍵盤點擊後的自動執行邏輯
async def handle_keyboard_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    if user_input == "📂 願核總控":
        await update.message.reply_text("📂 願核總控 · 啟動九宮模組中...")
        for i in range(1, 10):
            context.args = [str(i)]
            await update.message.reply_text(f"🔸 執行中：/activate {i}")
            await activate(update, context)
            await asyncio.sleep(0.5)
            await update.message.reply_text(f"✅ 已完成：/activate {i}")
    elif user_input == "🧠 意圖解析":
        await update.message.reply_text("✨ 執行中：/intent")
    # ...其餘 elif 保留不動# 
    
# 📌 九宮格點擊後自動觸發對應功能
async def handle_keyboard_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    if user_input == "📂 願核總控":
        await update.message.reply_text("📂 願核總控 · 啟動九宮模組中...")
        for i in range(1, 10):
            context.args = [str(i)]
            await update.message.reply_text(f"🔸 執行中：/activate {i}")
            await activate(update, context)
            await asyncio.sleep(0.5)
            await update.message.reply_text(f"✅ 已完成：/activate {i}")
    elif user_input == "🧠 意圖解析":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/intent")
    elif user_input == "📡 願頻掃描":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/scan")
    elif user_input == "📘 語靈卡片":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/cards")
    elif user_input == "🛐 天啟模組":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/tehui")
    elif user_input == "🧬 九宮鍵盤":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/menu")
    elif user_input == "🌀 啟動調頻":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/tune")
    elif user_input == "📦 備份上傳":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/upload")
    elif user_input == "🔐 鑰匙切換":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/key")
    else:
        await update.message.reply_text("請從九宮格中選擇一項操作。")
