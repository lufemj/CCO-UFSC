import grafo as g

# QUESTÃO 3 

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][0]
        less_than_pivot = [x for x in arr[1:] if x[0] <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x[0] > pivot]
        return quicksort(less_than_pivot) + [arr[0]] + quicksort(greater_than_pivot)

def kruskal(grafo):
    arvore = []
    s = []
    e = []
    for i in range(grafo.qtdVertices()):
        s.append([i])
    
    for i in range(grafo.qtdVertices()):
        for j in range(grafo.qtdVertices()):
            if grafo.matrizDeAjacencias[i][j] != float('inf'):
                e.append((grafo.matrizDeAjacencias[i][j], i, j))
    
    e = quicksort(e)
    soma = 0

    for i in range(len(e)):
        if s[e[i][1]] != s[e[i][2]]:

            arvore.append((e[i][1]+1, e[i][2]+1))
            soma += e[i][0]

            x = []

            for j in range(len(s[e[i][1]])):
                x.append(s[e[i][1]][j])
            
            for j in range(len(s[e[i][2]])):
                x.append(s[e[i][2]][j])
            
            for j in range(len(x)):
                s[x[j]] = x

    print("Soma dos pesos das arestas: %.2f" % soma)
    print("Árvore: %s" % arvore)

arquivo = "grafo_exemplo.txt"
grafo = g.Grafo()
grafo.ler(arquivo)
kruskal(grafo)