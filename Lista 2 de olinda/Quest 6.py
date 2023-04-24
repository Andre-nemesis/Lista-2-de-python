'''
Crie uma lista vazia e peça para o usuário digitar 10 números. 
Em seguida, adicione esses números à lista utilizando um loop for.
'''
lista = []
print('Digite 10 números.')
for i in range(10):
    lista.append(float(input(f'Digite o {i + 1}° número: ')))
print(lista)
