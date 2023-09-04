
#EJERCICIOS PARCIAL
#Derivadas: 8 (python)

#derivada por interpolación de newton
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 1.1, 50)
def funcion(x):
    return np.sqrt(np.tan(x))
    
#PUNTO C
def derivada_progresiva(x,h=0.01):
    d = (1/(2*h))*(-3*funcion(x) + 4*funcion(x+h) - funcion(x+2*h))
    return d

y1 = derivada_progresiva(x)



#PUNTO D
def derivada_centrada(x,h=0.01):
    d = (1/(2*h))*(funcion(x+h)-funcion(x-h))
    return d

y2 = derivada_centrada(x)


#PUNTO E
y3 = 1/(2*np.sqrt(np.tan(x))*(np.cos(x))**2)

plt.plot(x,y1, label='Derivada progresiva') 
plt.plot(x,y2, label='Derivada centrada') 
plt.plot(x,y3, label='Derivada analítica') 
plt.legend()
plt.title('Derivada de raíz de tangente, h = 0.01 ')

#PUNTO F
error_nodal_progresiva = np.abs(y3-y1)
error_nodal_centrada = np.abs(y3-y2)

#plt.scatter(x,error_nodal_progresiva, label='Error nodal: Derivada progresiva') 
#plt.scatter(x,error_nodal_centrada, label='Error nodal: Derivada centrada') 
#plt.legend()
#plt.title('Errores nodales')
