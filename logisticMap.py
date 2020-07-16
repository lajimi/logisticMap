
# © 2020-2030 S. AMIR MOUSAVI LAJIMI All Rights Reserved
# https://linkedin.com/in/lajimi All Rights Reserved

import numpy as numpy
import matplotlib
#matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

plt.close("all")

def orbit(xInit,xLen,alpha):
    xVec  = [xInit for item in range(0,xLen)]
    for nx in range(1,xLen):
        xVec[nx] = (4 * alpha * xVec[nx-1] * (1 -  xVec[nx-1]))       
    
    return xVec

xInit = 0.25       # initial condition or where the orbit(s) starts
xLen  = 100         # the length of each orbit

alphaLen     = 1000  # the bifurcation/control parameter
alphaVec     = numpy.zeros(alphaLen)
alphaVec[0]  = 0.6
alphaMax     = 1.0
alphaInc     = (alphaMax - alphaVec[0]) / (alphaLen - 1)

for i in range(1,(alphaLen)):
    alphaVec[i] = alphaVec[i-1]  + alphaInc

xVec  = orbit(xInit,xLen,alphaVec[0])

xMatrix = numpy.array([xVec])

for na in range(1,alphaLen):
    xMatrix = (numpy.append(xMatrix, [orbit(xInit,xLen,alphaVec[na])])).reshape(na+1,xLen)

noItToPlot = 20
stItToPlot = xLen - noItToPlot   

alphaVecToPlot = [[alphaVec[na] for item in range(0,noItToPlot)] for na in range(0,alphaLen)]

xVecToPlot = [[xMatrix[na][stItToPlot + noIt] for noIt in range(0,noItToPlot)] for na in range(0,alphaLen)]

fig, ax = plt.subplots()
ax.scatter(alphaVecToPlot, xVecToPlot,s=1)

ax.set_title("Logistic Difference Equation Bifurcation Diagram")
ax.set_xlabel('Control/Bifurcation Parameter')
ax.set_ylabel('$x_k$')

plt.show()
