import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
n = 15

def GetLegendre(n,x,y):
    
    y = (x**2 - 1)**n
    
    poly = sym.diff( y,x,n )/(2**n*math.factorial(n))
    
    return poly


def GetDLegendre(n,x):
    Pn = GetLegendre(n,x, y)
    return sym.diff(Pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGLeg(n):

    xn = np.linspace(-1,1,100)
    
    Legendre = []
    DLegendre = []
    
    for i in range(n+1):
        Legendre.append(GetLegendre(i,x, y))
        DLegendre.append(GetDLegendre(i,x))
    
    poly = sym.lambdify([x],Legendre[n],'numpy')
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLeg(n):

    Roots = GetAllRootsGLeg(n)

    

    DLegendre = []
    
    for i in range(n+1):
        DLegendre.append(GetDLegendre(i,x))
    
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights

print(f"Las raíces del polinomio 50 son: {GetAllRootsGLeg(50)}")

def funcion_a_integrar(temperatura, tamano_banda):
    raices = GetAllRootsGLeg(n)
    pesos = GetWeightsGLeg(n)

    funcion = lambda x: (math.tanh(np.sqrt(x**2 + tamano_banda**2)*300/(2*temperatura)))/(np.sqrt(x**2 + tamano_banda**2))

    I = 0
    for i in range(n):
        I += pesos[i]*funcion(raices[i])

    return I/2

def temperatura_critica():
    step = 10**(-2)
    for i in range(12, int(20 / step)):
        x = i * step + 12
        I = funcion_a_integrar(x, step)
        NOV = 0.3
        if np.abs(1 - I * NOV) < step:
            return x

print(f"La temperatura crítica es aproximadamente: {temperatura_critica()}K")