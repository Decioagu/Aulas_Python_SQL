# Aulas_Python_SQL

- __CRUD em SQL__, uma sigla para __Criar, Rear, Atualizar e Deletar__ (em português: Criar, Ler, Atualizar e Excluir), representa as operações fundamentais utilizadas para gerenciar dados em um banco de dados relacional, como o próprio SQL.

- Veja um resumo de cada operação:
    - __Create (Criar)__: Insere novos registros em uma tabela do banco de dados.
    - __Read (Ler)__: Recupera dados existentes na tabela, podendo filtrar por critérios específicos.
    - __Update (Atualizar)__: Modifica o conteúdo de registros já existentes.
    - __Delete (Excluir)__: Remove registros da tabela.

- CRUD - Create   |  Read        |  Update     |  Delete
- =====> Criar    |  Ler         |  Atualizar  |  Excluir
- <==========================================================>
- SQL  - INSERT   |  SELECT      |  UPDATE     |  DELETE
- =====> Inserir  |  Selecionar  |  Atualizar  |  Excluir
- <==========================================================>
- API  - POST    |  GET         |  PUT        |  DELETE
- =====> Enviar  |  Selecionar  |  Atualizar  |  Excluir
---

## MySQL
- __PyMySQL__ é uma biblioteca leve e pura de Python que facilita a interação com bancos de dados MySQL.
  
OBS: para execução do programa é necessário esta conectado no banco de dados já criado no __SGBD__ de sua escolha.
-   SGBD = Sistema de Gerenciamento de Banco de Dados

---
### Arguivo .env
- O Python-dotenv é uma biblioteca Python que facilita o gerenciamento de variáveis de ambiente em seus projetos. Ele permite que você armazene suas variáveis em um arquivo __.env__ separado, o que pode ser útil para manter suas __configurações confidenciais e organizadas__.
---

**aula_01**
- __CREATE__ (Criar):
- Esta operação permite __inserir__ novos registros em uma tabela (colunas).
---
    CREATE TABLE [table_name] (
    [column1] [type_dado] [regras],
    [column2] [type_dado] [regras],
    ... 
    );
---

**aula_02**
- __INSERT INTO__ (Inserir):
- É uma instrução usada no contexto de bancos de dados relacionais para __inserir__ novas linhas em uma tabela (valores).
---
    INSERT INTO table_name (column1, column2, ...)
    VALUES (value1, value2, ...)
---

**aula_03**
- __TRUNCATE TABLE__ (Excluir):
- É uma instrução utilizada em SQL para remover __TODAS AS LINHAS DE UMA TABELA__ de maneira rápida e eficiente.
---
    TRUNCATE TABLE table_name;
---

**aula_04 e aula_05**
- __INSERT INTO__ (Inserir):
- Inserir um ou mais valores no banco de dados de forma __SEGURA__.
---
    INSERT INTO table_name (column1, column2, ...)
    VALUES (%s, %s, ...)
---

**aula_06**
- __SELECT__ (Selecionar):
- É a instrução fundamental em SQL para __exibir__ dados de tabelas em um banco de dados relacional.
    -   .fetchone(): Recupera apenas uma linha do conjunto de resultados.
    -   .fetchmany(n): Recupera linhas do conjunto de resultados "n"
    -   .fetchall(): Recuperar todas as linhas de banco de dados em uma lista de tuplas.
    -   iter(cursor): Permite iterar sobre o conjunto de resultados linha por linha.
---
    SELECT [column1], [column2], ...
    FROM [table_name]
    [WHERE condition]
    [ORDER BY column_name [ASC | DESC]]
    [LIMIT offset, rows];
---

**aula_07**
- __DELETE__ (Excluir):
- É uma instrução usada em SQL para remover registros específicos de uma tabela. É crucial para a manipulação de dados, pois permite a exclusão de linhas que não são mais necessárias ou que estejam incorretas.
---
    DELETE FROM [table_name]
    WHERE [condition];
---

**aula_08**
- __UPDATE__ (Atualizar):
- Serve para alterar informações armazenadas em tabelas.
---
    UPDATE [tabela_nome]
    SET [coluna1] = [novo_valor1], [coluna2] = [novo_valor2], ...
    WHERE [condição];
---

**aula_09**
- __SELECT__ (Selecionar):
- __Cursor de banco de dados__: Em sistemas de banco de dados, existem cursores roláveis. Eles permitem a navegação pelos dados, uma vez solicitado os dados o cursor permanece na posição conforme a busca solicitada como iterável, não permitindo nova consulta dos dados já exibidos.
---

**aula_10**
- __SELECT__ (Selecionar):
- cursorclass = pymysql.cursors.DictCursor
- Retorna o resultado do __SELECT__ como dicionários:
---

**aula_11**
- __SELECT__ (Selecionar):
- "cursor.scroll()": É o método que permite reposicionar o cursor para posição desejada para nova consulta.

**aula_12**
- __SELECT__ (Selecionar):
- cursor.fetchall_unbuffered(): é um método utilizado em algumas bibliotecas Python para interagir com bancos de dados, como MySQL Connector/Python. Ele serve para recuperar todas as linhas de um resultado de consulta sem armazená-las na memória de uma só vez.

**aula_13**
- __SELECT__ (Selecionar):
- Rastreia a contagem de linhas: "cursor.rowcount" monitora o número de linhas impactadas pela última operação de banco de dados executada no cursor específico.

## SQLite

**aula_01**
- __CREATE__ (Criar):
- Esta operação permite __inserir__ novos registros em uma tabela (colunas).
---
    CREATE TABLE [table_name] (
    [column1] [type_dado] [regras],
    [column2] [type_dado] [regras],
    ...
    );
---

**aula_02**
- __INSERT INTO__ (Inserir):
- É uma instrução usada no contexto de bancos de dados relacionais para __inserir__ novas linhas em uma tabela (valores).
---
    INSERT INTO table_name (column1, column2, ...)
    VALUES (value1, value2, ...)
---

**aula_03 e aula_06**
- __DELETE__ (Excluir):
- É uma instrução usada em SQL para remover registros específicos de uma tabela. É crucial para a manipulação de dados, pois permite a exclusão de linhas que não são mais necessárias ou que estejam incorretas.
---
    DELETE FROM [table_name]
    WHERE [condition];
---
    - Reiniciar "id" da tabela SQLite:
---
    DELETE FROM sqlite_sequence 
    WHERE name="{TABLE_NAME}
---

**aula_04**
- __INSERT INTO__ (Inserir):
- Inserir um ou mais valores no banco de dados de forma __SEGURA__.
---
    INSERT INTO table_name (column1, column2, ...)
    VALUES (?, ?, ...)
---

**aula_05**
- __SELECT__ (Selecionar):
- É a instrução fundamental em SQL para __exibir__ dados de tabelas em um banco de dados relacional.
    -   .fetchone(): Recupera apenas uma linha do conjunto de resultados.
    -   .fetchmany(n): Recupera linhas do conjunto de resultados "n"
    -   .fetchall(): Recuperar todas as linhas de banco de dados em uma lista de tuplas.
    -   iter(cursor): Permite iterar sobre o conjunto de resultados linha por linha.
---
    SELECT [column1], [column2], ...
    FROM [table_name]
    [WHERE condition]
    [ORDER BY column_name [ASC | DESC]]
    [LIMIT offset, rows];
---

**aula_07**
- __UPDATE__ (Atualizar):
- Serve para alterar informações armazenadas em tabelas.
---
    UPDATE [tabela_nome]
    SET [coluna1] = [novo_valor1], [coluna2] = [novo_valor2], ...
    WHERE [condição];
---

**BD**
- Arquivo banco de dados local de SQLite.
---

## MongoDB

- O __MongoDB__ é um sistema de gerenciamento de banco de dados (SGBD) __NoSQL__ de código aberto e multiplataforma, conhecido por sua flexibilidade e escalabilidade. Ele se diferencia dos bancos de dados relacionais tradicionais por utilizar um modelo de dados orientado a documentos, em vez de tabelas estruturadas.

**aula_01**
- __.create_collection()__ (Create):
- O método é usado para criar uma nova coleção dentro de um banco de dados específico no MongoDB.

- __.list_database_names()__:
- Esse método é utilizado para listar os nomes de todos os banco de dados existente ativos.
---

**aula_02**
- __CRUD__ : __Criar, Rear, Atualizar e Deletar__

- __.collection.insert_one()__ (Create):
- O método é usado para insere apenas um documento por chamada.

- __.collection.find()__ (Read):
- O método é usado para retornará todos os documentos presentes na coleção.

- __.collection.find_one()__ (Read):
- O método é usado para retornar apenas um documento presentes na coleção.

- __.collection.update_one()__ (Update):
- O método é usado para atualizar dados específicos em um documento com base em um critério de pesquisa

- __.collection.update_many()__ (Update):
- O método é usado para atualizar vários documentos em uma coleção ao mesmo tempo.

- __.collection.delete_one()__ (Delete):
- O método é usado para excluir um único documento de uma coleção.

- Um __índice TTL__ (Time-to-Live) é um tipo especial de índice de campo único que o MongoDB usa para remover automaticamente documentos de uma coleção após um período de tempo especificado.
---

**aula_03**
- Na __aula_03__ esta sendo empregado o uso de __armazenamento de senhas no arquivo .env__ e uso de __método de classe__ para gerir operações de __CRUD__. 