from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import config
from bot.handlers import handle_message

async def start(update: Update, context):
    if str(update.effective_user.id) == config.ADMIN_ID:
        await update.message.reply_text("Добро пожаловать, Администратор!")
    else:
        await update.message.reply_text("Access denied. This bot is for the administrator only.")

def main():
    app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
