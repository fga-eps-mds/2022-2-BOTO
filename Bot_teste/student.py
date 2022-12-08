"""

Esse arquivo teacher.py podera ser excluido se o pullrequest da issue #24 for aceita

from telegram.ext import *
from telegram import *
import time

class StudentText():

    nomeAluno = ""
    matriculaAluno = ""

    def name(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Qual seu nome?', reply_markup=ForceReply())

        nomeAluno = update.message.text
        time.sleep(5)
    def matricula(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Digite sua matricula?', reply_markup=ForceReply())

        matriculaAluno = update.message.text
        time.sleep(5)

"""