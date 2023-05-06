.data
	texto1:	.asciiz "Digite 1 ou 0 para ligar ou desligar um byte: "
	texto2:	.asciiz "Digite posicao para alterar um byte: "
	
	byte:		.byte 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
	posicao:	.word 0
	
.text
MAIN:
	la	$s0, 0x10010020
	lb	$s1, byte
	sb	$s1, ($s0)
	la	$s2, posicao
	
	li	$v0, 4
	la	$a0, texto1
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s1)
	
	li	$v0, 4
	la	$a0, texto2
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s2)
	
	add	$t0, $s0, $zero
	lw	$t1, ($s1)
	lw	$t2, ($s2)
	
	add	$t0, $t0, $t2
	sw	$t1, ($t0)
	
	
