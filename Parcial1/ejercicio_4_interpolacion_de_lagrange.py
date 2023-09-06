#Interpolación de Lagrange: 4
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

a = open("Parcial1\Parabolico.csv", "r", encoding = "UTF-8")
x_lista = []
y_lista = []
linea = a.readline()
linea = a.readline()
while linea != "":
    x_lista.append(float(linea.strip("\n").split(",")[0]))
    y_lista.append(float(linea.strip("\n").split(",")[1]))
    linea = a.readline()
#print(x_lista, y_lista)
a.close()

def Li(x_lista, x):
    li = []
    i = 0
    j = 0
    L = 1
    final = len(x_lista)
    while i < final:
        while j < final:
            if i != j:
                L *= (x-x_lista[j])/(x_lista[i]-x_lista[j])
            j += 1
        li.append(L)
        L = 1
        j = 0
        i += 1
    return li

x_ = sym.Symbol("x",real=True)
L0 = Li(x_lista, x)[0]
L1 = Li(x_lista, x)[1]
L2 = Li(x_lista, x)[2]
L0_expandida = sym.expand(L0)
L1_expandida = sym.expand(L1)
L2_expandida = sym.expand(L2)
#print(L0_expandida)
#print(L1_expandida)
#print(L2_expandida)

def funcion_(y_lista, Li):
    f = 0
    i = 0
    for y in y_lista:
        if i < len(Li):
            f += y*Li[i]
        i += 1
    return f
#print(funcion_(y_lista, Li(x_lista, x)))

x_ = np.linspace(0, 6.6, 1000)
fun_expandida = sym.expand(funcion_(y_lista, Li(x_lista, x)))
#print(fun_expandida)
#plt.plot(x_, funcion_(y_lista, Li(x_lista, x_)))
#plt.show()

def DerivadaCentral(h=1e-6):
    
    d = []
    for i in x_:
        if h != 0:
            d.append((funcion_(y_lista, Li(x_lista, i+h)) - funcion_(y_lista, Li(x_lista, i-h)))/(2*h))
        
    return d
#print(DerivadaCentral())

def posicion_final_en_y():
    d = DerivadaCentral()
    i = 0
    ymax = 0
    while i < len(d):
        if round(d[i], 3) == 0:
            ymax = funcion_(y_lista, Li(x_lista, x_[i]))
            i += len(d)
        else:
            i += 1
    return ymax
#print(posicion_final_en_y())

def velocidad_inicial_en_y(yf, y0=0, vf=0, g=-9.8):
    v02 = vf**2 - 2*g*(yf-y0)
    return np.sqrt(v02)
#print(velocidad_inicial_en_y(posicion_final_en_y()))

def tiempo(v0, yf, y0=0, vf=0):
    return 4*(yf-y0)/(vf+v0)
#print(tiempo(velocidad_inicial_en_y(posicion_final_en_y()), posicion_final_en_y()))

def posicion_final_en_x():
    d = DerivadaCentral()
    i = 0
    xmax = 0
    while i < len(d):
        if round(d[i], 3) == 0:
            xmax = 2*(x_[i])
            i += len(d)
        else:
            i += 1
    return xmax
#print(posicion_final_en_x())

def velocidad_en_x(t, xf, x0=0):
    return (xf-x0)/t
#print(velocidad_en_x(tiempo(velocidad_inicial_en_y(posicion_final_en_y()), posicion_final_en_y()), posicion_final_en_x()))

def velocidad_inicial(vx, vy):
    return np.sqrt(vx**2 + vy**2)

def direccion(vx, vy):
    angulo_radianes = np.arctan(vy/vx)
    angulo_grados = angulo_radianes*180/np.pi
    return angulo_grados
vx = velocidad_en_x(tiempo(velocidad_inicial_en_y(posicion_final_en_y()), posicion_final_en_y()), posicion_final_en_x())
vy = velocidad_inicial_en_y(posicion_final_en_y())
print(f"La velocidad inicial fue aproximadamente de {velocidad_inicial(vx, vy)}m/s a un ángulo de {direccion(vx, vy)}° sobre la horizontal.")

