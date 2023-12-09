import grafo as g

def buscaEmLargura(G, v):
    visitados = [False] * G.qtdVertices()
    fila = [v]
    visitados[v] = True
    indiceNivel = 0

    print("Nível", indiceNivel, ":", (v+1))
    indiceNivel += 1

    while len(fila) > 0:
        nivel = []
        v = fila.pop(0)

        for u in range(G.qtdVertices()):
            if G.haAresta(v, u) and not visitados[u]:
                fila.append(u)
                visitados[u] = True
                nivel.append(u + 1)

        if len(nivel) == 0:
            continue
        
        resultado = ', '.join(map(str, nivel))
        print("Nível", indiceNivel, ":", resultado)
        indiceNivel += 1

grafo = g.Grafo()
grafo.ler("grafo_exemplo.txt")
origem = 3

buscaEmLargura(grafo, origem - 1)