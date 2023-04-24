'''
Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
Em seguida, peça para o usuário escolher um dos números e removê-lo do conjunto.
'''
conjuntoNum = []

print('Digite 5 números.\n')
for i in range(0,5):
    conjuntoNum.append(float(input(f'\nDigite o {i +1}° número: ')))

print(conjuntoNum)

conjuntoNum.remove(float(input('Digite um valor acima para remover: ')))
print(f'Removido com sucesso!\n\n{conjuntoNum}')