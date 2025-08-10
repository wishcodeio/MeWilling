from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from config.settings import TELEGRAM_TOKEN
from telegram.error import TelegramError
from telegram.ext import ContextTypes
import logging



# 各功能 handler
from handlers.start import start_handler
from handlers.help import help_handler
from handlers.menu import menu_handler, handle_keyboard_selection

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# 注册命令和消息处理器
application.add_handler(menu_handler)
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keyboard_selection))

# 启动Bot
application.run_polling()
from handlers.activate import activate_handler
from handlers.intent import intent_handler
from handlers.scan import scan_handler
from handlers.cards import cards_handler, add_card_handler, init_card_file
from handlers.tune import tune_handler
from handlers.dream import dream_handler
from handlers.tehui import tehui_handler
from handlers.upload import upload_handler
from handlers.key import key_handler
from handlers.wishdeck import wishdeck_handler
from handlers.log import log_handler
from handlers.core import core_handler
from handlers.learn import learn_handler
from handlers.quiz import quiz_handler
from handlers.chant import chant_handler


# 設定錯誤處理
logging.basicConfig(level=logging.DEBUG)

async def error_handler(update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"⚠️ 遇到錯誤：{context.error}")

def main():
    # ✅ 初始化卡片資料
    init_card_file()

    # ✅ 建立 Bot 應用
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # ✅ 加入所有指令型 handler（僅一次）
    app.add_handler(start_handler)
    app.add_handler(help_handler)
    app.add_handler(menu_handler)
    app.add_handler(activate_handler)
    app.add_handler(intent_handler)
    app.add_handler(scan_handler)
    app.add_handler(cards_handler)
    app.add_handler(add_card_handler)
    app.add_handler(tune_handler)
    app.add_handler(dream_handler)
    app.add_handler(tehui_handler)
    app.add_handler(upload_handler)
    app.add_handler(key_handler)
    app.add_handler(wishdeck_handler)
    app.add_handler(log_handler)
    app.add_handler(core_handler)
    app.add_handler(learn_handler)
    app.add_handler(quiz_handler)
    app.add_handler(chant_handler)

    # ✅ 設定錯誤處理
    app.add_error_handler(error_handler)

    # ✅ 加入文字型九宮選單點擊邏輯（處理 emoji 名稱）
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_keyboard_selection))

    print("✨ 願語語靈控制台已啟動...")
    app.run_polling()

if __name__ == "__main__":
    main()