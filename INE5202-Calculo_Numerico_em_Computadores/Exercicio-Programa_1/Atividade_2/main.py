'''import cmath

def muller_method(f, x0, x1, x2, tol=1e-6, itmax=100):
    it = 2
    while it < itmax:
        c = f(x2)
        q0 = (f(x0) - f(x2)) / (x0 - x2)
        q1 = (f(x1) - f(x2)) / (x1 - x2)
        a = (q0 - q1) / (x0 - x1)
        b = q0 * (x2 - x1) / (x0 - x1) + q1 * (x0 - x2) / (x0 - x1)
        
        # Handle complex numbers in the calculations
        discriminant = cmath.sqrt(b**2 - 4*a*c)
        if abs(b + discriminant) > abs(b - discriminant):
            den = b + discriminant
        else:
            den = b - discriminant
            
        x = x2 - (2*c) / den
        x0, x1, x2 = x1, x2, x
        if abs(f(x)) < tol:
            return x
        it += 1
    return None  # If the maximum number of iterations is reached without convergence

# Defining the polynomial function
def f(x):
    return x**4 - 3*x + x**2 + x + 1

# Initial guesses for complex root
x0, x1, x2 = -0.5, 0, 0.5

# Approximating the complex root
complex_root = muller_method(f, x0, x1, x2)
print("Complex root:", complex_root)'''


def muller (funcao, x0, x1, x2, itmax):
    f = funcao    
    tolerancia = 10**-7 
    x = x2
    it = 2

    while (abs(f(x)) > tolerancia) and (it < itmax):
        c = f(x2)
        q0 = (f(x0) - f(x2))/(x0 - x2)
        q1 = (f(x1) - f(x2))/(x1 - x2)
        a = (q0-q1)/(x0-x1)
        b = q0*((x2-x1)/(x0-x1)) + q1*((x0-x2)/(x0-x1))

        #todo valores complexos passo 9

        x0 = x1
        x1 = x2
        x2 = x

        x0, x1, x2 = x1, x2, x

        it = it+1
    
    return None


if __name__ == "__main__":
    funcao = lambda x: x**4 - 3*x + x**2 + x + 1
    x0 = -0.5
    x1 = 0
    x2 = 0.5

    itmax = 10

    raiz_complexa = muller (funcao, x0, x1, x2, itmax)
    print(f"Raiz complexa após {itmax} iterações: {raiz_complexa} ")
