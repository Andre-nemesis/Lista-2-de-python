'''
Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
Em seguida, peça para o usuário escolher um dos nomes e substituir esse nome por outro nome que ele também deve digitar.
'''
print('Digite 3 nomes: ')
nomes_list = []
def troca_nomes(nome,novo_nome):
    if nome in nomes_list:
        indice = nomes_list.index(nome)    
        nomes_list[indice] = novo_nome
        nomes_alterados = tuple(nomes_list)
        print('\nNome alterado com sucesso!')
        return nomes_alterados
    else:
        return print('Nome não encontrado')

for i in range(0,3):
    nomes_list.append(str(input(f'Digite o {i + 1}° nome: ')))

nomes_tupple = tuple(nomes_list)

print(nomes_tupple)
print('\nEscolha um nome acima para ser substituido.\n')
nome_p_substituir = str(input('Digite o nome: '))
novo_nome = str(input('\nDigite o novo nome: '))

print(troca_nomes(nome_p_substituir,novo_nome))