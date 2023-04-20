import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import cm, colors
from matplotlib import pyplot as plt

def func(x,y):
    return (-x**8 + 2 * x**7 + (1/2) * x**6 * y**2 - (1/2) * x**5 * y**2 - (1/8) * x**3 * y**4 + (11/8) * x * y**6 - (1/2) * y ** 8)/(x**6 + y**6)

fig = plt.figure()

x = np.linspace(0.1,5,100)
y = np.linspace(0.1,5,100)

X, Y = np.meshgrid(x,y)
Z = func(X, Y)

fig = plt.figure(figsize=(8,8))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.scatter(1.32245, 1.08505, func(1.32245,1.08505))
print(func(1.32245,1.08505))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()