# Laços➰



## O que é o For ❓

Material de estudo com base em [Curso em Video](https://www.youtube.com/watch?v=cL4YDtFnCt4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=60) e [W3school](https://www.w3schools.com/python/python_for_loops.asp).

Em linguagens de programação nem sempre queremos que nosso codigo rode apenas uma vez e pare, fique em so condições. As vezes queremos que nosso codigo rode mais vezes, que possamos fazer algo rapido de uma vez só. 
Digamos que voce quer fazer uma tabuada, se fosse fazer de forma tradicional, teria que fazer numero por numero, usando um loop podemos fazer isso so com 2 ou 3 açoes.


### Como o For funciona;

O FOR e um loop e deve seguir a regra de indentacao, que no python e bem impotante para que seu codigo funciona. 
Veja um exemplo abaixo 🔽

```
for i in c:
    print(i)
```
**O codigo acima e so um exmplo de como e escrito o for nao funciona**

Aqui vai exemplos de o que o for faz 🔽

```
nome = 'Adryan'

for c in nome
    print(nome)

A
d
r
y
a
n
```

O for faz com que uma vavriavel que recebe algo quebre em pedaços e pode ser modificado por ela.
Se voce pegar o C ele ira temostrar os indeses como 0 1 2 3 4...

O for serve para listas e muito mais 🔽

```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

Podemos usar o for de outra forma, uma forma em que ele ira gerar palavras ou numeros, fatinado eles ou deixando como esta mesmo.
Aqui vai alguns exemplos 🔽

```
for x in range(6):
  print(x)
```

**Neste codigo sera gerado 5 numeros pois o ultimo nao aparece.**

```
for x in range(2, 6):
  print(x) 
```
**Ja neste vai comecar do 2 e terminar no 6. Lembrese que o ultimo numero nao aparece**

```
for x in range(2, 30, 3):
  print(x)
```
**Este comeca no 2 vai ate o 29 e pula de 3 em 3**

Voce pode colocar variavies no for para ela servirem de parametros de como voce vai querer fazer algo ou alguma coisa.

Em palavras resumidas este e o for, um loop que nao e infinito, precisa de parametros de inicio e de fim para determinada funcao, agora se queremos algo infinito devemos usar outro.
 

## Whilhe 
E um Loop que pode ser infinito, sua funcao e parecida com a do For, mudando so a forma que e escrita e o seu sentido.
Veja aqui um exmplo. 🔽

```
i = 1

while i < 6:

    print(i)
    i += 1
```

Para este tipo de While e necessario um parametro de inicio e em sim um parametro de termino. O numero 6 e o termino e 1 e o de inicio 
O acressimo de 1 é para fazer a conta para chegar no final, e como se fosse um contador.

Podemos ter um **While Infito** para isso e necessario colocar um true na frente e dentro dele fazer sua condicao de parada.
Olha abaixo um exemplo 🔽

```
While True:
    codigo
```

O que acaontece no While e que ele se treduz como Enquanto algo, entao para voce entender melhor tente lembrar sempre desta parte.
Logico a mais coisas do While, mas e algo mais aprofundado e eu ainda nao sei explicar tao bem, pois nao entendi tao perfeitamente.