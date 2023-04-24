'''
Peça para o usuário digitar 5 números e crie uma lista com esses números. 
Em seguida, peça para o usuário digitar mais um número e adicione esse número à lista.
'''
print('Digite 5 números: \n3')
numeros = []

for i in range(0,5):
    numeros.append(float(input(f'Digite o {i + 1}° número: ')))

print('\nDigite mais um número: ')
numeros.append(float(input(f'Digite o número: \n')))

print(numeros)