#Alunos: Luis Fernando Mendonça Junior	Matricula: 22103512
#	Isaque Floriano Beirith		Matricula: 22100624
#Atividade 3	Exercício 1

.data
matriz:		.space 256		#Aloca espaço da Matriz na memória
	  

.text
MAIN:
	la	$s0, matriz		#Carrega o endereço da matriz
	li	$s1, 0			#Armazena o valor do elemento a ser armazenado
	li	$t0, 0			#Armazena o valor da linha
	li	$t1, 0			#Armazena o valor da coluna
	
	j	LOOP_COLUNA		#Inicia o Loop
	
LOOP_LINHA:
	addi	$t0, $t0, 1		#Soma 1 no valor da linha
	beq	$t0, 16, END		#Se finalizar a utlima linha vai para o fim do programa

LOOP_COLUNA:
	beq	$t1, 16, RESET_COLUNA	#Se finalizar a utlima coluna vai chama a função para resetar o valor
	
	mul $t3, $t0, 4			#Multiplica o valor da linha por 4 para encontrar a posição correta no endereço
	mul $t4, $t1, 64		#Multiplica o valor da coluna por 64 para encontrar a posição correta no endereço
	add $t3, $t3, $t4		#Soma esse dois valores e armazena o resultado em $t3
	add $t4, $t3, $s0		#Por fim, soma o resultado ao endereço da matriz para obter a posição atual da matriz
	
	sw $s1, 0($t4)			#Armazena o valor atual na posição correta da matriz
	addi $s1, $s1, 1		#Soma mais um no valor a ser armazenado
	
	addi	$t1, $t1, 1		#Soma 1 no valor da coluna
	j	LOOP_COLUNA		#Volta para o loop da coluna
	
RESET_COLUNA:
	li	$t1, 0			#Reseta o valor da coluna
	j	LOOP_LINHA		#Após resetar o valor da coluna ele chama a função para próxima linha
	
END:
	li $v0, 10 			#Chamada do sistema para sair
	syscall
