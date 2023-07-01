//Alunos: Luis Fernando Mendonça Junior     22103512
//        Isaque Floriano Beirith           22100624

#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

class TrieNode {
    char letra;        
    TrieNode *filhos[26];
    unsigned long prefixos;
    unsigned long posicao;
    unsigned long comprimento;  


    public: TrieNode(char letra) {
        this->letra = letra;
        for (int i = 0; i < 26; i++) {
            filhos[i] = NULL;
        }
        prefixos = 0;
        posicao = 0;
        comprimento = 0;
    }

    public: void insert_(string palavra, unsigned long posicao, unsigned long comprimento) {
        if (palavra.length() == 0) {
            return;
        }
        char c = palavra[0];
        int i = c - 'a';
        if (filhos[i] == NULL) {
            filhos[i] = new TrieNode(c);
            if (palavra.length() == 1) {
                filhos[i]->posicao = posicao;
                filhos[i]->comprimento = comprimento;
            }
        }
        filhos[i]->insert_(palavra.substr(1), posicao, comprimento);
        filhos[i]->prefixos++;
    }

    public: int contarPrefixos(string palavra) {
        if (palavra.length() == 0) {
            return prefixos;
        }
        char c = palavra[0];
        int i = c - 'a';
        if (filhos[i] == NULL) {
            return 0;
        }
        return filhos[i]->contarPrefixos(palavra.substr(1));
    }

    public: unsigned long retornaPos(string palavra) {
        if (palavra.length() == 0) {
            return posicao;
        }
        char c = palavra[0];
        int i = c - 'a';
        if (filhos[i] == NULL) {
            return 0;
        }
        return filhos[i]->retornaPos(palavra.substr(1));
    }

    public: unsigned long retornaComp(string palavra) {
        if (palavra.length() == 0) {
            return comprimento;
        }
        char c = palavra[0];
        int i = c - 'a';
        if (filhos[i] == NULL) {
            return 0;
        }
        return filhos[i]->retornaComp(palavra.substr(1));
    }

    public: void delete_(){
        for (int i = 0; i < 26; i++) {
            if (filhos[i] != NULL) {
                filhos[i]->delete_();
            }
        }
        delete this;
    }
};

void extractDado(std::string filename, TrieNode* raiz) {
    std::string word;
    std::ifstream arquivo;
    arquivo.open(filename);
    std::string line;
    int Pos = 0;
    while (getline(arquivo, line)) {
        size_t startPos = line.find('[');
        size_t endPos = line.find(']', startPos);
        word = line.substr(startPos + 1, endPos - startPos - 1);
        raiz->insert_(word, Pos, line.length());
        Pos = Pos + line.length() + 1;
    }
    arquivo.close();
}


int main() {
    TrieNode* raiz = new TrieNode(' ');
    std::string filename;
    std::string word;

    std::cin >> filename;  


    extractDado(filename, raiz);

    while (1) { 
        cin >> word;
        if (word.compare("0") == 0) {
            break;
        }
        int prefixos = raiz->contarPrefixos(word);
        unsigned long posicao = raiz->retornaPos(word);
        unsigned long comprimento = raiz->retornaComp(word);
        
        if (!prefixos) {
            cout << word << " is not prefix" << endl;
        } else {
            cout << word << " is prefix of " << prefixos << " words" << endl;
            if (comprimento){
                cout << word << " is at (" << posicao << "," << comprimento << ")" << endl;
            }
        }
    }

    return 0;
}