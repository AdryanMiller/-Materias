# Integracao Python com SQL
Para comecar a dizer sobre como vamos integrar o Pyhon e necessario saber o que se trata o **SQL**. Para comecar o **SQL e uma linguam de banco de dados** onde voce executa comando que iram controlar
o que um banco de dados irar realizar como iram se relacionar.
Normalmente usamos uma interface que chamamos de **SGBD**, que so onde realizamos os comandos SQL e criamos os bancos. Entretanto, no dia a dia e raro termos que criar um banco de dados normalmente o mesmo
ja estara pronto para realizar as consultas.

## Biblioteca para a integracao
Normalmente a varias bibliotecas e ate mesmo especificas para cada banco de dado, aqui vamos falar de duas, do **MySQL** e o **Pyodbc**, primeiro iremos como instalamos a mesma e a utilizamos elas.
- Instalacao Pyodbc;

```
  pip install -m pip install pyodbc
```

- Instalcao MySQL 

```
   pip install mysqlx-connector-python
```

## Como funciona
Agora que temos as bibliotecas instaldas e prontas para uso vamos explicar como funciona a integracao e os pontos principais que ela permite.
Para realizarmos uma integracao no iremos criar um BD do zero iremos apenas realizar os comando que sao necessario para isso. Antes iremos explicar como iremos conectar o Python com o SQL e o banco.
No inicio voce deve pegar os dados do banco de dados, normalmente devemos pegar os seguintes dados.
- Driver: O que fazer o banco de dados se comunicar com um determinado banco como SQLlite, MySQL ou Postreegs. Cada SGBD tem o seu driver expecifico
- Server: Local que o servidor do banco de dados esta localizado se e local ou externo
- Database: Nome do banco que iremos pegar 
- Outros: Tambem pode se pegar o nome de **usuario(username/UID**) ou **senha(password/PWD)**

Todos essas dados colocaremos em uma variavel e montaremos o que chamamos de **dados de conexao**
```
   dados_conexao =('Driver=SQLite3 ODBC Driver;'
           'Server=localhost;'
           'Database=salarios.sqlite')
```

Temos os dados do banco de dados que iremos usar e suas informacoes, agora temos que fazer sua conxecao com o python aqui estamos usando **Pyodbc**, mas logo em baixo irei colocar com o MySQL.
```
   conexao = pyodbc.connect(dados_conexao) 
```

- Conexao com MySQL
```
   dados_conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password = '123456',
    database = 'bdyoutube'
)
```

A conexao com MySQL e mais simplificada sem necessariamente fazer um conexao.connect pois isso ja e feito nos dados_conexao.

Para que possamos realizar um tarefa mexer em um banco e necessario criar o que chamamos de **cursor** para isso funciona na mesma forma para o **Pyodbc e para o MySQL**
```
   curso = conexao.cursor()
```

Temos tudo para comecarmos a realizar as modificacoes ou consultas no banco de dados, para isso vamos usar um caoando que e bem simples mas a algumas regras para isso.
1. Nao devemos criar o comando dentro diretamente, precisamos de uma variavel para isso. Sim e possivel criar diretamente e ate mais facil no entanto nao e recomendado.
2. Quando formoas usar uma variavel vamos lembrar do ```f``` e do ```{}``` para colocar a variavel que queremos usar
3. Se variavel for um string nao esquecer de colocar as ```"{nomeVariavel}"```

Veja o comando:
```
nome_produto = 'Nestle'
valor = 45
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}",{valor}) '

cursor.execute(comando)
```
Voce passa o comando SQL dentro da varaivel **comando** e logo em seguida voce ira executar a ```cursor.execute(comando)``` chamando a variavel comando
Sim voce pode passar o comando diretamente e iria ficar assim
```
cursor.execute("""SELECT * FROM customers""")
```

Neste momento nos temos dois comando SQL o primeiro e um comando que modifica os dados da tabela o que faz com que voce tenha que dar o comando ```cursor.commit()```, que faz com que a alteracao
salve dentro do Banco
No outro caso voce tem um comando de leitura que nao modifica nada no banco apenas faz uma leitura e para isso voce tem que pegar os dados usando alguns comando
```
valores = cursor.fetchall()
```
Que pega os valores da leitura e guarda dentro da variavel que esta escrito **valores**, lembrando se a leitura mostrar muitos dados tome cuidados pois pode travar o sistema para isso voce pode fazer
um filtro ja que os valores e uma **Lista de tuplas.**

## Encerrando
Agora sempre que voce fazer uma modificacao em um banco e necessario voce encerrar tanto o cursor e a conexao para que voce nao faca um travamento do banco de dados.
```
cursor.close()
conexao.close()
```
