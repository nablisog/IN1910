
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class ExponentialDecay:
     """ Exponential decay class """

     def __init__(self, a):
          """ The class Exponential Decay takes decay constant as an arugment  """
          self.a = a         

     def __call__(self,t,u):
          """ The special call method returns the derivative of the decay  """
          return -self.a*u

     def solve(self,u0,T,dt):
          """ The function solves the ODE and returns the time and velocity

              Parameters:-
              u0 = Initical condition
              T  = Time
              dt = Time steps

          """
          T= (T/dt)*dt 
          x= solve_ivp(self,(0,T),(u0,),t_eval=np.arange(0,T+dt,dt))
          return x.t, x.y[0]
              
     
if __name__ =='__main__':
     u0=3.2;T=15;dt=0.1
     decay_model = ExponentialDecay(0.4)
     t, u = decay_model.solve(u0, T, dt)

     plt.plot(t,u)
     plt.title("Exponential decay")
     plt.show()
     
