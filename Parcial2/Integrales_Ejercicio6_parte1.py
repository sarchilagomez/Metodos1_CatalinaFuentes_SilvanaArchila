import numpy as np

#PARCIAL 2
#Integrales - Ejercicio 6: Inductancia bobina toroidal (parte 1)

#MÉTODO DEL TRAPECIO
class Integrator:
    
    def __init__(self,x,f):
        
        self.x = x
        self.h = self.x[1] - self.x[0]
        self.y = f(self.x)
        
        self.Integral = 0.
        
    def GetIntegral(self):
        
        self.Integral += 0.5*(self.y[0]+self.y[-1])
        
        for i in range(1,self.y.shape[0]-1):
            self.Integral += self.y[i]
        
        self.Integral *= self.h
        
        return self.Integral
    
    def GetDerivative(self):
        d = f(self.x + self.h) - 2*f(self.x) + f(self.x - self.h)
        d /= self.h**2
        return d
        

#Hallando error de trapecio
    def GetError(self):
           
           d = self.GetDerivative()
           max_ = np.max(np.abs(d))
           
           self.error = (self.x[-1]-self.x[0])*self.h**2*max_/12
           
           return self.error
       
        

        
x = np.linspace(-0.009,0.009,50)
f = lambda x: np.sqrt(0.01**2 - x**2)/(0.5+x)

I = Integrator(x,f)
print("La estimación de la integral con Trapecio es:", I.GetIntegral())
print("El error de esta estimación es:", I.GetError())






