'''
Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
Em seguida, retorne o primeiro elemento da tupla.
'''
lista = []

print('Digite 5 números.')
for i in range(0,5):
    lista.append(float(input(f'Digite o {i + 1}° número: ')))

tupla = tuple(lista)

print(tupla[0])