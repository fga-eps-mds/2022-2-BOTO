from db import nova_con
from mysql.connector import ProgrammingError
import pandas as pd

tabela = pd.read_excel(r"E:\cadastro.xlsx")
numeroDeLinhas = len(tabela.index)
print(numeroDeLinhas)

for i in range(numeroDeLinhas):
    titulo = tabela['TITULO'] [i]
    conteudo = tabela['CONTEUDO'] [i]

    SQL = "INSERT INTO professor(nome,email) VALUES (%s,%s)"
    aluno= (str(titulo),str(conteudo))

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL,aluno)
            con.commit()
            print("sucesso")
        except ProgrammingError as e :
            print(f'Erro: {e.msg}')
        else:
            print('1 id incluido, ID:',cursor.lastrowid)
