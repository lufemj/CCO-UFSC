import grafo as grafo_modulo

def edmonds_karp(grafo, vertice_origem, vertice_destino):
    rede_residual = [[grafo.arestas[u][v] if grafo.arestas[u][v] is not None else 0 for v in range(grafo.qtd_vertices())] for u in range(grafo.qtd_vertices())]
    caminho_aumentante = busca_em_largura_fluxo(grafo, vertice_origem, vertice_destino, rede_residual)
    total_caminhos = 0
    fluxo_maximo = 0

    while caminho_aumentante is not None:
        fluxos = [grafo.arestas[caminho_aumentante[i + 1]][caminho_aumentante[i]] - rede_residual[caminho_aumentante[i + 1]][caminho_aumentante[i]] for i in range(len(caminho_aumentante) - 1)]
        fluxo_caminho = minimo(fluxos)
        fluxo_maximo += fluxo_caminho

        for i in range(len(caminho_aumentante) - 1):
            entrada = caminho_aumentante[i + 1]
            saida = caminho_aumentante[i]
            rede_residual[entrada][saida] += fluxo_caminho

        total_caminhos += 1
        caminho_aumentante = busca_em_largura_fluxo(grafo, vertice_origem, vertice_destino, rede_residual)

    return fluxo_maximo

def busca_em_largura_fluxo(grafo, vertice_origem, vertice_destino, rede_residual):
    visitados = [False for x in range(len(grafo.vertices))]
    antecessores = [None for x in range(len(grafo.vertices))]
    visitados[vertice_origem] = True
    fila = [vertice_origem]

    while fila:
        u = fila.pop(0)

        for v in range(len(grafo.arestas[u])):
            if grafo.arestas[u][v] is not None and not visitados[v] and (grafo.arestas[u][v] - rede_residual[u][v] > 0):
                visitados[v] = True
                antecessores[v] = u
                if v == vertice_destino:
                    caminho_aumentante = []
                    while v is not None:
                        caminho_aumentante.append(v)
                        v = antecessores[v]
                    return caminho_aumentante[::-1]
                fila.append(v)
    return None

def minimo(valores):
    if not valores or len(valores) < 1:
        print("Erro")
        return None
    return min(valores)

grafo = grafo_modulo.Grafo()
grafo.ler("grafo_exemplo.txt")
vertice_origem = 0
vertice_destino = 6

fluxo_maximo = edmonds_karp(grafo, vertice_origem, vertice_destino)

print(f"Fluxo máximo: {fluxo_maximo}")
