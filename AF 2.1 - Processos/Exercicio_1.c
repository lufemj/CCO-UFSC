#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

//       (pai)      
//         |        
//    +----+----+
//    |         |   
// filho_1   filho_2


// ~~~ printfs  ~~~
// pai (ao criar filho): "Processo pai criou %d\n"
//    pai (ao terminar): "Processo pai finalizado!\n"
//  filhos (ao iniciar): "Processo filho %d criado\n"

// Obs:
// - pai deve esperar pelos filhos antes de terminar!


int main(int argc, char** argv) {

    // ....

    /*************************************************
     * Dicas:                                        *
     * 1. Leia as intruções antes do main().         *
     * 2. Faça os prints exatamente como solicitado. *
     * 3. Espere o término dos filhos                *
     *************************************************/

    pid_t pFilho1;
    pFilho1 = fork();

    if (pFilho1 == 0){
        printf("Processo pai criou %d\n", getpid());
    }
    else{
        wait(NULL);
    }

    pid_t pFilho2;
    pFilho2 = fork();

    if (pFilho2 == 0){
        printf("Processo pai criou %d\n", getpid());
    }
    else{
        wait(NULL);
    }

    printf("Processo pai finalizado!\n");   
    return 0;
}
