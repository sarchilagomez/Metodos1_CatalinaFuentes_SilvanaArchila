#Raices de polinomios: 3
import matplotlib.pyplot as plt
import numpy as np


def Funcion(x):
    return (3*x**5 + 5*x**4 - x**3)

def DerivadaCentral(f,x,h=1e-6):
    
    d = 0.
    
    if h != 0:
        d = (f(x+h) - f(x-h))/(2*h)
        
    return d

def x_n(x, der, fun, precision=1e-5, itmax=1000):
    error = 1
    it = 0
    while error > precision and it < itmax:
        try:
            xn1 = x - fun(x)/der(fun, x)
            error = np.abs(fun(x)/der(fun, x))
        except:
            print("División por cero")
        
        x = xn1
        it += 1
    return x

def get_all_roots(x, tolerancia=2):
    roots = np.array([])
    for i in x:
        
        root = x_n(i, DerivadaCentral, Funcion)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in roots:
                roots = np.append(roots,croot)
                
    roots.sort()
    
    return f"Las raices encontradas son: {roots}"

x = np.linspace(-2, 1, 1000)
print(get_all_roots(x))
#print(Funcion(x))
plt.plot(x, Funcion(x))
plt.show()