/*
 * The Game of Life
 *
 * RULES:
 *  1. A cell is born, if it has exactly three neighbours.
 *  2. A cell dies of loneliness, if it has less than two neighbours.
 *  3. A cell dies of overcrowding, if it has more than three neighbours.
 *  4. A cell survives to the next generation, if it does not die of lonelines or overcrowding.
 *
 * In this version, a 2D array of ints is used.  A 1 cell is on, a 0 cell is off.
 * The game plays a number of steps (given by the input), printing to the screen each time.
 * A 'x' printed means on, space means off.
 *
 */

#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include "gol.h"

/* Statistics */
stats_t statistics;

// Barreiras inicilizadas como variáveis globais
extern pthread_barrier_t barrier_steps;
extern pthread_barrier_t barrier_board;

cell_t **allocate_board(int size)
{
    cell_t **board = (cell_t **)malloc(sizeof(cell_t *) * size);
    int i;
    for (i = 0; i < size; i++)
        board[i] = (cell_t *)malloc(sizeof(cell_t) * size);
    
    statistics.borns = 0;
    statistics.survivals = 0;
    statistics.loneliness = 0;
    statistics.overcrowding = 0;

    return board;
}

void free_board(cell_t **board, int size)
{
    int i;
    for (i = 0; i < size; i++)
        free(board[i]);
    free(board);
}

int adjacent_to(cell_t **board, int size, int i, int j)
{
    int k, l, count = 0;

    int sk = (i > 0) ? i - 1 : i;
    int ek = (i + 1 < size) ? i + 1 : i;
    int sl = (j > 0) ? j - 1 : j;
    int el = (j + 1 < size) ? j + 1 : j;

    for (k = sk; k <= ek; k++)
        for (l = sl; l <= el; l++)
            count += board[k][l];
    count -= board[i][j];

    return count;
}

void *play(void *args)
{
    // Converte o ponteiro args para o tipo arguments_t
    arguments_t *p = (arguments_t *) args;

    // Atribui os valores da estrutura a suas variaveis
    int size = p->size;
    int steps = p->steps;
    int start = p->start;
    int end = p->end;
    int id = p->id;

    // Obtém as matrizes de células (tabuleiro) a partir dos campos prev e next
    cell_t ***board = p->prev;
    cell_t ***newboard = p->next;

    // Obtém o ponteiro para a estrutura de estatísticas stats_t
    stats_t *stats = &(p->stats);

    for (int s = 0; s < steps; ++s)
    {
        for (int i = start; i < end; ++i)
        {
            // A divisão inteira de i pelo size da matriz resulta no valor da linha
            // O resto da divisão de i pelo size da matriz resulta no valor da coluna
            int row = i / size; 
            int col = i % size;

            int a = adjacent_to((*board), size, row, col);

            /* if cell is alive */
            if((*board)[row][col]) {
                /* death: loneliness */
                if(a < 2) {
                    (*newboard)[row][col] = 0;
                    stats->loneliness++;
                } else {
                    /* survival */
                    if(a == 2 || a == 3) {
                        (*newboard)[row][col] = (*board)[row][col];
                        stats->survivals++;
                    } else {
                        /* death: overcrowding */
                        if(a > 3) {
                            (*newboard)[row][col] = 0;
                            stats->overcrowding++;
                        }
                    }
                }
            } else { /* if cell is dead */ 
                if(a == 3) { /* new born */
                    (*newboard)[row][col] = 1;
                    stats->borns++;
                } else {
                    (*newboard)[row][col] = (*board)[row][col];
                } /* stay unchanged */
            }
        }

        // Barreira para que as threads esperem que todas terminem
        pthread_barrier_wait(&barrier_steps);

        // Caso seja a primeira thread, o tabuleiro é alterado por ela
        if (id == 0)
        {
            cell_t **tmp = (*board);
            (*board) = (*newboard);
            (*newboard) = tmp;
        }

        // Barreira para que as threads que não sejam a primeira aguardem a operação de troca de tabuleiro
        pthread_barrier_wait(&barrier_board);
    }

    return NULL;
}

void print_board(cell_t **board, int size)
{
    int i, j;
    /* for each row */
    for (j = 0; j < size; j++)
    {
        /* print each column position... */
        for (i = 0; i < size; i++)
            printf("%c", board[i][j] ? 'x' : ' ');
        /* followed by a carriage return */
        printf("\n");
    }
}

void print_stats(stats_t stats)
{
    /* print final statistics */
    printf("Statistics:\n\tBorns..............: %u\n\tSurvivals..........: %u\n\tLoneliness deaths..: %u\n\tOvercrowding deaths: %u\n\n",
        stats.borns, stats.survivals, stats.loneliness, stats.overcrowding);
}

void read_file(FILE *f, cell_t **board, int size)
{
    char *s = (char *) malloc(size + 10);

    /* read the first new line (it will be ignored) */
    fgets(s, size + 10, f);

    /* read the life board */
    for (int j = 0; j < size; j++)
    {
        /* get a string */
        fgets(s, size + 10, f);

        /* copy the string to the life board */
        for (int i = 0; i < size; i++)
            board[i][j] = (s[i] == 'x');
    }

    free(s);
}