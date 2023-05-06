.data
	text_altura:	.asciiz "Digite a algura: "
	text_largura:	.asciiz "Digite a lagura: "
	
	altura:		.word 0
	largura:	.word 0
	area:		.word 0

.text	
MAIN:
	la	$s0, altura
	la	$s1, largura
	la	$s2, area
	
	li	$v0, 4
	la	$a0, text_altura
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s0)
	
	li	$v0, 4
	la	$a0, text_largura
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s1)
	
	
	lw	$a0, ($s0)
	lw	$a1, ($s1)
	jal	CALCULOAREA
	move	$t0, $v0
	sw	$t0, ($s2)
	
	li	$v0, 1
	lw	$a0, ($s2)
	syscall
	
	li	$v0, 10
	syscall
	
	
CALCULOAREA:
	mul	$v0, $a0, $a1
	jr	$ra