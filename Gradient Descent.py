# Suchea Rares-Andrei
# Group 917
# !!! What I've noticed: as b gets smaller, the gradient descent becomes slower !!!

import matplotlib.pyplot as plt
import numpy as np

#the function is f(x, y) = 1/2(x^2 + by^2), where b > 0
#the gradient is (2x, 2by)
def f(x, y, b):
    return 0.5 * (x**2 + b*(y**2))

#the step size (I computed it on paper)
def step(x, y, b):
    return (x**2 + (b*y)**2) / (x**2 + (b**3)*(y**2))

def next_iteration(x, y, s, b):
    return [(1 - s)*x, (1 - b*s)*y]

iterations = 5
x = np.zeros(iterations+2)
y = np.zeros(iterations+2)

#initial values
x[0] = 1
y[0] = 2

B = [1, 0.5, 0.2, 0.1]
for b in B:
    # gradient descent
    k = 0
    s = step(x[k], y[k], b)
    [x[k+1], y[k+1]] = next_iteration(x[k], y[k], s, b)

    successfulIterations = 1
    while k < iterations:
        print(k, x[k], y[k], f(x[k], y[k], b))
        k += 1
        s = step(x[k], y[k], b)
        [x[k+1], y[k+1]] = next_iteration(x[k], y[k], s, b)
        if not np.isnan(x[k+1]):
            successfulIterations += 1

    #create meshgrid for contour
    xList = np.linspace(-3, 3, 100)
    yList = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(xList, yList)
    Z = f(X, Y, b)

    #define the contour levels
    nLevels = successfulIterations
    levels = np.zeros(nLevels)
    for k in range(nLevels):
        levels[k] = f(x[k], y[k], b)
    levels = np.sort(levels)

    #plot the contour lines
    contours = plt.contour(X, Y, Z, levels, colors = 'black')
    plt.clabel(contours, inline=True, fontsize=8)

    #plot the gradient
    plt.plot(x[:iterations], y[:iterations], 'r--o')

    plt.show()
    print()













