#!/usr/bin/env python3
""" model.py: Simulates a neuron according to
Eugene M. Izhikevich: Simple Model of Spiking Neurons (2003) """
__author__  = "Christoph Bartsch";
__credits__ = ["Eugene M. Izhikevich"];
__license__ = "MIT";
__status__  = "Prototype";


import matplotlib.pyplot as plt


class Neuron:
    # The base neuron class that does all the computation.
    # For different neuron dynamics, change the parameters
    # a through d
    def __init__ (self, a, b, c, d):
        self.a = a;
        self.b = b;
        self.c = c;
        self.d = d;
        self.u = 0;
        self.v = 0;
        self.vecV = [];
        self.vecU = [];
        self.vecI = [];
    
    def Step(self, t = 0.1, I = 10):
        # Simulates a single step of length t with dc-voltage I
        # This corresponds directly to the paper
        self.u = self.u + t * (self.a * (self.b*self.v - self.u));
        self.v = self.v + t * (0.04 * (self.v*self.v) + 5* self.v + 140 - self.u +I);
        if (self.v >= 30):
            self.v = self.c;
            self.u = self.u + self.d;
    
    def Simulate (self, steps = 2000, I = [10]*2000):
        # Simulate number of steps with dc-voltage I
        #  I is a list, I[n] corresponds to I during step n.
        #  If the size of I is smaller than the number of steps,
        #  the last entry of I will be used for the remainder of the sim.
            
        for i in range (0, steps):
            _I = I[0];
            if (len (I) > 1):
                I = I[1:];
            self.Step(t=1, I = _I);
            self.vecV.append(self.v);
            self.vecU.append(self.u);
            self.vecI.append(_I);
    
    def Plot(self):
        Plot (self.vecV, self.vecU, self.vecI);



def Plot (vecV, vecU, vecI):
    # Plots the given vectors using matplotlib
    plt.plot(vecV, linestyle='solid');
    plt.plot(vecU, linestyle='dashdot');
    plt.plot(vecI, linestyle='dashdot');
    plt.legend(['v', 'u', 'I'], loc='upper right');
    plt.xlabel('mS');
    plt.ylabel('mV');
    plt.show();


if (__name__ == '__main__'):
    print ("Enter a b c d:");
    inp = list(map(float, input().split(' ')));
    neuron = Neuron(inp[0], inp[1], inp[2], inp[3])
    print ("Enter steps I:");
    inp = list(map(float, input().split(' ')));
    neuron.Simulate(steps=int(inp[0]), I=[inp[1]]);
    print (int (inp[0]));
    neuron.Plot();
