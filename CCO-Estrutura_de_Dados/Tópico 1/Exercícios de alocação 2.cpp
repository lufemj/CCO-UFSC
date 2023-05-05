// Copyright [2022] <COLOQUE SEU NOME AQUI...>
#include <string>


class Aluno {
 public:
    Aluno() {}  // construtor
    ~Aluno() {}  // destrutor
    std::string devolveNome() {
        return nome;
    }
    int devolveMatricula() {
        return matricula;
    }
    void escreveNome(std::string nome_) {
        nome = nome_;
    }
    void escreveMatricula(int matricula_) {
        matricula = matricula_;
    }
 private:
    std::string nome;
    int matricula;
};


Aluno *turma_filtra(Aluno t[], int N, int menor_matr) {
    Aluno *tf;
    tf = nullptr;  // retirar e alocar (com new)
    return tf;
}

int *turma_conta(Aluno t[], int N) {
    int *c;
    c = nullptr;  // retirar e alocar (com new)
    return c;
}



/*
    *** Importante ***

    A função 'main()' não deve ser escrita aqui, pois é parte do código dos testes e já está implementada

*/
