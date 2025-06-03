estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Nome estado: '))
    estado['sigla'] = str(input('Sigla estado: '))
    brasil.append(estado.copy())

print(brasil)

for c, k in estado:
    print(f'O estado e {c} sua sigla e {k} ')