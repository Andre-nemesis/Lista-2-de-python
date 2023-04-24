'''
Peça para o usuário digitar 5 números e crie um conjunto com esses números.
Em seguida, verifique se o número 3 está presente no conjunto.
'''
num = []
print('Digite 5 números.')
for i in range(0,5):
    num.append(float(input(f'Digite o {i+1}° número: ')))
if 3 in num:
    print('\nO número 3 está na lista.')
else:
    print('\nO número "3" não está na lista.')