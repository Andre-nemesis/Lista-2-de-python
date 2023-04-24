'''
Crie um dicionário vazio. Peça para o usuário digitar uma chave e um valor e adicione esses dados ao dicionário. 
Em seguida, peça para o usuário adicionar mais uma chave e um valor e adicione esses dados ao dicionário também.
'''
dicionario = {}
def add_chave_e_valor():
    chave = str(input('Digite uma uma chave para ser adicionado ao dicionário: '))
    valor = input('Digite algo que vc queira armazenar nesse chave: ')

    dicionario[chave] = valor

add_chave_e_valor()
add_chave_e_valor()

print(dicionario)