import threading

def divideTabuleiro(tabuleiro):
    for i in range(9):
        celulas = []
        for j in range(9):
            celulas.append(tabuleiro[j][i])
        tabuleiro.append(celulas)
    
    for i in range(3):
        for j in range(3):
            celulas = []
            for k in range(3):
                for l in range(3):
                    celulas.append(tabuleiro[i*3+k][j*3+l])
            tabuleiro.append(celulas)
        
    return tabuleiro    

def verificaRepeticao(array):
    if isinstance(array, str):
        array_aux = array
        array = ''.join(sorted(array_aux))
    else:
        array.sort()

    for i in range(len(array)-1):
            if array[i] == array[i+1]:
                return True
    return False

def rotinaThread(*args):
    for i in range(len(args)):
        lock = args[i][4]
        tipo = args[i][0]
        num = args[i][1]
        array = args[i][3]

        if verificaRepeticao(array):
            errosTabuleiro[args[i][2]].append(f"{tipo}{num}")
            with lock:
                errosTabuleiro['quantidade'].append(1)
        
def validaTabuleiro(processID, tabuleiros, numThreads, idTabuleiros, lock):
    global errosTabuleiro

    for i in range(len(tabuleiros)):
        with lock:
            print('Processo %d: resolvendo quebra-cabeças %d' % (processID, idTabuleiros[i]))

        threadArgs = []
        threads = []
        errosTabuleiro = {'quantidade': []}
        for l in range(numThreads): 
            threadArgs.append([]) 
            errosTabuleiro[l+1] = []

        tabuleiros[i] = divideTabuleiro(tabuleiros[i])

        for j in range(len(tabuleiros[i])):
            array = tabuleiros[i][j]
            if j < 9:
                threadArgs[j % numThreads].append(['L', (j%9)+1, 
                                                   (j % numThreads)+1, array, 
                                                   lock])
            elif j < 18:
                threadArgs[j % numThreads].append(['C', (j%9)+1, 
                                                   (j % numThreads)+1, array, 
                                                   lock])
            else:
                threadArgs[j % numThreads].append(['R', (j%9)+1, 
                                                   (j % numThreads)+1, array, 
                                                   lock])

        for k in range(numThreads):
            thread = threading.Thread(target=rotinaThread, args=threadArgs[k])
            threads.append(thread)
            threads[k].start()

        for z in range(numThreads):
            threads[z].join()
        
        f = True
        print('Processo %d: %d erros encontrados' % (processID, 
                                                     len(errosTabuleiro['quantidade'])), end=' ')
        if len(errosTabuleiro['quantidade']) == 0:
            print()
            continue
        else:
            errosTabuleiro.pop('quantidade')
            print('(', end='')

            for thread in errosTabuleiro:
                if errosTabuleiro[thread] == []:
                    continue

                if f: 
                    f = False
                    print('T%d:' % thread, end=' ')
                else: 
                    print('; T%d:' % thread, end=' ')
                
                for i in range(len(errosTabuleiro[thread])):
                    if i == len(errosTabuleiro[thread])-1:
                        print(f'{errosTabuleiro[thread][i]}', end='')
                    else:
                        print(f'{errosTabuleiro[thread][i]},', end=' ')
        print(')')