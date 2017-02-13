import matplotlib.pyplot as plt
import numpy as np

def draw_line(P, X):
    # Create new figure
    plt.figure(figsize = (12,6), dpi = 80)
    plt.subplot(111)

    #Plot
    plt.plot(X, P, color = "black", linewidth = 1.0, linestyle = "-")

    # set limits, ticks
    plt.xlim(X.min() - 10, X.max() + 10)
    plt.ylim(P.min(), P.max())

    plt.xticks([0,30,60,90,120,150,180,210,240])

    # show it
    plt.show()

# Create base line
X = np.linspace(0, 240, 240, endpoint = True)
P = np.random.random_sample(240) * 10 + 5
