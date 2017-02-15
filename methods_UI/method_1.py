# method_1 includes thoes methods about drawing lines
import matplotlib.pyplot as plt
import numpy as np

def resetPlot():

    X = np.linspace(0, 240, 240, endpoint = True)

    # Create new figure
    plt.figure(figsize = (12,6), dpi = 80)
    plt.subplot(111)

    # set limits, ticks
    plt.xlim(X.min() - 10, X.max() + 10)
    # plt.ylim(P.min(), P.max())

    plt.xticks([0,30,60,90,120,150,180,210,240])

    # show it
    # plt.show()

def drawLine(P):
    X = np.linspace(0, 240, 240, endpoint = True)
    plt.plot(X, P)

def drawAll():
    plt.show()

# #For testing
#
# #Create base line
X = np.linspace(0, 240, 240, endpoint = True)
P = np.random.random_sample(240) * 10 + 15
P1 = np.random.random_sample(240) * 10 + 5
P2 = np.random.random_sample(240) * 20 + 5
