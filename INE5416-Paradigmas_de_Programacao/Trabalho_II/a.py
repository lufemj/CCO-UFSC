# Definição do tipo Tabuleiro
Tabuleiro = list[list[int]]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro: Tabuleiro) -> None:
    for linha in tabuleiro:
        print(linha)

# Função para verificar se o valor pode ser colocado em uma posição específica
def posicao_valida(tabuleiro: Tabuleiro, grupos: Tabuleiro, grupos_valores: dict, linha: int, coluna: int, valor: int) -> bool:
    # Verifica se o valor já está na linha ou coluna
    if valor in tabuleiro[linha] or valor in [tabuleiro[i][coluna] for i in range(len(tabuleiro))]:
        return False

    # Verifica se o valor respeita as restrições do grupo
    grupo = grupos[linha][coluna]
    if valor not in grupos_valores[grupo]:
        return True

    return False

# Função para encontrar a próxima posição vazia no tabuleiro
def encontrar_posicao_vazia(tabuleiro: Tabuleiro) -> tuple[int, int]:
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == 0:
                return i, j
    return -1, -1

# Função principal de backtracking para resolver o tabuleiro
def resolver_tabuleiro(tabuleiro: Tabuleiro, grupos: Tabuleiro, grupos_valores: dict) -> bool:
    linha, coluna = encontrar_posicao_vazia(tabuleiro)

    # Se não houver posição vazia, o tabuleiro está resolvido
    if linha == coluna == -1:
        return True

    # Tenta preencher cada valor de 1 a 10
    for valor in range(1, 11):
        if posicao_valida(tabuleiro, grupos, grupos_valores, linha, coluna, valor):
            tabuleiro[linha][coluna] = valor

            # Recursivamente tenta resolver o restante do tabuleiro
            if resolver_tabuleiro(tabuleiro, grupos, grupos_valores):
                return True

            # Se a atribuição não levar a uma solução, desfaz a atribuição
            tabuleiro[linha][coluna] = 0

    # Nenhuma atribuição levou a uma solução, backtrack
    return False

# Tabuleiros fornecidos
valores6x6 = [
    [2, 0, 0, 0, 1, 0],
    [0, 0, 0, 3, 0, 0],
    [0, 3, 0, 0, 5, 3],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 4, 2],
    [0, 0, 0, 0, 0, 0]
]

grupos6x6 = [
    [1, 1, 2, 2, 2, 3],
    [4, 4, 4, 4, 4, 3],
    [5, 6, 6, 6, 4, 7],
    [5, 5, 5, 6, 7, 7],
    [8, 8, 10, 0, 0, 0],
    [9, 9, 10, 10, 0, 0]
]

# Inicialização de grupos_valores
grupos_valores = {}
for i in range(len(grupos6x6)):
    for j in range(len(grupos6x6[i])):
        grupo = grupos6x6[i][j]
        if grupo != 0:
            grupos_valores.setdefault(grupo, set()).add(valores6x6[i][j])

# Execução do algoritmo de backtracking
resolver_tabuleiro(valores6x6, grupos6x6, grupos_valores)

# Imprime o tabuleiro resolvido
imprimir_tabuleiro(valores6x6)
