from cmath import sin
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import time
import scipy


def gradient_descent_by_dots_single_iteration(Z, dotx, doty, order): #единичная итерация поиска градиента на заднном пространсве точек 
    vectorlst = []
    dotx2 = dotx
    doty2 = doty
    is_minimum = True
    for i in range(order + 1):
        maxdif = 0
        vectorlst.append([dotx2, doty2])
        if (dotx > 0 and dotx < Z.shape[1]-1) and (doty > 0 and doty < Z.shape[0]-1):
            if (Z[dotx, doty] - Z[dotx-1, doty-1] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx-1, doty-1]
                dotx2 = dotx-1
                doty2 = doty-1
                is_minimum = False
            if (Z[dotx, doty] - Z[dotx-1, doty] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx-1, doty]
                dotx2 = dotx-1
                doty2 = doty
                is_minimum = False
            if (Z[dotx, doty] - Z[dotx-1, doty+1] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx-1, doty+1]
                dotx2 = dotx-1
                doty2 = doty+1
                is_minimum = False
            if (Z[dotx, doty] - Z[dotx, doty+1] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx, doty+1]
                doty2 = doty+1
                dotx2 = dotx
                is_minimum = False
            if (Z[dotx, doty] - Z[dotx+1, doty+1] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx+1, doty+1]
                dotx2 = dotx+1
                doty2 = doty+1
                is_minimum = False
            if (Z[dotx, doty] - Z[dotx+1, doty] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx+1, doty]
                dotx2 = dotx+1
                doty2 = doty
                is_minimum = False
            if (Z[dotx, doty] - Z[dotx+1, doty-1] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx+1, doty-1]
                dotx2 = dotx+1
                doty2 = doty-1
                is_minimum = False
            if (Z[dotx, doty] - Z[dotx, doty-1] > maxdif):
                maxdif = Z[dotx, doty] - Z[dotx, doty-1]
                doty2 = doty-1
                dotx2 = dotx
                is_minimum = False
            if is_minimum:
                pass

    return vectorlst
                
fig = plt.figure()
fig1 = plt.figure()
ax = fig.gca(projection='3d')

order = 1                                   # порядок метода (сколько векторов будут сложены в итоговый вектор)
startx = 0                                  # стартовое значение по Х
stopx = 5                                   # конечное значение по Х
resolutionx = 100                           # разрешение по Х (количество точек в диапазоне от startx до stopx)
stepx = abs((stopx-startx)/resolutionx)     # шаг по Х 
starty = 0                                  # стартовое значение по У
stopy = 5                                   # конечное значение по У
resolutiony = 100                           # разрешение по У
stepy = abs((stopy-starty)/resolutiony)     # шаг по У

X = np.arange(startx, stopx+stepx, stepx)
Y = np.arange(starty, stopy+stepy, stepy)
X, Y = np.meshgrid(X, Y)
R = np.sqrt((X-2.5)**2 + (Y-2.5)**2)
Z = np.sin(R)
Z3 = 0.5 + 0.125*(np.sin(np.power(0.9*X, 1.75))+np.sin(np.power(0.7*Y, 2.25)))



surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)


for i in range(1, Z.shape[1]-1):
    for j in range(1, Z.shape[0]-1):
        if (i % (order + 3) == 0) and (j % (order + 3) == 0):
            vectors = gradient_descent_by_dots_single_iteration(Z, i, j, order)
            plt.arrow(-vectors[0][0], -vectors[0][1], -vectors[order][0] + vectors[0][0], -vectors[order][1] + vectors[0][1], width = 0.4)


plt.show()