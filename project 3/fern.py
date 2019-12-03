import numpy as np
import matplotlib.pyplot as plt

class AffineTransform:

     def __init__(self,a,b,c,d,e,f):
          """
          The class AffineTransform takes 6 arguments
          parameters :-
          a,b,c,d,e,f
          
          """
          self.a = a
          self.b = b
          self.c = c
          self.d = d
          self.e = e
          self.f = f

     def __call__(self,r):
          
          """
          The specal call method takes an arument r
          x,y = r
          calculates the affine transformation
          """
          x,y = r 
          x0 = self.a * x + self.b * y + self.e
          y0 = self.c * x + self.d * y + self.f
          return x0, y0
          


if __name__ == '__main__': 
     f1 = AffineTransform(0,0,0,0.16,0,0)
     f2 = AffineTransform(0.85,0.04,-0.04,0.85,0,1.60)
     f3 = AffineTransform(0.20,-0.26,0.23,0.22,0,1.60)
     f4 = AffineTransform(-0.15,0.28,0.26,0.24,0,0.44)
     functions = [f1,f2,f3,f4]
     p = [0.01,0.85,0.07,0.07]
     p_cumulative = np.cumsum(p)
     n = 50000
     x = ([0,0])
     y = []
     

               
     def iterate(x): 
         r = np.random.random()
         for j,p  in enumerate(p_cumulative):
             if r < p:
                 return functions[j]
             
     for i in range(n):
         j = iterate(functions)
         new = j(x)
         y.append(new)
         x = new


     plt.scatter(*zip(*y),s=0.1,color ="green")
     plt.axis('equal')
     plt.axis('off')
     plt.savefig("barnsley_fern.png")
     plt.show()
     
     
    


     

 

          
        


