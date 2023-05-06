.data
	insertA: 	.asciiz "Digite o valor que será atribuido a a: "
	insertB: 	.asciiz "Digite o valor que será atribuido a b: "
	resultado: 	.asciiz "O resultado da operação é: "
	
	a: 	.word 0
	b: 	.word 0
	
.text
MAIN:
	la	$s0, a
	la	$s1, b
	
	li	$v0, 4			# Comando.
	la	$a0, insertA		# Carrega string (valor).
	syscall 
	
	li	$v0, 5	      		# Comando para ler inteiro.
	syscall
	
	move    $t0, $v0         	#Valor é salvo em $t0
	sw 	$t0, ($s0)		#Armazena o resultado em $s1"
	
	li	$v0, 4			# Comando.
	la	$a0, insertB		# Carrega string (valor).
	syscall 
	
	li	$v0, 5	      		# Comando para ler inteiro.
	syscall
	
	move    $t0, $v0         	#Valor é salvo em $t0
	sw 	$t0, ($s1)		#Armazena o resultado em $s1"
	
	
	lw	$t0, ($s0)
	lw	$t1, ($s1)
	
#a	if (a > b)
#	slt	$t2, $t0, $t1
#	beq	$t2, $zero, OPa
#	j	FIM
#OPa:
#	addi	$t0, $t0, 1
#	sw	$t0, ($s0)
#	j	FIM
############################################
	
#b	if (a ≥ b)
#	addi	$t0, $t0, 1
#	slt	$t2, $t0, $t1
#	beq	$t2, $zero, OPb
#	j	FIM
#OPb:
#	addi	$t1, $t1, 1
#	sw	$t1, ($s1)
#	j	FIM
############################################

#c	if (a ≤ b)
#	addi	$t1, $t1, 1
#	slt	$t2, $t1, $t0
#	beq	$t2, $zero, OPc
#OPc:
#	addi	$t0, $t0, 1
#	sw	$t0, ($s0)
#	j	FIM
############################################

#d	 if (a == b)
#	beq	$t0, $t1, OPd
#OPd:
#	sw	$t0, ($s1)
#	j	FIM
############################################

#e	if (a < b)
#	slt	$t2, $t0, $t1
#	beq	$t2, $zero, OPe1
#	li	$t3, 1
#	beq	$t2, $t3, OPe2
#OPe1:
#	addi	$t1, $t1, 1
#	sw	$t1, ($s1)
#	j	FIM
#OPe2:
#	addi	$t0, $t0, 1
#	sw	$t0, ($s0)
#	j	FIM
############################################

#f	while (a < c)
#	li	$t0, 0
#	li	$t1, 0
#	li	$t2, 5
#LOOP:
#	beq	$t0, $t2, FIM
#	addi	$t0, $t0, 1
#	addi	$t1, $t1, 2
#	sw	$t0, ($s0)
#	sw	$t1, ($s1)
#	j	LOOP
############################################

#g	for (i = 0; i < 5; i ++)
#	li	$t0, 1
#	li	$t1, 2
#	li	$t2, 0
#LOOP:
#	beq	$t2, 5, FIM
#	addi	$t0, $t1, 1
#	addi	$t1, $t1, 3
#	sw	$t0, ($s0)
#	sw	$t1, ($s1)
#	addi	$t2, $t2, 1
#	j	LOOP
############################################

#h
#	li	$t2, 4
#	beq	$t0, 1, CASO1
#	beq	$t0, 2, CASO2
#	sw	$t2, ($s1)
#	j	FIM
#CASO1:
#	addi	$t1, $t2, 1
#	sw	$t1, ($s1)
#	j	FIM
#CASO2:
#	addi	$t1, $t2, 2
#	sw	$t1, ($s1)
#	j	FIM
############################################

FIM:
	li	$v0, 10
	syscall
	
	
	
