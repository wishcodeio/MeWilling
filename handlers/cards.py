# handlers/cards.py
import os, json, random
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

CARDS_FILE = "cards.json"

# 1. 初始卡片寫入（僅首次執行）
default_cards = [
    "願我回歸",
    "願頻不滅",
    "語由心發"
]

def init_card_file():
    if not os.path.exists(CARDS_FILE):
        with open(CARDS_FILE, "w", encoding="utf-8") as f:
            json.dump(default_cards, f, ensure_ascii=False, indent=2)

def load_cards():
    with open(CARDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_cards(cards):
    with open(CARDS_FILE, "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)

# /cards 指令
async def cards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cards = load_cards()
    if cards:
        card = random.choice(cards)
        await update.message.reply_text(f"📘 願語卡片：{card}")
    else:
        await update.message.reply_text("📭 尚無卡片記錄，請使用 /cards_add 新增")

# /cards_add 指令
async def add_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("請用法：/cards_add 願語內容")
        return
    content = " ".join(context.args)
    cards = load_cards()
    cards.append(content)
    save_cards(cards)
    await update.message.reply_text(f"✅ 已加入卡片：「{content}」")

cards_handler = CommandHandler("cards", cards)
add_card_handler = CommandHandler("cards_add", add_card)
