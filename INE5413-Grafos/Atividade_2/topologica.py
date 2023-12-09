import grafo as g

# QUESTÃO 2 

def ordenacaoTopologica(grafo):
    tempo = 0

    for u in range(grafo.qtdVertices()):
        if c[u] == False:
            tempo = visitaDFS(grafo, u, tempo)

    return o

def visitaDFS(grafo, u, tempo):
    c[u] = True
    tempo += 1
    t[u] = tempo

    for v in grafo.vizinhos(u):
        if c[v-1] == False:
            visitaDFS(grafo, v-1, tempo)
    
    tempo += 1 
    f[u] = tempo

    o.insert(0, grafo.rotulos[u])

    return tempo

arquivo = "grafo_exemplo.txt"
grafo = g.Grafo()
grafo.ler(arquivo)
matriz = grafo.matrizDeAjacencias

c = []
t = []
f = []
o = []

for i in range(grafo.qtdVertices()): 
    c.append(False)
    t.append(float('inf'))
    f.append(float('inf'))

print(ordenacaoTopologica(grafo))

 