#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np


class Plot(object):

    def __init__(self):
        self.setXAxis()
        self.functs = []
        self.verts = []

    def prepare(self, d):
        a, b, c = d
        if b == 0:
            if a == 0:
                raise ValueError('Not a line.')
            else:
                self.verts.append(d)
        else:
            self.functs.append(d)

    def setXAxis(self, xmin = -10, xmax = 10):
        self.xmin = xmin
        self.xmax = xmax

    def reset(self):
        self.setXAxis()
        self.functs = []
        self.verts = []

    def plot(self, t, y, d):
        (a,b,c) = d
        plt.plot(t, y, label = '%.4g*x + %.4g*y = %.4g' % (a, b, c))

    def draw(self):
        for a, b, c in self.functs:
            t = np.array([self.xmin, self.xmax])
            y = (-a*1.0/b) * t + (c*1.0/b)
            self.plot(t, y, (a, b, c))
        for a, b, c in self.verts:
            x = c / a
            self.plot([x, x], plt.ylim(), (a, b, c))
        plt.axis('tight')
        plt.legend()
        plt.title('Exercices sur les droites')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    p = Plot()
    p.prepare((1,1,3))
    p.prepare((-2,1,-1))
    p.prepare((1,0,-5))
    p.draw()
    input()
