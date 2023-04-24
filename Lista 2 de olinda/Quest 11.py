'''
Crie uma lista vazia e peça para o usuário digitar 10 números.
Em seguida, retorne os elementos de índice par da lista.
'''
listaNum = []
listaIndPar = []
print('Digite 10 números.')
for i in range(0,5):
    listaNum.append(float(input(f'Digite o {i + 1}° número: ')))
for i in range(0,5):
    if i % 2 == 0:
        listaIndPar.append(listaNum[i])
print(listaIndPar)