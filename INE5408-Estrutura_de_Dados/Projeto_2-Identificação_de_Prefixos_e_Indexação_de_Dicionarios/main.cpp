#include <iostream>
#include <fstream>
#include <omp.h>
using namespace std;

NoTrie {
    char           letra;        //opcional
    NoTrie        *filhos[26];   //pode ser uma 'LinkedList' de ponteiros
    unsigned long  posição;
    unsigned long  comprimento;  //se maior que zero, indica último caracter de uma palavra
}


int main() {
    string filename;
    string word;

    cin >> filename;  // entrada

    cout << filename << endl;  // esta linha deve ser removida
    
    while (1) {  // leitura das palavras ate' encontrar "0"
        cin >> word;
        if (word.compare("0") == 0) {
            break;
        }
        cout << word << endl;
    }

    return 0;
}
