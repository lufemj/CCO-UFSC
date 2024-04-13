import numpy as np
import matplotlib.pyplot as plt

# Definindo a função que calcula as raízes complexas
def complex_roots(n, k):
    return np.exp(2 * np.pi * 1j * k / n)

# Definindo o número de raízes e o grau da raiz
n = 5  # Número de raízes
root_degree = 3  # Grau da raiz

# Calculando as raízes complexas
roots = [complex_roots(n, k) for k in range(n)]

# Plotando as raízes complexas
plt.figure(figsize=(6, 6))
plt.scatter(np.real(roots), np.imag(roots), color='red')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title(f'Raízes Complexas de {n}ª raiz de {root_degree}')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()