# Dicionarios 📕

Dados pegos do site [Curso em Video](https://www.youtube.com/watch?v=ZWj8o692qGY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=110)

### Como se escreve ?

Antes de qualquer coisa, os dicionarios se parecem com listas e tuplas a diferença e que possui um nome para determinado item. 
Vamos ver como se escreve agora

```
dados = dict()
dados = {nome:'Pedro', idade:'18'}
```

Nisso diferente das tuplas e listas para voce dar um print voce precisa pegar o indice com o nome. 
```
dados = dict()
dados = {nome:'Pedro', idade:'18'}
print(dados['nome'])
print(dados['idade'])
```

Em base e assim que se escreve um dicionario. 

### Como adciona e tira item 

Para voce adicionar nao a um metado expecifico, voce consegue adicionar assim. 

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