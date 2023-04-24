'''
Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes.
Em seguida, verifique se o nome 'Maria' está presente na tupla.
'''
nomes = []
print('Digite 3 nomes.')
for i in range(0,3):
    nomes.append(str(input(f'Digite o {i+1}° nome: ')))
nomestupla = tuple(nomes)
if 'maria' in nomestupla or 'Maria' in nomestupla:
    print('A palavra: Maria está na Tupla.')
else:
    print('A palavra: Maria não está na tupla.')