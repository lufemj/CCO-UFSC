def horner(coeficientes, x0):
    n = len(coeficientes) - 1
    y = coeficientes[0]
    z = coeficientes[0]
    for j in range(1, n):
        k = coeficientes[j]
        y = x0 * y + k
        z = x0 * z + y
    y = x0 * y + coeficientes[n]
    return y, z

def newton(coeficientes, x0, iteracoes):
    precicao = 10**-7    
    xn = x0
    for _ in range(iteracoes):
        p_xn, p_0_xn = horner(coeficientes, xn)
        if abs(p_xn) < precicao:
            break
        xn -= p_xn / p_0_xn
    return xn


coeficientes = [2, 0, -3, 3, -4]        # Coeficientes do polinômio p(x) = x^4 + x^3 + x^2 + x + C
x0 = -2                                 # Valor inicial para x0
iteracoes = 10                          #Número de iterações                         


# Encontrando a raiz aproximada
raiz_aproximada = newton(coeficientes, x0, iteracoes)
print("Raiz aproximada:", raiz_aproximada)
