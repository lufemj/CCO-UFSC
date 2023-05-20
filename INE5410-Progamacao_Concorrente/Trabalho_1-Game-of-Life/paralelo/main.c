#include <stdio.h>
#include <stdlib.h>
#include "gol.h"
#include <pthread.h>

stats_t stats_total = {0, 0, 0, 0};
pthread_mutex_t mutex;

typedef struct {
    cell_t *prev;
    cell_t *next;
    cell_t *tmp;
    int size, steps, start, end;
} arguments;


void* threadFunction(void* arg) {
    arguments* params = (arguments *) arg;



    stats_t stats_step = {0, 0, 0, 0};


    for (int i = 0; i < params->steps; i++)
    {
        stats_step = play(params->prev, params->next, params->size, params->start-1, params->end-1);
        
        pthread_mutex_lock(&mutex);
        stats_total.borns += stats_step.borns;
        stats_total.survivals += stats_step.survivals;
        stats_total.loneliness += stats_step.loneliness;
        stats_total.overcrowding += stats_step.overcrowding;
        pthread_mutex_unlock(&mutex);


#ifdef DEBUG
        printf("Step %d ----------\n", i + 1);
        print_board(params->next, params->size);
        print_stats(stats_step);
#endif
        params->tmp = params->next;
        params->next = params->prev;
        params->prev = params->tmp;
    }
    return NULL;
}

int main(int argc, char **argv)
{
    int size, steps;
    cell_t *prev, *next, *tmp = NULL;
    FILE *f;

    if (argc != 3)
    {
        printf("ERRO! Você deve digitar %s <nome do arquivo do tabuleiro> <numero de threads>!\n\n", argv[0]);
        return 0;
    }

    if ((f = fopen(argv[1], "r")) == NULL)
    {
        printf("ERRO! O arquivo de tabuleiro '%s' não existe!\n\n", argv[1]);
        return 0;
    }

    if (atoi(argv[2]) <= 0)
    {
        printf("ERRO! O número de threads deve ser maior que zero!\n\n");
        return 0;
    }
    fscanf(f, "%d %d", &size, &steps);

    prev = allocate_board(size);
    next = allocate_board(size);

    read_file(f, prev, size);

    fclose(f);

#ifdef DEBUG
    printf("Initial:\n");
    print_board(prev, size);
    print_stats(stats_step);
#endif
//Logica threads

    int start, end, n_threads;

    n_threads = atoi(argv[2]);
    pthread_t threads[n_threads];

    int num_elementos = size*size;
    int resto = num_elementos % n_threads;

    arguments arg_vector[n_threads];


    for (int i = 0; i < n_threads; i++) {
    arg_vector[i].size = size;
    arg_vector[i].steps = steps; // Correção: atribuir o valor correto para steps
    arg_vector[i].prev = prev;
    arg_vector[i].next = next;
    arg_vector[i].tmp = tmp;

    if (i < resto) { // Correção: trocar o operador de comparação de "<-" para "<"
        int op_por_thread = (num_elementos / n_threads) + 1;

        start = op_por_thread * i;
        end = op_por_thread * (i+1);

        arg_vector[i].start = start;
        arg_vector[i].end = end;

        pthread_create(&threads[i], NULL, threadFunction, &arg_vector[i]);
    } else {
        int op_por_thread = num_elementos / n_threads;

        start = op_por_thread * i;
        end = op_por_thread * (i+1);

        arg_vector[i].start = start;
        arg_vector[i].end = end;

        pthread_create(&threads[i], NULL, threadFunction, &arg_vector[i]);
    }
}
    for (int i = 0; i < n_threads; i++) {
        pthread_join(threads[i], NULL);
    }

//ele vai de num_op*i ate num_op* (i+1)
#ifdef RESULT
    printf("Final:\n");
    print_board(prev, size);
    print_stats(stats_total);
#endif

    free_board(prev, size);
    free_board(next, size);
}
