.data
	texto_S:	.asciiz	"Digite o primeiro valor: "
	texto_C:	.asciiz	"Digite o segundo valor: "
	resultado:	.asciiz	"A media entre os valores e: "
	
	S:	.word	0
	C:	.word	0
	M:	.float 0
.text
MAIN:	
	la	$s0, S
	la	$s1, C
	la	$s2, M
	
	li	$v0, 4
	la	$a0, texto_S
	syscall
	li	$v0, 5
	syscall
	sw	$v0, ($s0)
	
	li	$v0, 4
	la	$a0, texto_C
	syscall
	li	$v0, 5
	syscall
	sw	$v0, ($s1)
	
	lw	$t0, ($s0)
	mtc1	$t0, $f2
	lw	$t1, ($s1)
	mtc1 	$t1, $f3
	
	div.s	$f1, $f2, $f3
	s.s	$f1,($s2)
	
	li	$v0, 4
	la	$a0, resultado
	syscall
	li	$v0, 2
	l.s	$f12, ($s2)
	syscall
	
	li	$v0, 10
	syscall
