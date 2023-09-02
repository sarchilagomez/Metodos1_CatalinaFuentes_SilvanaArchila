#Interpolación de Lagrange: 4
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

a = open("Parcial1\\Parabolico.csv", "r", encoding = "UTF-8")
x_lista = []
y_lista = []
linea = a.readline()
linea = a.readline()
while linea != "":
    x_lista.append(float(linea.strip("\n").split(",")[0]))
    y_lista.append(float(linea.strip("\n").split(",")[1]))
    linea = a.readline()
#print(x, y)
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

x = sym.Symbol("x",real=True)
L0 = Li(x_lista, x)[0]
L1 = Li(x_lista, x)[1]
L2 = Li(x_lista, x)[2]
L0_expandida = sym.expand(L0)
L1_expandida = sym.expand(L1)
L2_expandida = sym.expand(L2)
#print(L0_expandida)
#print(L1_expandida)
#print(L2_expandida)

def funcion(y_lista, Li):
    f = 0
    i = 0
    for y in y_lista:
        if i < len(Li):
            f += y*Li[i]
        i += 1
    return f

x_ = np.linspace(0, 6.6, 1000)
fun_expandida = sym.expand(funcion(y_lista, Li(x_lista, x)))
print(fun_expandida)
plt.plot(x_, funcion(y_lista, Li(x_lista, x_)))
plt.show()