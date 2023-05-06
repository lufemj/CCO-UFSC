.data
	vetor: .word 1, 3, 2, 1, 4, 5
.text

MAIN:
	la	$s0, 0x10010020


LOOP:
	beq	$t0, 6, FIM
	lw	$t1, ($s1)
	addi	$s1, $s1, 4
	sw	$t1, ($s0)
	addi	$s0, $s0, 4
	add	$t0, $t0, 1
	j	LOOP
	
FIM:
	li	$v0, 10	
	syscall