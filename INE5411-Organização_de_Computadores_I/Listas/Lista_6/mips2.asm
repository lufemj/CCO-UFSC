# TC/5 = (TF – 32)/9 CONVERTE F PARA C
.data
	texto:	.asciiz "Digite a temperatura em Fahrenheit: "
	result: .asciiz "A temperatura em Celcius e: "
	
	tempF:		.double 0
	tempC:		.double 0
	formula:	.double	32, 9, 5
.text
MAIN:
	la	$s0, tempF
	la	$s1, tempC
	la	$s2, formula
	
	li	$v0,	4
	la	$a0,	texto
	syscall
	li	$v0,	7
	syscall
	
	s.d	$f0, ($s0)
	
	la	$a0, ($s0)
	la	$a1, ($s1)
	la	$a2, ($s2)
	
	jal	CALCULO
	
	li	$v0, 4
	la	$a0, result
	syscall
	li	$v0, 3
	l.d	$f12, ($s1)
	syscall
	
	li	$v0,10
	syscall
	
	
	
CALCULO: # TC/5 = (TF – 32)/9
	l.d	$f2, ($a0)	
	l.d	$f12, ($a2)
	l.d	$f14, 8($a2)
	l.d	$f16, 16($a2)

	sub.d 	$f4, $f2, $f12
	div.d	$f4, $f4, $f14
	mul.d 	$f4, $f4, $f16
	s.d	$f4, ($a1)
	jr	$ra
