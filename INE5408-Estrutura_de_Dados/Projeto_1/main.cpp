#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

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

int** matrizGerador(const std::string& matriz_string, int altura, int largura, bool zero) {
    int** matriz = new int*[altura];
    
    std::string matriz_valores = matriz_string;
    
    matriz_valores.erase(std::remove(matriz_valores.begin(), matriz_valores.end(), '\n'), matriz_valores.end());

    for (int i = 0; i < altura; i++) {
        matriz[i] = new int[largura];
        for (int j = 0; j < largura; j++) {
            char valor = matriz_valores[i * largura + j];
            if (valor == '0' || valor == '1') {
                matriz[i][j] = zero ? 0 : valor - '0';
            }
        }
    }
    return matriz;
}

int operacaoRobo(int** matriz_cenario, int** matriz_zero, int altura, int largura, int robo_x, int robo_y) {
    int casasLimpas = 0;
    
    return casasLimpas;
}

int main() {
    std::ifstream arquivo("cenarios1.xml");
    std::ostringstream ss;
    ss << arquivo.rdbuf();
    std::string file = ss.str();

    /*
    LÓGICA DE VALIDAÇÃO
    */

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
        
        std::string matriz_string = extractDado(file, pos_cenarios[i], "cenario", "matriz"); 
        int **matriz_cenario = matrizGerador(matriz_string, altura, largura, false);
        int **matriz_zero = matrizGerador(matriz_string, altura, largura, true);

        int casasLimpas = operacaoRobo(matriz_cenario, matriz_zero, altura, largura, robo_x, robo_y);

        std::cout << nome << " " << casasLimpas << std::endl;

    }
    return 0;
}
