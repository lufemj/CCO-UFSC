object KojunSolver extends App {

  // Definição de tipos
  type Valor = Int
  type Linha[A] = List[A]
  type Matriz[A] = List[Linha[A]]
  type Tabuleiro = Matriz[Valor]
  type Escolhas = List[Valor]

  // Retorno de informações da matriz
  def linhas[A](matriz: Matriz[A]): List[Linha[A]] = matriz
  def colunas[A](matriz: Matriz[A]): List[Linha[A]] = matriz.transpose
  def dimensao[A](matriz: Matriz[A]): Int = matriz.headOption.map(_.length).getOrElse(0)

  // Função grupoFiltro
  def grupoFiltro[A](grupo: A, list: List[(A, A)]): Linha[A] =
    list.collect { case (valor, `grupo`) => valor }

  // Correção na função gruposMatriz
  def gruposMatriz(valores: Matriz[Valor], grupos: Tabuleiro): List[Linha[Valor]] = {
    val valoresTupla: List[(Valor, Valor)] = valores.flatten.zip(grupos.flatten)
    val gruposMapa: List[Valor] = valoresTupla.map(_._2).distinct

    gruposMapa.map(grupo => grupoFiltro(grupo, valoresTupla))
  }

  // Obtém o tamanho de um grupo pela quantidade de elementos em um grupo
  def tamanhoGrupo[A](id: A, grupos: Matriz[A]): Int =
    grupos.flatten.count(_ == id)

  // Obtém a lista de valores de um grupo
  def valorGrupo[A](valores: Matriz[A], grupos: Tabuleiro, id: Int): Linha[A] =
    (valores, grupos).zipped.flatMap((linha, grupo) => linha.zip(grupo)).collect {
      case (valor, `id`) => valor
    }

   // Correção na função grupoColunas
  def grupoColunas(valores: Matriz[Valor], grupos: Tabuleiro): List[Linha[Valor]] =
    colunas(valores).zip(colunas(grupos)).flatMap {
      case (valoresColuna, gruposColuna) => grupoFiltro(gruposColuna.head, valoresColuna)
    }

  // Função singles
  def singles[A](xss: List[Linha[A]]): Linha[A] =
    xss.flatten.distinct

  // Forma as colunas de origem de acordo com as divididas por blocos
  def origemColunas[A](bs: List[Linha[A]], n: Int): List[Linha[A]] =
    dividirLista(n, bs.flatten)

  // Divide uma lista em outras pequenas listas
  def dividirLista[A](n: Int, lista: List[A]): List[List[A]] =
    lista.grouped(n).takeWhile(_.nonEmpty).toList

  // Kojun

  // Adquire a primeira solução para o tabuleiro
  def solucao(valores: Tabuleiro, grupos: Tabuleiro): Tabuleiro =
    buscaSolucao(reduzirEscolhas(escolhas(valores, grupos), grupos), grupos).head

  // Define as escolhas possíveis para cada espaço no tabuleiro
  def escolhas(valores: Tabuleiro, grupos: Tabuleiro): Matriz[Escolhas] =
    valores.zip(grupos).map { case (linhaValores, linhaGrupos) =>
      linhaValores.zip(linhaGrupos).map { case (v, p) =>
        if (v == 0) (1 to tamanhoGrupo(p, grupos)).filterNot(valorGrupo(valores, grupos, p).contains)
        else List(v)
      }
    }

  // Define o valor para um espaço onde há somente uma solução possível
  def reduzirEscolhasLista(xss: Linha[Escolhas]): Linha[Escolhas] =
    xss.map(xs => if (elementoUnico(xs)) xs else xs.diff(singles(xss)))

  // Com as colunas divididas em grupos, reduz o número de escolhas dentro de cada lista
  def reduzirEscolhas(valores: Matriz[Escolhas], grupos: Tabuleiro): Matriz[Escolhas] =
    colunas(origemColunas(grupoColunas(valores, grupos).map(reduzirEscolhasLista), dimensao(valores)))

  // Verifica se não há mais de um elemento em uma lista
  def elementoUnico[A](xs: Linha[A]): Boolean = xs.length == 1

  // Subtrai os elementos de uma lista por outra lista
  def minus(xs: Escolhas, ys: Escolhas): Escolhas =
    if (elementoUnico(xs)) xs else xs.diff(ys)

  // Faz a busca de todas as soluções possíveis por casa, informando se o tabuleiro possui soluções ou não e se é necessário expandir a busca
  def buscaSolucao(valores: Matriz[Escolhas], grupos: Tabuleiro): List[Tabuleiro] =
    if (semSolucao(valores, grupos)) Nil
    else if (valores.flatten.forall(elementoUnico)) List(valores.flatten)
    else expandirBusca(valores).flatMap(solucao(valores12x12, grupos12x12).map(_.mkString(" ")))

  // Define se é impossível uma solução para o tabuleiro
  def semSolucao(valores: Matriz[Escolhas], grupos: Tabuleiro): Boolean =
    nula(valores) || !valida(valores, grupos)

  // Verifica se há casas vazias na matriz do tabuleiro
  def nula[A](matriz: Matriz[A]): Boolean =
    matriz.flatten.contains(null)

  // Define se a matriz é válida
  def valida(valores: Matriz[Escolhas], grupos: Tabuleiro): Boolean =
    colunas(valores).forall(adjacenteValido) &&
      linhas(valores).forall(adjacenteValido) &&
      gruposMatriz(valores, grupos).forall(linhaValida) &&
      grupoColunas(valores, grupos).forall(linhaDecrescente)

  // Verifica se casas adjacentes não possuem o mesmo valor
  def adjacenteValido[A](linha: Linha[Escolhas]): Boolean = linha.sliding(2).forall {
    case List(a, b) => !(elementoUnico(a) && elementoUnico(b) && a.head == b.head)
    case _ => true
  }

  // Verifica se não há valores repetidos em uma linha
  def linhaValida[A](linha: Linha[Escolhas]): Boolean =
    linha.flatten.groupBy(identity).values.forall(_.size == 1)

  // Verifica se a linha está em ordem decrescente
  def linhaDecrescente[A](linha: Linha[Escolhas]): Boolean =
    linha.flatten.sliding(2).forall {
      case List(a, b) => !(elementoUnico(a) && elementoUnico(b) && a.head < b.head)
      case _ => true
    }

  // Expande as escolhas para as casas do tabuleiro
  def expandirBusca[A](matriz: Matriz[Escolhas]): List[Matriz[Escolhas]] =
    matriz.foldRight(List(List.empty[Escolhas])) {
      case (linha, acumulado) =>
        for {
          valoresAnteriores <- acumulado
          c <- linha
        } yield valoresAnteriores :+ c
    }

  // Tabuleiros:

  // Tabuleiro 12x12
  val valores12x12: Tabuleiro = List(
    List(2, 0, 6, 3, 5, 4, 0, 0, 3, 0, 0, 2),
    List(0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0),
    List(0, 1, 0, 4, 2, 3, 0, 4, 0, 0, 1, 0),
    List(0, 0, 6, 0, 7, 0, 7, 0, 2, 7, 0, 0),
    List(0, 2, 0, 0, 0, 2, 5, 4, 0, 0, 0, 0),
    List(0, 0, 0, 0, 3, 0, 0, 1, 3, 0, 0, 0),
    List(4, 2, 0, 6, 5, 0, 5, 0, 0, 2, 0, 0),
    List(7, 6, 0, 4, 0, 2, 0, 3, 7, 6, 5, 0),
    List(0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0),
    List(0, 0, 0, 7, 4, 3, 0, 6, 0, 0, 3, 0),
    List(0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0),
    List(0, 0, 0, 2, 4, 0, 1, 0, 0, 4, 1, 0)
  )
  val grupos12x12: Tabuleiro = List(
    List(0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3),
    List(0, 0, 0, 1, 1, 4, 5, 5, 6, 7, 7, 8),
    List(9, 9, 9, 10, 1, 5, 5, 5, 6, 7, 7, 8),
    List(9, 11, 10, 10, 10, 10, 12, 13, 13, 14, 14, 8),
    List(9, 11, 15, 10, 16, 16, 12, 12, 12, 17, 14, 8),
    List(11, 11, 18, 10, 16, 16, 12, 12, 12, 17, 14, 19),
    List(11, 18, 18, 18, 20, 20, 21, 21, 14, 14, 14, 19),
    List(22, 22, 22, 18, 20, 20, 21, 21, 21, 21, 23, 23),
    List(22, 22, 22, 18, 20, 24, 25, 25, 25, 21, 23, 23),
    List(26, 27, 22, 24, 24, 24, 24, 24, 25, 25, 23, 28),
    List(26, 26, 29, 29, 29, 29, 29, 24, 30, 31, 31, 28),
    List(26, 32, 32, 33, 33, 33, 33, 30, 30, 30, 31, 31)
  )

  // Imprime a resolução do tabuleiro
  println("Resolução do tabuleiro:")
  solucaoFinal.foreach(println)
}
