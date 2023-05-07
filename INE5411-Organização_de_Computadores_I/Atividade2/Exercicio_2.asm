#Aluno: Luis Fernando Mendonça Junior	Matricula: 22103512
#Aluno: Isaque Floriano Beirith		Matricula: 22100624
#Atividade 2	Exercício 2

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
	
resultante:	.asciiz "resultante.txt"
		.align 2
matriz:		.asciiz ""
		.align 2

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
	beq	$s4, 9, ESCREVER	#Se o número de valores armazenados na matriz for igual a 9, vai para a função END
	li	$s3, 0			#Reseta o valor de elementos armazenados na linha de volta para 0
	addi	$s0, $s0, 12		#Adiciona 12 ao endereço de A, para que no próximo loop sejam carregados os valores da próxima linha
	la	$s1, B			#ACarrega cada novamente o endereço original de B para realizar novamente as operações
	j	LOOP			#Volta ao loop para calcular os próximos valores da matriz
	
ESCREVER:
	li	$v0, 13			#Comando para ler arquivo
	la	$a0, resultante		#Carrega o endereço do arquivo a ser aberto
	li	$a1, 1			#Carrega a operação de escrita no arquivo aberto
	li	$a2, 0			#Modo ignorado
	syscall
	move	$s6, $v0		#Move o descritor do arquivo no registrador $s6
	
	jal	CONVERSAO		#Chama um procedimento para realizar a manipulação dos dados da matriz 
	
	li	$v0, 15			# Comando para escrever no arquivo
	move	$a0, $s6		# Passa o descritor do arquivo salvo anteriormente
	la	$a1, matriz		# Passa endereço do buffer a ser salvo
	li	$a2, 44			# Delimita tamanho do buffer a ser escrito
	syscall
	
	li	$v0, 16			# Comando para fechar o arquivo.
	move	$a0, $s6		# Passa o descritor do arquivo que será fechado
	syscall
	
END:
	li	$v0, 10 		#Chamada do sistema para sair
	syscall


CONVERSAO:
	addi	$sp, $sp, -12		# Prepara PUSH para salvar dados de a0 e a1 (usados na rotina principal!)
	sw	$ra, 8($sp)		# Salva retorno - Stack Pointer
	sw	$a0, 4($sp)		# Salva $a0
	sw	$a1, 0($sp)		# Salva $a1

	la	$a0, AB			# Atualiza os endereços da matriz resultante AB em $a0
	la	$a1, matriz		#Atualiza os endereços do texto final em $a1
	
	li	$s2, 9			# Limite de iterações a serem feitas para transferir os dados
	li	$s7, 0   		# Será usado para contar laço de loop
	li	$s4, 0  		# Índice da matriz AB começando em i = 0
	li	$s5, 0   		# Índice do texto matriz começando em j = 0

TRANSCRICAO:
	#
	# ----- Nesta sequência vamos tirar um dado de AB[i] -----
	#
	move	$s3, $s4		# Pega índice da matriz AB
	add	$t1, $s3, $s3		# Aponta para o próximo índice (2*i)
	add	$t1, $t1, $t1		# (4*i), sendo que i está armazenado em $s3
	add	$t1, $t1, $a0		# Endereço Base + 4*i --> agora, apontando para o elemento do array
	
	lw	$t0, 0($t1)		# $t0 <-- AB[i].
	addi	$t0, $t0, 48		# Incrementa de 48 para transformar em caractere ASCII.
	addi	$s4, $s4, 1		# Incrementa índice i para a próxima iteração.
	
	#
	# ----- Nesta sequência vamos colocar o dado retirado de AB[i] em matriz[j] -----
	#
	move	$s3, $s5		# Pega índice do texto matriz de destino.
	add	$t1, $s3, $s3		# Aponta para o próximo índice (2*j)
	add	$t1, $t1, $t1		# (4*j), sendo que j está armazenado em $s3
	add	$t1, $t1, $a1		# Endereço Base + 4*i --> agora, apontando para o elemento do array
	
	sw	$t0, 0($t1)		# Armazena conteúdo retirado de AB[i] em matriz[j]
	li	$t0, 32			# Coloca caracter de "espaco em branco" (ASCII) em $t0
	sw	$t0, 4($t1)		# Armazena espeço em branco em matriz[j+1]
	addi	$s5, $s5, 1		# Incrementa índice j para a próxima iteração
	addi	$s7, $s7, 1		# Incrementa laço do loop
	bne	$s2, $s7, TRANSCRICAO
	
	lw	$a1, 0($sp)		# Restaura $a1
	lw	$a0, 4($sp)		# Restaura $a0
	lw	$ra, 8($sp)		# Restaura $ra
	addi	$sp, $sp, 12		# Atualiza $SP (POP de três instruções)
	jr	$ra			# Retorna do procedimento para o programa principal