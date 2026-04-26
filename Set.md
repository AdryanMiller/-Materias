# Set

### Estrutura:

meu_set = {valor, valor, valor, valor,...}

### Observações:

- Não pode ter valores duplicados
- Não tem ordem fixa

```
set_produtos = {'arroz', 'feijao', 'macarrao', 'atum', 'azeite'}

print(set_produtos)
```

- Aplicação bem útil:

    1. Quantos clientes tivemos na loja?
```
cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']

set_cpf_clientes = set(cpf_clientes)
cpf_clientes_unicos = list(set_cpf_clientes)
print(cpf_clientes_unicos)
print('Temos {} clientes na loja'.format(len(set_cpf_clientes)))

```

# Métodos de Sets

### Esses são os métodos mais usados de set

- add -> adiciona um item no set
```
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.add('airpod')
print(meu_set)
```

- remove -> retira um item de um set
```
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.remove('iphone')
print(meu_set)
```

- clear -> retira todos os itens de um set
```
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.clear()
print(meu_set)
```

- union -> junta as informações de 2 sets. Se houver algum valor duplicado, ele constará apenas 1 vez no set final
```
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
todos_produtos = produtos.union(lancamentos)
print(todos_produtos)
```

- intersection -> pega apenas as informações que existem nos 2 sets ao mesmo tempo
```
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
intersecao = produtos.intersection(lancamentos)
print(intersecao)
```

- difference -> retorna todas as informações de um set que não fazem parte de outro set
```
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
produtos_nao_lancamentos = produtos.difference(lancamentos)
print(produtos_nao_lancamentos) #repare que ipad foi retirado do resultado porque ele estava contido no set de lançamentos
```
