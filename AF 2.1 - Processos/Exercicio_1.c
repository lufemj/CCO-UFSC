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

    int filho1;
    filho1 = fork();

    if (filho1 > 0) {
        printf("Processo filho %d criado\n", filho1);


        int filho2;
        filho2 = fork();

        if (filho2 > 0) {
            printf("Processo filho %d criado\n", filho2);
        } 
        else if (filho2 == 0) {
            printf("Processo filho criado\n");
        }

    } 
    else if (filho1 == 0) {
        printf("Processo filho criado\n");
    }

    // ....

    /*************************************************
    * Dicas: *
    * 1. Leia as intruções antes do main(). *
    * 2. Faça os prints exatamente como solicitado. *
    * 3. Espere o término dos filhos *
    *************************************************/

    printf("Processo pai finalizado!\n");
    return 0;
}
