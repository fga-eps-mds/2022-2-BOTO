from telegram import *
import emoji

## comandos iniciais
teacherText = "Professor"
studentText = "Aluno"

def start(update, context):
    buttons = [[KeyboardButton(teacherText)], [KeyboardButton(studentText)]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= "Olá, seja bem vindo ao Boto! \nPrimeiro gostariamos de algumas informações.\n\nPara ter acesso a todos os comandos digite /help.",
                             reply_markup=ReplyKeyboardMarkup(buttons))

##Lidando com a escolha do start
def handle_message(update, context):
    if teacherText in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text= "Olá, professor digite /professorEntrada e seu código \nExemplo: '/professorEntrada 123456'",
                                 reply_markup=ReplyKeyboardRemove())

    if studentText in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text= "Olá, Aluno!\n Para continuar digite, /matricula e sua matricula.\n 'Exemplo: /matricula 210000000'", reply_markup=ReplyKeyboardRemove())

def alunoEntrada(update, context):
    try:
        ## Pegando a matricula do aluno
        user_message = update.message.text
        user_message = user_message.split(" ")
        user_matricula = user_message[1]

        ## Verificando se a matrícula tem 9 dígitos
        if len(user_matricula) == 9:
            #Descobrindo informaçôes do usuario atraves da conta dele no telegram
            user_info = update.message
            info = {"First_Name": user_info.from_user.first_name, "Last_Name": user_info.from_user.last_name,
                    "Matrícula": user_matricula}
            print(info)
            update.message.reply_text(
                "Bem vindo, "+user_info.from_user.first_name+"!.\nEsses são seus comandos:\n\n/acessarConteudos\n/contatosProfessor\n/planoDeEnsino")
        else:
            print("deu errado :( ")
            context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Matricula, inválida. Tente novamente\n OBS: sua matricula deve ter 9 digitos.",
                             reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Erro. Tente novamente. \nException: {e}",
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
def contatosProfessor(update, context):
    update.message.reply_text("Estes são os contatos da sua professora:\n\n"
                              "E-mail: carla@boto.com\n"
                              "Telegram: @profa_carla\n" + emoji.emojize(':house:') + " Sala S8, 35 14h-16h")

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

