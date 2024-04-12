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

def newton(coeficientes, x0, itmax):
    tolerancia = 10**-7    
    xn = x0
    for _ in range(itmax):
        p_xn, dp_xn = horner(coeficientes, xn)
        if abs(p_xn) < tolerancia:
            break
        xn -= p_xn / dp_xn
    return xn


if __name__ == "__main__":
    coeficientes = [2, 0, -3, 3, -4]        # Coeficientes do polinômio p(x) = x^4 + x^3 + x^2 + x + C
    x0 = -2                                 # Valor inicial para x0
    itmax = 10                          #Número de iterações                         

    raiz_aproximada = newton(coeficientes, x0, itmax)
    print(f"Raiz aproximada após {itmax} iterações: {raiz_aproximada} ")
