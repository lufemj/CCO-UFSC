#Aluno: Luis Fernando Mendonça Junior	Matricula: 22103512
#Aluno: Isaque Floriano Beirith		Matricula: 22100624
#Atividade 2	Exercício 1

.data
A:
	.word 1, 2, 3			#Matriz A
	.word 0, 1, 4
	.word 0, 0, 1
	  
B:
	.word 1, -2, 5			#Matriz B
	.word 0, 1, -4
	.word 0, 0, 1

AB:
	.word 0, 0, 0			#Matriz Resultante (Produto de A.B)
	.word 0, 0, 0
	.word 0, 0, 0

.text
MAIN:
	la	$s0, A			#Carrega o endereço da matriz A
	la	$s1, B			#Carrega o endereço da matriz B
	la	$s2, AB			#Carrega o endereço da matriz Resultante
	
	li	$s3, 0			#Armazena a quantidade de elementos armazenados por linha 
	li	$s4, 0			#Armazena a quantidade de elementos que foram armazenados na matriz
	
LOOP:
	lw	$t0, ($s0) 		#
	lw	$t1, 4($s0)		#Carrega cada valor da linha de A
	lw	$t2, 8($s0)		#
	
	lw	$t3, ($s1)		#
	lw	$t4, 12($s1)		#Carrega cada valor da coluna de B
	lw	$t5, 24($s1)		#
	
	mul	$t6, $t0, $t3		#Multiplica o primeiro valor da linha pelo primeiro valor da coluna e armazena o valor em $t6
	mul	$t7, $t1, $t4		#Multiplica o segundo valor da linha pelo segundo valor da coluna e armazena o valor em $t7
	add	$t6, $t6, $t7		#Soma o resultado das duas operações e armazena o valor em $t6
	mul	$t7, $t2, $t5		#Multiplica o terceiro valor da linha pelo terceiro valor da coluna e armazena o valor em $t7
	add	$t6, $t6, $t7		##Soma o resultado das operação anterior com o resultado antigo e armazena o valor em $t6

	sw	$t6, ($s2)		#Armazenao valor salvo em $t6 na matriz AB
	addi	$s2, $s2, 4		#Adiciona 4 ao endereço de AB, para armazenar o próximo valor no loop em seu respectivo lugar da matriz
	
	addi	$s1, $s1, 4		#Adiciona 4 ao endereço de B, para que no proximo loop sejam carregados os valores da próxima coluna
	addi	$s3, $s3, 1		#Adiciona 1 ao valor de elementos armazenados na linha
	beq 	$s3, 3, RESET		#Se o número de valores armazenados na linha for igual a 3, vai para a função RESET
	j	LOOP			#Volta ao loop para calcular os próximos valores da matriz
	
RESET:
	addi	$s4, $s4, 3		#Adiciona 3 ao valor de elementos armazenados na matriz
	beq	$s4, 9, END		#Se o número de valores armazenados na matriz for igual a 9, vai para a função END
	li	$s3, 0			#Reseta o valor de elementos armazenados na linha de volta para 0
	addi	$s0, $s0, 12		#Adiciona 12 ao endereço de A, para que no próximo loop sejam carregados os valores da próxima linha
	la	$s1, B			#ACarrega cada novamente o endereço original de B para realizar novamente as operações
	j	LOOP			#Volta ao loop para calcular os próximos valores da matriz
	
END:
	li $v0, 10 			#Chamada do sistema para sair
	syscall
