# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print(f'União: {conjunto_uniao}')

conjunto_interseccao = conjunto.intersection(conjunto2)
print(f'Intersecção: {conjunto_interseccao}')

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(f'Diferença 1: {conjunto_diferenca1}')
print(f'Diferença 2: {conjunto_diferenca2}')

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(f'Diferença Simétrica: {conjunto_diff_simetrica}')

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(f'O Conjunto a é Subconjunto de b: {conjunto_subset}')
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(f'O Conjunto b é Subconjunto de a: {conjunto_subset}')
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print(f'O Conjunto a é Superconjunto de b: {conjunto_superset}')
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(f'O Conjunto b é Superconjunto de a: {conjunto_superset}')


lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(f'{conjunto_animais}')

lista_animais = list(conjunto_animais)
print(f'{lista_animais}')




