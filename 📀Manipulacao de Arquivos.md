# Manipulacao de Arquivos

Manipular arquivos em diversos codigos e importante, nao importa a linguagem, saber como manipulalos e uma grande passo para que possa ler os arquivos
No python isso nao e diferente, a linguagem apresanta varios metados para que possamos manipular esses arquivos, e ajudar no que precisamos ralizar.

## Abrir aquivos Python

Para que possamos abrir um arquivo no python e necessario usarmos o motado ```Open```, que ira receber dois parametros, o nome do aqruivo e como deve abri-lo.

```
 arquivo = open('texto.txt', 'r')
```

No exemplo a cima esta abrindo o arquivo em modo ```r```, que seria modo de leitura.
Veja a baixo as formmas que se pode usar para abrir os arquivos.

- ```'r'```: modo de leitura, o arquivo deve existir previamente
- ```'w'```: modo de escrita, se o arquivo não existir, ele será criado
- ```'a'```: modo de anexar, adiciona informações ao final do arquivo
- ```'x'```: modo exclusivo, cria um novo arquivo somente se ele não existir
- ```'b'```: modo binário, usado para arquivos binários, como imagens ou vídeos
- ```'t'```: modo de texto, usado para arquivos de texto
  
Podemos tambem usar combinacoes para abrir arquivos, vamos supor que voce quer ler mas tambem que escrever voce pdoe usar ```r+``` que serar para ler e escrever no arquivo.

## Lendo arquivos

Agora que sabemos as formar que podemos abrir um arquivos devemos saber ler os mesmos
Para isso vamos o usar o metado ```read``` 

Veja abaixo

```
arquivo = open('texto.txt', 'r')

conteudo = arquivo.read()

print(conteudo)
```

No exemplo estamos lendo o arquivo que esta na varaivel **arquivo** e estamos atibundo ela a varaivel **conteudo** para ler, e mostrando na tela seu conteudo. 
No exemplo estamos lendo o arquivo por interio, mas tambem podemos ler linha por linha do arquivo usando o metado ```readline```

```
arquivo = open('texto.txt', 'r')

linha = arquivo.readline()

print(linha)

```

Neste exemplo, a cada chamada do método readline(), uma nova linha do arquivo é lida e armazenada na variável linha.

## Escrevendo nos arquivos 

Agora que sabemos abrir um arquivo, ler e necessario que sabemos como colocar informacoes dentro deles, como vamos escrever nos arquivos 
E para escrever em um arquivo no python usamos o metado ```write```, mas lembre de abrir o arquivo com ```w``` ou ```+```.
Veja abaixo

```
arquivo = open('novo_texto.txt', 'w')
arquivo.write('Olá, Mundo!')
arquivo.close()
```

Neste exemplo, criamos um novo arquivo chamado “novo_texto.txt” e escrevemos a string “Olá, Mundo!” no arquivo.

Em seguida, fechamos o arquivo utilizando o método ```close()```.

É importante fechar o arquivo depois de terminar de escrever para liberar os recursos do sistema operacional.

## Manipulacao de arquivos com Statemet 

No python a uma sintex muito melhor para que se abra um arquivo, nela sera muito mais rapido, conviniente e mais eficaz na hora de fechamentos de arquivos
O fechamento de um arquivo e muito importante pois muito das vezes o arquivo ficando aberto no programa alem de cosumir do SO, a protecao do mesmo se tornara mais funeravel. 

O statemet ```with``` e usado para abrir o arquivo e garantir que ira fechar mesmo que o programa der problema.

Veja abaixo

```
with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```
Neste exemplo, o arquivo é aberto dentro do bloco ```with``` e o conteúdo é lido e armazenado na variável ```conteudo```.

Ao final do bloco ```with```, o arquivo é automaticamente fechado, mesmo que ocorra uma exceção durante a leitura.

O statement ```with``` é especialmente útil quando manipulamos arquivos grandes ou quando há várias operações a serem realizadas no arquivo.

Ele garante que os recursos do sistema operacional sejam liberados de forma eficiente.
