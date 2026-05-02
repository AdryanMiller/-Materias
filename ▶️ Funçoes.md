# Introducao a Funçoes

### O que sao funcoes ❓
Em Python funcoes sao blocos de codigos separados que geram metados para serem reutilizados no codigo. Para se definir uma funcao usamos a palavra ```def```, e logo em seguida do
nome da funcao e de parênteses.

```
def ola_Mundo():
  print('Ola Mundo')

```

###  Importancia das Funcoes
A utilizacao de funcao em um condigo, vem para facilidade.Isso não apenas facilita a compreensão do código, mas também torna a manutenção e a resolução de problemas mais eficientes.

## Sintaxe de Funcao

## Como se declara uma Funcao
Para declarar uma funao e simples. Para se definir uma funcao usamos a palavra ```def```, e logo em seguida do nome da funcao e de parênteses. Veja exemplo abaixo:

```
def ola_Mundo():
  print('Ola Mundo')

```

### Paramentos e Argumentos 
Uma funcao pode receber parametros que sao dados que ela espera a receber. Para passar um parametro se coloca dentro dos Parenteses. Veja o exemplo abaixo:

```
def aluno(nome):
  print('O aluno se chama' + nome)

```

### Retorno de um Função 
A funcoes que apenas retornam valores de um determinada tarefa. Para isso usamos a Palavra-chave ```return```. Veja abaixo:

```
def soma(a,b):
  return a + b

```

## Variaveis em Funcoes

### Variaveis locais e Variaveis Globais
Em fucoes podemos usar dois tipos de variaveis as que estao dentro do bloco de codigo que sao chamadas de varaiveis locais, e as que estao fora do codigo que podem ser usadas em 
varias ocacioes que sao as globais.

Veja o exmplo de uma Variavel Global:

```
variavel_global = 10

def soma_varaivel(a):
  print(variavel_global + a)

```

Veja um exemplo de varaivel Local:

```
def soma_varaivel(a, b):
  soma = a + b
  print(soma)

```

### Como chamar uma funcao
Nos em Python usamos funcao ou metados muitas vezes ja que sao bem rapidos e eficases de se utilizar, para que possamos chamar uma funcao basta colocar seu nome
e colocar seus paraemtros de necessario.

```
def soma_varaivel(a, b):
  soma = a + b
  print(soma)

soma_varaivel(10, 5)

#ResultadoPrograma
15
```

## Funcoes existentes Python
No python nos ja utilizamos muito das funcoes e nem percebermos, a linguem por se so ja vem com varias funcoes ja pronta para o uso.

- ```len()```: Retorna o comprimento de um objeto.
- ```print()```: Imprime valores no console.
- ```sum()```: Retorna a soma dos elementos de uma sequência.

## Interactive Help
Muitas linguagens de programação a uma boa documentação, muito feitas pela comunidade, ja achando codigos prontos e explicações detalhadas de um daterminada função. No Python esta documentacao e muito mais ampla e amplificada pela comunidade e pela propria linguagem que ja tem uma farma de encontrar documentacao de maneira rapida que ja e integrada a linguagem.
Usamos o ```HELP()``` uma funcao que busta a documentacao tanto de outras funcoes, metados ou ate modulos
Maneira de usar o **HELP()**
- 1 MANEIRA: TERMINAL 
  - Abra o terminal e escreva help, logo em seguida digite a funcao ou o metado que voce quer descobrir sua documentacao
- 2 MANEIRA: IDE
  - Na parte de escrever codigo escreva
  ``` help(metado) ```


## Docstrings
Todas as funções ou modulos devem esta sempre catalogadas e tendo uma documentaca, e para isso voce deve fazer a documentação do seu projeto, mas nao so dele, suas funcoes tambem devem esta sempre documentadas tanto para que voce possa entender ou para que outras pessoas entendam tambem.
Entao imaginei que voce criou uma funcao de um contador e para isso voce tem que documentala veja abaixo um exemplo;

```
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passos da contagem
    :return: sem return 
    Autor Adryan Miller
    """

    c = i

    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')

contador(2,10,2)
```

## Argumentos Opcionis
Nem sempre queremos passar todos os argumentos em uma funcao, as vezes so queremos passar alguns, o problema acontece e que dara erro se nao passarmos todos para que isso nao ocorra usamos o que chamamos de **Argumentos Opcionais**, que faz os argumentos escolhidos nao serem necessaria mente preenchido pelo usuario
```
def contador(i=0,f=0,p=0):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passos da contagem
    :return: sem return 
    Autor Adryan Miller
    """

    soma = i + f + p

contador(2,10,2)
```
O que ocorre e que voce pode escolher qual argumento nao ira precisar de uma iniciativa, aquilo faz com que nao seja necessario passar o valor pois ela ja ira receber um valor caso nao passe algum.

## Map 
A funcao do metado map e para que voce possa colocar uma funcao determinada em cada item de um Iterable.
Para voce ter um exemplo mais pratico observe como isso funciona.

```
def dobro(a):
    return a*2

lista_numeros = [1,2,3,4,5,6,7,8]

lista_dobro = list(map(dobro, lista_numeros))

print(lista_dobro)
```

Se voce nao transformar ele em algum iterable, a resposta dele sera um espaco na memoria.

## Key
O parametro key em muitos dos metados normalmente esperam que voce passa uma funcao para que eles possam order o que voce quer 
- sort()
- min()
- max()

Veja um exemplo pratico

```
def segundo_item(tuplas):
    return tuplas[1]

vendas_produtos = {'venho': 100, 'cafeteira': 150, 'microondas': 300, 'iphone': 5500}

lista_vendas = list(vendas_produtos.items())

lista_vendas.sort(key=segundo_item, reverse=True)
```

## Lambda

Uma funcao Lambda e por sua vez uma funcao que nao tem nome, o que chamados de anonimas, muito usadas em codigos que o resultado irar ser unico e simples, sem a necessidade de criar uma funcao deterministica.

## Criando um Funcao Lambda

Uma função lambda é criada usando a palavra-chave ```lambda```, seguida de um ou mais argumentos, e uma expressão:

- argumentos são os dados de entrada que esta função irá receber
- expressão é o código que será executado quando a função lambda for chamada.

Basico da Sintaxe 
```
lambda {argumentos}: {expressão}
```

Veja o exemplo abaixo

```
soma = lambda x, y: x + y
print(soma(2, 3))
```

Podemos chamar uma funcao lambda em uma variavel igual fizemos a cima ou podemos tambem chamar diretamente teria o mesmo resultado
```
print((lambda x, y: x + y)(2, 3))
```

## Usando funções lambda com map e filter

A utilizacao da expressao Lambda muito e usada com metados que pedem funcoes internas para que possam modificar algo

Veja o exemplo abaixo, onde usamos a função map para aplicar uma função lambda que eleva cada elemento de uma lista ao quadrado:

```
lista = [1, 2, 3, 4]

print(list(map(lambda x: x ** 2, lista)))

#E a saída será:

[1, 4, 9, 16]
```

No exemplo abaixo,usamos a função filter para retornar apenas os números pares de uma lista:

```
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: x % 2 == 0, lista)))

#Gerando a saída:

[2, 4, 6, 8, 10]
```

### Agradecimentos
Para que possam saber mais aqui estao alguns artigos e vidoes para que entendam mais sobre o tema
- [Rocketseat](https://www.rocketseat.com.br/blog/artigos/post/como-criar-funcoes-empython#60e8db5ae9694832bf5051f217052012)
- [Curso em Video](https://www.youtube.com/watch?v=ezfr9d7wd_k)
- [DeviMedia](https://www.devmedia.com.br/funcoes-em-python/37340?gad_source=1&gad_campaignid=22326280955&gclid=Cj0KCQjwuKnGBhD5ARIsAD19RsYrZaRLAqMJu7PLslNZyo0Zo8xgo6KnOZHJmkcwWc5qnFnPsAFqwhAaAkAHEALw_wcB)
