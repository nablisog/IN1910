import numpy as np
import matplotlib.pyplot as plt

# Problem 1
"""Finding the corners of an equilateral triangle"""
corners = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
colors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
"""Picking a starting point"""
x = []
y = []
color_pt = []
for i in range(1000):
    weight = np.random.random(3)
    x += [weight / np.sum(weight)]
    y += [corners[0] * x[i][0] + corners[1] * x[i][1] + corners[2] * x[i][2]]
    color_pt += [colors[0] * x[i][0] + colors[1] * x[i][1] + colors[2] * x[i][2]]
"""iterating the triangle to produce a sequence of points and adding colors"""
N = 10000
points = []
points += y
points_red = []
points_blue = []
points_yellow = []
color_sequence = []
color_sequence += color_pt
for i in range(0, N + 5):
    j = np.random.randint(3)
    points += [(points[i] + corners[j]) / 2]
    color_sequence += [(color_sequence[i] + colors[j]) / 2]
    if i > 4:
        if j == 0:
            points_red += [(points[i] + corners[j]) / 2]
        elif j == 1:
            points_blue += [(points[i] + corners[j]) / 2]
        elif j == 2:
            points_yellow += [(points[i] + corners[j]) / 2]
points = points[5:]
color_sequence = color_sequence[5:]

# Plot problem 1a
plt.scatter(*zip(*corners))
plt.show()

#plot pronlem 1b
plt.scatter(*zip(*y))
plt.show()

# Plot problem 1d - Sierpinski Triangle
plt.scatter(*zip(*points), s=0.1)
plt.axis('equal')
plt.axis('off')
plt.show()

# Plot problem 1e - Adding colors
plt.scatter(*zip(*points_red), s=0.1, color = 'red')
plt.scatter(*zip(*points_blue), s=0.1, color = 'blue')
plt.scatter(*zip(*points_yellow), s=0.1, color = 'yellow')
plt.axis('equal')
plt.axis('off')
plt.show()

# Plot problem 1f - RGB
plt.scatter(*zip(*points), c=color_sequence, s=0.2)
plt.axis('equal')
plt.axis('off')
plt.show()

          
       

          
          

