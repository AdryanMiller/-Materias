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

### Agradecimentos
Para que possam saber mais aqui estao alguns artigos e vidoes para que entendam mais sobre o tema
- [Rocketseat](https://www.rocketseat.com.br/blog/artigos/post/como-criar-funcoes-empython#60e8db5ae9694832bf5051f217052012)
- [Curso em Video](https://www.youtube.com/watch?v=ezfr9d7wd_k)
- [DeviMedia](https://www.devmedia.com.br/funcoes-em-python/37340?gad_source=1&gad_campaignid=22326280955&gclid=Cj0KCQjwuKnGBhD5ARIsAD19RsYrZaRLAqMJu7PLslNZyo0Zo8xgo6KnOZHJmkcwWc5qnFnPsAFqwhAaAkAHEALw_wcB)
