estado = dict()
brasi  = list()

for c in range(0, 3):
    estado['uf'] = str(input('Digite seu eestado: '))
    estado['singla'] = str(input('Digite a sigla do seu estado: '))

    brasi.append(estado.copy())

print(brasi)