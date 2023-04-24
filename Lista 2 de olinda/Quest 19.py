'''
Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
Em seguida, verifique quantos elementos estão no conjunto.
'''
num = []
print('Digite 5 números.')
for i in range(0,5):
    num.append(float(input(f'Digite o {i+1}° número: ')))
print(f'Existem "{len(num)}" elementos no conjunto.')