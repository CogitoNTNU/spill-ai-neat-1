import matplotlib.pyplot as plt
import numpy as np

def scatterGenerations(generations):
    x = []
    y = []
    for gen, result in generations:
        x.append(gen)
        y.append(result)
    plt.scatter(x, y)
    plt.show()

def scatterWithTrend(generations):
    x = []
    y = []
    for gen, result in generations:
        x.append(gen)
        y.append(result)

    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r")
    plt.scatter(x, y)
    plt.show()


#Eksempel på input med tupler (a,b) hvor a er generasjonsnr og b er snittscore.
generations = [(1, 2), (2, 100), (3, 2), (4, 3), (5, 50), (6, 200), (7, 500)]
# scatterGenerations(generations)
scatterWithTrend(generations)


