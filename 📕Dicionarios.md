# Dicionarios 📕

Dados pegos do site [Curso em Video](https://www.youtube.com/watch?v=ZWj8o692qGY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=110) | [Python Academy](https://pythonacademy.com.br/blog/dicts-ou-dicionarios-no-python)

### Introdução

Dicionarios sao um conjunto de elementos que armazenam dados de forma nao ordenada.
Esses elementos sao separados em em duas formas, **Chaves** e **Valores**

### Como se escreve ?   

Antes de qualquer coisa, os dicionarios se parecem com listas e tuplas e quase a mesma forma de escrita sendo que Dicionarios a chaves e valores.
```
dados = {'chave': 'valor'}
```

### Criando Dicionarios 

A varias formas de crir um dicionario, vou mostrar as 2 mais usadas 

A funcao mais simples e mais comum de se fazer a dois tipos com dados ou vazio
```
dicio = {'nome': 'Adryan', 'Idade': 18}
dicio = {}
```

Agoras temos uma funcao mais simplificada. A dois jeitos com os dados ou vazio.

```
dicio = dict() 
dicio = dict{'nome': 'Adryan', 'Idade': 18}
```

##### OBS:
Para printar um dicionario e diferente das tuplas e listas para voce dar um print voce precisa pegar o indice com o nome. 
```
dados = dict()
dados = {nome:'Pedro', idade:'18'}
print(dados['nome'])
print(dados['idade'])
```

Em base e assim que se escreve um dicionario. 

### Como adciona e tira item 

Para voce adicionar nao a um metado expecifico, basta voce colocar uma chave e seu valor. 

```
dados = {nome:'Pedro', idade:'18'}
dados['sexo'] = 'M'
```

E so voce colocar a chave que voce quer e na sua frente o dado que serar inserido nela. 

Para que um item seja deletado do dicionario e necessario que voce use um metado ja conhecido o que e bem tranquito. 

```
dados = {nome:'Pedro', idade:'18'}
del.dados['idade']
```
A chave idade irar ser deletada e pronto 

### O que e chave(Keys), Valores(Values) e Itens(Items)

No python cada parte tem o que nome expecifico, e bem tranquilo de entender nao e complexo. 
As **chaves(Keys)** sao os indises como 'nome' e 'idade'.
Os **Valores(Values)** sao os valores como 'Pedro' e '18'
Os **itens** e o conjunto completo 

### Pegando Chaves e Valores

Para pegar as chaves a um metado do proprio dicionario que e o ```keys()```

```
computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250bg'}

print(computador.keys())

dict_keys(['CPU', 'RAM', 'SSD'])

```

Agora para pegar valores a metado ```values()```

```
notas = {'Mat': 5, 'Por': 7, 'His': 8}

print(notas.values())

dict_values([5, 7, 8])
    
```

### Conceito Interessante

Voce pode misturar listas, com dicionarios ou ate mesmo tuplas, o que muitas das vezes e utilizado como Json e varios outras formas. Aqui vai um exemplo 

```
alunos = [

    dados = {
        nome = 'Laura'
        idade = '14'
    },
    {
        nome = 'Mateus'
        idade = '48'

    }

]
```

Vamos supor que voce quer pegar um elementos voce pode fazer assim 

```
print(alunos[0]['nome'])
print(alunos[1]['idade'])
```

Muitas das outras coisas e voce utilizar a sua nocao. 