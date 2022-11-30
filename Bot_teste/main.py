from telegram.ext import *
from telegram import *
from teacher import TeacherText
import emoji

print("Bot started...")

TOKEN = ""

##comando iniciais
teacherText = "Professor"
studentText = "Aluno"

def start(update, context):
    buttons = [[KeyboardButton(teacherText)], [KeyboardButton(studentText)], [KeyboardButton("Menu de Comandos")]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text = "Olá, seja bem vindo ao Boto! \nPrimeiro gostariamos de algumas informações.",
                             reply_markup=ReplyKeyboardMarkup(buttons))

def handle_message(update, context):
    if teacherText in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,text = "Olá, professor",
                                 reply_markup = ReplyKeyboardRemove())
        t = TeacherText()
        t.name(update, context)
        t.password_input(update, context)

    if studentText in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "Olá, Aluno",
                                 reply_markup=ReplyKeyboardRemove())

    if "Menu de Comandos" in update.message.text:
        update.message.reply_text("Eu posso te ajudar a enviar e acessar conteúdos e materiais.\n "
                                  "Você pode utilizar os seguintes comandos:\n"
                                  "\n"
                                  "/novoConteudo - envia um link de um novo conteúdo para a base de dados;\n"
                                  "/acessarConteudo - acessa um conteúdo existente na base de dados;\n"
                                  "/deletarConteudo - apaga um conteudo na base de dados;\n"
                                  "/editarConteudo - altera um conteudo existente na base de dados.")


## comando para quando alguma funcao nao esta pronta
def not_finished(update, context):
    update.message.reply_text("Ainda estamos trabalhando nesse comando." + emoji.emojize(':hammer_and_wrench:'))

##menu de comandos
def help_command(update, context):

    update.message.reply_text("Eu posso te ajudar a enviar e acessar conteúdos e materiais.\n "
                              "Você pode utilizar os seguintes comandos:\n"
                              "\n"
                              "/novoConteudo - envia um link de um novo conteúdo para a base de dados;\n"
                              "/acessarConteudo - acessa um conteúdo existente na base de dados;\n"
                              "/deletarConteudo - apaga um conteudo na base de dados;\n"
                              "/editarConteudo - altera um conteudo existente na base de dados.")


def main():

    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(CommandHandler("novoConteudo", not_finished))
    dp.add_handler(CommandHandler("acessarConteudo", not_finished))
    dp.add_handler(CommandHandler("deletarConteudo", not_finished))
    dp.add_handler(CommandHandler("editarConteudo", not_finished))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(3)
    updater.idle()

main()
