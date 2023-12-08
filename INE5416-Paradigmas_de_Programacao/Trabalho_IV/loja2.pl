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
    aoLado(cliente(_, Otavio, _, _, _, _), cliente(_, _, _, _, hatch, _), ListaSolucao),

    %Quem vai comprar Água está em algum lugar entre o cliente de Vermelho e quem vai comprar Refrigerante, nessa ordem.
    entre(cliente(vermelha, _, _, _, _, _), cliente(_, _, _, agua, _, _), cliente(_, _, _, refrigerante, _, _), ListaSolucao),

    %Na quinta posição está o cliente que está acompanhado do Filho.
    noCanto(cliente(_, _, filho, _, _, _), ListaSolucao),

    %Gilberto está em algum lugar à direita do cliente de camiseta Vermelha.
    aDireita(cliente(vermelha, _, _, _, _, _), cliente(_, Gilberto, _, _, _, _), ListaSolucao),

    %O dono do Hatch está exatamente à esquerda de quem vai comprar um Salgadinho.
    aoLado(cliente(_, _, _, salgadinho, hatch, _), cliente(_, _, _, _, _, _), ListaSolucao),

    %Quem abasteceu 15 l está exatamente à esquerda de quem abasteceu 20 l.
    aEsquerda(cliente(_, _, _, _, _, 15), cliente(_, _, _, _, _, 20), ListaSolucao),

    %O dono do SUV está ao lado do cliente que está acompanhado do Irmão.
    aoLado(cliente(_, _, _, _, SUV, _), cliente(_, _, irmao, _, _, _), ListaSolucao),

    %O cliente que abasteceu 25 l está exatamente à direita do cliente de camiseta Verde.
    aDireita(cliente(verde, _, _, _, _, _), cliente(_, _, _, _, _, 25), ListaSolucao),

    %Pedro está ao lado de quem está acompanhado do Irmão.
    aoLado(cliente(_, Pedro, _, _, _, _), cliente(_, _, irmao, _, _, _), ListaSolucao),

    %O cliente de Azul está exatamente à esquerda de quem vai comprar um Suco.
    aoLado(cliente(azul, _, _, _, _, _), cliente(_, _, _, suco, _, _), ListaSolucao),

    %O dono do Crossover está exatamente à esquerda do cliente que está acompanhado do Tio.
    aoLado(cliente(_, _, _, _, crossover, _), cliente(_, _, tio, _, _, _), ListaSolucao),

    %Fabrício está ao lado de quem está acompanhado do Pai.
    aoLado(cliente(_, fabricio, _, _, _, _), cliente(_, _, pai, _, _, _), ListaSolucao),

    %O cliente que abasteceu 10 l está em algum lugar à direita do cliente de Verde.
    aDireita(cliente(verde, _, _, _, _, _), cliente(_, _, _, _, _, 10), ListaSolucao),

    %O cliente de camiseta Vermelha está em algum lugar entre quem está acompanhado do Avô e o dono da Pickup, nessa ordem.
    entre(cliente(_, _, avo, _, _, _), cliente(vermelha, _, _, _, _, _), cliente(_, _, _, _, pickup, _), ListaSolucao),

    %Na terceira posição está o cliente que abasteceu menos combustível.
    nth0(2, ListaSolucao, cliente(_, _, _, _, _, 5)),

    %O dono do Crossover vai comprar Suco.
    member(cliente(_, _, _, suco, crossover, _), ListaSolucao),

    %Quem está acompanhado do Irmão está exatamente à esquerda do dono da Pickup.
    aoLado(cliente(_, _, irmao, _, _, _), cliente(_, _, _, _, pickup, _), ListaSolucao),

    %Pedro está em algum lugar à direita do cliente de camiseta Branca.
    aDireita(cliente(branca, _, _, _, _, _), cliente(_, Pedro, _, _, _, _), ListaSolucao),

    %O cliente que vai comprar Água está exatamente à direita do dono do Crossover.
    aoLado(cliente(_, _, _, agua, _, _), cliente(_, _, _, _, crossover, _), ListaSolucao),

    %O cliente de camiseta Verde está em algum lugar à esquerda do dono da Pickup.
    aEsquerda(cliente(verde, _, _, _, _, _), cliente(_, _, _, _, pickup, _), ListaSolucao),

    
    % Testa todas as possibilidades...
    camiseta(Camiseta1), camiseta(Camiseta2), camiseta(Camiseta3), camiseta(Camiseta4), camiseta(Camiseta5),
    todosDiferentes([Camiseta1, Camiseta2, Camiseta3, Camiseta4, Camiseta5]),

    nome(Nome1), nome(Nome2), nome(Nome3), nome(Nome4), nome(Nome5),
    todosDiferentes([Nome1, Nome2, Nome3, Nome4, Nome5]),

    companhia(Companhia1), companhia(Companhia2), companhia(Companhia3), companhia(Companhia4), companhia(Companhia5),
    todosDiferentes([Companhia1, Companhia2, Companhia3, Companhia4, Companhia5]),

    compra(Compra1), compra(Compra2), compra(Compra3), compra(Compra4), compra(Compra5),
    todosDiferentes([Compra1, Compra2, Compra3, Compra4, Compra5]),

    carro(Carro1), carro(Carro2), carro(Carro3), carro(Carro4), carro(Carro5),
    todosDiferentes([Carro1, Carro2, Carro3, Carro4, Carro5]),

    combustivel(Combustivel1), combustivel(Combustivel2), combustivel(Combustivel3), combustivel(Combustivel4), combustivel(Combustivel5),
    todosDiferentes([Combustivel1, Combustivel2, Combustivel3, Combustivel4, Combustivel5]).
    
