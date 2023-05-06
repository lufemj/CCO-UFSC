.data
	texto:		.asciiz	"Digite o raio do Circulo: "
	result_t:	.asciiz	"A area do Circulo e: "
	

	pi:		.double	3.141592653589793
	raio:		.double 0 
	resultado:	.double 0 
.text
MAIN:
	la	$s0, pi	
	la	$s1, raio
	la	$s2, resultado
	
	li	$v0, 4
	la	$a0, texto
	syscall
	li	$v0, 7
	syscall
	mov.d	$f14, $f0
	
	s.d	$f14, ($s1)

	la	$a0, ($s0)
	la	$a1, ($s1)
	la	$a2, ($s2)
	jal	CALCULO
	
	li	$v0, 4
	la	$a0, result_t
	syscall
	
	li	$v0, 3
	l.d	$f12, ($s2)
	syscall
	
	li	$v0, 10
	syscall
	
CALCULO:
	l.d	$f2, ($a0)
	l.d	$f4, ($a1)
	mul.d 	$f4, $f4, $f4
	mul.d	$f6, $f4, $f2
	s.d 	$f6, ($a2)
	jr $ra
	
