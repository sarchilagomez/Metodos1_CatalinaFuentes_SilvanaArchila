#PARCIAL 2
#Raices - Ejercicio 5 (Hallar raices de primeros 20 polinomios de Laguerre de 0 a infinito)

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math

#Hallando todas las raices para un polinomio dado
x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLaguerreRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 1 - x
    else:
        poly = ((2*(n-1)+1-x)*GetLaguerreRecursive(n-1,x)-(n-1)*GetLaguerreRecursive(n-2,x))/n
   
    return sym.expand(poly,x)

def GetDLaguerre(n,x):
    Pn = GetLaguerreRecursive(n,x)
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

def GetAllRootsGLag(n):

    xn = np.linspace(0, n + ((n-1)*math.sqrt(n)),100) #Solo hace falta hallar las raices en este intervalo pues es allí donde existen
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerreRecursive(i,x))
        DLaguerre.append(GetDLaguerre(i,x))
    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

print("Las raices reales de los primeros 20 polinomios de Laguerre son:")
for i in range(1,20): 
    Raiz = GetAllRootsGLag(i)
    print(Raiz)



"""

#Hallando las raices para los primeros 20 polinomios
def Roots20Poli():
    #Raices = []
    for i in range(1,20): #se daña si empiexo en 0
        Raiz = GetAllRootsGLag(i)
        #Raices.append(Raiz)
        print(Raiz)
    return Raiz 

#print("Las raices reales de los primeros 20 polinomios de Laguerre son:", Roots20Poli())

#se demora mucho mucho
"""
