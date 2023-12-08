/* Alunos: Luis Fernando Mendonça Junior e Isaque Floriano Beirith */

/* Comandos para execução */
/* swipl main.pl */
/* set_prolog_flag(answer_write_options, [max_depth(0)]), solution(Result) */

:- use_module(library(clpfd)).

/* Define um tabuleiro em uma matriz, onde o primeiro
elemento é a região  e o segundo elemento é o número */
board([[[1,2],[1,_],[2,_],[2,_],[2,1],[3,_]],
            [[4,_],[4,_],[4,_],[4 ,3],[4,_],[3,_]],
            [[5,_],[6,3],[6,_],[6,_],[4,5],[7,3]],
            [[5,_],[5,_],[5,_],[6,_],[7,_],[7,_]],
            [[8,_],[8,_],[10,3],[0,_],[0,4],[0,2]],
            [[9,_],[9,_],[10,_],[10,_],[0,_],[0,_]]]).

/* Define a quantidade de células que cada região deve conter */
region_size(0,5).
region_size(1,2).
region_size(2,3).
region_size(3,2).
region_size(4,6).
region_size(5,4).
region_size(6,4).
region_size(7,3).
region_size(8,2).
region_size(9,2).
region_size(10,3).

/* Lógica principal da solução */
solver(Puzzle) :-
    append(Puzzle, List),
    maplist(max_region_value, List),
    maplist(different_neighbors, Puzzle),
    transpose(Puzzle, Columns),
    maplist(different_neighbors,Columns),
    maplist(superior_greater, Columns),
    group_elements(0, List, Group0),
    group_elements(1, List, Group1),
    group_elements(2, List, Group2),
    group_elements(3, List, Group3),
    group_elements(4, List, Group4),
    group_elements(5, List, Group5),
    group_elements(6, List, Group6),
    group_elements(7, List, Group7),
    group_elements(8, List, Group8),
    group_elements(9, List, Group9),
    group_elements(10, List, Group10),
    Groups = [Group0, Group1, Group2, Group3, Group4, Group5, 
              Group6, Group7, Group8, Group9, Group10], 
    all_different_regions(Groups), !.


/* Restringe os valores possíveis de cada cregião */
max_region_value([R,X]) :- region_size(R,T), X in 1..T.

/* Garante que os vizinhos à direita são diferentes.*/
different_neighbors([[_,_]]).
different_neighbors([[_,X1],[R2,X2]|T]) :-
    X1 #\= X2, append([[R2,X2]],T,L), different_neighbors(L).

/* Garante que o valor acima é maior quando fazem parte do mesmo grupo */
superior_greater([[_,_]]).
superior_greater([[R1,X1],[R2,X2]|T]) :-
    ((R1 #\= R2);
    (X1 #> X2)), append([[R2,X2]],T,L), superior_greater(L).

/* Agrupa os elementos que pertencem ao mesmo grupo */
group_elements(_, [], []).
group_elements(R, [[R1, X1] | T], [X1 | L]) :- R #= R1, group_elements(R, T, L).
group_elements(R, [[R1, _] | T], L) :- R #\= R1, group_elements(R, T, L).

/* Verifica se todos os membros de uma região são distintos*/
all_different_regions([H]) :-
    all_distinct(H).
all_different_regions([H|T]) :-
    all_distinct(H),
    all_different_regions(T).

/* Chama a solução e recebe resposta */
solution(BoardResult) :-
    board(BoardProblem), 
    solver(BoardProblem),
    extract_second_values(BoardProblem, BoardResult).

/* Adquire a lista de cada linha da matriz */
extract_second_values([], []).
extract_second_values([Sublist | Rest], [SecondValues | Result]) :-
    extract_second(Sublist, SecondValues),
    extract_second_values(Rest, Result).

/* Adquire o segundo elemento de cada lista adquirida */
extract_second([], []).
extract_second([[_, Second] | Rest], [Second | SecondValues]) :-
    extract_second(Rest, SecondValues).


% set_prolog_flag(answer_write_options, [max_depth(0)]), solution(Result).
