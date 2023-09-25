class Grafo(): 
    def __init__(self):
        self.rotulos = [] # Vetor utilizado para armazaenar os rótulos dos vértices com base em sua posição (índice)
        self.matrizDeAjacencias = []

    def qtdVertices(self):
        return len(self.matrizDeAjacencias)
        
    def qtdArestas(self):
        arestas = 0
        for linha in range(len(self.matrizDeAjacencias)+1):
            for coluna in range(linha):
                if self.matrizDeAjacencias[linha][coluna] != float('inf'):
                    arestas += 1
        return arestas

    def grau(self, v):
        grau = 0
        for j in self.matrizDeAjacencias[v]:
            if j != float('inf'):
                grau += 1
        return grau

    def rotulo(self, v):
        return self.rotulos[v]
        
    def vizinhos(self, v):
        vizinhos = []
        for i in range(len(self.matrizDeAjacencias)):
            if self.matrizDeAjacencias[v][i] != float('inf'):
                vizinhos.append(i+1)
        return print(vizinhos)
    
    def haAresta(self, u, v):
        if self.matrizDeAjacencias[u][v] != float('inf'):
                return True
        return False

    def peso(self, u, v):
        if self.matrizDeAjacencias[u][v] != float('inf'):
            return self.matrizDeAjacencias[u][v]
        return float('inf')
    

    #                          MUDAR                          #
    ########################################################################

    def ler(self, arquivo):
        with open(arquivo, 'r') as arquivo:
            lines = arquivo.readlines()

        # Encontrar o número de vértices a partir da primeira linha
        num_vertices = int(lines[0].split()[1])

        # Preencher os rótulos dos vértices
        for i in range(1, num_vertices + 1):
            rotulo = lines[i].strip().split()[1]
            self.rotulos.append(rotulo)

        # Inicializar a matriz de adjacências com valores infinitos
        self.matrizDeAjacencias = [[float('inf')] * num_vertices for _ in range(num_vertices)]

        # Preencher a matriz de adjacências com as arestas
        for linha in lines[num_vertices + 2:]:
            partes = linha.strip().split()
            u = int(partes[0]) - 1  # Ajustar o índice do vértice para começar em 0
            v = int(partes[1]) - 1  # Ajustar o índice do vértice para começar em 0
            peso = float(partes[2])
            self.matrizDeAjacencias[u][v] = peso
            self.matrizDeAjacencias[v][u] = peso  # Se o grafo for não-direcionado, descomente esta linha

########################################################################
