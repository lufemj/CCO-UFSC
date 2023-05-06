.data
	input_g: 	.asciiz "Digite o valor de G: "
	input_h: 	.asciiz "Digite o valor de H: "
	input_i: 	.asciiz "Digite o valor de I: "
	input_j: 	.asciiz "Digite o valor de J: "
	
	val_g:	.word 0
	val_h:	.word 0
	val_i:	.word 0
	val_j:	.word 0
	val_f:	.word 0
	
.text
MAIN:
	la	$s0, val_g
	la	$s1, val_h
	la	$s2, val_i
	la	$s3, val_j
	la	$s4, val_f
	
	
	li	$v0, 4
	la	$a0, input_g
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s0)
	
	li	$v0, 4
	la	$a0, input_h
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s1)
	
	li	$v0, 4
	la	$a0, input_i
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s2)

	li	$v0, 4
	la	$a0, input_j
	syscall
	li	$v0, 5
	syscall
	move	$t0, $v0
	sw	$t0, ($s3)
	
	
	lw	$a0, ($s0)
	lw	$a1, ($s1)
	lw	$a2, ($s2)
	lw	$a3, ($s3)
	jal	CALCULO
	move	$t0, $v0
	sw	$t0, ($s4)
	
	li	$v0, 1
	lw	$a0, ($s4)
	syscall
	
	li	$v0, 10
	syscall

CALCULO:
	add	$t0, $a0, $a1
	add	$t1, $a2, $a3
	sub	$v0, $t0, $t1
	jr	$ra
