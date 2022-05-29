import time

def dijkstra(G, s, dest):
    inicio = time.time()
    print("\n")
    print("Processando . . .")
    Q = list()
    infinito = float("inf")
    dist = []
    pred = []
    for v in range(len(G)):
        dist.append(infinito) #Vetor que armazena a distancia de s a cada vertice
        pred.append(None)     #Vetor que armazena o predecessor de cada vertice
        Q.append(v)           #Q: lista dos vertices a serem processados

    dist[s] = 0

    while (len(Q)!=0):        #Lista Q não for vazia (ha vertices a processar)
        min = infinito
        for i in Q:
            if (dist[i] < min):
                min = dist[i]
                u = i         #u: Vertice de menor distancia em Q

        try:
            Q.remove(u)           #Remover u de Q
        except:
            Q.pop(0)

        for v in range(len(G[u])):
            if dist[v] > dist[u] + G[u][v] and G[u][v] != 0: #w(u, v): peso da aresta (u, v)

                dist[v] = dist[u] + G[u][v]
                pred[v] = u
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