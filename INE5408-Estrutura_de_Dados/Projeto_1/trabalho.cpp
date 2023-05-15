#include <iostream>
#include <fstream>
#include <string>
#include <stack>

struct Tag {
    std::string name;
    bool isOpening;

    Tag(const std::string& n, bool opening) : name(n), isOpening(opening) {}
};

bool verificar_aninhamento_fechamento(const std::string& xmlfilename) {
    std::ifstream arquivo(xmlfilename);
    if (!arquivo) {
        std::cout << "Erro ao abrir o arquivo." << std::endl;
        return false;
    }

    std::stack<std::string> pilha;
    std::string linha;

    while (std::getline(arquivo, linha)) {
        std::string tag;
        for (char c : linha) {
            if (c == '<') {
                if (!tag.empty()) {
                    std::cout << "Erro: Caractere '<' inválido." << std::endl;
                    return false;
                }
                tag += c;
            } else if (c == '>') {
                if (tag.empty()) {
                    std::cout << "Erro: Caractere '>' inválido." << std::endl;
                    return false;
                }
                tag += c;

                bool isOpening = (tag[1] != '/');
                std::string tagName = tag.substr(1, tag.length() - 2);

                if (isOpening) {
                    pilha.push(tagName);
                } else {
                    if (pilha.empty()) {
                        std::cout << "Erro: Marcação fechada sem ter sido aberta antes: " << tagName << std::endl;
                        return false;
                    }
                    std::string openingTag = pilha.top();
                    pilha.pop();
                    if (tagName != openingTag) {
                        std::cout << "Erro: Marcação fechada sem ter sido aberta antes: " << tagName << std::endl;
                        return false;
                    }
                }

                tag.clear();
            } else {
                tag += c;
            }
        }
    }

    if (!pilha.empty()) {
        std::cout << "Erro: Marcação aberta sem ter sido fechada: ";
        while (!pilha.empty()) {
            std::cout << pilha.top() << " ";
            pilha.pop();
        }
        std::cout << std::endl;
        return false;
    }

    return true;
}

int main() {
    std::string xmlfilename;
    std::cin >> xmlfilename;

    if (verificar_aninhamento_fechamento(xmlfilename)) {
        std::cout << "Aninhamento e fechamento das marcações estão corretos." << std::endl;
    }

    return 0;
}
