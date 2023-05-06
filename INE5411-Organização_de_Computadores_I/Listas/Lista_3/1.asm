.data
	A: .word 10
	B: .word 15
	C: .word 20
	D: .word 25
	E: .word 30
	F: .word 35
	G: 
		.align 2
		.space 12
	H:
		.align 2
		.space 12

.text
MAIN:
	lw $s0, A
	lw $s1, B
	lw $s2, C
	lw $s3, D
	lw $s4, E
	lw $s5, F
	la $s6, G
	la $s7, H
		
	#a)
	add	$t0, $s1, $s2
	sub	$t1, $s0, $t0
	add	$t0, $t1, $s5
	sw	$t0, 0($s6)
	
	#b)
	sub	$t0, $s0, $s1
	sub	$t1, $s4, $t0
	sub	$t0, $s1, $s2
	mul	$t2, $t0, $t1
	sw	$t2, 4($s6)
	
	#c)
	lw	$t0, 4($s6)
	sub	$t1, $t0, $s2
	sw	$t1, 8($s6)
	
	#d)
	lw	$t0, 8($s6)
	lw	$t1, 0($s6)
	add	$t1, $t0, $t1
	sw	$t1, 12($s6)
	
	#e)
	sub	$t0, $s1, $s2
	sw	$t0, 0($s7)
	
	#f)
	add	$t0, $s0, $s2
	sw	$t0, 4($s7)
	
	#g)
	lw	$t0, 12($s6)
	sub	$t1, $s1, $s2
	add	$t2, $t0, $t1
	sw	$t2, 8($s7)
	
	#h)
	lw	$t0, 0($s6)
	sub	$t1, $s1, $t0
	add	$t0, $t1,  $s3
	sw	$t0, 12($s6)
		
	li	$v0, 10	
	syscall
	
	
	
	
	
	