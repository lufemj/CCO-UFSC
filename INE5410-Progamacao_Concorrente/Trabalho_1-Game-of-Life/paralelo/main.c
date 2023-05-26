#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include "gol.h"
// Alunos: Isaque Beirith e Luis Fernando Mendonça

// Barreiras inicilizadas como variáveis globais
pthread_barrier_t barrier_steps;
pthread_barrier_t barrier_board;

int main(int argc, char **argv)
{
    int size, steps;
    cell_t **prev, **next;
    FILE *f;
    stats_t stats_total = {0, 0, 0, 0};

    // Verifica se foram passados o número correto de argumentos
    if (argc != 3)
    {
        printf("ERRO! Você deve digitar %s <nome do arquivo do tabuleiro> <número de threads>!\n\n", argv[0]);
        return 0;
    }

    // Verifica se o arquivo existe
    if ((f = fopen(argv[1], "r")) == NULL)
    {
        printf("ERRO! O arquivo de tabuleiro '%s' não existe!\n\n", argv[1]);
        return 0;
    }

    // Número de threads deve ser maior que zero
    if (atoi(argv[2]) <= 0)
    {
        printf("ERRO! O número de threads deve ser maior do que zero!\n\n");
        return 0;
    }

    fscanf(f, "%d %d", &size, &steps);

    // Terceiro argumento é o número de threads da aplicação
    int n_threads = atoi(argv[2]);

    // Se o número de threads for maior do que o tamanho do tabuleiro,
    // o numero de threads passa a ser o tamanho do tabuleiro
    if (n_threads > size*size)
    {
        n_threads = size*size;
    }

    // Vetor com as threads
    pthread_t threads_vector[n_threads];

    // Vetor com os argumentos de cada thread
    arguments_t args_vector[n_threads];

    // Alocando os boards next e prev
    prev = allocate_board(size);
    next = allocate_board(size);
    
    read_file(f, prev, size);

    fclose(f);

#ifdef DEBUG
    printf("Initial:\n");
    print_board(prev, size);
    print_stats(stats_total);
#endif
    
    // Verificando se o número de threads é divisível pelo tamanho do tabuleiro
    int size_total = size*size;
    int resto = size_total % n_threads;
    int start_prev = 0;
    int end_prev = 0;

    // Inicializando uma barreira
    pthread_barrier_init(&barrier_steps, NULL, n_threads);
    pthread_barrier_init(&barrier_board, NULL, n_threads);
    
    // Loop de criação dos argumentos das threads
    for (int i = 0; i < n_threads; i++) {
        args_vector[i].size = size;
        args_vector[i].steps = steps;

        // Inicializa as estatísticas em 0
        args_vector[i].stats.borns = 0;
        args_vector[i].stats.overcrowding = 0;
        args_vector[i].stats.loneliness = 0;
        args_vector[i].stats.survivals = 0;

        args_vector[i].next = (&next);
        args_vector[i].prev = (&prev);

        // Utilizado para identificar as threads, e também para garantir que apenas uma thread
        // mude o tabuleiro
        args_vector[i].id = i;

        // Separa as regiões
        end_prev += size_total/n_threads;
        args_vector[i].start = start_prev;

        // Se o resto for maior que zero, adiciona mais uma célula para cada thread
        if (i < resto) {
            end_prev += 1;
        }

        args_vector[i].end = end_prev;
        start_prev = end_prev;
    }

    // Loop de criação das threads
    for (int i = 0; i < n_threads; i++) {
        pthread_create(&threads_vector[i], NULL, play, &args_vector[i]);
    }

    // Loop de espera das threads
    for (int i = 0; i < n_threads; i++) {
        pthread_join(threads_vector[i], NULL);
    }

    // Destroi as barreiras
    pthread_barrier_destroy(&barrier_steps);
    pthread_barrier_destroy(&barrier_board);

    // Imprime os stats finais
    for (int i = 0; i < n_threads; i++) {
        stats_total.borns += args_vector[i].stats.borns;
        stats_total.overcrowding += args_vector[i].stats.overcrowding;
        stats_total.loneliness += args_vector[i].stats.loneliness;
        stats_total.survivals += args_vector[i].stats.survivals;
    }

#ifdef RESULT
    printf("Final:\n");
    print_board(prev, size);
    print_stats(stats_total);
#endif

    free_board(prev, size);
    free_board(next, size);
}
