#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

//                          (principal)
//                               |
//              +----------------+--------------+
//              |                               |
//           filho_1                         filho_2
//              |                               |
//    +---------+-----------+          +--------+--------+
//    |         |           |          |        |        |
// neto_1_1  neto_1_2  neto_1_3     neto_2_1 neto_2_2 neto_2_3

// ~~~ printfs  ~~~
//      principal (ao finalizar): "Processo principal %d finalizado\n"
// filhos e netos (ao finalizar): "Processo %d finalizado\n"
//    filhos e netos (ao inciar): "Processo %d, filho de %d\n"

// Obs:
// - netos devem esperar 5 segundos antes de imprmir a mensagem de finalizado (e terminar)
// - pais devem esperar pelos seu descendentes diretos antes de terminar

int main(int argc, char** argv) {
    pid_t pid1, pid2, pid_neto;
    int i;

    // criação dos dois processos filhos
    pid1 = fork();
    if (pid1 == 0) { // processo filho 1
        for (i = 0; i < 3; i++) {
            pid_neto = fork();
            if (pid_neto == 0) { // processo neto
                printf("Processo %d, filho de %d\n", getpid(), getppid());
                sleep(5);
                printf("Processo %d finalizado\n", getpid());
                _exit(0);
            }
        }
        for (i = 0; i < 3; i++) {
            wait(NULL);
        }
        printf("Processo %d finalizado\n", getpid());
        _exit(0);
    }

    pid2 = fork();
    if (pid2 == 0) { // processo filho 2
        for (i = 0; i < 3; i++) {
            pid_neto = fork();
            if (pid_neto == 0) { // processo neto
                printf("Processo %d, filho de %d\n", getpid(), getppid());
                sleep(5);
                printf("Processo %d finalizado\n", getpid());
                _exit(0);
            }
        }
        for (i = 0; i < 3; i++) {
            wait(NULL);
        }
        printf("Processo %d finalizado\n", getpid());
        _exit(0);
    }

    // processo principal
    printf("Processo principal %d, criou os processos filhos %d e %d\n", getpid(), pid1, pid2);
    for (i = 0; i < 2; i++) {
        wait(NULL);
    }
    printf("Processo principal %d finalizado\n", getpid());
    return 0;
}
