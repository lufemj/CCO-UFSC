.data
	ENTRADA:	.byte 1 2 -2 -3 -4 5
			.align 1
			
.text
main:
	la	$s2, ENTRADA
	lb	$t0, 2($s2)
	lbu	$t1, 5($s2)
loop:
	j	loop
