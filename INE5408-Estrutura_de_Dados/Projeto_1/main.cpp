#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include "fila.cpp"
#include "lista.cpp"

struct Coordenadas {
    int x;
    int y;
    
    bool operator==(const Coordenadas& other) const {
        return x == other.x && y == other.y;
    }
};

int operacaoRobo(int** matriz_cenario, int** matriz_zero, int altura, int largura, int robo_x, int robo_y) {
   
    int casasLimpas = 0;
    Coordenadas coord{robo_x, robo_y};
    structures::ArrayQueue<Coordenadas> fila(100);
    structures::ArrayList<Coordenadas> lista(9999);

    // Inicializa o robo na posição correta da matriz de zeros; 
    if (matriz_cenario[robo_x][robo_y] == 1) {
        matriz_zero[robo_x][robo_y] = 1;
    } else {
        matriz_zero[robo_x][robo_y] = 0;
    }
    lista.push_back(coord);
    fila.enqueue(coord);

    while(!fila.empty()) {

        // Tira o valor da primeira coordenada da fila, e atribui a uma variável;
        Coordenadas first = fila.dequeue();

        // Coordenadas dos 4 pontos vizinhos da primeira coordenada da fila;
        Coordenadas coordRight{first.x + 1, first.y};;
        Coordenadas coordLeft{first.x - 1, first.y};
        Coordenadas coordUp{first.x, first.y + 1};
        Coordenadas coordDown{first.x, first.y - 1};

        if (coordRight.x < altura && coordRight.y >= 0 && coordRight.y < largura) {
            if (matriz_cenario[coordRight.x][coordRight.y] == 1 && !lista.contains(coordRight)) {
                matriz_zero[coordRight.x][coordRight.y] = 1;
                lista.push_back(coordRight);
                fila.enqueue(coordRight);
            }
        }

        if (coordLeft.x >= 0 && coordLeft.y >= 0 && coordLeft.y < largura) {
            if (matriz_cenario[coordLeft.x][coordLeft.y] == 1 && !lista.contains(coordLeft)) {
                matriz_zero[coordLeft.x][coordLeft.y] = 1;
                lista.push_back(coordLeft);
                fila.enqueue(coordLeft);
            }
        }

        if (coordUp.x >= 0 && coordUp.x < altura && coordUp.y >= 0) {
            if (matriz_cenario[coordUp.x][coordUp.y] == 1 && !lista.contains(coordUp)) {
                matriz_zero[coordUp.x][coordUp.y] = 1;
                lista.push_back(coordUp);
                fila.enqueue(coordUp);
            }
        }


        if (coordDown.x >= 0 && coordDown.x < altura && coordDown.y >= 0 && coordDown.y < largura) {
            if (matriz_cenario[coordDown.x][coordDown.y] == 1 && !lista.contains(coordDown)) {
                matriz_zero[coordDown.x][coordDown.y] = 1;
                lista.push_back(coordDown);
                fila.enqueue(coordDown);
            }
        }
    }

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (matriz_zero[i][j] == 1) {
                casasLimpas++;
            }
        }
    }

    return casasLimpas;
}

bool validacaoArquivo(const std::string& file) {
    /*
    LÓGICA DE VALIDAÇÃO
    */
   return true;
}

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

int main() {
    std::ifstream arquivo("cenarios1.xml");
    std::ostringstream ss;
    ss << arquivo.rdbuf();
    std::string file = ss.str();

    bool valido = validacaoArquivo(file);

    if (!valido) {
        std::cout << "erro" << std::endl;
        return 1;
    }

    int num_cenarios = 0;
    std::size_t init = 0;
    std::string tag = "<cenario>";
    while ((init = file.find(tag, init)) != std::string::npos) {
        num_cenarios++;
        init += tag.length();
    }

    std::size_t* pos_cenarios = new std::size_t[num_cenarios];

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
