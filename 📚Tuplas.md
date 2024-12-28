# O que sao Tuplas e como a usar 📚

Material de estudo com base em [Curso em video](https://www.youtube.com/watch?v=0LB3FSfjvao&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=90),e [Alura](https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python?srsltid=AfmBOoqZi6AOht-Cz98SGvyZtiN5iJsXcQKbfv2MH3ike49hwdt9F6Ta).

## O que sao Tuplas ?

As tuplas sao formas de torna uma variavel primeira e simples, em uma **variavel complexa e que aceite mais elementos e um so campo**.
O que e uma variavel simples voce me pregunta. Aqui esta a sua resposta. Uma vrariavel simples e uma variavel que **aceita apenas um elemento**.
Veja um Exemplo abaixo 🔽
```
nome = 'Adryan'
```
### Como criar uma Tupla

Uma tupla e criada como se vosse uma varaivel como as mesmas regras. Veja Abaixo 🔽
```
lanche = 'Cozinha','Pastel','Empada'
Ou
lanche = ('Cozinha','Pastel','Empada')
```
As duas formas acima daram certo do mesmo jeito.

Tuplas sao como uma lista de supermercado (Nao se apegue neste exemplo, a uma forma de fazer Listas no python sem ser tuplas).
A tupla é **Imutavel**. O termo imutavel quer dizer que ela nao pode ser mudada durante a execucao do codigo. 
Veja um exemplo 🔽
```
lanche = 'Cozinha','Pastel','Empada'

lanche[1] = Amora

print(lanche)

**O codico dara erro. Dira que a tupla nao pode mudar**
```

### Como usar as Tuplas

Voce pode usar as tuplas como bem entender tanto para ajudar em agrupar certos elementos, voce pode usar em Loops ou ate mesmo as fataindo 

Para fatiar uma tupla é o mesmo conseito das varaiaveis, so lembre que voce esta fatiando elementos 
```
lanche = 'Cozinha','Pastel','Empada'

print(lanche[1])

'Pastel'
-------------------------------------------------
lanche = 'Cozinha','Pastel','Empada'

print(lanche[2:])

'Pastel', 'Empada'
```

Se for usar ela em loops, na meioria das vezes e usado no For;

```
lanche = 'Cozinha','Pastel','Empada'

for c in lanche:
    print(c)

Cozinha
Pastel
Empada
-------------------------------------------------------
lanche = 'Cozinha','Pastel','Empada'

for comida in range(0, len(lanche)):
    print(lanche[comida])

Cozinha
Pastel
Empada
---------------------------------------------------------
lanche = 'Cozinha','Pastel','Empada'

for comida in range(0, len(lanche)):
    print(lanche[comida], + comida)

Cozinha 0
Pastel 1
Empada 2
----------------------------------------------------------
lanche = 'Cozinha','Pastel','Empada'

for pos, comida in enumerate(lanche):
    print(comida, pos)

Cozinha 0
Pastel 1
Empada 2

```
Esses foram algumas exemplos que podem ser usados com o For, a muitas coisas que podem ser usados com isso.

### Metados em Tuplas

- Sorted() - Este metado e usado para organizar as tuplas, tonto em ordem alfabetica ou em numeral.

- Count(numero) - Serve para voce achar quantas vezes um numero se repete na tupla, basta colocar o numero e vai mostrar para voce.

- Index(numero) - Vai achar a posicao que esta o numero que voce desejou, caso tenha se reedido o numero voce precisa saber de onde comecar e meio que fatorar 

- Del() - Voce apaga da memoria, isso serve para qualque coisa no python. Nao serve para voce Deletar um elemento da tupla 