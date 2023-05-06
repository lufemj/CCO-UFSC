.data
	texto:		.asciiz "Digite uma palavra: "
	input:		.space 8
	num:		.word 0
.text
MAIN:
	la	$s0, input
	la	$s1, num
	
	li	$v0, 4
	la	$a0, texto
	syscall
	
	li	$v0, 8
	la	$a0, input
	li	$a1, 8
	syscall
	
	li	$t0, 7
	li	$t1, 0
	
LOOP:
	lb	$a0, ($s0)
	beq	$a0, $zero, FIM
	beq	$a0, 'a', CONTA
	addi	$s0, $s0, 1
	j	LOOP
	
CONTA:
	addi	$t1, $t1, 1
	addi	$s0, $s0, 1
	j	LOOP
	
FIM:
	sw	$t1, ($s1)
	li	$v0, 1
	lw	$a0, ($s1)
	syscall
	
	li	$v0, 10
	syscall

	