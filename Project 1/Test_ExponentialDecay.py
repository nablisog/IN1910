from ExponentialDecay import ExponentialDecay
import nose.tools as nt
import nose


def test_Expo_Decay():
     
     """ Test funtion for the Exponentional Decay class """ 
     
     u0=3.2  
     a=-1.28 
     eps= 10e-13
     x= ExponentialDecay(0.4)
     assert(abs(x(0,u0)-a)<eps)
     if True:
          print("TEST PASSED")
     else:
          print("TEST FAILED")

test_Expo_Decay()

if __name__ == '__main__':
     nose.run



     
