from telegram import Update,BotCommand
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes

from config import BOT_TOKEN
from database import add_user
from modules.fileid import get_file_id

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.id
    add_user(user)

    await update.message.reply_text(
"""
Welcome to Bot Hosting System

/runbot
/enhance
/fileid
/savefile
"""
)

async def fileid(update:Update,context:ContextTypes.DEFAULT_TYPE):

    msg = update.message.reply_to_message

    if not msg:
        await update.message.reply_text("Reply to file")
        return

    fid = get_file_id(msg)

    await update.message.reply_text(f"FILE ID:\n{fid}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("fileid",fileid))

app.run_polling()