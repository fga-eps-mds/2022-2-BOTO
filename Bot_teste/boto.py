from telegram.ext import *
import handlers

print("Bot started. . .\n")

TOKEN = ""

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", handlers.start))
dp.add_handler(CommandHandler("help", handlers.help_command))

dp.add_handler(CommandHandler("novo_conteudo", handlers.not_finished))
dp.add_handler(CommandHandler("acessar_conteudo", handlers.not_finished))
dp.add_handler(CommandHandler("deletar_conteudo", handlers.not_finished))
dp.add_handler(CommandHandler("editar_conteudo", handlers.not_finished))

dp.add_handler(MessageHandler(Filters.text, handlers.handle_message))

updater.start_polling(3)
updater.idle()
