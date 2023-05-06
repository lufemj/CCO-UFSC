#Aluno: Luis Fernando Mendonça Junior	Matricula: 22103512
#Atividade 1	Exercício 1

.data
        a: .word 0			#Valor será atribuido
	b: .word 20			#Valor pré-definido
	c: .word 0			#Valor será atribuido
	d: .word 50			#Valor pré-definido
	e: .word 120			#Valor pré-definido
.text
main:
	la	$s0, a			#Carrega valor de "a"
	la	$s1, b			#Carrega valor de "b"
	la	$s2, c			#Carrega valor de "c"
	la	$s3, d			#Carrega valor de "d"
	la	$s4, e			#Carrega valor de "e"

	lw	$t0, 0($s1)		#Armazena o valor de "b" em $t0
	addi 	$t1, $t0, 35		#Soma os valores de $t0 e 35, e armazena o resultado em $t1
	sw 	$t1, 0($s0)		#Armazena o resultado da operação "a" em $s0
	
	lw	$t0, 0($s3)		#Armazena o valor de "d" em $t0
	lw	$t1, 0($s0)		#Armazena o valor de "a" em $t1
	lw	$t2, 0($s4)		#Armazena o valor de "e" em $t2
	sub	$t3, $t0, $t1		#Subtrai os valores de "d" e "a", e armazena o resultado em $t3
	add	$t4, $t3, $t2		#Soma os valores de $t3 e "e", e armazena o resultado em $t4
	sw	$t4, 0($s2)		#Armazena o resultado final da operação "c" em $s2

	li	$v0, 10			#Chamada do sistema para sair
	syscall
