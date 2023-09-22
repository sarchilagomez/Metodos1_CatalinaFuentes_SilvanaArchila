import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)


#GAUSS-HERMITE (de -infinito a infinito)

#1
def GetHermite(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 2*x
    else:
        poly = (2*x)*GetHermite(n-1,x) - (2*(n-1))*GetHermite(n-2,x)
    
    return sym.expand(poly,x)


#2

def GetDHermite(n,x):
    Pn = GetHermite(n,x)
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

def GetAllRootsGHer(n):

    xn = np.linspace(-np.sqrt((4*n)+1),np.sqrt((4*n)+1),100)
    
    Hermite = []
    DHermite = []
    
    for i in range(n+1):
        Hermite.append(GetHermite(i,x))
        DHermite.append(GetDHermite(i,x))
    
    poly = sym.lambdify([x],Hermite[n],'numpy')
    Dpoly = sym.lambdify([x],DHermite[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots


#3

def GetWeightsGHer(n):

    Roots = GetAllRootsGHer(n)
    Hermite= []
    
    for i in range(n):
        Hermite.append(GetHermite(i,x))
    
    poly = sym.lambdify([x],Hermite[n-1],'numpy')
    Weights = (2**(n-1) * math.factorial(n) * np.sqrt(np.pi))/(n**2*(poly(Roots))**2)
    
    return Weights

n = 5
raices = GetAllRootsGHer(n)
pesos = GetWeightsGHer(n)

funcion = lambda x: 1 #Esta la cambias por la función que quieras 

I = 0
for i in range(n):
    I += pesos[i]*funcion(raices[i])
#print(I)

print("Los primeros 20 ceros de los polinomios son:")
print(GetAllRootsGHer(20))
print("Y sus correspondientes pesos de cuadratura son:")
print(GetWeightsGHer(20))