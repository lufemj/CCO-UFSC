from itertools import combinations
import grafo as grafo_module

def lawler(graph):
    X = [n for n in range(2**graph.qtd_vertices())]
    S = conjunto_potencia_ordenado(list(graph.vertices.keys()))
    
    color_assignment = {vertex: -1 for vertex in graph.vertices}

    for index, s in enumerate(S):
        if index == 0:
            X[0] = 0
            continue
        X[index] = float('inf')
        G = sub_grafo(graph, s)

        for I in conjuntos_independentes_maximais(G):
            s_copy = s.copy()
            for v in I:
                if v in s_copy:
                    s_copy.remove(v)
            i = S.index(s_copy)

            if X[i] + 1 < X[index]:
                X[index] = X[i] + 1
                for v in I:
                    color_assignment[v] = X[i]

    return X[-1], color_assignment

def conjunto_potencia_ordenado(values):
    entries = (list(y) for n in range(len(values) + 1) for y in combinations(values, n))

    def binary_index(s):
        return sum(2 ** list(reversed(values)).index(y) for y in s)

    return sorted(entries, key=binary_index)

def sub_grafo(graph, entries):
    vertices = {key: graph.vertices[key] for key in entries}
    vertex_indices = {graph.vertices[key]: key for key in entries}
    edges = [[graph.arestas[x][y] if x in entries and y in entries else None for x in range(max(vertices)+1)] for y in range(max(vertices)+1)]

    return grafo_module.Grafo(vertices, vertex_indices, edges, graph.dirigido)

def conjuntos_independentes_maximais(graph):
    independent_sets = list()
    for v in graph.vertices:
        max_set = set()

        for u in graph.vertices:
            if graph.arestas[v][u] is None:
                max_set.add(u)

        to_remove = list()
        for x in max_set:
            for y in max_set:
                if x == y:
                    continue
                if x in to_remove:
                    continue
                if graph.arestas[x][y] is not None:
                    to_remove.append(y)

        for x in to_remove:
            max_set.discard(x)

        is_subset = False
        for c in independent_sets:
            if max_set.issubset(c):
                is_subset = True
                break
        if is_subset:
            continue

        independent_sets.append(max_set)
    return independent_sets

graph = grafo_module.Grafo()
graph.ler("grafo_exemplo.txt")

minimum_coloring, color_assignment = lawler(graph)

print(f"Coloração Mínima: {minimum_coloring}")
print("Atribuição de Cores:")
for vertex, color in color_assignment.items():
    print(f"Vértice {vertex}: Cor {color}")
