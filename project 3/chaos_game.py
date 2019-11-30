import numpy as np
import matplotlib.pyplot as plt


class chaos_game:

     def __init__(self, n, r):
          if type(n) != int and type(r) != float:
               raise TypeError("n must be integer and r must be float")
          
          if n >=3:
               self.n = n
          if 0 < r < 1:
               self.r = r

          else:
               raise ValueError("range out of index")

          self.corner = self._generate_ngon()


     def _generate_ngon(self):
          values = np.linspace(0,2*np.pi,self.n)
          corner= [(np.sin(thehta), np.cos(thehta)) for thehta in values]
          return corner

     def plot_ngon(self):
          plt.scatter(*zip(*self.corner))
          plt.axis("equal")
          plt.axis("off")
          plt.show()

     def _starting_point(self):
          x=[];y=[]
          weight = np.random.random(self.n)
          for i in range(self.n):
               x += [weight[i]/np.sum(weight)]
               y += [np.array(self.corner[i]) * x[i]]
                       
          return sum(y)

     def iterate(self,steps, discard=5):
          points=[]
          points = [self._starting_point()]
          for i in range(steps):
               j = np.array(self.corner)[np.random.randint(0,self.n)]
               points += [self.r*(points[i] + (1-self.r)*j)]              
          self.points = points

     def plot(self,color=False, cmap="jet"):
          if color:
               liste = []
               for i in self.corner:
                    liste.append(i)

               plt.scatter(*zip(*liste))
               plt.show()
               
          else:
               cmap = "black"

          plt.scatter(*zip(*self.points),s = 0.1 ,c = cmap)
          plt.axis("equal")
          plt.axis("off")
          

          

     def show(self):
          self.plot(False,"jet")
          plt.show()
          
          
        

     def savepng(self,outfile,color=False, cmap="jet"):
          
          if "." not in outfile: 
              name = outfile + ".png"
              
          elif ".png" in outfile:
               name = outfile
             
          elif outfile[:-4] != ".png":
             raise TypeError("must end with .png")


          
          self.plot()
          plt.savefig(name, dpi=300,transparent=True)
          
          
         

if __name__ == "__main__":
     for i in range(3,9):
          c = chaos_game(i,0.9)
          c.plot_ngon()

         


     c1 = chaos_game(4, float(1/3))
     c1.iterate(10000)
     c1.show()
     c1.savepng("fig1")
     
    
     c2 = chaos_game(5, float(1/3))
     c2.iterate(10000)
     c2.show()
     c2.savepng("fig2")
     
     
         
     c3 = chaos_game(5, float(3/8))
     c3.iterate(10000)
     c3.show()
     c3.savepng("fig3")
     
     
     
     c4 = chaos_game(6, float(1/3))
     c4.iterate(10000)
     c4.show()
     c4.savepng("fig4")
