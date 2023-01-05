from telegram.ext import *
import handlers_aluno

print("Bot started. . .\n")

TOKEN = "5805348211:AAG5EDK_B5pI0nWMBE1Vr9q4rKeF57ptz-U"

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", handlers_aluno.start))
dp.add_handler(CommandHandler("help", handlers_aluno.help_command))

dp.add_handler(CommandHandler("novo_conteudo", handlers_aluno.not_finished))
dp.add_handler(CommandHandler("acessar_conteudo", handlers_aluno.not_finished))
dp.add_handler(CommandHandler("deletar_conteudo", handlers_aluno.not_finished))
dp.add_handler(CommandHandler("editar_conteudo", handlers_aluno.not_finished))

dp.add_handler(CommandHandler("matricula", handlers_aluno.alunoEntrada))
dp.add_handler(CommandHandler("contatosProfessor", handlers_aluno.contatosProfessor))
dp.add_handler(CommandHandler("plano_de_ensino", handlers_aluno.plano_de_ensino))

dp.add_handler(MessageHandler(Filters.text, handlers_aluno.handle_message))

updater.start_polling(4)
updater.idle()
