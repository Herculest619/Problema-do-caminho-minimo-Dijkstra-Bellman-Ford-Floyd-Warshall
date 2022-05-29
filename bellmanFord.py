import time

def bellmanFord(G, s, dest):
    inicio = time.time()
    print("\n")
    print("Processando . . .")
    infinito = float("inf")
    dist = []
    pred = []
    for v in range(len(G)):
        dist.append(infinito) #Vetor que armazena a distancia de s a cada vertice
        pred.append(None)     #Vetor que armazena o predecessor de cada vertice

    dist[s] = 0

    for u in range(len(G)):
        trocou = False
        for v in range(len(G)):
            if dist[v] > dist[u] + G[u][v] and G[u][v] != 0: # w(u, v): peso da aresta (u, v)
                dist[v] = dist[u] + G[u][v]
                pred[v] = u
                trocou = True
        if trocou == False:   #A execução pode ser encerrada prematuramente
            break

    # print(dist)
    # print(pred)

    if dest < len(dist) and dest >= 0 and s < len(dist) and s >= 0:
        caminho = []
        caminho.append(dest)
        custo = dist[dest]
        if pred[dest] != None:
            while dest != s:
                caminho.append(pred[dest])
                dest = pred[dest]
        else:
            print("Não existe caminho para o vertice escolhido!")
            pass

        fim = time.time()
        print("Caminho: ",caminho[::-1])
        print("Custo: ", custo)
        print("Tempo", fim - inicio, "s")
    else:
        print("Erro!")