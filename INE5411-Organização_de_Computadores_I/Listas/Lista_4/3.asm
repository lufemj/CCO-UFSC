.data	
	texto_base:	.asciiz "Digite a base: "
	texto_expoente:	.asciiz "Digite o expoente: "
	
	base:		.word 0
	expoente:	.word 0
	resultado:	.word 0
	
.text
MAIN:
	la	$s0, base
	la	$s1, expoente
	la	$s2, resultado
	
	li	$v0, 4
	la	$a0, texto_base
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s0)

	li	$v0, 4
	la	$a0, texto_expoente
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s1)
	
	lw	$a0, ($s0)
	lw	$a1, ($s1)
	li	$a2, 1
	lw	$a3, ($s0)
	
	jal	POW
	move	$t0, $v0
	sw	$t0, ($s2)
	
	li	$v0, 1
	lw	$a0, ($s2)
	syscall
	
	li	$v0, 10
	syscall
	
POW:
	add	$t1, $a1, $zero 
	mul	$a0, $a3, $a0
	addi	$a2, $a2, 1
	bne	$a2, $a1, POW
	move	$v0, $a0
	jr	$ra
	
	
	