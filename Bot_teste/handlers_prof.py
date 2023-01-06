from telegram import *
import emoji

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= "Olá, seja bem vindo ao Boto! \nPrimeiro gostariamos de algumas informações.\n\nPara ter acesso a todos os comandos digite /help.",
                             reply_markup=ReplyKeyboardRemove())

##Lidando com a escolha do start
def handle_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Olá, professor digite /professorEntrada e seu código \nExemplo: '/professorEntrada 123456'",
                             reply_markup=ReplyKeyboardRemove())

## comando para verificar a entrada do professor
def professorEntrada(update,context):
    ##Codigo correto professor
    codigoprofessor = "p123"

    try:
        ##Pegando o codigo digitado na mensagem
        user_message = update.message.text
        user_message = user_message.split(" ")
        user_code = user_message[1]

        ##Verificando se o codigo inserido é o desejado
        if user_code == codigoprofessor:
            ##Descobrindo informaçôes do usuario atraves da conta dele no telegram
            user_info = update.message
            info = {"First_Name": user_info.from_user.first_name, "Last_Name": user_info.from_user.last_name,
                    "Código": user_code}
            print(info)
            update.message.reply_text(
                "Bem vindo, Professora " + user_info.from_user.first_name + "!\n\nEsses são seus comandos:\n/informacoesAlunos\n/estatisticasAluno\n/enviarMensagem.")

        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text = "Código, incorreto. Tente novamente.\nDigite /start para entrar como aluno ou /professorEntrada e seu código. \nExemplo: '/professorEntrada 123456'",
                                     reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text= f"Erro. Tente novamente. \nException: {e}",
                                 reply_markup=ReplyKeyboardRemove())

## comando para quando alguma funcao nao esta pronta
def not_finished(update, context):
    update.message.reply_text("Ainda estamos trabalhando nesse comando." + emoji.emojize(':hammer_and_wrench:'))

##menu de comandos
def help_command(update, context):

    update.message.reply_text("Eu posso te ajudar a enviar e acessar conteúdos e materiais.\n "
                              "Você pode utilizar os seguintes comandos:\n"
                              "\n"
                              "/novo_conteudo - envia um link de um novo conteúdo para a base de dados;\n"
                              "/acessar_conteudo - acessa um conteúdo existente na base de dados;\n"
                              "/deletar_conteudo - apaga um conteudo na base de dados;\n"
                              "/editar_conteudo - altera um conteudo existente na base de dados.\n"
                              "/contatosProfessor - exibe formas de entrar em contato com o professor.")

def plano_de_ensino(update, context):
    update.message.reply_text("https://drive.google.com/file/d/1PqsmJ7QVNAPDuodKE5TQriUnKYLzisqp/view?usp=share_link")



