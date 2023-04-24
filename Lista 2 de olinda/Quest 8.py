'''
Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
Em seguida, retorne o valor da chave 'idade'.
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
if 'idade' in dicionario or 'Idade' in dicionario:
    print(dicionario['idade'])
else:
    print('A chave "idade" não está no dicionário.')
