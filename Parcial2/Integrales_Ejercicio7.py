#PARCIAL 2
#Integrales - Ejercicio 7 (trapecio y volumen semiesfera)

import numpy as np
import matplotlib.pyplot as plt

#PARTE A
n = 20000 #número de divisiones
x = np.linspace(-1, 1, n + 1) #diametro de -1 a 1: radio 1
y = np.linspace(-1, 1, n + 1)
area = float((x[1]-x[0])*(y[1]-y[0])) #hallando area del cu
a=0
X, Y = np.meshgrid(x, y) #crea grilla de tamaño x,y}



#PARTE B
Z = np.zeros_like(X) #Guardar valores volumen en una matriz
volumen = 0. #volumen calculado

def funcion(x,y):
    return  np.sqrt(1 - x**2 - y**2) if x**2 + y**2 < 1 else 0.0 #raiz: semiesfera. condicion:usar dentro del circulo
    

# Bucle para recorrer los cuadrados pequeños en la grilla
for i in range(n):
    for j in range(n):
        #creo los 4 puntos (vertices)
        x1 = x[i]
        x2 = x[i + 1]
        x3 = x[i]
        x4 = x[i + 1]
        
        y1 =  y[j]
        y2 =  y[j]
        y3 = y[j + 1]
        y4 = y[j + 1]
                
        # Calcula el promedio de la función en los vértices del cuadrado
        promedio = (funcion(x1, y1) + funcion(x2, y2) + funcion(x3, y3) + funcion(x4, y4))/4
                  
        volumen += promedio*area
        Z[i,j] =  promedio*area


print("Volumen semiesfera:", volumen)



# Crear la figura y el objeto de los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie 3D del volumen
ax.plot_surface(X, Y, Z, cmap='viridis')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Volumen')
ax.set_title('Volumen de la Semiesfera en 3D')

# Mostrar la gráfica
plt.show()


