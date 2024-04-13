import cmath
import numpy as np
import matplotlib.pyplot as plt

#função que plota o gráfico do polinômio e sua derivada
def grafico(raiz_complexa, raizes_reais):
    x_values = np.linspace(-2, 3, 400)
    y_values = f(x_values)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='Função')
    plt.title('Gráfico da função')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    for i in raizes_reais:
        plt.scatter(i.real, f(i.real), color='red', label='Raiz Real')
    plt.scatter(raiz_complexa.real, raiz_complexa.imag, color='blue', label='Raiz Complexa')
    plt.legend()
    plt.show()

#função que calcula a raiz de um polinômio pelo método de Muller
def muller (funcao, x0, x1, x2, itmax):
    f = funcao    
    tolerancia = 10**-9 
    x = x2
    it = 2

    while ((abs(f(x)) > tolerancia) and (it < itmax)):
        c = f(x2)
        q0 = (f(x0) - f(x2))/(x0 - x2)
        q1 = (f(x1) - f(x2))/(x1 - x2)
        a = (q0-q1)/(x0-x1)
        b = q0*((x2-x1)/(x0-x1)) + q1*((x0-x2)/(x0-x1))

        #Passo 9 tratando dos numeros complexos
        discriminante = cmath.sqrt(b**2 - 4*a*c)
        if abs(b + discriminante) > abs(b - discriminante):
            den = b + discriminante
        else:    
            den = b - discriminante
        
        x = x2 - ((2*c) / den)
        x0, x1, x2 = x1, x2, x
        it = it+1
    return x


if __name__ == "__main__":
    funcao = lambda x: x**4 - 3*x**3 + x**2 + x + 1       # Polinomio p(x) = x^4 - 3x^3 + x^2 + x + 1
    f = funcao
    x0 = -0.5                                             # Valor inicial para x0
    x1 = 0                                                # Valor inicial para x1
    x2 = 0.5                                              # Valor inicial para x2
    intervalos_arbitrario = [(0.2, 1,5), (1.6, 2.5)]      # Intervalos arbitrários para encontrar as raízes reais
    itmax = 10                                            # Número de iterações

    raizes_reais = []
    for intervalo in intervalos_arbitrario:
        raiz_real = muller(funcao, intervalo[0], intervalo[1], (intervalo[0] + intervalo[1]) / 2, itmax)
        raizes_reais.append(raiz_real.real)

    for i in range(len(raizes_reais)):
        raiz = raizes_reais[i]
        print(f"Raiz real {i+1} após {itmax} iterações: {raiz.real}")

    raiz_complexa = muller (funcao, x0, x1, x2, itmax)
    print(f"Raiz complexa após {itmax} iterações: {raiz_complexa} ")

    grafico(raiz_complexa, raizes_reais)