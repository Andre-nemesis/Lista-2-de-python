'''
Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
O usuário deve informar os pares de vértices que formam cada aresta.
'''
grafo = {}

numVertices = int(input('Digite o número de vértices do grafo: '))

for i in range(numVertices):
    v = input(f'Digite o {i+1}° vértice: ')
    grafo[v] = []

while True:
    aresta = str(input('Digite os vértices que formam a aresta (ou fim para encerrar): '))
    if aresta == 'fim' or aresta == 'Fim' or aresta == 'FIM':
        break
    v1, v2 = aresta.split()
    if v1 in grafo and v2 in grafo:
        grafo[v1].append(v2)
        grafo[v2].append(v1)
    else:
        print('Vértice não encontrado. Tente novamente.')
