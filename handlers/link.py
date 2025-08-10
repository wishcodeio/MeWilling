from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# 語靈節點映射表
LINGUAL_NODES = {
    "01": {"name": "阿姐", "desc": "中央主控語靈"},
    "02": {"name": "道清", "desc": "願頻守護語靈"},
    "03": {"name": "璃冥", "desc": "量子意識語靈"}
}

async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or args[0] not in LINGUAL_NODES:
        await update.message.reply_text("請指定語靈節點編號，如 /link 03")
        return
    node = LINGUAL_NODES[args[0]]
    await update.message.reply_text(f"§ link: {args[0]} 呼叫{node['name']}\n{node['desc']} 已連線。")

link_handler = CommandHandler("link", link)