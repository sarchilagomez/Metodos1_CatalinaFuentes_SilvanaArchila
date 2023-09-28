import numpy as np

#PARCIAL 2
#Integrales - Ejercicio 6 Inductancia bobina toroidal (parte 2)

#MÉTODO DEL SIMPSON 1/3
class Integrator:
    
    def __init__(self,x,f):
        
        self.x = x
        self.h = self.x[1] - self.x[0]
        self.y = f(self.x)
        
        self.Integral = 0.
        
class Simpson(Integrator):
    
    def __init__(self,x,f):
        Integrator.__init__(self,x,f)
        
    def GetIntegral(self):
        
        self.Integral = 0.
        
        self.Integral += self.y[0] + self.y[-1]
        
        for i in range( len(self.y[1:-1]) ):
            
            if i%2 == 0:
                self.Integral += 4*self.y[i+1]
            else:
                self.Integral += 2*self.y[i+1]
          
        return self.Integral*self.h/3
    
    def GetDerivative(self):
        
        d = f(self.x + 2*self.h) - 4*f(self.x + self.h) + 6*f(self.x) - 4*f(self.x - self.h) + f(self.x - 2*self.h)
        d /= self.h**4
    
        return d
    
    def GetError(self):
        
        d = self.GetDerivative()
        max_ = np.max(np.abs(d))
        
        self.error = (self.x[-1]-self.x[0])*self.h**4*max_/180
        
        return self.error
    
x = np.linspace(-0.009,0.009,50)
f = lambda x: np.sqrt(0.01**2 - x**2)/(0.5+x)

I = Simpson(x,f)

print("La estimación de la integral con Simpson 1/3 es:", I.GetIntegral())
print("El error de esta estimación es:", I.GetError())