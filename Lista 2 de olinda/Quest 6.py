'''
Crie uma lista vazia e peça para o usuário digitar 10 números. 
Em seguida, adicione esses números à lista utilizando um loop for.
'''
lista2 = []
print('Digite 10 números.')
for i in range(10):
    lista2.append(float(input(f'Digite o {i + 1}° número: ')))

lista = []

for i in lista2:
    lista.append(i)
print(lista)