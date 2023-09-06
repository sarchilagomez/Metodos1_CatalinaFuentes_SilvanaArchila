#PARCIAL 1 


import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
import math



#PUNTO A
def funcion(x):
    return math.e**(-x)-x

#PUNTO B 
x = [0, 2]


#PUNTO C
punto_medio = (x[0]+x[1])/2 #Creando x2 
x.append(punto_medio)

y0 = [funcion(x[0]), funcion(x[1]), funcion(x[2])]




#PUNTO D

#HALLANDO DIFERENCIAS DIVIDIDAS (coeficientes/pendientes/As) 
y1= [] #pendientes orden 1
for i in range(0,len(y0)-1):
    z = (y0[i+1]-y0[i])/(x[i+1]-x[i])
    y1.append(z)
    
y2 = [] #pendientes orden 2
for i in range(0,len(y1)-1):
    z = (y1[i+1]-y1[i])/(x[i+2]-x[i])
    y2.append(z)
    
y3 = [] #pendientes orden 3
for i in range(0,len(y2)-1):
    z = (y2[i+1]-y2[i])/(x[i+3]-x[i])
    y3.append(z)

    #ajustar rango (len), ajustar x[i+NUM] y donde appendear cada vez

#CONSTRUYENDO POLINOMIO CON SYMPY 
X = sym.Symbol('x') #elegimos la letra que va a representar nuestra variable en los polinomios (x)
polinomio = y0[0] #1er término del polinomio (1er dato de y: f(0))
    
Y = [y1,y2,y3] #creo lista con todas las pendientes/As

termino = 1 #termino son los paréntesis que acompañan a las pendientes/As
for i in range(0,len(x)-1):
    termino = termino*(X-x[i]) #interación de los paréntesis donde se van añadiendo para formar término
    polinomio = polinomio + termino*Y[i][0] #multiplica el termino con las pendientes/As que guardamos en la lista Y y los suma para formar el polinomio
poli_simpli = polinomio.expand() #simplifica el polinomio (ya ese es :D)

#print(poli_simpli)


#HALLANDO A B Y C 

string = str(poli_simpli)
#print(string)
string = string.split(" ")
#print(string)
a_varios = string[0]
b_varios = string[2]

c = float(string[4])
a = float(a_varios.split("*")[0])
b = float(b_varios.split("*")[0])

def x3(a, b, c):
    respuesta = 0
    if b > 0:
        respuesta = (-2*c)/(b + np.sqrt(b**2 - 4*a*c))
    if b < 0:
        respuesta = (-2*c)/(b - np.sqrt(b**2 - 4*a*c))
    return respuesta

#PUNTO E 

fx3 = funcion(x3(a,b,c))
x.append(x3(a, b, c))
y0.append(fx3)



parar = 10**(-10)
iter = 0
while np.abs(y0[-1]) > parar and iter < 100:
    iter += 1

    def dif2(x0, x1, F):
        resul= (F(x1)-F(x0))/(x1-x0)
        return resul

    def dif3(x0,x1,x2,F):
        resul= (dif2(x1,x2,F)- dif3(x0,x1,F))/(x2-x0)
        return resul

    def sacar_abc(x0,x1,x2,F):
        a = dif3(x0,x1,x2,F)
        b = dif2(x0,x1,F)-((x0+x1)*(dif3(x0,x1,x2,F)))
        c = F(x0)-((x0)*dif2(x0,x1,F))+(x0*x1*dif3(x0,x1,x2,F))
        abc = []
        abc.append(a)
        abc.append(b)
        abc.append(c)
        return abc
    
    abc = sacar_abc(x[0], x[1], x[2], funcion(X))
    a = abc[0]
    b = abc[1]
    c = abc[2]

    fx3 = funcion(x3(a,b,c))
    x = [x[iter+1], x[iter+2], x[iter+3]]
    y0 = [y0[iter+1], y0[iter+2], y0[iter+3]]




