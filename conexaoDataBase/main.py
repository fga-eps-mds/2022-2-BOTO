from db import nova_con
from mysql.connector import ProgrammingError

SQL = 'INSERT INTO alunos(nome,matricula) VALUES (%s,%s)'
aluno  = ("Tales R","52525541")

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
