from telegram.ext import *
import handlers_prof

print("Bot started. . .\n")

TOKEN = "5805348211:AAG5EDK_B5pI0nWMBE1Vr9q4rKeF57ptz-U"

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", handlers_prof.start))
dp.add_handler(CommandHandler("help", handlers_prof.help_command))

dp.add_handler(CommandHandler("novo_conteudo", handlers_prof.not_finished))
dp.add_handler(CommandHandler("acessar_conteudo", handlers_prof.not_finished))
dp.add_handler(CommandHandler("deletar_conteudo", handlers_prof.not_finished))
dp.add_handler(CommandHandler("editar_conteudo", handlers_prof.not_finished))

dp.add_handler(CommandHandler("professorEntrada", handlers_prof.professorEntrada))
dp.add_handler(CommandHandler("plano_de_ensino", handlers_prof.plano_de_ensino))

dp.add_handler(MessageHandler(Filters.text, handlers_prof.handle_message))

updater.start_polling(4)
updater.idle()
