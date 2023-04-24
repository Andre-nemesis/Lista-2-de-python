'''
Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
Em seguida, verifique se a chave 'profissão' está presente no dicionário.
'''
dicionario = {}
print('Digite chaves e valores para o dicionário(crie uma chave para idade).')
num_chaves = int(input('Quantas chaves você vai querer adicionar? '))
def add_dict():
    chave = str(input('Digite uma uma chave para ser adicionado ao dicionário: '))
    valor = input('Digite algo que vc queira armazenar nesse chave: ')
    dicionario[chave] = valor

for i in range(num_chaves):
    add_dict()
if 'profissão' in dicionario or 'Profissão' in dicionario:
    print('\nA chave "Profssião", está no dicionário')
else:
    print('\nA chave "Profssião", não está no dicionário')