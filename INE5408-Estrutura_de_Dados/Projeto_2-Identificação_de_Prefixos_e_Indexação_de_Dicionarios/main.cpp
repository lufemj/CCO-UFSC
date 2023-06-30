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



// Função parametrizada que retorna a informação desejada do .xml
void extractDado() {
    std::string dado;
    size_t startPos = file.find("<" + tag + ">", pos_cenario);
    if (startPos != std::string::npos) {
        startPos = file.find("<" + var + ">", startPos);
        if (startPos != std::string::npos) {
            size_t endPos = file.find("</" + var + ">", startPos);
            if (endPos != std::string::npos){
                startPos += var.length() + 2;
                dado = file.substr(startPos, endPos - startPos);
            }
        }
    }
    return dado;
}

int main() {
    string filename;
    string word;

    cin >> filename;  // entrada

    ifstream arquivo(filename);
    ostringstream saved_string;
    saved_string << arquivo.rdbuf();
    file = saved_string.str();

    extractDado(file)
    
    while (1) {  // leitura das palavras ate' encontrar "0"
        cin >> word;
        if (word.compare("0") == 0) {
            break;
        }
        cout << word << endl;
    }

    return 0;
}
