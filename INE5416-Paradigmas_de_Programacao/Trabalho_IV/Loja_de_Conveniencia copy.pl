camiseta(amarela).
camiseta(azul).
camiseta(branca).
camiseta(verde).
camiseta(vermelha).

nome(Fabricio).
nome(Gilberto).
nome(Otavio).
nome(Pedro).
nome(Tulio).

companhia(avo).
companhia(filho).
companhia(irmao).
companhia(pai).
companhia(tio).

compra(agua).
compra(chiclete).
compra(refrigerante).
compra(salgadinho).
compra(suco).

carro(crossover).
carro(hatch).
carro(pickup).
carro(sedan).
carro(SUV).

combustivel(5L).
combustivel(10L).
combustivel(15L).
combustivel(20L).
combustivel(25L).



%X está à ao lado de Y
aoLado(X,Y,Lista) :- nextto(X,Y,Lista);nextto(Y,X,Lista).
                       
%X está à esquerda de Y (em qualquer posição à esquerda)
aEsquerda(X,Y,Lista) :- nth0(IndexX,Lista,X), 
                        nth0(IndexY,Lista,Y), 
                        IndexX < IndexY.
                        
%X está à direita de Y (em qualquer posição à direita)
aDireita(X,Y,Lista) :- aEsquerda(Y,X,Lista). 

%X está no canto se ele é o primeiro ou o último da lista
noCanto(X,Lista) :- last(Lista,X).
noCanto(X,[X|_]).

todosDiferentes([]).
todosDiferentes([H|T]) :- not(member(H,T)), todosDiferentes(T).

solucao(ListaSolucao) :- 

    ListaSolucao = [
        cliente(Camiseta1, Nome1, Companhia1, Compra1, Carro1, Combustivel1),
        cliente(Camiseta2, Nome2, Companhia2, Compra2, Carro2, Combustivel2),
        cliente(Camiseta3, Nome3, Companhia3, Compra3, Carro3, Combustivel3),
        cliente(Camiseta4, Nome4, Companhia4, Compra4, Carro4, Combustivel4),
        cliente(Camiseta5, Nome5, Companhia5, Compra5, Carro5, Combustivel5),
        
    ],

    %Otávio está ao lado do dono do Hatch.
    aoLado(cliente(_, Otavio, _, _, _, _), cliente(_, _, _, _, Hatch, _), ListaSolucao)

    
    
    %Testa todas as possibilidades...
    nacionalidade(Nacionalidade1), nacionalidade(Nacionalidade2), nacionalidade(Nacionalidade3), nacionalidade(Nacionalidade4), nacionalidade(Nacionalidade5),
    todosDiferentes([Nacionalidade1, Nacionalidade2, Nacionalidade3, Nacionalidade4, Nacionalidade5]),
    
    saida(Saida1), saida(Saida2), saida(Saida3), saida(Saida4), saida(Saida5),
    todosDiferentes([Saida1, Saida2, Saida3, Saida4, Saida5]),
    
    carregamento(Carregamento1), carregamento(Carregamento2), carregamento(Carregamento3), carregamento(Carregamento4), carregamento(Carregamento5),
    todosDiferentes([Carregamento1, Carregamento2, Carregamento3, Carregamento4, Carregamento5]),
    
    chamine(Chamine1), chamine(Chamine2), chamine(Chamine3), chamine(Chamine4), chamine(Chamine5),
    todosDiferentes([Chamine1, Chamine2, Chamine3, Chamine4, Chamine5]),
    
    destino(Destino1), destino(Destino2), destino(Destino3), destino(Destino4), destino(Destino5),
    todosDiferentes([Destino1, Destino2, Destino3, Destino4, Destino5]).
    
    
