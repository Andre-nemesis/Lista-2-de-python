'''
Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
Em seguida, adicione uma nova chave e valor ao dicionário, onde a chave é 'cidade' e o valor é a 
cidade em que o usuário nasceu.
'''
dicionario = {}
print('Digite chaves e valores para o dicionário(crie uma chave para idade).')
num_chaves = int(input('Quantas chaves você vai querer adicionar? '))
def add_dict():
    chave = str(input('\nDigite uma uma chave para ser adicionado ao dicionário: '))
    valor = input('Digite algo que vc queira armazenar nesse chave: ')
    dicionario[chave] = valor

for i in range(num_chaves):
    add_dict()

cidadeNatal = str(input('\nDigite a cidade onde você nasceu: '))
dicionario['cidade'] = cidadeNatal
print(dicionario)