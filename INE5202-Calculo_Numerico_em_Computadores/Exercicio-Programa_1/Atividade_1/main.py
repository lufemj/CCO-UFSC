import numpy as np
import matplotlib.pyplot as plt

#função que plota o gráfico do polinômio e sua derivada
def grafico(raiz_aproximada, coeficientes):
    x_vals = np.linspace(-3, 2, 400)
    y_vals = np.polyval(coeficientes, x_vals)
    tangente = np.polyval(np.polyder(coeficientes), x0) * (x_vals - x0) + np.polyval(coeficientes, x0)
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label='p(x)')
    plt.plot(x_vals, tangente, label="Tangente em x0", linestyle='--', color='orange')
    plt.scatter(raiz_aproximada, 0, color='red', label='Raiz Aproximada')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(raiz_aproximada, color='gray', linestyle='--', linewidth=0.5)
    plt.title("Polinômio e sua Derivada")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

#função que calcula o valor do polinômio e sua derivada em x0
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

#função que calcula a raiz de um polinômio pelo método de Newton
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
    itmax = 10                              # Número de iterações                         

    raiz_aproximada = newton(coeficientes, x0, itmax)
    print(f"Raiz aproximada após {itmax} iterações: {raiz_aproximada} ")

    grafico(raiz_aproximada, coeficientes)
