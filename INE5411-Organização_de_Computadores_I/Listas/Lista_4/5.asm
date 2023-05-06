.data
	texto:		.asciiz "Digite o numero a ser fatorado: "
	texto_resultado:	.asciiz "Resultado: "
	numero:		.word	0
	resultado:	.word	0
.text
MAIN:
	la	$s0, numero
	la	$s1, resultado
	
	li	$v0, 4
	la	$a0, texto
	syscall
	li	$v0, 5
	syscall
	move	$a0, $v0
	sw	$a0, ($s0)
	
	jal	FATORIAL
	
	sw	$v0, ($s1)
	
	li	$v0, 4
	la	$a0, texto_resultado
	syscall
	
	li	$v0, 1
	lw	$a0, ($s1)	
	syscall
	
	li	$v0, 10
	syscall
	
FATORIAL:
	sub	$sp, $sp, 8
	sw	$ra, 4($sp)
	sw	$a0, 0($sp)
	
	slti	$t0, $a0, 1
	beq	$t0, $zero, ELSE
	
	li	$v0, 1
	add	$sp, $sp, 8
	jr	$ra
	
	
ELSE:
	sub	$a0, $a0, 1
	jal	FATORIAL
	
	lw	$ra, 4($sp)
	lw	$a0, 0($sp)
	
	add	$sp, $sp, 8
	
	mul	$v0, $a0, $v0
	
	jr	$ra