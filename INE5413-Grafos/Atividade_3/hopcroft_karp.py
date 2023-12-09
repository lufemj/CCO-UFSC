import grafo as grafo_module

def hopcroft_karp(grafo):
    distancias = [float("inf") for _ in range(len(grafo.vertices))]
    emparelhamentos = [None for _ in range(len(grafo.vertices))]
    dist_none = [0]

    metade_vertices = (int)(grafo.qtd_vertices()/2 - 1)
    emparelhamentos_count = 0
    while busca_em_largura_emparelhamento(grafo, emparelhamentos, distancias, dist_none):
        for x in range(metade_vertices + 1):
            if emparelhamentos[x] is None:
                if busca_em_profundidade_emparelhamento(grafo, emparelhamentos, x, distancias, dist_none):
                    emparelhamentos_count += 1

    print(f"Emparelhamento Máximo: {emparelhamentos_count}")
    return emparelhamentos

def busca_em_largura_emparelhamento(grafo, emparelhamentos, distancias, dist_none):
    Q = []
    metade_vertices = (int)(grafo.qtd_vertices()/2 - 1)

    for x in range(metade_vertices + 1):
        if emparelhamentos[x] is None:
            distancias[x] = 0
            Q.append(x)
        else:
            distancias[x] = float("inf")

    dist_none[0] = float("inf")
    while len(Q) > 0:
        x = Q.pop()
        if distancias[x] < dist_none[0]:
            for y in grafo.vizinhos(x):
                if emparelhamentos[y] is None:
                    if dist_none[0] == float("inf"):
                        dist_none[0] = distancias[x] + 1
                else:
                    if distancias[emparelhamentos[y]] == float("inf"):
                        distancias[emparelhamentos[y]] = distancias[x] + 1
                        Q.append(emparelhamentos[y])

    return dist_none[0] != float("inf")

def busca_em_profundidade_emparelhamento(grafo, emparelhamentos, x, distancias, dist_none):
    if x is not None:
        for y in grafo.vizinhos(x):
            if emparelhamentos[y] is None:
                if dist_none[0] == distancias[x] + 1:
                    if busca_em_profundidade_emparelhamento(grafo, emparelhamentos, emparelhamentos[y], distancias, dist_none):
                        emparelhamentos[x] = y
                        return True
                    else:
                        if distancias[emparelhamentos[y]] == distancias[x] + 1:
                            if busca_em_profundidade_emparelhamento(grafo, emparelhamentos, emparelhamentos[y], distancias, dist_none):
                                emparelhamentos[y] = x
                        emparelhamentos[x] = y
                        return True
                    distancias[x] = float("inf")
        return False

    return True

def obter_arestas_do_emparelhamento_maximo(emparelhamento):
    arestas = []
    for i, parceiro in enumerate(emparelhamento):
        if parceiro is not None:
            arestas.append((i, parceiro))
    return arestas

grafo = grafo_module.Grafo()
grafo.ler("grafo_exemplo.txt")

emparelhamento = hopcroft_karp(grafo)

arestas_do_emparelhamento_maximo = obter_arestas_do_emparelhamento_maximo(emparelhamento)
print("Arestas no Emparelhamento Máximo:", arestas_do_emparelhamento_maximo)
