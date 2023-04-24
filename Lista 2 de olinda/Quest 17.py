'''
Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.
'''
listNomes = []
print('Digite 3 nomes.\n')
for i in range(3):
    listNomes.append(str(input(f'Digite o {i + 1}° nome: ')))
tupNome = tuple(listNomes)

for i in range(3):
    if 'Maria' in tupNome:
        print('\nMaria está na tupla.')
        break
    else:
        print('\nMaria não está na tupla.')
        break