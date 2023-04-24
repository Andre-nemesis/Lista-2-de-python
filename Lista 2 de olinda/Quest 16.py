'''
Peça para o usuário digitar 10 números e crie uma lista com esses números. 
Em seguida, multiplique cada elemento da lista por 2 e crie uma nova lista com esses valores.
'''
num = []
print('Digite 10 números.')
for i in range(0,10):
    num.append(float(input(f'Digite o {i+1}° número: ')))
for i in range(0,10):
    num[i] *= 2
print(num)