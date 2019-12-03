import numpy as np
import matplotlib.pyplot as plt
from chaos_game import chaos_game
from fern import AffineTransform


class Variations:
    """Constructor with variables and dictionary for the class follows"""
    def __init__(self, x, y, colors="Black"):
        self.x = x
        self.y = y
        self.colors = colors
        self.collection = {"linear": self.linear,
                           "handkerchief": self.handkerchief,
                           "swirl": self.swirl,
                           "disc": self.disc,
                           "spherical": self.spherical,
                           "cylinder": self.cylinder}

    @property
    def u(self):
        return self._u

    @property
    def v(self):
        return self._v

    """Under follows six method with functions from the catalog, 
    then adding the mapping to the lists u and v, which can be
    called from the properties."""

    def linear(self):
        u = []
        v = []
        for i in self.x:
            u.append(i)

        for i in self.y:
            v.append(i)

        self._u = u
        self._v = v

    def handkerchief(self):
        x = self.x
        y = self.y
        u = []
        v = []
        for i in range(len(self.x)):
            r = np.sqrt(x[i] ** 2 + y[i] ** 2)
            thetha = np.arctan2(x[i], y[i])
            u.append(r * np.sin(thetha + r))
            v.append(r * np.cos(thetha - r))

        self._u = u
        self._v = v

    def swirl(self):
        x = self.x
        y = self.y

        u = []
        v = []
        for i in range(len(self.x)):
            r = np.sqrt(x[i] ** 2 + y[i] ** 2)
            u.append(x[i] * np.sin(r**2) - y[i] * np.cos(r**2))
            v.append(x[i] * np.cos(r**2) + y[i] * np.sin(r**2))
        self._u = u
        self._v = v

    def disc(self):
        x = self.x
        y = self.y
        u = []
        v = []
        for i in range(len(self.x)):
            r = np.sqrt(x[i] ** 2 + y[i] ** 2)
            thetha = np.arctan2(x[i], y[i])
            u.append(thetha / np.pi * (np.sin(np.pi * r)))
            v.append(thetha / np.pi * (np.cos(np.pi * r)))
        self._u = u
        self._v = v

    def cylinder(self):
        x = self.x
        y = self.y
        u = []
        v = []
        for i in range(len(self.x)):
            u.append(np.sin(x))
            v.append(y)
        self._u = u
        self._v = v

    def spherical(self):
        x = self.x
        y = self.y
        u = []
        v = []
        for i in range(len(self.x)):
            r = np.sqrt(x[i] ** 2 + y[i] ** 2)
            u.append(1 / r**2 * x)
            v.append(1 / r**2 * y)
        self._u = u
        self._v = v

    """Plotting the codomain of the mappings.
    Note that as v is a list, we need to set the minus
    operator for every element"""
    def plot(self, cmap ='black'):
        v = self.v
        for i in range(len(v)):
            v[i] = -v[i]
        plt.scatter(self.u, v, c=self.colors, cmap=cmap, s=0.1)
        plt.axis('equal')
        plt.axis('off')


class chaos_game:
    """ A single chaos_game class creating a fractal, using ngon and
         an initial point selected at random inside it. """

    def __init__(self, n, r):

        """
        The class chaos_game takes 2 arugments
        Parameters:-
        n = Type:- integer. Value:- grater than or equal to 3
        r = Type:- float. Value:- between 0 and 1

        """
        if type(n) != int and type(r) != float:
            raise TypeError("n must be integer and r must be float")

        if n >= 3:
            self.n = n
        if 0 < r < 1:
            self.r = r


        else:
            raise ValueError("range out of index")

        self.corner = self._generate_ngon()

    def _generate_ngon(self):
        """ Computes the corners of ngon. """
        values = np.linspace(0, 2 * np.pi, self.n)
        corner = [(np.sin(thehta), np.cos(thehta)) for thehta in values]
        return corner

    def plot_ngon(self):
        """ plots the generated n-gon."""
        plt.scatter(*zip(*self.corner))
        plt.axis("equal")
        plt.axis("off")
        plt.show()

    def _starting_point(self):
        """ Picks a random point within the ngon """
        x = []
        y = []
        weight = np.random.random(self.n)
        for i in range(self.n):
            x += [weight[i] / np.sum(weight)]
            y += [np.array(self.corner[i]) * x[i]]

        return sum(y)

    def iterate(self, steps, discard=5):
        """ Iterate number of steps and stores it as a list"""
        points = []
        points.append(self._starting_point())
        for i in range(steps):
            j = np.array(self.corner)[np.random.randint(0, self.n)]
            points += [self.r * (points[i] + (1 - self.r) * j)]

        self.points = points
        return points

    def plot(self, color=False, cmap="jet"):
        """ plots figures that are generated by the iterature """
        if color:
            liste = []
            for i in self.corner:
                liste.append(i)

            plt.scatter(*zip(*liste))
            plt.show()

        else:
            cmap = "black"

        plt.scatter(*zip(*self.points), marker='.', s=0.1, c=cmap)
        plt.axis("equal")
        plt.axis("off")

    def show(self):
        """ calls the method plot and shows the plot"""
        self.plot(False, "jet")
        plt.show()


if __name__ == '__main__':
    """Calling the points from the chaos-class and returning them"""
    def plot_squares():
        cg1 = chaos_game(5, float(1 / 3))
        cg1._generate_ngon()
        points = cg1.iterate(50000)
        return points

    """Grid, given from problem-text"""
    def plot_grid():
        plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color="grey")
        plt.plot([-1, 1], [0, 0], color="grey")
        plt.plot([0, 0], [-1, 1], color="grey")

    """Methods from problem-text"""
    def problem3ab():
        N = 60
        grid_values = np.linspace(-1, 1, N)
        x_values = np.ones(N * N)
        y_values = np.ones(N * N)
        for i in range(N):
            index = i * N
            x_values[index:index + N] *= grid_values[i]
            y_values[index:index + N] *= grid_values

        coords_varia = Variations(x_values, y_values)

        variations = ["linear", "handkerchief", "swirl", "disc", "spherical", "cylinder"]

        plt.figure(10, figsize=(9, 9))
        for i in range(4):
            plt.subplot(221 + i)
            plot_grid()
            variation = variations[i]
            coords_varia.collection[variation]()
            coords_varia.plot()
            plt.title(variation)
        plt.savefig("variations_grid.png")
        plt.show()


    """Note; The mirroring across the y-axis happends in the plotting
    of the class Variations, so we dont need to flip the list, nor   
    change the sign of y."""
    def problem3c():
        x_values = []
        y_values = []
        points = plot_squares()
        N = 50000
        for i in range(N):
            x_values.append(points[i][0])
            y_values.append(-points[i][1])
        coords_varia = Variations(x_values, y_values)

        variations = ["linear", "handkerchief", "swirl", "disc", "spherical", "cylinder"]

        plt.figure(10, figsize=(9, 9))
        plt.show()
        for i in range(4):
            plt.subplot(221 + i)
            variation = variations[i]
            coords_varia.collection[variation]()
            coords_varia.plot()
            plt.title(variation)
        plt.savefig("variations_chaos_game.png")
        plt.show()

    def problem3c2():
        f1 = AffineTransform(0, 0, 0, 0.16, 0, 0)
        f2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
        f3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)
        f4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
        functions = [f1, f2, f3, f4]
        p = [0.01, 0.85, 0.07, 0.07]
        p_cumulative = np.cumsum(p)
        n = 50000
        x = ([0, 0])
        y = []


        def iterate(x):
            r = np.random.random()
            for j, p in enumerate(p_cumulative):
                if r < p:
                    return functions[j]


        for i in range(n):
            j = iterate(functions)
            new = j(x)
            y.append(new)
            x = new

        x_values = []
        y_values = []
        N = 50000
        for i in range(N):
            x_values.append(y[i][0]/10)
            y_values.append(-y[i][1]/10)
        coords_varia = Variations(x_values, y_values)

        variations = ["linear", "handkerchief", "swirl", "disc", "spherical", "cylinder"]

        plt.figure(10, figsize=(9, 9))
        plt.show()
        for i in range(4):
            plt.subplot(221 + i)
            variation = variations[i]
            coords_varia.collection[variation]()
            coords_varia.plot()
            plt.title(variation)
        plt.savefig("variations_barnsley_fern.png")
        plt.show()




    """run problem 3a and 3b"""
    problem3ab()
    """run problem 3c"""
    problem3c()
    """run problem 3c2"""
    problem3c2()



