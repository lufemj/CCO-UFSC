.data
	var:	.word 1
	max:	.word 5
.text
MAIN:
	lw	$s0, var
	lw	$s1, max

	addi	$t0, $zero, 0
	
	j	LOOP
	
LOOP:
	add	$t0, $t0, $s0
	add	$t1, $t1, $t0
	beq	$t0, $s1, FIM
	j	LOOP

FIM:
	add	$s2, $t1, $zero

	li	$v0, 10	
	syscall


