# O que sao Listas ?

Material de estudo [Curso em Video](https://www.youtube.com/watch?v=N1hTsbW50eM&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=96)

Para com vamos apresentar o que e uma Lista em python. Uma lista vem como um conseito de agrupar varios elementos dentro de um so, igual uma lista na vida real. 
Uma lista e representada assim; Veja Abaixo 🔽

```
Lista = []
Comida = ['Manteiga','Carne','Feijao','Arroz']
valores = list[....]
```

Acima voce pode ter percebifo que a 3 formas de representar uma lista. Na **primeira** é a forma de represntar uma lista vazia sem nada, a **sengunda** é uma forma de como e uma lista normalmente representada e a **terceira** é usando uma funca que transforma as em lista o list.

Uma lista e de facil manipulacao e muitas das vezes e feita por fatiamento, isso faz uma lista ser mutavel, onde voce pode mudar os intens, excluir, adicionar e tudo mais.

### Metados das Listas

Para comecar vamos mostrar para voce um fatiamento, nao e um metado em si, e importante aprender pois as listas se usa muito disso.

```
Valores = [1,22,34,4]

print(Valores[3])

```
Voce ira pegar o elemnto de indise 3 o que seria o **4**. Podemos fatiar as listas de varias formas.

Voce pode trocar um elemento por outro usando o fatiamento.

```
Valores = [1,22,34,4]

Valores[1] = 3

```

A resposta que sera obitida e esta **[1,3,34,4]**. Ele consegue trocar um elemento por outro.
**Obs: Nao tem como adicionar um elemento exatamente com esse metado, deve-se usar outro;**

Agora vamos adicionar elemento a uma lista 🔽🔽

```
valores = [1,22,34,4]

valores.append(55)

[1,22,34,4,55]
-------------------------------------------------------------------------
valores.insert(0,5)

[5,22,34,4,55]

```

O metado **append()** coloca o elemento no final da lista sempre, ele colocarar sempre um elemento no final de sua lista.

Ja o metado **insert()** ele coloca um elemento em uma regiao especifica, o **primeiro paramento e o local o segundo e o elemento a ser adicionado**.

Como tudo se formos adcionar devemos tambem excluir 🔽

```
valores = [1,22,34,4]

valores.remove(22)

[1,34,4,55]
-------------------------------------------------------------------------
valores.pop()

[1,34,4]
-------------------------------------------------------------------------
del.valores(1)
[1,4]
```

Vamos falar de cada uma de uma forma rapida os metados **del()** remove por indese, ja o medado **pop()** por padrao ele remove o ultimo elemento mas pode se passar o indese, e o metado **remove()** deleta o elemento expecifico.

Agora vamos falar sobre lista com For e Range 🔽

Paraa comecar e possivel fazer uma lista ja rapida usando o range
Veja abaixo

```
Valores = list(range(0,11))

[0,1,2,3,4,5,6,7,8,9,10]

```

Voce pode usar os paremetros normais que sao os 3 inicio, fim e separacao. Voce pode usar isso para criar listar rapidas.

Pode se usar lista em for, onde ele vai pegar elemento por elemento. 🔽

```
Valores = [1,22,34,4]

for v im Valores:
    print(v, end=')

[1,22,34,4]
```

Temos tambem como organizar uma lista usando o metado sort() ou sort(reverse=True)

```
Valores = [1,22,34,4]

valores.sort()

[1,4,22,34]

valores.sort(reverse=True)

[34,22,4,1]
```

Um  coloca em ordem crescente e o outro em decrecente.


## List Comprehension
Nada mais é do que uma maneira de construir listas no Python de forma mais rápida, em uma linha de código!

OBS: Lembrando que essa lista vai ser construída pelo seu código e não você escrevendo ou puxando de uma base de dados!

Para que serve o list comprehension? Na verdade, ele vai te ajudar em 2 situações.

A primeira é para que você saiba como fazer para criar uma lista de forma mais rápida e eficiente no seu código quando for gerar uma lista dentro dele.

E a segunda é para que você tenha conhecimento de como isso funciona, pois muita das vezes quando for fazer alguma busca na internet é possível que você se depare com essa maneira de construir uma lista.

Então se você souber como o list comprehension funciona você vai de cara entender o que aquele código está fazendo.

Isso é fundamental quando estamos buscando informações na internet, entender os códigos para que possamos replicar ou pegar parte desse código para a nossa aplicação.

Vamos ao exemplo prático para te mostrar a diferença entre a utilização de uma estrutura de repetição para a criação de uma lista para a utilização do list comprehension.

- Primeiro Caso

```
#Sem list 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#----------------------------
#Com List

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

Aqui voce irar pegar a expressao x que voce irar usar como base e irar escrever o for pos a sua condicao

- Caso 2
  
```
#Sem list 

preco = [100,200,300]
precoNovo = []

for item in preco:
  precoNovo.append(item*2)

print(precoNovo)

#------------------------
#Com list

preco_Novo = [i * 2 for i in preco]

print(preco_Novo)
```

Aqui dobrar o preco de um item na lista a primeira parte **i * 2** e o que irar ser adicionado na lista depois realizar o for.


A varios outros metados mas ate o momento isso e tuo 🧐
