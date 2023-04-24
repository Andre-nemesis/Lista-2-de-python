'''
Peça para o usuário digitar 10 números e crie um conjunto com esses números. 
Em seguida, remova todos os números pares do conjunto.
'''
listaNum = []
print('Digite 10 números.')
for i in range(0,5):
    listaNum.append(float(input(f'Digite o {i + 1}° número: ')))
for i in listaNum:
    if i % 2 == 0:
        listaNum.remove(i)
print(listaNum)