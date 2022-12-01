from telegram.ext import *
from telegram import *
from teacher import TeacherText
from student import StudentText
import emoji


TOKEN = ""

##comando iniciais
teacherText = "Professor"
studentText = "Aluno"

def start(update, context):
    buttons = [[KeyboardButton(teacherText)], [KeyboardButton(studentText)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Olá, seja bem vindo ao Boto! \nPrimeiro gostariamos de algumas informações.", reply_markup=ReplyKeyboardMarkup(buttons))

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
        t = StudentText()
        t.name(update, context)
        t.matricula(update, context)

def main():

    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(3)
    updater.idle()

main()
