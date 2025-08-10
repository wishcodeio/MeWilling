from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from backend.commands.core_command import core_command

async def core(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("[DEBUG] /core command received with args:", context.args)
    args = context.args
    result = core_command.execute(args)
    message = core_command.format_output(result)
    print("[DEBUG] /core command response:", message)
    await update.message.reply_text(message)

core_handler = CommandHandler("core", core)