-- Alunos: Luis Fernando Mendonça Junior e Isaque Floriano Beirith

-- Comandos para execução
-- ghc main.hs
-- ./main

import Data.List

------------------------------------------------------------------
-- Matriz

-- Definição de tipos

-- Tipo para representar os valores nas células do tabuleiro
type Valor = Int
-- Tipo para representar uma linha da matriz
type Linha i = [i]
-- Tipo para representar a matriz do tabuleiro
type Matriz a = [Linha a]
-- Tipo para representar o tabuleiro do Kojun
type Tabuleiro = Matriz Valor

-- Retorno de informações da matriz
-- Retorna as linhas da matriz
linhas :: Matriz m -> [Linha m]
linhas i = i
-- Retorna as colunas da matriz
colunas :: Matriz m -> [Linha m]
colunas j = transpose j
-- Retorna a dimensão da matriz
dimensao :: Matriz m -> Int
dimensao d = length (d !! 0)

-- Divide a matriz com valores de acordo com a matriz de grupos
gruposMatriz :: Eq m => Matriz m -> Tabuleiro -> [Linha m]
gruposMatriz valores grupos = [grupoFiltro grupo valoresTupla | grupo <- gruposMapa]
    where
        -- Combina os valores da matriz original e a matriz de grupos em tuplas
        valoresTupla = foldl1 (++) (zipWith zip valores grupos)
        -- Obtém os grupos únicos da matriz de grupos
        gruposMapa = nub (map snd valoresTupla)
        -- Filtra os valores da matriz original com base nos grupos
        grupoFiltro grupo list = map fst $ filter ((== grupo) . snd) list

-- Obtém o tamanho de um grupo pela quantidade de elementos em um grupo
tamanhoGrupo :: Eq m => m -> Matriz m -> Int
tamanhoGrupo _ [] = 0
tamanhoGrupo id grupos = sum [count id p | p <- grupos]
    where count x xs = length (filter (== x) xs)

-- Obtém a lista de valores de um grupo
valorGrupo :: Eq m => Matriz m -> Tabuleiro -> Int -> [m]
valorGrupo valores grupos id = map fst $ filter ((== id) . snd) tuplaValores
    where
        -- Combina os valores da matriz original e a matriz de grupos em tuplas
        tuplaValores = foldl1 (++) (zipWith zip valores grupos)

-- Usa os grupos criados para delimitar as colunas da matriz
grupoColunas :: Eq m => Matriz m -> Tabuleiro -> [Linha m]
grupoColunas valores grupos = zipWith zip (colunas valores) (colunas grupos) >>= map (map fst) . groupBy (\m b -> snd m == snd b)

-- Forma as colunas de origem de acordo com as divididas por blocos
origemColunas :: [Linha l] -> Int -> [Linha l]
origemColunas bs n = dividirLista n (concat bs)

-- Divide uma lista em outras pequenas listas
dividirLista :: Int -> [l] -> [[l]]
dividirLista n = takeWhile (not . null) . map (take n) . iterate (drop n)

------------------------------------------------------------------
-- Kojun

-- Definição de tipos
-- Tipo para representar as escolhas possíveis para cada espaço no tabuleiro
type Escolhas = [Valor]

-- Adquire a primeira solução para o tabuleiro
solucao :: Tabuleiro -> Tabuleiro -> Tabuleiro
solucao valores grupos = head (buscaSolucao (reduzirEscolhas (escolhas valores grupos) grupos) grupos)

-- Define as escolhas possíveis para cada espaço no tabuleiro
escolhas :: Tabuleiro -> Tabuleiro -> Matriz Escolhas
escolhas valores grupos = map (map choice) (zipWith zip valores grupos)
    where
        -- Se o valor for 0, as escolhas são os números não presentes no grupo; caso contrário, a escolha é o próprio valor
        choice (v, p) = if v == 0 then [1..(tamanhoGrupo p grupos)] `minus` (valorGrupo valores grupos p) else [v]

-- Define o valor para um espaço onde há somente uma solução possível
reduzirEscolhasLista :: Linha Escolhas -> Linha Escolhas
reduzirEscolhasLista xss = [xs `minus` singles | xs <- xss]
    where
        -- Remove valores já escolhidos nas células que têm uma única escolha possível
        singles = concat (filter elementoUnico xss)

-- Com as colunas divididas em grupos, reduz o número de escolhas dentro de cada lista
reduzirEscolhas :: Matriz Escolhas -> Tabuleiro -> Matriz Escolhas
reduzirEscolhas valores grupos = colunas $ origemColunas (map reduzirEscolhasLista (grupoColunas valores grupos)) (dimensao valores)

-- Verifica se não há mais de um elemento em uma lista
elementoUnico :: [a] -> Bool
elementoUnico [_] = True
elementoUnico _ = False

-- Subtrai os elementos de uma lista por outra lista
minus :: Escolhas -> Escolhas -> Escolhas
xs `minus` ys = if elementoUnico xs then xs else xs \\ ys

-- Faz a busca de todas as soluções possíveis por casa, informando se o tabuleiro possui soluções ou não e se é necessário expandir a busca
buscaSolucao :: Matriz Escolhas -> Tabuleiro -> [Tabuleiro]
buscaSolucao valores grupos
    | semSolucao valores grupos = []  -- Retorna uma lista vazia se não houver solução possível
    | all (all elementoUnico) valores = [map concat valores]  -- Retorna a solução se todas as células têm escolhas únicas
    | otherwise = [g | valores' <- expandirBusca valores, g <- buscaSolucao (reduzirEscolhas valores' grupos) grupos]

-- Define se é impossível uma solução para o tabuleiro
semSolucao :: Matriz Escolhas -> Tabuleiro -> Bool
semSolucao valores grupos = nula valores || not (valida valores grupos)
    
-- Verifica se há casas vazias na matriz do tabuleiro
nula :: Matriz Escolhas -> Bool
nula m = any (any null) m
    
-- Define se a matriz é válida
valida :: Matriz Escolhas -> Tabuleiro -> Bool
valida valores grupos = all adjacenteValido (colunas valores) &&
                        all adjacenteValido (linhas valores) &&
                        all linhaValida (gruposMatriz valores grupos) &&
                        all linhaDecrescente (grupoColunas valores grupos)

-- Verifica se casas adjacentes não possuem o mesmo valor
adjacenteValido :: Eq a => Linha [a] -> Bool
adjacenteValido [] = True
adjacenteValido [a] = True
adjacenteValido (a:b:bs) 
    | (length a  <= 1) && (length b <= 1) = if a == b then False else adjacenteValido (b:bs) 
    | otherwise = adjacenteValido (b:bs)

-- Verifica se não há valores repetidos em uma linha
linhaValida :: Eq a => Linha [a] -> Bool
linhaValida [] = True
linhaValida (x:xs) = if (length x <= 1) then not (elem x xs) && linhaValida xs else linhaValida xs

-- Verifica se a linha está em ordem decrescente
linhaDecrescente :: Ord a => Linha [a] -> Bool
linhaDecrescente [] = True
linhaDecrescente [a] = True
linhaDecrescente (a:b:bs) 
    | (length a <= 1) && (length b <= 1) = if a < b then False else linhaDecrescente (b:bs)
    | otherwise = linhaDecrescente (b:bs)

-- Expande as escolhas para as casas do tabuleiro
expandirBusca :: Matriz Escolhas -> [Matriz Escolhas]
expandirBusca m = [rows1 ++ [row1 ++ [c] : row2] ++ rows2 | c <- cs]
    where
        (rows1,row:rows2) = break (any (not . elementoUnico)) m
        (row1,cs:row2) = break (not . elementoUnico) row

------------------------------------------------------------------
-- Tabuleiros:

-- Tabuleiro 6x6 - https://www.janko.at/Raetsel/Kojun/001.a.htm
valores6x6 :: Tabuleiro
valores6x6 = [[2,0,0,0,1,0],
             [0,0,0,3,0,0],
             [0,3,0,0,5,3],
             [0,0,0,0,0,0],
             [0,0,3,0,4,2],
             [0,0,0,0,0,0]]
-- Grupos do Tabuleiro 6x6
grupos6x6 :: Tabuleiro
grupos6x6 = [[1,1,2,2,2,3],
            [4,4,4,4,4,3],
            [5,6,6,6,4,7],
            [5,5,5,6,7,7],
            [8,8,10,0,0,0],
            [9,9,10,10,0,0]]

-- Tabuleiro 8x8 - https://www.janko.at/Raetsel/Kojun/004.a.htm
valores8x8 :: Tabuleiro
valores8x8 = [[2,5,0,0,3,0,0,0],
             [0,0,6,0,0,0,0,0],
             [0,0,5,0,5,2,0,0],
             [0,0,0,2,0,0,0,0],
             [0,0,1,0,4,0,0,0],
             [3,0,2,0,0,4,0,0],
             [0,0,0,6,0,0,0,0],
             [0,0,0,0,4,0,3,2]]
-- Grupos do Tabuleiro 8x8
grupos8x8 :: Tabuleiro
grupos8x8 = [[0,1,1,1,1,2,3,3],
            [0,0,5,1,2,2,4,4],
            [6,7,5,8,2,2,9,9],
            [6,10,5,5,5,2,9,9],
            [6,10,5,11,11,11,9,12],
            [13,10,14,11,14,14,12,12],
            [13,13,14,14,14,15,15,12],
            [13,13,16,16,15,15,15,12]]

-- Tabuleiro 10x10 - https://www.janko.at/Raetsel/Kojun/010.a.htm
valores10x10 :: Tabuleiro
valores10x10 = [[5,0,2,0,2,0,3,1,3,1],
               [0,4,0,1,0,5,0,5,0,4],
               [7,5,1,7,0,0,3,1,3,0],
               [0,4,0,0,0,0,0,0,0,3],
               [2,0,3,4,0,2,0,0,4,0],
               [5,0,2,0,6,0,0,0,0,0],
               [0,1,3,0,1,0,0,4,0,3],
               [6,7,0,3,0,1,4,0,0,1],
               [4,0,3,0,4,0,0,0,0,3],
               [0,1,0,2,0,6,2,0,2,1]]
grupos10x10 :: Tabuleiro
grupos10x10 = [[1,2,2,2,3,3,3,3,4,4],
              [1,1,1,2,6,6,7,7,4,7],
              [5,5,1,6,6,9,8,7,7,7],
              [5,5,6,6,10,9,8,8,8,11],
              [5,5,5,6,10,10,11,11,11,11],
              [12,12,15,15,15,10,22,22,21,21],
              [12,12,12,15,15,16,17,18,21,21],
              [13,13,12,15,16,16,17,18,20,20],
              [13,13,14,14,14,14,17,18,18,19],
              [13,13,13,14,14,14,17,17,19,19]]

-- Tabuleiro 12x12 - https://www.janko.at/Raetsel/Kojun/019.a.htm
valores12x12 :: Tabuleiro
valores12x12 = [[2,0,6,3,5,4,0,0,3,0,0,2],
               [0,4,0,0,0,0,0,0,0,0,3,0],
               [0,1,0,4,2,3,0,4,0,0,1,0],
               [0,0,6,0,7,0,7,0,2,7,0,0],
               [0,2,0,0,0,2,5,4,0,0,0,0],
               [0,0,0,0,3,0,0,1,3,0,0,0],
               [4,2,0,6,5,0,5,0,0,2,0,0],
               [7,6,0,4,0,2,0,3,7,6,5,0],
               [0,0,0,0,0,0,0,4,0,0,0,0],
               [0,0,0,7,4,3,0,6,0,0,3,0],
               [0,0,3,0,0,5,0,0,0,0,0,0],
               [0,0,0,2,4,0,1,0,0,4,1,0]]
-- Grupos do Tabuleiro 12x12
grupos12x12 :: Tabuleiro
grupos12x12 = [[0,0,0,0,1,1,1,2,2,2,3,3],
               [0,0,0,1,1,4,5,5,6,7,7,8],
               [9,9,9,10,1,5,5,5,6,7,7,8],
               [9,11,10,10,10,10,12,13,13,14,14,8],
               [9,11,15,10,16,16,12,12,12,17,14,8],
               [11,11,18,10,16,16,12,12,12,17,14,19],
               [11,18,18,18,20,20,21,21,14,14,14,19],
               [22,22,22,18,20,20,21,21,21,21,23,23],
               [22,22,22,18,20,24,25,25,25,21,23,23],
               [26,27,22,24,24,24,24,24,25,25,23,28],
               [26,26,29,29,29,29,29,24,30,31,31,28],
               [26,32,32,33,33,33,33,30,30,30,31,31]]
------------------------------------------------------------------


main = do

-- Definir valores para o tabuleiro
-- Valores possíveis: 6x6, 8x8, 10x10, 12x12
    let valores = valores6x6
    let grupos = grupos6x6

    putStrLn "Resolução do tabuleiro:"
    mapM_ print (solucao valores grupos)
    putStr("\n\n")