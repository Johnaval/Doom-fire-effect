import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
import random

class DoomFireEffect:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.width = 100
        self.height = 37
        colors = [[7,7,7],[31,7,7],[47,15,7],[71,15,7],[87,23,7],[103,31,7],[119,31,7],[143,39,7],[159,47,7],[175,63,7],[191,71,7],[199,71,7],[223,79,7],[223,87,7],
                  [223,87,7],[215,95,7],[215,95,7],[215,103,15],[207,111,15],[207,119,15],[207,127,15],[207,135,23],[199,135,23],[199,143,23],[199,151,31],[191,159,31],
                  [191,159,31],[191,167,39],[191,167,39],[191,175,47],[183,175,47],[183,183,47],[183,183,55],[207,207,111],[223,223,159],[239,239,199],[255,255,255]]
        for color in colors:
            for j in range(3):
                color[j] = color[j]/255
        self.cm = LinearSegmentedColormap.from_list('fireCmap', colors, N=37)

    def createDataStructure(self):
        self.data = np.zeros((self.height, self.width), dtype=int)
        for i in range(self.width):
            self.data[0][i] = 36
        self.plot = self.ax.imshow(self.data, cmap=self.cm, origin='lower')
        return self.plot

    def calculateFire(self, k):
        for i in range(1, self.height):
            for j in range(self.width):
                self.decay = random.randrange(1,3,1)
                x = self.data[i-1][j] - self.decay
                if x >= 0:
                    self.data[i][j-self.decay] = x
                else:
                    self.data[i][j-self.decay] = 0
        self.plot.set_data(self.data)
        return self.plot

    def renderFire(self):
        ani = FuncAnimation(self.fig, self.calculateFire, init_func = self.createDataStructure, interval=100)
        plt.show()
    

fireEffect = DoomFireEffect()
fireEffect.renderFire()
