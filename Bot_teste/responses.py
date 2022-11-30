from datetime import datetime


def respostas(entrada):
    mensagem = str(entrada).lower()

    if mensagem in ("oi", "ola", "bom dia", "oie"):
        return "E aí?"

    if mensagem in ("qual o seu nome?", "qual o seu nome", "qual o teu nome?", "qual o teu nome", "qual seu nome?", "qual seu nome"):
        return "Eu sou o Boto"

    if mensagem in ("me ajuda?", "me ajuda", "tu me ajuda?", "tu me ajuda", "vc me ajuda?", "vc me ajuda", "voce me ajuda?", "voce me ajuda",  "você me ajuda?", "você me ajuda"):
        return "se vira"

    if mensagem in ("horas", "horas?"):
        agora = datetime.now()
        data = agora.strftime("%d/%m/%y,   %H:%M:%S")

        return str(data)

    return "I'm sorry Dave, I'm afraid I can't do that"
