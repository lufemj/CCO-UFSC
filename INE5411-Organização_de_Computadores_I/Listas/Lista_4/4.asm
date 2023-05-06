.data
    n1: .word 0
    n2: .word 0
    str_n1: .asciiz "\nDigite o valor do primeiro numero: "
    str_n2: .asciiz "\nDigite o valor do segundo numero: "
    str_res: .asciiz "\nO resultado da soma e: "
    
.text
leitura:
    # Imprime mensagem para digitar o primeiro numero
    li $v0, 4
    la $a0, str_n1
    syscall
    
    # Lê o primeiro número digitado pelo usuário
    li $v0, 5
    syscall
    sw $v0, n1
    
    # Imprime mensagem para digitar o segundo numero
    li $v0, 4
    la $a0, str_n2
    syscall
    
    # Lê o segundo número digitado pelo usuário
    li $v0, 5
    syscall
    sw $v0, n2
    
    jr $ra

soma:
    # Chama a função leitura para ler os números
    jal leitura
    
    # Carrega os valores lidos
    lw $t0, n1
    lw $t1, n2
    
    # Soma os valores lidos
    add $v0, $t0, $t1
    
    jr $ra

main:
    # Chama a função soma
    jal soma
    
    # Imprime o resultado da soma
    li $v0, 4
    la $a0, str_res
    syscall
    lw $a0, n1
    lw $a1, n2
    jal soma
    move $a0, $v0
    li $v0, 1
    syscall
    
    li $v0, 10
    syscall
