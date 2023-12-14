# 6818768246:AAHR7Q5Fp2gp7t-7ux9UXvZeIE06IGdt8p4

from tracemalloc import start
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Напиши /help")

def help_command(update: Update, context: CallbackContext) -> None:
    help_text = "Это бот"
    update.message.reply_text(help_text)

def main() -> None:
    token = "6818768246:AAHR7Q5Fp2gp7t-7ux9UXvZeIE06IGdt8p4"
    updater = Updater(token)
    dp = updater.dispatcher

    #Команди
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    #Запуск
    updater.start_polling()

if __name__ == "__main__":
    main()