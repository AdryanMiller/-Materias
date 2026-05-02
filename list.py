#NIVEL 1

#1
numeros = [1, 2, 3, 4]

numeros_drobro = [item * 2 for item in numeros]
#print(numeros_drobro)

#2

strings = ["python", "java"]

strings_menusculas = [item.upper() for item in strings]
#print(strings_menusculas)


#NIVEL 2

#1

num = [1,2,3,4,5,6]

num_pares = [item for item in num if item % 2 == 0]
#print(num_pares)

#2
palavras = ['naruto', 'uva', 'banana', 'jaca', 'oliva']

palavras_mais_cinco = [item for item in palavras if len(item) > 5]
#print(palavras_mais_cinco)

#NIVEL 3

#1

numeross = [1, 2, 3, 4]

numeros_drobroo = [item * 2 for item in numeross if item % 2 == 0]
#print(numeros_drobroo)

#2

colecao = [1,-2,3,-1]

nova_colecao = [0 if item < 0 else item for item in colecao]
#print(nova_colecao)

def dobro(a):
    return a*2

lista_numeros = [1,2,3,4,5,6,7,8]

lista_dobro = list(map(dobro, lista_numeros))

#print(lista_dobro)

def segundo_item(tuplas):
    return tuplas[1]

vendas_produtos = {'venho': 100, 'cafeteira': 150, 'microondas': 300, 'iphone': 5500}

lista_vendas = list(vendas_produtos.items())

lista_vendas.sort(key=segundo_item, reverse=True)

#print(lista_vendas)

print((lambda x,y: x+y) (2,3))