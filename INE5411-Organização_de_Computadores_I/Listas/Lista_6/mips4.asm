.data
	textoA: .asciiz "Digite o valor de A: "
	textoB: .asciiz "Digite o valor de B: "
	raizT:	.asciiz "A raiz e: "
	
	A:	.float 0
	B:	.float 0
	X:	.float 0
.text
MAIN:
	la	$s0, A
	la	$s1, B
	la	$s2, X
	
	li	$v0, 4
	la	$a0, textoA
	syscall
	li	$v0, 6
	syscall
	s.s	$f0, ($s0)
	
	li	$v0, 4
	la	$a0, textoB
	syscall
	li	$v0, 6
	syscall
	s.s	$f0, ($s1)
	
	la	$a0, ($s0)
	la	$a1, ($s1)
	la	$a2, ($s2)
	jal	CALCULO
	
	li	$v0, 4
	la	$a0, raizT
	syscall
	li	$v0, 2
	l.s	$f12, ($s2)
	syscall
	
	li	$v0, 10
	syscall
	
CALCULO:
	l.s	$f0,($a0)
	l.s	$f1,($a1)
	add.s	$f3, $f1,$f1
	sub.s	$f4, $f1,$f3
	div.s	$f3, $f4, $f0
	s.s	$f3,($a2)
	jr	$ra
	
	
	
	
	