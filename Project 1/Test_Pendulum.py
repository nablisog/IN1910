import nose.tools as nt
import nose
from math import sin,pi
from Pendulum import Pendulum


def test_pendulum_1():
     """ Tests the specal method if it returns the angle and
        angular momentum as a tuple"""
     
     L = 2.2
     G = 9.81
     T = 1
     thetha = pi/4
     omega = 0.01
     y =(thetha,omega)
     x = -G/L*sin(thetha)
     p = Pendulum(L)

     nt.assert_equal(p(T,y),(omega,x))

     

def test_pendulum_2():
     """ Tests if the Pendulum at rest stays at rest"""

     T = 1
     thetha = 0
     omega = 0
     y =(thetha,omega)
     p = Pendulum()
     nt.assert_equal(p(T,y),(0,0))


def test_radius_constant():
     """ Tests if the length of Pendulum is constant """
     
     T = 10
     dt = 0.01
     y= [pi/4,0.1]
     p = Pendulum(L=2.2)
     p.solve(y,T,dt,angle='rad')
     radius = p.x**2 + p.y**2
     for i in range(len(radius)):
          nt.assert_almost_equal(radius[i],2.2**2)
     
@nt.raises(AttributeError)
def test_t():
     """ Tests for Attribute Error if called before solve function """
     p = Pendulum()
     p.t


@nt.raises(AttributeError)
def test_thetha():
     """ Tests for Attribute Error if called before solve function """
     p = Pendulum()
     p.thetha



@nt.raises(AttributeError)
def test_omega():
     """ Tests for Attribute Error if called before solve function """
     p = Pendulum()
     p.omega


if __name__ == "__main__":
     nose.run()
















     
