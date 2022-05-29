import dijkstra
import bellmanFord
import floydWarshall
from random import randint
try:
    print("Digite a quantidade de vertices: ", end='')
    vertices = int(input())
    print("Digite a quantidade de arestas: ", end='')
    arestas = int(input())
    print("Digite o valor minimo para o peso da aresta: ", end='')
    peso_min = int(input())
    print("Digite o valor maximo para o peso da aresta: ", end='')
    peso_max = int(input())
    print("Digite qual algoritimo deseja usar:\n\t1: Dijksrta\n\t2: Bellman Ford\n\t3: Floyd Warshall")
    algoritmo = int(input())
    print("Origem: ", end='')
    origem = int(input())
    print("Destino: ", end='')
    destino = int(input())

    if arestas < ((vertices * vertices) - vertices + 1):
        print("Gerando grafo . . .")
        grafo = [[0 for x in range(vertices)] for x in range(vertices)]
        cont = 0
        while cont < arestas:
            i = randint(0,vertices-1)
            j = randint(0,vertices-1)
            if i != j and grafo[i][j] == 0:
                grafo[i][j] = randint(peso_min, peso_max)
                cont += 1
    else:
        print("Valor de arestas superior ao máximo possível para esse grafo!")
        quit()

    if algoritmo == 1:
        dijkstra.dijkstra(grafo, origem, destino)
    elif algoritmo == 2:
        bellmanFord.bellmanFord(grafo, origem, destino)
    elif algoritmo == 3:
        floydWarshall.floydWarshall(grafo, origem, destino)
    else:
        print("Valor não corresponde à nenhum algoritmo")
except:
    print("Foi digitado algum caractere que não é um numero!")


# Testes
# G = [[0, 6, 9, 0, 0],
#      [0, 0, 0, 5, 0],
#      [9, 0, 0, 0, 8],
#      [0, 5, 7, 0, 7],
#      [0, 0, 0, 5, 0]]
#
# H = [[0, 1, 0, 5, 0],
#      [0, 0, 5, 3, 8],
#      [0, 0, 0, 0, 1],
#      [0, 0,-1, 0, 0],
#      [0, 0, 0, 0, 0]]
#
# I = [[0,-1, 6],
#      [0, 0, 4],
#      [5, 3, 0]]

# --------------------imprir matriz---------------------
# for i in range(len(grafo)):
#     for j in range(len(grafo)):
#         print(grafo[i][j], " ", end="")
#     print()



# dijkstra.dijkstra(G, 0, 1)

# bellmanFord.bellmanFord(H, 0, 4)

# floydWarshall.floydWarshall(I, 1, 2)