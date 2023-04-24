'''
Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
O usuário deve informar os pares de vértices que formam cada aresta. 
Em seguida, peça para o usuário escolher uma das arestas e removê-la do grafo.
'''
grafo = {}

numVertices = int(input('Digite o número de vértices do grafo: '))

def insertVert():
    for i in range(numVertices):
        v = input(f'Digite o {i+1}° vértice: ')
        grafo[v] = []
    insertArest()
    
def insertArest():
    while True:
        aresta = str(input('Digite os vértices que formam a aresta (ou fim para encerrar): '))
        if aresta == 'fim' or aresta == 'Fim' or aresta == 'FIM':
            excluirGrafo()
            break
        v1, v2 = aresta.split()
        if v1 in grafo and v2 in grafo:
            grafo[v1].append(v2)
            grafo[v2].append(v1)
        else:
            print('Vértice não encontrado. Tente novamente.')

def mostGraf():
    print('Grafo:')
    for i in grafo:
        print(f'{i}: {grafo[i]}')
    exit()

def excluirGrafo():
    print('Grafo:')
    for i in grafo:
        print(f'{i}: {grafo[i]}')

    excluir = str(input('\nDigite a aresta que você quer excluir: '))
    v1, v2 = excluir.split()

    if v1 in grafo and v2 in grafo:
        if v2 in grafo[v1]:
            grafo[v1].remove(v2)
            grafo[v2].remove(v1)
            mostGraf()
        else:
            print(f'A aresta ["{v1}":"{v2}"] não existe.')
    else:
        print(f'Vertice não encontrado.')

insertVert()