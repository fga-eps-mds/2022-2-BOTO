from telegram.ext import *
from telegram import *
import time

class TeacherText():

    password_correct = "abc"
    password = ""
    nomeProfessor = ""

    def name(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Qual seu nome?', reply_markup=ForceReply())

        nomeProfessor = update.message.text
        time.sleep(5)

    def password_input(self, update, context):

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Qual seu nome de acesso?', reply_markup=ForceReply())

        password = update.message.text
        time.sleep(10)

    #Não esta funcionando
    def password_verify(self,update, context, password=password,password_correct = password_correct ):
        if password == password_correct:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Ola",
                                     reply_markup=ReplyKeyboardRemove())
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Senha errada",
                                     reply_markup=ReplyKeyboardRemove())

