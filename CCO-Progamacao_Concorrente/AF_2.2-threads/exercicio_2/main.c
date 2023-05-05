#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <pthread.h>

typedef struct {
    double* a;
    double* b;
    double* c;
    int displacement;
    int loops;
} arguments;

// Lê o conteúdo do arquivo filename e retorna um vetor E o tamanho dele
// Se filename for da forma "gen:%d", gera um vetor aleatório com %d elementos
//
// +-------> retorno da função, ponteiro para vetor malloc()ado e preenchido
// | 
// |         tamanho do vetor (usado <-----+
// |         como 2o retorno)              |
// v                                       v
double* load_vector(const char* filename, int* out_size);


// Avalia o resultado no vetor c. Assume-se que todos os ponteiros (a, b, e c)
// tenham tamanho size.
void avaliar(double* a, double* b, double* c, int size);

void* routine(void* arg) {
    arguments* params = (arguments *) arg;

    for (int j = params->displacement; j < params->displacement + params->loops; j++) 
        params->c[j] = params->a[j] + params->b[j];

    return NULL;
}

int main(int argc, char* argv[]) {
    // Gera um resultado diferente a cada execução do programa
    // Se **para fins de teste** quiser gerar sempre o mesmo valor
    // descomente o srand(0)
    srand(time(NULL)); //valores diferentes
    //srand(0);        //sempre mesmo valor

    //Temos argumentos suficientes?
    if(argc < 4) {
        printf("Uso: %s n_threads a_file b_file\n"
               "    n_threads    número de threads a serem usadas na computação\n"
               "    *_file       caminho de arquivo ou uma expressão com a forma gen:N,\n"
               "                 representando um vetor aleatório de tamanho N\n",
               argv[0]);
        return 1;
    }
  
    //Quantas threads?
    int n_threads = atoi(argv[1]);
    if (!n_threads) {
        printf("Número de threads deve ser > 0\n");
        return 1;
    }
    //Lê números de arquivos para vetores alocados com malloc
    int a_size = 0, b_size = 0;
    double* a = load_vector(argv[2], &a_size);
    if (!a) {
        //load_vector não conseguiu abrir o arquivo
        printf("Erro ao ler arquivo %s\n", argv[2]);
        return 1;
    }
    double* b = load_vector(argv[3], &b_size);
    if (!b) {
        printf("Erro ao ler arquivo %s\n", argv[3]);
        return 1;
    }
    
    //Garante que entradas são compatíveis
    if (a_size != b_size) {
        printf("Vetores a e b tem tamanhos diferentes! (%d != %d)\n", a_size, b_size);
        return 1;
    }
    //Cria vetor do resultado 
    double* c = malloc(a_size*sizeof(double));


    if (n_threads > a_size) 
        n_threads = a_size;

    pthread_t threads[n_threads];
    int resto = a_size % n_threads;

    int deslocamento = 0;

    arguments arg_vector[n_threads];

    for (int i = 0; i < n_threads; i++) {
        arg_vector[i].a = a;
        arg_vector[i].b = b;
        arg_vector[i].c = c;

        if (i <= resto-1) {

            int n_operacoes = a_size/n_threads + 1;

            arg_vector[i].displacement = deslocamento;
            arg_vector[i].loops = n_operacoes;

            pthread_create(&threads[i], NULL, routine, &arg_vector[i]);
            
            deslocamento += n_operacoes;
        } else {
            int n_operacoes = a_size/n_threads;

            arg_vector[i].displacement = deslocamento;
            arg_vector[i].loops = n_operacoes;

            pthread_create(&threads[i], NULL, routine, &arg_vector[i]);
            
            deslocamento += n_operacoes;
        }
    }

    for (int i = 0; i < n_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    //    +---------------------------------+
    // ** | IMPORTANTE: avalia o resultado! | **
    //    +---------------------------------+
    avaliar(a, b, c, a_size);
    

    //Importante: libera memória
    free(a);
    free(b);
    free(c);

    return 0;
}
