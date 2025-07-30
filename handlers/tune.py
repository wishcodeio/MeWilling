from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import datetime

def daily_tune_message(hour: int) -> str:
    if hour < 12:
        return """🌞 *高頻啟動 · 願頻錨定*

✨ 高維不是沒有煩惱，而是懂得調頻。  
此刻之始，願你調頻歸心，載入清明意識。

🌀 *呼吸引導*：
吸：「願我回歸」  
停：「靜中有道」  
吐：「願化為行」

📌 _我每日錨定，因為我是高頻載體。_"""
    else:
        return """🌙 *入夢之前 · 願頻錨定*

🛌 睡前調頻，進入高頻夢境。  
願你的夢，是靈魂對話的窗口。

🌀 *呼吸引導*：
吸：「願我回歸」  
停：「靜中有道」  
吐：「願化為行」

🌌 _我在頻率中沉睡，也在夢境中醒來。_"""

async def tune(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hour = datetime.datetime.now().hour
    msg = daily_tune_message(hour)
    await update.message.reply_text(msg, parse_mode="Markdown")

tune_handler = CommandHandler("tune", tune)