#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

std::string extractDado(const std::string& file, std::size_t pos_cenario, const std::string& tag, const std::string& var) {
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
    std::ifstream arquivo("cenarios1.xml");
    std::ostringstream ss;
    ss << arquivo.rdbuf();
    std::string file = ss.str();
    int num_cenarios = 0;

    std::size_t init = 0;
    std::string tag = "<cenario>";
    while ((init = file.find(tag, init)) != std::string::npos) {
        num_cenarios++;
        init += tag.length();
    }

    std::size_t* pos_cenarios = new std::size_t[num_cenarios]; // Definir o tamanho do array após contar as ocorrências

    std::size_t aux = 0;
    for (int i = 0; i < num_cenarios; i++) {
        std::size_t startPos = file.find(tag, aux);
        std::size_t endPos = file.find("</cenario>", aux);
        pos_cenarios[i] = startPos;
        aux = endPos + 10;
    }

    for (int i = 0; i < num_cenarios; i++) {
        std::string nome = extractDado(file, pos_cenarios[i], "cenario", "nome");
        int altura = std::stoi(extractDado(file, pos_cenarios[i],"dimensoes", "altura"));
        int largura = std::stoi(extractDado(file, pos_cenarios[i],"dimensoes", "largura"));
        int robo_x = std::stoi(extractDado(file, pos_cenarios[i],"robo", "x"));
        int robo_y = std::stoi(extractDado(file, pos_cenarios[i],"robo", "y"));
        std::cout << nome << std::endl;
        std::cout << altura << std::endl;
        std::cout << largura << std::endl;
        std::cout << robo_x << std::endl;
        std::cout << robo_y << std::endl;
        
        std::cout << "=======================" << std::endl;
    }

    delete[] pos_cenarios;

    return 0;
}
