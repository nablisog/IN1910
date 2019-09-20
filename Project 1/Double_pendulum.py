from math import sin,cos, pi
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation




class Double_Pendulum:
    def __init__(self,M1=1,L1=1,M2=1,L2=1,G=9.81):
         self.L1=L1
         self.L2=L2
         self.M1=M1
         self.M2=M2
         self.G=G

    def __call__(self, t, y):
         L1=self.L1
         L2=self.L2
         M1=self.M1
         M2=self.M2
         G=self.G
         
         thetha1= y[0]
         omega1 = y[1]
         thetha2= y[2]
         omega2 = y[3]
         
         delta =thetha2 - thetha1
         d1 = ((M2*L1*(omega1**2)*sin(delta)*cos(delta)
                 + M2*self.G*sin(thetha2)*cos(delta)
                 + M2*L2*(omega2**2)*sin(delta)
                 - (M1 + M2)*self.G*sin(thetha1))
                 / ((M1 + M2)*L1 - M2*L1*cos(delta)**2))
         d2 = ((-M2*L2*omega2**2*sin(delta)*cos(delta)
                 + (M1 + M2)*self.G*sin(thetha1)*cos(delta)
                 - (M1 + M2)*L1*omega1**2*sin(delta)
                 - (M1+M2)*self.G*sin(delta))
                 / ((M1 + M2)*L2 - M2*L2*cos(delta)**2))
         
         return(omega1,d1,omega2,d2)



        

    def solve(self, y0, T, dt, angle ='rad'):
        if angle == "deg":
            y0 = np.radians(y0)

        
        answer = solve_ivp(self, (0,T), y0, t_eval=np.arange(0,T,dt))
        self._thetha1 = answer.y[0]
        self._omega1 = answer.y[1]
        self._thetha2=answer.y[2]
        self._omega2=answer.y[3]
        self._t = answer.t

    @property
    def thetha1(self):
        return self._thetha1
        

    @property
    def thetha2(self):
        return self._thetha2
            

    @property
    def omega1(self):
        return self._omega1
            
    @property
    def omega2(self):
        return self._omega2

          
    @property
    def t(self):
        return self._t


    @property
    def dt(self):
        return self.t[1] - self.t[0]

    @property
    def T(self):
        return self._T
            

    @property
    def x1(self):
        return self.L1 * np.sin(self.thetha1)
    
    @property
    def y1(self):
        return - self.L1 * np.cos(self.thetha1)
    
    @property
    def x2(self):
        return self.x1 + self.L2 * np.sin(self.thetha2)
    
    @property
    def y2(self):
        return self.y1 - self.L2 * np.cos(self.thetha2)



    @property
    def vx1(self):
        return np.gradient(self.x1, self.t)
     
    @property
    def vx2(self):
        return np.gradient(self.x2, self.t)

    @property
    def vy1(self):
        return np.gradient(self.y1, self.t)

    @property
    def vy2(self):
        return np.gradient(self.y2, self.t)

    @property
    def kinetic(self):
        k = 0.5*self.M1*(self.vx1**2 + self.vy1**2)\
           +0.5*self.M2*(self.vx2**2 + self.vy2**2)
        return k

    @property
    def potential(self):
        p = self.M1*self.G*(self.y1 + self.L1)\
           +self.M2*self.G*(self.y2 + self.L1 + self.L2)
        return p

    def create_animation(self):
        
        fig = plt.figure()

        
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))

       
        self.pendulums, = plt.plot([], [], 'o-', lw=2)

       
        self.animation = animation.FuncAnimation(fig,
                                                 self._next_frame,
                                                 frames=range(len(self.x1)), 
                                                 repeat=None,
                                                 interval=1000*self.dt, 
                                                 blit=True)

    def _next_frame(self, i):
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,


    def show_animation(self):
        plt.show()


    def save_animation(self,f,fps):
        a_saver=animation.writers['ffmpeg']
        a_saver=a_saver(fps=60)
        self.animation.save(f,writer=a_saver)

if __name__ == '__main__':
    p = Double_Pendulum()
    p.solve((3, 1, 0, -4), 10, 0.01)
    x = p.kinetic;y = p.potential
    total=x+y

    plt.plot(p.t,p.kinetic)
    plt.plot(p.t,p.potential)
    plt.plot(p.t,total)
    plt.show()

    p.create_animation()
    p.show_animation()

    

        

    











    
