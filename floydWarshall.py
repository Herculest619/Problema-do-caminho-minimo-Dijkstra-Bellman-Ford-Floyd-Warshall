import time

def floydWarshall(G, s, dest):
    inicio = time.time()
    print("\n")
    print("Processando . . .")
    dist = [[0 for x in range(len(G))] for x in range(len(G))]
    pred = [[0 for x in range(len(G))] for x in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if i == j:
                dist[i][j] = 0
                pred[i][j] = None
            elif G[i][j] != 0:
                dist[i][j] = G[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = float("inf")
                pred[i][j] = None

    #TESTES
    # for i in range(len(G)):
    #     for j in range(len(G)):
    #         print(dist[i][j], " ", end="")
    #     print()
    #
    # print("\n")
    # for i in range(len(G)):
    #     for j in range(len(G)):
    #         print(pred[i][j], " ", end="")
    #     print()

    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    #imprimir as duas matrizes
    # for i in range(len(G)):
    #     for j in range(len(G)):
    #         print(dist[i][j], " ", end="")
    #     print()
    #
    # print("\n")
    # for i in range(len(G)):
    #     for j in range(len(G)):
    #         print(pred[i][j], " ", end="")
    #     print()

    if dest < len(dist) and dest >= 0 and s < len(dist) and s >= 0:
        caminho = []
        caminho.append(dest)
        custo = dist[s][dest]
        if pred[s][dest] != None:
            while dest != s:
                caminho.append(pred[s][dest])
                dest = pred[s][dest]
        else:
            print("Não existe caminho para o vertice escolhido!")
            pass

        fim = time.time()
        print("Caminho: ",caminho[::-1])
        print("Custo: ", custo)
        print("Tempo", fim - inicio, "s")
    else:
        print("Erro!")