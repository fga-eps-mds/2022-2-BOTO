import constants as keys
from telegram.ext import *
import responses as res

print("Bot started ...")


def start(update, context):
    update.message.reply_text("Digite algo!")


def help_command(update, context):
    update.message.reply_text("Boa sorte")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = res.respostas(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Atualizar {update} causou erro {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(3)
    updater.idle()


main()
