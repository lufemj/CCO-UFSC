#Alunos: Luis Fernando Mendonça Junior	Matricula: 22103512
#	Isaque Floriano Beirith		Matricula: 22100624
#Atividade 5	Exerc�cio 1

.data
	.eqv 	MAX 4			#Tamanaho das matrizes

.text
MAIN:

	li	$t0, MAX		#Carrega o valor do tamanaho das linhas e colunas
	
	mul	$t1, $t0, $t0		#Define o número de elementos das matrizes
	mul	$t1, $t1, 4		#Define o tamanho de 4 bytes para as matrizes
	
	
	li	$v0, 9			#Código 9 é utilizado para alocar memóira
	move	$a0, $t1		#Passa o tamanho da matriz em bytes
	syscall
	move	$s0, $v0		#Armazena o endereço da matriz A retornado

	li	$v0, 9			#Código 9 é utilizado para alocar memóira
	move	$a0, $t1		#Passa o tamanho da matriz em bytes
	syscall
	move	$s1, $v0		#Armazena o endereço da matriz B retornado
	
	li	$t0, 0			#Define o valor da linha
	li	$t1, 0			#Define o valor da coluna
	
	j	LOOP_COLUNA		#Inicia o Loop
	
LOOP_LINHA:
	addi	$t0, $t0, 1		#Soma 1 no valor da linha
	beq	$t0, MAX, END		#Se finalizar a utlima linha vai para o fim do programa

LOOP_COLUNA:
	beq	$t1, MAX, RESET_COLUNA	#Se finalizar a utlima coluna vai chama a função para resetar o valor
	
	#Deslocamento da matriz A
	mul	$t2, $t0, MAX		#Multiplica o valor da linha pelo tamanho máximo dela
	add	$t2, $t2, $t1		#Adiciona o resultado anterior com o valor da coluna
	mul	$t2, $t2, 4		#Multiplica esse valor por 4 para encontrar a posição no endereço
	add 	$t2, $t2,$s0		#Soma a posição encontrada com o endereço da matriz A
	
	#Deslocamento da matriz B
	mul	$t3, $t1, MAX		#Multiplica o valor da coluna pelo tamanho máximo dela
	add	$t3, $t3, $t0		#Adiciona o resultado anterior com o valor da linha
	mul	$t3, $t3, 4		#Multiplica esse valor por 4 para encontrar a posição no endereço
	add 	$t3, $t3, $s1		#Soma a posição encontrada com o endereço da matriz B
	
	#Opera��o e armazenamento
	l.s	$f0, ($t2)		#Carrega o valor da posição atual da matriz A
	l.s	$f1, ($t3)		#Carrega o valor da posição atual da matriz B
	add.s	$f2, $f0, $f1		#Soma esses dois elementos
	s.s	$f2, ($t2)		#Armazena o resultado na matriz A
	
	addi	$t1, $t1, 1		#Soma 1 no valor da coluna
	j	LOOP_COLUNA		#Volta para o loop da coluna
	
RESET_COLUNA:
	li	$t1, 0			#Reseta o valor da coluna
	j	LOOP_LINHA		#Após resetar o valor da coluna ele chama a função para próxima linha
	
END:
	li $v0, 10 			#Chamada do sistema para sair
	syscall
