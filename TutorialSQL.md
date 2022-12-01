# Tutorial SQL

## O que é o SQL?

Linguagem padrão para trabalhar com bancos de dados, ela é declarativa, o que não exije profundo conhecimento de programação.
Sua sigla significa **Standard Query Language**, linguagem padrão para realizar queries.

###### Queries: consulta ou dúvida, uma solicitação de informações feita ao banco de dados.

## Principais comandos
Para começarmos, vamos utlizar de exemplo uma planilha do nosso projeto de bot de conteudos,
ela se chamará `bot_conteudos` e terá por variáveis `codigo`, `disciplina` e `professor`. Agora com essa visualização, vamos aos principais comandos:

* `SELECT`: busca linhas em tabelas de acordo com um critério definido dentro da chamada cláusula de `WHERE`
```
SELECT disciplina FROM bot_conteudos WHERE codigo = 0138;
```
* `INSEERT`: insere novas linhas na tabela
```
INSERT INTO bot_conteudos (codigo, disciplina, professor) VALUES (0138, 'Métodos 
de Desenvolvimenos de Software', 'Carla Aguiar');
```
* `UPDATE`: atualiza linhas no banco de dados de acordo com um críterio de `WHERE`
```
UPDATE bot_conteudos SET professor = 'Hilmer' WHERE codigo = 0138;
```
* `DELETE`: remove linhas da tabela de acordo com um crítério
```
DELETE FROM bot_conteudos WHRE codigo = 0138;
```


## Modelagem de banco de dados

É a forma que definimos como as tabelas vão armazenar e relacionar os nossos dados, algo organizado que não seja de difícil manutencção e identificação.

* `CREATE`: criar o banco de dados e as tabelas que ele contém.
```
CREATE DATABASE bot_conteudos;
```
* `CREATE TABLE`: criação de tabelas e de colunas onde se armazena os registros.
```
CREATE TABLE conteudos(codigo int, disciplina VARCHAR(50), professor VARCHAR(50));
```
Aqui estamos especificando as colunas que a tabela irá conter e os tipos dedados que cada uma aceitará e o comprimento máximo para os campos do tipo VARCHAR.
* `ALTER TABLE`: responsável por modificar a estrutura de objetos armazenados no banco, podemos adicionar ou remover colunas e ainda alterar o tipo de dados especificados para uma coluna.
```
ALTER TABLE bot_conteudos ADD turma VARCHAR(10);
```

## Comandos que aprimoram a experiência no SQL

* Para buscas mais complexas e refinadas pro `SELECT`, podemos usar as cláusulas `JOIN`. Com elas se pode **combinar linhas de várias tabelas com base na relação existente entre as colunas dessa tabela**. 
  - `INNER JOIN`: retorna registros iguais de ambas as tabelas;
  - `LEFT JOIN`: retorna oa registros da tabela esquerda e os valores iguais da tabela direita;
  - `RIGHT JOIN`: retorna os registros da tabela direita e os valores iguais da tabela esquerda;
  - `FULL JOIN`: retorna os registros de ambas as tabelas quando há correspondentes entre si.

* `UNION`: utilizada para combinar o conjunto de resultados de dois ou mais comandos `SELECT`. Mas devem seguir as regras:
  - cada `SELECT`deve ter o mesmo número de colunas;
  - as colunas de cada `SELECT`devem estar na mesma ordem;
  - os tipos de dados das colunas devem ser iguais.
 ```
 SELECT professor FROM bot_conteudos
 UNION
 SELECT alunos FROM alunos_bot_conteudos;
 ```
 * `CASE`: define condições que devem ser atendidas durante a execução de um comando. Para melhor visualização, vamos imagianr que o professor quer dar uma nota extra para quem ativou o bot de conteúdos da disciplina. Para isso vamos pensar em 1 como assinante e 0 para não assinante, assim temos:
 ```
 SELECT aluno, assinante
 CASE
 WHEN assinante = 1 THEN 100*0.01
 ELSE 0
 END AS ponto_extra
 FROM alunos_assinantes;
 ```
* `LIKE`: encontrar padrão em diferentes strings. Para isso utilizamos (%) que indica a posição e (_ ) que serve para representar uma quantidade de caracteres.
  - `LIKE`: 'a%': retorna qualquer string qye inicie com "a";
  - `LIKE`: '%Aguiar': retorna strings que terminam com "Aguiar";
  - `LIKE`: '_ b%': retorna strings que tenham a letra "b" na segunda posição;
 ```
 SELECT * FROM bot_conteudos WHERE disciplina LIKE 'Metodos%';
 ```
 * `BETWEEN`: seleciona valores em um determinado intervalo, podendo ser strings, datas ou números. Para o exemplo do nosso bot de conteúdos, podemos fazer uma busca pelos códigos de determinadas disciplinas num intervalo de 0130 e 0158, assim:
 ```
 SELECT * FROM bot_conteudos WHERE codigo BETWEEN 0130 AND 0158;
 ```
 Case fosse o contrário, fora desse intervalo, teríamos:
 ```
 SELECT * FROM bot_conteudos WHERE codigo NOT BETWEEN 0130 AND 0158;
```

## Para mais

Aqui abordamos algumas funcionalidades do SQL, mas há muitas outras que podem ser exploradas. A prória Microsoft disponibilizou uma documentação que pode ser encontrada [aqui](https://learn.microsoft.com/pt-br/sql/?view=sql-server-ver16).
Além de tutoriais práticos que existem no Youtube, aqui vai uma listagem:
* [Introdução SQL](https://www.youtube.com/watch?v=90wh_Gms8gs&ab_channel=RafaBrito);
* [Basic SQL in 15 Minutes](https://www.youtube.com/watch?v=90wh_Gms8gs&ab_channel=RafaBrito);
* [Dicionario do Programador - SQL](https://www.youtube.com/watch?v=kMznyI7r2Tc&ab_channel=C%C3%B3digoFonteTV).

Em sites também há mais funcionalidades que podem nos ajudar ao decorrer do projeto e facilitar nossas vidas, encontram-se [aqui](https://blog.betrybe.com/sql/).












