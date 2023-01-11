from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
import logging
import emoji

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

"""
Essa parte e para lidar com a comandos extras
"""
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

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Conversa encerrada.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

"""
Essa parte e para lidar o envio de plano de ensino
"""

# isso esta com algum erro, mas depois sera alterado entao nao vou resolver ou excluir agora
def plano_de_ensino(update, context):
    update.message.reply_text("https://drive.google.com/file/d/1PqsmJ7QVNAPDuodKE5TQriUnKYLzisqp/view?usp=share_link")


"""
Essa parte e para lidar com a entrada do professor
"""
ENTRADA = range(4)

async def start(update, context) -> int:
    await update.message.reply_text("Olá, professor digite código")

    return ENTRADA

## comando para verificar a entrada do professor
async def professorEntrada(update,context)-> int:
    ##Codigo correto professor
    codigoprofessor = "p123"

    try:
        ##Pegando o codigo digitado na mensagem
        user_message = update.message.text
        user_code = user_message

        ##Verificando se o codigo inserido é o desejado
        if user_code == codigoprofessor:
            ##Descobrindo informaçôes do usuario atraves da conta dele no telegram
            user_info = update.message
            info = {"First_Name": user_info.from_user.first_name, "Last_Name": user_info.from_user.last_name,
                    "Código": user_code}
            print(info)
            await update.message.reply_text(
                "Bem vindo, Professora " + user_info.from_user.first_name + "!\n\nEsses são seus comandos:\n/informacoesAlunos\n/estatisticasAluno\n/enviarMensagem.")

        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text = "Código, incorreto. Tente novamente.\nDigite /start para entrar como aluno ou /professorEntrada e seu código. \nExemplo: '/professorEntrada 123456'",
                                     reply_markup=ReplyKeyboardRemove())


    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                 text= f"Erro. Tente novamente. \nException: {e}",
                                 reply_markup=ReplyKeyboardRemove())


    return ConversationHandler.END


entrada_conversation = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        ENTRADA: [MessageHandler(filters.TEXT, professorEntrada)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

"""
Essa parte e para lidar com a conversa de envio de conteudo com o professor
"""

def cadastrar_conteudo(update,context):
    update.message.reply_text("Para cadastrar o seu conteudo faça uma copia da planilha abaixo, depois a preencha.")
    update.message.reply_text("Tome cuidado não inclua nem exclua alguma coluna e nem altere seu nome.")
    update.message.reply_text("https://1drv.ms/x/s!AkMmeo5LMub_aWBf1UGvt0X_hTs?e=t3JAMj")
    update.message.reply_text("Apos preenche-la envie no chat e digite /enviar_planilha")

PLANILHA = range(4)

async def enviar_planilha (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Envie a planilha:")

    return PLANILHA

async def recebe_planilha (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Recebido!")

    user = update.message.from_user
    logger.info("Planilha de %s: %s", user.first_name, update.message.text)
    print(logger.info)

    return ConversationHandler.END


enviar_planilha_conversation = ConversationHandler(
    entry_points=[CommandHandler("enviar_planilha", enviar_planilha)],
    states={
        PLANILHA: [MessageHandler(filters.TEXT, recebe_planilha)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)