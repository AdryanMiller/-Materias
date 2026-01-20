# Tratamento de exceções e erros em Python

Muitas vezes nos programas precisamos fazer um polimento para que possamos evitar falhas, erros ou ate mesmos excessoes no nosso codigo.
No Python vem com muitas ferramentas robustas para que possamos fazer uma melhor dentencia do nosso programa, e que possamos tratar, identificar e realizar um melhor polimento.

## Erros e Excecoes 

Antes de falar da forma que tratamos os erros e excecoes em python primeiro e necessario conhecer os mais frequentes para entendermos melhor o funcionamento.

1. ```AssertionError:``` gerado quando a instrução assert falha.
   
2. ```EOFError:```: gerado quando a função input() atende à condição de fim de arquivo.
   
3. ```AttributeError```: Quando a atribuição de atributo ou a referência falhar.
   
4. ```TabError```: Quando você não tem acesso a um recuo, o que acontece é que o recuo consiste em tabulações ou espaços inconsistentes. 
   
5. ```ImportError```: gerado quando a importação do módulo falha. 
   
6. ```IndexError```: Ocorre quando o índice de uma sequência está fora do intervalo
   
7. ```KeyboardInterrupt```: Quando o usuário digita teclas de interrupção (Ctrl + C ou Delete).
   
8. ``` RuntimeError```: Ocorre quando um erro não se enquadra em nenhuma categoria. 
   
9. ```NameError```: Quando uma variável não é encontrada no escopo local ou global. 
    
10. ```MemoryError```: Quando você está em um programa, o que você está fazendo? 
    
11. ```ValueError```: Ocorre quando a operação ou função recebe um argumento com o tipo correto, mas com o valor incorreto. 
    
12. ```ZeroDivisionError:```: gerado quando você divide um valor ou uma variável por zero. 
    
13. ```SyntaxError:```: levantado pelo analisador quando a sintaxe do Python está errada. 
    
14. ```IndentationError```: Ocorre quando há um recuo errado.
    
15. ```SystemError```Erro interno: gerado quando o interpretador detecta um erro interno.

## Tratamentos de excecoes

### Utilizando Try e Except 

No python há maneira de tratarmos erros e excecoes, para isso usamos os seguintes comando que a linguem
disponibiliza ```Try```, ```Except``` e ```Finally```.

```
try:
    # código potencialmente problemático
except TipoDeErro:
    # ação em caso de erro
```

    
#### Exemplo Pratico

```
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não permitida.")
```

### Multiplas Excecoes 

Para que seu codigo rode o mais proximo do 100% e necessario pensar em varios erros possiveis,
um codigo pode aparecer varios problemas e para isso pode-se criar varias excecoes para um melhor polimento

```
try:
    # código
except ZeroDivisionError:
    # tratamento para ZeroDivisionError
except TypeError:
    # tratamento para TypeError
```

## Utilizacao do Finally e Else

O camando ```Finally```, e usado para que o codigo o realize mesmo que algo de errado ou nao passe na
```except```, o camando dentro sempre sera execultado.

- **Else:** Executado se nenhuma exceção for capturada no bloco try.
- **Finally:** Sempre executado, independentemente de uma exceção ocorrer ou não.

```
try:
    # código
except TipoDeErro:
    # tratamento da exceção
else:
    # executado se não houver exceção
finally:
    # sempre executado
```