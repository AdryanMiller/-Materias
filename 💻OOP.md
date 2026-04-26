# Programacao Orienta a Objeto

Para que possamos enteder o que se trata esse avanço da tecnologia e necessario que entendermos alguns pontos da evolucao das liguagens de programcao ate que chegamos no nivel que estamos hoje.

## Crise de software de 1960

Para um breve contextualizacao, muito antigamente quando os computadores foram criados era necessario uma programcao por cartuchos perfurados, este metado deixava muito limitado o nivel do que poderiamos fazzer um um computador, com o tempo se passando foi necessario se criar uma linguagem para que os seres humanos conseguisem se comunicar com os computadores com isso surgiu a primeira linguagem comoputacional.

A linguagem chamada Assembly, esta linguagem por muitas das vezes nao era estruturada entao nao tinha formas basicas como loops ou condicionais. Pare resolver este problema que se foi criado a primeira liguagem estruturada Algol 60, criada em 1960, para resolver o problema do Assembly nela ja era estruturada entao ja tinhamos blocos de codigos de inicio e fim, loosp e if/else.

Com tudo ainda tinhamos um grande problema, com tudo os codigos ainda nao eram Modularizados, entao todo o codigo ficava em um so arquivo gigante, com o tempo foram evoluindo e conseguiram se fazer com que os codigos fosse modularizados e bem separados.

## A onde entra a Programação Orientada a Objetos ?

Na prgramacao ainda havia muitos problemas, os codigos eram ainda uma estrutura muito complexa de se manusiar e realizar algumas funcoes, muito espalhados com funcoes modulares ainda para cada coisa, com a ideia da orientacao a objetos era de se juntar tudo de uma determinada coisa em um so. Mas isso iremos entender melhor quando chegarmos na explicacao.

## Nomeclaturas e vantagens

A nomeclatura em portugues Brasil e como esta escrito Anteriormente, **Programacao Orientada a Objetos com a sigla POO,** ja em muitos casos que iram esta em ingles a sigla e o nome ficariam **Object Oriented  Programming sendo a sigla OOP**.

Certo agora que sabemos o contexto, os nomes precisamos entender as vantagens e  porque de usar isso nos dias atuais. Nenhum codigo hoje em dia tem a utilizacao de OOP. Antes de tudo  vamos enteder como funciona um Objeto com a utilizacao do exemplo mais comum de uma carro e como funciona.

Um Objeto pode ser explicavel como tudo que e palpavel normalmente, pois ele seria um grupo que tem algumas funcoes especificas, imagine em uma montadora de carro, o carro em si seria o objeto por completo, entretanto quando iremos montar um carro cada parte e imdependete e se comunica com a outra, por exemplo, quando a pessoa que esta fazendo os bancos esta colocando eles, nao necessariamente a pessoa que esta fazendo o motor precisa esperar ou enteder de como funciona a colocaçao dos bancos e versi versa.
**Ta podemos entender melhor como funciona mas vou melhor isso com o tempo.**

OOP tem suas vantagens e para que voce possa entender uma paavras como **COMER NADA** pode ajudar muito a entender os paramentros.

* **Cofiavel** - Uma das partes tem que serem tratadas individuais, nao afetando as outras partes
* **Oportuno** - Quando separadas em partes cada parte deve ser capaz de ser desenvolvida em paralelo com as outras sem impecilhos
* **Manutenivel** - As partes tem que ser de facil manutensao, se uma forma que nao afete todo o progama.
* **Extensivel** - De ver capaz de acrecentar coisas em alguma parte sem afetar todas, apenas fazendo algumas alteracoes na parte especifica
* **Reutilizavel** - Deve ser capaz de ser reutilizael em diversos casos
* **Natural** - Tudo deve ser de forma natural sem parecer esta forcando o programa a realizar

## O que sao Classes, Atibutos e Metados

Antes de criamos um Objeto e necessario criar o que dara foma aos objetos, esta estrutura nos chamamos de **Classe** esta forma de estrutura e onde iremos passar as regras para criamos um objeto.

Para um melhor intendimento vamos entrar em um raciocinio mais simples, antes de darmos nomes tecnicos.
Imagine que voce esta fazendo um bolo, este bolo deve ter o formato de estrela, para que o mesmo tenha este formato é necessario que possua uma forma em formato de estrela assim todos os bolos que voce fazer iram ter o mesmo formato.
E**m base isto seria o chamamos de classe.** Uma classe e o **conjunto de caracteristicas e acoes que iram ter o seu objeto**
Na classe tambem temos as caracteristicas que em outras palavras chamamos de **Atibutos**, so eles que daram aspctos a classe. Tambem temos aquilo que chamamos de ações que sao os **Metados**, aqui ira ocorrer as acoes que a classe sofrerar.

Vamos agorar usar um exemplo de uma construcao de uma casa;
O engenheiro vem para realizar um planta de uma casa, ele começa a desenhar uma planta simples **(planta olhada de cima), esta planta seria nossa Classe**, nosso atributo seria o **tamanho da casa, a cor, andares,** ja os nossos metados seriam algo como, **se a casa e movel, derrubar a casa, pintar a casa, mobilhar.**

Isso tambem poderia ser para o bolo sendo a forma a classe tendo o **tamnho, temperatura, sabor, cozido sendo os Atributos**
Ja os **Metados sendo, comer, partir, cozinhar, guardar.**

Show, agora que entendemos esta parte e necessio que sabemos montar uma classe, para isso e necessario sabermos o diagrama de classe da UML.
Veja o Exemplo do bolo abaixo;
![alt text](ImagemUMLOPP.png)

Temos 2 conceitos importantes que devemos saber deles.
 1- **Instancias** - E o ato de fazer com que a classe se torne um objeto, e o momento que passamos a planta da casa para os pedreiros e eles estao contruindo, ali acontece a instancia, fazendo assim uma classe se tornar um objeto expecifico

 2-**Estado** - O estado e tudo que um objeto esta no momento, como o bolo a temperatura, tamanho, sabor tudo junto e um estado, este estado muda com o passar do tempo, ja que um objeto na maioria das vezes nao e fixo 

==========================================================================================

## Como criar uma Classe e um Objeto

Para a criacao de um classe e um objeto temos varios fatores importantes de se endender, vamos para a pratica e destrinchamos cada parte

### Como criar uma Classe

```
#DECLARACAO DE CLASSE
class Gafanhoto:
    def __init__(self): #Metador construtor
        # Atributos
        self.nome = 'desconhecido'
        self.idade = 0

    #Metados 

    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos'

g1 = Gafanhoto()
g1.nome = 'Ana'
g1.idade = 15
g1.aniversario()
g1.aniversario()
print(g1.mensagem())

```

Vamos descrinchar cada parte 

  1 - **Nomeclatura da class;** Nesta parte todo nome de uma classe deve ser com **Letra Maiuscula** 
  2 - Definicao do metato contrutor;** __int__** e para criar a funcao que irar **receber os atributos do objto quando instaciado**. Ja o** self**, ele e o metado construtor ele sera a variavel generica que irar ser como um atributo e **identificar de qual objeto estamos modificando**.
  3 - **Adicao de atributos;** Dentro da funcao __int__, iremos colocar os atributos sendo **self.nomeAtributo = seu_valor**.
  4 - **Criacao de metados;** Fora desta funcao iremos criar nossa funcao de metados, para isso voce irar criar a funcao e passar o atributo de **self**.
  5 - Fora e onde iremos estaciar nosso Objeto, e onde criaresmo com g1 nome do objeto e chamar a classe Gafanhoto()
  6 - Passaremos os atibutos (Esta nao e a forma mais ideal para que possamos passar)
  7 - Logo chamaremos nossos metados.

Aqui vimos uma forma simplificada e com um exemplo simples so para que possamos entender como criar uma classe e instaciar um objetos. A varias formas e regras para que possamos otimizar nosso classe.

### Nomeclatura de atributos 

Diferenca de **__** e de **_** para os atributos no __init__

Quando se coloca **__** no seu atributo voce esta indicando para o usuario que nao e para mexer no mesmo e nao ha metados para modificar

Ja quando e **_** voce esta indicando para o usuario que ele pode consultar o atributo e tem um metado para modificar, mas nao e para mexer em seu estado diretamente e para usar o metado criado

Exemplo
```
self.__cpf = cpf
self._nome = nome
```
Colocar um **_** para o python em si e so necessario se o usuario nao tiver que mexer com o atributo, mas caso o atributo ele deve ter um verificacao e for mais sencivel usamos o conceito de Get e Set isso faz com que o atributo tenha veficacoes 

Imagine que voce tenha um atributo de senha, mas o mesmo tem que ser de 4 digitos e o usuario pode mexer nele mas seguindo as verificacoes e ai que voce usa os metados

```
self._senha = '1234'

    @property (Get)
    def senha(self):
        return self._senha
    
    @senha.setter (set)
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova senha invalidade')


cartao_Adran.senha = '1235'

print(cartao_Adran.senha)
```

No get e o que voce quer que acontece quando o usuario quer visualizar o atributo
Ja no set e para fazer a verificacao caso o usuario queira mexer no atributo

Voce deve esta se perguntando quando que usamos _nomevaraivel para um metado auxilizar e quando usamos para get ou set. No Python por se so voce ira usar o get e set so se voce quiser que o usuario possa mexer no atributo com algum tipo de verificacao caso ao contrario, voce so ira usar self.nomevariavel.

### Metado Estatico

Um metado estatico e um metado que iria ficar na classe por se so e nao nas instancias ele serve muito para auxiliar os metados dos objetos.
Para voce dizer que um metado e estatico voce deve escrever **@staticmethod**, isso irar informar que a metado e um metado estatico

```
class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y as %H:%M:%S')

    def __init__(self, nome:str, cpf:int, agencia:int, num_conta:int):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        return 'Seu saldo atual e de R${:,.2f}'.format(self.saldo)
    
```

## Abstracao

### O que e ?

A arte de ignorar o irrelevante e se focar no estremamante essencial

Imagine o exemplo da classe de pessoas, quando voce começa a criar voce começa a pensar em muitas coisas e começa a ficar perdido, sendo assim o exercício e voce focar no relevante, no essencial.

Para melhorar mais ainda a explicacao iremos usar um exemplo de um controle remoto

Quando voce ver um controle remoto se bem construido, voce por se so sabe o que a mariora do botoes fazem. Entretanto voce nao precisa saber como estes botes funcionam so as suas funcionalidades. 

‘’A pessoa deve se **fornar somente na interface publica que esta disponivel e nao no funcionamento.’’**

### Vantagens

- Melhor legibilidade
- Padronizacao
- Simplificação dos problemas
- Seguranca - Nao expoem com funciona por dentro

### Frases teoria

‘’Existem abstracao de dados que acontece quando ignoramos informaçoes desnecessárias para o escopo do projeto ’’ - Quando vai cadastrar alunos voce pode ter nome cpf altura peso, mas faria sentido voce ter o peso e a altura ?

“Existe abstracao de processos, quando nao precisamos saber como um metado faz seu trabalho, apenas sabe que ele existe pela sua interface” - Quando voce sabe que o metado esta la mas voce nao precisa saber como ele funciona so usa somente ele

### Padronizacao

Vem muito da sua classe abstrata, seria uma classe que nao e usada para virar objetos mas sim para servir como base para evitar repeticoes.

Lembra do nosso exemplo pessoas. A classe pessoas seria nossa classe abstrata, ja que a gente nao vai criar uma pessoa generica a gente vai criar um Aluno, Professor, Funcionario.

A classe pessoas serve somente para que as seguintes classes especializadas tenham um padrao.

Agora vem comigo, imagina que na classe Pessoas, nos temos o metado aniversario, todas as classes filhas recebem este metado ja que todo mundo faz aniversario da mesma formar. Mas a classe pessoas tambem tem um metado estudar, entretanto cada classe Aluno, Professor e Funcionario estudam de uma forma diferente.

O que quer dizer, a classe mae fala que todas as filhas devem estudar, mas do seu jeito. Para isso criamos um **metado Abstrato {Abstrato},** um metado que obriga as sub classes a receber da classe mae.

Este metado nao pode ter linhas de codigo, porque se ele tiver voce esta informando que todos devem estudar daquela forma.

“Uma classe Abstrata nunca sera instanciada, ja que ela sera usada como base para as subclasses”

“Ao definir um conjunto de metados abstratos, estamos dizendo que estamos criando uma intrface publica da classe”

“Uma classe abstrata pode ter metados abstratos que deverao ser implementados nas subclasses”

“Mas uma classe abstrata pode ter metados contratos se eles funcioarem da mesma maneira para todas as subclasses **(DRY)”**

### Pratica

Antes a gente tem que importar o modulo **ABC(Abstract Base Class),** o python por natividade nao tem abstracao entao tem que importar

```
from rich import print, inspect
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = '', idade = 0):
        self.name = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self. curso = curso
        self.turma = turma

    
    def fazer_matricula(self):
        print('[green]Aluno fez matricula[/]')

    def estudar(self):
        print(f'Aluno {self.name} o curso de {self.curso}')

class Professor(Pessoa):    
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Professor começo a dar aula')

    def estudar(self):
        print(f'{self.name} e especialista {self.especialidade} do nivel {self.nivel}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    
    def bater_ponto(self):
        print(f'Funcionario bateu ponto')

    def estudar(self):
        print(f'{self.name} se especializa na area de {self.setor}')
```

- Analisa que todos **metado de estudar ele tem suas proprias linhas de codigo.**
- Observe que voce tem que colocar o **ABC na sua classa Mae**
- Observa tembem que la em cima no metado que sera abstrato ele tem um `@abstractmethod`

## Encapsulmento

falar sobre en

## Herança

### O que e Heranca

Em uma forma tecnica de se explicar herança seria assim
" É um relacionamento entre itens **gerais(acestrais)** e **tipos mais especificos(decendentes)** desses itens, que **herdam atributos e metados** dos niveis superiores

Em uma explicacao mais simples
Imagine um casal de passarinhos, cada passarinho tem seus caracteristicas, a um tem as penas azuis com olhos amarelos, o outro e vermelho com olhos verdes.
Os mesmos tiverem um filhote, este mini passarinho herda dos seus pais suas caracteristicas o corpo e azul, o olho e verde dizemos que ele herdeou suas caracteristicas. Entretando nao se herda so caracteistica se herda tambem jeitos, o jeito de siscar, bater assas. Logico como o passarinho filhote e unico ele tambem tem suas proprias caracteristicas e jeitos.

### Nomeclaturas
- Heranca- A heranca de uma classe para outra se dar por meio de uma seca aberta, chama de **Generalizacao** e e um relacionamento de **'E um'**
- SuperClasse - A classe de cima tem varios outros nomes **(Classe Base, Ancestral, Classe mae)**
- SubClasse - Classe abaixo **(Classe Derivada, Desendente, Classe Filha)**

### Vantagens 

- Reutilizacao de codigo
- Organizacao hierarquica
- Facilidade de manutencao
- Extensibilidade 
- Suporte a Polimofismo

### Utilizacao de Herança
Vamos pensar em um sistema que cadastras pessoas de uma escola, professores, alunos e funcionarios, a gente poderia criar uma classe para todos mundo e cadastrar cada um isolademente, mas percepe uma coisa cada classe tem coisas idendicas com a outras (imagine que todos fazer aniversario como metado)

- nome
- idade
- fazer aniversario

Voce pode usar isso como base e criar uma classe generica que irar ter esses mesmo atributos e pode ter uma classe especialidades que teram seus proprios metados e atributos 

Exemplo Pratico

```
class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.name = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self. curso = curso
        self.turma = turma

    
    def fazer_matricula(self):
        print('[green]Aluno fez matricula[/]')


class Professor(Pessoa):    
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f'Professor começo a dar aula')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    
    def bater_ponto(self):
        print(f'Funcionario bateu ponto')

a1 = Aluno('Lorran',20,'Informatica','T01')
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor('Bira',45,'Portugues','Mestre')
p1.dar_aula()

f1 = Funcionario('Ana', 18, 'TI', 'Informatica')
f1.bater_ponto()
```

- Observe que para herdar os atributos e os metados de uma classe mae **usamos seu nome nas classes filhas**
- Observe: Dentro da funcao que inicia uma classe tem um **super().__(nome, idade)**, voce ira colocar os **atributos da classe mae.**

## Polimofismo

falar de poli

 e Criacao de Documentacao

Vamos usar o exemplo anterior mas colocando algumas modificacoes para que seguicemos o pradrao geral

```
class Gafanhoto:
    '''
        Esta classe cria um Gafanhoto
        Variavel = Gafanhoto(nome, idade)
        return nome e idade
        return aniversario (idade + 1)
    '''
    def __init__(self, nomeUsuario='desconhecido', idadeUsurario=0): #Metador construtor
        # Atributos
        self.nome = nomeUsuario
        self.idade = idadeUsurario

    #Metados 

    def aniversario(self):
        self.idade += 1


    def __str__(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos'
    

    def __getstate__(self):
        return f'Nome: {self.nome}, Idade {self.idade}'



#dECLARACAO DE OBJETOS

g1 = Gafanhoto('Adryan', 20)

g1.aniversario()
print(g1)
print(g1.__getstate__())
print(g1.__doc__)
print(g1.__dict__)
print(g1.__class__)
```

1 - **Atributos;** Mudanca na onde se coloca um atributo assim como nas funcoes normais colocamos **variaveis para receber e depois passamos para o self**
2 - **__srt__ ;** Isso e uma mensagem padrao que irar aparecer sempre que **chamarmos nosso objeto.**
3 - **__getstate__ ;** Aqui irar mostrar o **estado que se encontra o objeto,** pode pegar so os atributos mas tambem pode pesonalizar por padrao ele mostra em forma de dicionario
4 - **__doc__ ;** Tudo no Python e um objeto aqui voce vai chamar a documentacao deste objeto, que voce pode ver que foi criada no inicio do codico com **"""conteudo"""**
5 - **__dict ; ** Ele irar mostrar o objeto em **forma de dicionario**, que se pode trabalhar no mesmo
6 - **__class ; ** Mostra de qual **classe e o objeto**

