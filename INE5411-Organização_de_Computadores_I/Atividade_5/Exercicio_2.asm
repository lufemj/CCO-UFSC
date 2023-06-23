#Alunos: Luis Fernando MendonÃ§a Junior	Matricula: 22103512
#	Isaque Floriano Beirith		Matricula: 22100624
#Atividade 5	ExercÃ­cio 2

.data
	.eqv 	MAX 4			#Tamanaho das matrizes
	.eqv 	block_size 4		#Tamanho dos blocos
.text
MAIN:
	li	$t0, MAX		#Carrega o valor do tamanaho das linhas e colunas
	
	mul	$t1, $t0, $t0		#Define o número de elementos das matrizes
	mul	$t1, $t1, 4		#Define o tamanho de 4 bytes para as matrizes
	
	li	$v0, 9			#Código 9 Ã© utilizado para alocar memóira
	move	$a0, $t1		#Passa o tamanho da matriz em bytes
	syscall
	move	$s0, $v0		#Armazena o endereço da matriz A retornado

	li	$v0, 9			#Código 9 utilizado para alocar memóira
	move	$a0, $t1		#Passa o tamanho da matriz em bytes
	syscall
	move	$s1, $v0		#Armazena o endereço da matriz B retornado
	
	li	$t0, 0			#Define o valor de i
	li	$t1, 0			#Define o valor de j
	li	$t2, 0			#Define o valor de ii
	li	$t3, 0			#Define o valor de jj
	
LOOP_I:
	bge	$t0, MAX, END_I		#Se o valor de i for igual ao numero máximo de linhas chama o fim da linha
	li	$t1, 0			#Reseta o valor da coluna

LOOP_J:
	beq	$t1, MAX, END_J		#Se o valor de j for igual ao numero máximo de colunas chama o fim da coluna
	move	$t2, $t0		#Reseta o sub-bloco da linha

LOOP_II:
	add	$t4, $t0, block_size	#Soma o valor da linha com o tamanho do bloco
	bge	$t2, $t4, END_II	#Se o sub-bloco ii for maior que o resultado da soma chama o fim do sub-bloco ii
	move	$t3, $t1		#Reseta o valor do sub-bloco jj
	
LOOP_JJ:
	add	$t5, $t1, block_size	#Soma o valor da coluna com o tamanho do bloco
	bge	$t3, $t5, END_JJ	#Se o sub-bloco jj for maior que o resultado da soma chama o fim do sub-bloco jj
	
	#Deslocamento da matriz A
	mul	$t6, $t2, MAX		#Multiplica o valor do sub-bloco ii pelo tamanho máximo dela
	add	$t6, $t6, $t3		#Adiciona o resultado anterior com o valor do sub-bloco jj
	mul	$t6, $t6, 4		#Multiplica esse valor por 4 para encontrar a posição no endereço
	add 	$t6, $t6,$s0		#Soma a posição encontrada com o endereço da matriz A
	
	#Deslocamento da matriz B
	mul	$t7, $t3, MAX		#Multiplica o valor do sub-bloco jj pelo tamanho máximo dela
	add	$t7, $t7, $t2		#Adiciona o resultado anterior com o valor do sub-bloco ii
	mul	$t7, $t7, 4		#Multiplica esse valor por 4 para encontrar a posição no endereço
	add 	$t7, $t7, $s1		#Soma a posição encontrada com o endereço da matriz B
		
	#Operação e armazenamento
	l.s	$f0, ($t6)		#Carrega o valor da posição atual da matriz A
	l.s	$f1, ($t7)		#Carrega o valor da posição atual da matriz B
	add.s	$f2, $f0, $f1		#Soma esses dois elementos
	s.s	$f2, ($t6)		#Armazena o resultado na matriz A
	
	addi	$t3, $t3, 1		#Soma 1 no valor do sub-bloco jj
	j	LOOP_JJ			#Volta para o loop do sub-bloco jj
	
END_JJ:
	addi	$t2, $t2, 1		#Soma 1 no valor do sub-bloco ii
	j	LOOP_II			#Volta para o loop do sub-bloco ii

END_II:
	addi	$t1, $t1, block_size	#Soma o tamanho do bloco com o valor da coluna
	j	LOOP_J			#Volta para o loop da coluna
	
END_J:
	addi	$t0, $t0, block_size	#Soma o tamanho do bloco com o valor da linha
	j	LOOP_I			#Volta para o loop da linha
	
END_I:
	li $v0, 10 			#Chamada do sistema para sair
	syscall
	