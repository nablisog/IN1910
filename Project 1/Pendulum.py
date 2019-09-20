from math import sin,cos, pi
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt



class Pendulum:
    """ A single Pendulum class """

    def __init__(self, L=1.0, M=1.0,G=9.81):
        """
    The class Pendulum takes 3 arugments
        Parameters:-
        L = Length
        M = Mass
        G = Gravity
       """

        self.L = L
        self.M = M
        self.G = G

    def __call__(self, t, y):
        """
        The specal Method calculates and returns the angle and
        angular momentum as a tuple

        Parameter:-
        t = Time
        y = Thetha & Omega

        """
        thetha = y[0];
        omega = y[1]
        return (omega, -(self.G/self.L)*sin(thetha))

    def solve(self, y0, T, dt, angle ='rad'):
        """
    The function calculates the ODE and stores the solution as an array

              Parameters:-
              u0 = Initical condition
              y0 = thetha & omega
              T  = Time
              dt = Time steps

        """

        if angle == "deg":
            y0 = np.radians(y0)

        answer = solve_ivp(self, (0,T), y0, t_eval=np.arange(0,T+dt,dt))
        self._thetha = answer.y[0]
        self._omega = answer.y[1]
        self._t = answer.t


    @property
    def thetha(self):
        """ Returns angle as an array"""
        try:
            return self._thetha
        except AttributeError:
            raise AttributeError("AttributeError,Missing a call")



    @property
    def omega(self):
        """ Returns velocity as an array"""
        try:
            return self._omega
        except AttributeError:
            raise AttributeError("AttributeError,Missing a call")



    @property
    def t(self):
        """ Returns time points as an array"""
        try:
            return self._t
        except AttributeError:
            raise AttributeError("AttributeError,Missing a call")

    @property
    def x(self):
        """ Returns X position"""
        return np.sin(self._thetha)*self.L

    @property
    def y(self):
        """ Returns Y position"""
        return -np.cos(self._thetha)*self.L

    @property
    def potential(self):
        """ Calculates & returns potential energy  """
        return self.M*self.G*(self.y + self.L)

    @property
    def vx(self):
        """ Calculates & returns speed in X direction  """
        return np.gradient(self.x, self.t)

    @property
    def vy(self):
        """ Calculates & returns speed in Y direction  """
        return np.gradient(self.y, self.t)

    @property
    def kinetic(self):
        """ Calculates & returns kinetic energy  """
        return 0.5*self.M*(self.vy**2 + self.vx**2)




class DampenedPendulum(Pendulum):
    """ A Dampened Pendulum  class """
    def __init__(self, L=1.0, M=1.0,G=9.81,B=0.5):
        """
    The Dampened Pendulum class inherits Pendulum class & takes 4 arugments
        Parameters:-
        L = Length
        M = Mass
        G = Gravity
        B = Damped factor
       """

        super().__init__(L, M,G)
        self.B = B

    def __call__(self, t, y):
        """
        The specal Method calculates and returns the angle and
        angular momentum as a tuple

        Parameter:-
        t = Time
        y = Thetha & Omega

        """
        thetha = y[0]
        omega = y[1]
        return (omega, -(self.G/self.L)*sin(thetha) - (self.B/self.M)*omega)


if __name__ == '__main__':
     p = Pendulum()
     p.solve((20,0),10,0.01, angle="rad")
     plt.plot(p.t, p.thetha)
     plt.xlabel("Time[s]")
     plt.ylabel("Thetha")
     plt.title("Pendulum")
     plt.show()

     plt.plot(p.t,p.kinetic,label='Kinetic')
     plt.plot(p.t,p.potential,label='Potential')
     plt.legend()
     plt.xlabel("Time[s]")
     plt.ylabel("Energy")
     plt.title("Pendulum")
     plt.show()


     d = DampenedPendulum()
     d.solve((30,0),10,0.01, angle="rad")
     plt.plot(d.t,d.thetha)
     plt.xlabel("Time[s]")
     plt.ylabel("Thetha")
     plt.title("DampenedPendulum")
     plt.show()


     x = p.kinetic;y=p.potential
     z = x + y
     plt.plot(d.t,d.kinetic,label='Kinetic')
     plt.plot(d.t,d.potential,label='Potential')
     plt.plot(p.t,z,label='Total')
     plt.legend()
     plt.xlabel("Time[s]")
     plt.ylabel("Energy")
     plt.title("DampendedPendulum")
     plt.show()
