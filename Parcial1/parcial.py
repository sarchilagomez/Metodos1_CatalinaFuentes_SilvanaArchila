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

#GRAFICANDO POLINOMIO

px = sym.lambdify(X, poli_simpli) #debe quedar (la x que tenias en sym.Symbol , polinomo)
plt.plot(x,y0,'o',label='Conjunto soporte') #plotea conjunto soporte (puntos)
pxi = np.linspace(0, 10, 50) #(menor dato x (o a bit antes), mayor dato x (o a bit despues), entre mas grande el num mas suave la grafica)
pfi = px(pxi) #evalua el poli en forma lambda (px) en los puntos de x que queremos (pxi)
plt.plot(pxi,pfi, label='Polinomio interpolado') #plotea el polinomio

#cositas extra
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Polinomio con Interpolación de Newton') 

plt.show()

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
while np.abs(y0[-1]) > parar:
    y1= [] #pendientes orden 1
    for i in range(0,len(y0)-1):
        z = (y0[len(y0)-2]-y0[len(y0)-3])/(x[len(y0)-2]-x[len(y0)-3])
        y1.append(z)
        
    y2 = [] #pendientes orden 2
    for i in range(0,len(y1)-1):
        z = (y1[len(y0)-2]-y1[len(y0)-3])/(x[len(y0)-1]-x[len(y0)-3])
        y2.append(z)
        
    y3 = [] #pendientes orden 3
    for i in range(0,len(y2)-1):
        z = (y2[len(y0)-2]-y2[len(y0)-3])/(x[len(y0)]-x[len(y0)-3])
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

    #GRAFICANDO POLINOMIO

    

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


