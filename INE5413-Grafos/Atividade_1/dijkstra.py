import grafo as g

def Dijkstra(G, s):
    s = s - 1
    distancias = [float('inf')] * G.qtdVertices()
    arvore = [[s+1] for _ in range(G.qtdVertices())]
    distancias[s] = 0
    visitados = [False] * G.qtdVertices()

    for _ in range(G.qtdVertices()):
        min_distancia = float('inf')
        u = None
        
        for v in range(G.qtdVertices()):
            if distancias[v] < min_distancia and not visitados[v]:
                min_distancia = distancias[v]
                u = v
        
        if u is None:
            break
        
        visitados[u] = True
        
        for v in range(G.qtdVertices()):
            if G.peso(u, v) > 0 and not visitados[v] and distancias[v] > distancias[u] + G.peso(u, v):
                distancias[v] = distancias[u] + G.peso(u, v)
                arvore[v] = arvore[u] + [v + 1]
        
    return distancias, arvore


grafo = g.Grafo()
grafo.ler("grafo_exemplo.txt")
origem = 1

distancias, arvore = Dijkstra(grafo, origem)

for destino in range(grafo.qtdVertices()):
    caminho = ', '.join(map(str, arvore[destino]))
    print(f'{destino+1}: {caminho}; d={distancias[destino]}')
    