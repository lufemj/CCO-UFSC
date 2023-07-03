import multiprocessing
from multiprocessing import Lock
from processo import *
import time

def validaEntrada():
    while True:
        # Entrada do usuário, utilizada para abrir o arquivo e definir o número de processos e threads.
        entry = input('Digite o nome do arquivo, o número de processos e o número de threads: ').split()

        # O número de argumentos passados na entrada deve ser igual a 3.
        if len(entry) != 3:
            print('Erro! Você deve digitar <nome do arquivo de entrada> <número de processos> <número de threads>!')
            print()
            continue
        
        # Caso o número de argumentos seja 3, verifica se o nome do arquivo é válido.
        else:
            nome = entry[0]
            nProcess = entry[1]
            nThreads = entry[2]

            try:
                file = open(nome)
                file.close()
            except FileNotFoundError:
                print('Erro! Arquivo não existe!')
                print('Você deve digitar o nome do arquivo de entrada com a extensão .txt!')
                print()
                continue

            # Verifica se o número de processos e threads é um inteiro positivo.
            if not nProcess.isdigit() or not nThreads.isdigit():
                print('Erro! O número de processos e o número de threads devem ser inteiros positivos!')
                print()
                continue

            # Verifica se o número de processos e threads é maior do que zero.
            elif (int(nProcess) < 1) or (int(nThreads) < 1):
                print("ERRO! O número de processos e o número de threads devem ser maiores que zero!")
                print()

            else:
                return entry

def lerArquivo(nArquivo):
    with open(nArquivo, 'r') as file:
        lista = []
        tabuleiros = []
        contador = 0

        # Lê o arquivo e armazena o conteúdo em uma lista.
        for linha in file:
            if linha != '\n':
                lista.append(linha.strip())
                contador += 1
            
            if contador == 9:
                tabuleiros.append(lista)
                contador = 0
                lista = []
    
    return tabuleiros
          
def criaProcesso(nProcess, nThreads):
    processos = []
    tabuleiroProcesso = []
    idTabuleiros = []
    lock = Lock()

    # Para que não hajam processos ociosos, o número de processos é limitado pelo número de tabuleiros.
    if len(tabuleiros) < nProcess:
        nProcess = int(len(tabuleiros))
    
    # Para que não hajam threads ociosas, o número de threads é limitado pela soma de linhas, colunas e regiões.
    if 27 < nThreads:
        nThreads = 27
    
    # Cria os processos. 
    for i in range(nProcess):
        tabuleiroProcesso.append([])
        idTabuleiros.append([])
        
    # Divide os tabuleiros entre os processos.
    for i in range(len(tabuleiros)):
        tabuleiroProcesso[i % nProcess].append(tabuleiros[i])
        idTabuleiros[i % nProcess].append(i+1)

    for i in range(nProcess):
        novoProcesso = multiprocessing.Process(target=validaTabuleiro, 
                                               args=(i+1, tabuleiroProcesso[i], 
                                                     nThreads, idTabuleiros[i], 
                                                     lock))
        processos.append(novoProcesso)
    return processos
    
def main():
    # Chama a função que valida a entrada do usuário e atribui os valores de retorno as variáveis.
    argumentos = validaEntrada()
    nArquivo = argumentos[0]
    nProcess = int(argumentos[1])
    nThreads = int(argumentos[2])

    global tabuleiros

    # Lê o arquivo e armazena o conteúdo em uma lista, que contém todos os tabuleiros.
    tabuleiros = lerArquivo(nArquivo)

    # Cria os processos e divide os tabuleiros entre eles. 
    processos = criaProcesso(nProcess, nThreads)

    start_time = time.time()

    for i in range(len(processos)):
        processos[i].start()
    
    for i in range(len(processos)):
        processos[i].join()

    end_time = time.time()

    final_time = end_time - start_time

    print("Tempo de execução:", final_time, "segundos")
    
if __name__ == '__main__':
    while True:
        main()