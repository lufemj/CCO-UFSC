#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

// (pai)
// |
// +----+----+
// | |
// filho_1 filho_2


// ~~~ printfs ~~~
// pai (ao criar filho): "Processo pai criou %d\n"
// pai (ao terminar): "Processo pai finalizado!\n"
// filhos (ao iniciar): "Processo filho %d criado\n"

// Obs:
// - pai deve esperar pelos filhos antes de terminar!


int main(int argc, char** argv) {

    pid_t pFilho1;
    printf("Processo pai criou %d\n", pFilho1);
    pFilho1 = fork();


    if (pFilho1 == 0) {
        pid_t pFilho2;
        printf("Processo pai criou %d\n", pFilho2);
        pFilho2 = fork();

        if (pFilho2 == 0) {
            wait(NULL);
        }

        else {
            printf("Processo filho %d criado\n", getpid());
        } 
    }
    else {
        printf("Processo filho %d criado\n", getpid());
    }

    if(wait(NULL) < 0){
        printf("Processo pai finalizado!\n");
    }

    return 0;
}
