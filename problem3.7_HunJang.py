# -*- coding: utf-8 -*-
from math import *
from pylab import *
from numpy import *
iterN_max=1000 # the Maximum number of Interations 
n=1000 # Grids size
xvalues = linspace(-2,2,n) # Partitions for x
yvalues = linspace(-2,2,n) # Partitions for y

MandelbrotSet = ones([n,n],int) # Backgrounds for making Mandelbrot set

for column,x in enumerate(xvalues): # Assigning x and y to their component numbers.
    for row,y in enumerate(yvalues): 
        z = 0+0j
        c = x+1j*y
        for i in range(iterN_max): # Interations loop
            z = z*z + c
        if abs(z)<=2: 
            MandelbrotSet[row,column] = 0 # Mandelbrot element indicator
            print "Processing"
            print "Processing..."

print "Complete!"

xlabel("Real part (x axis)")
ylabel("Imaginary part (y axis)")
title("Mandelbrot Set")
imshow(MandelbrotSet,origin="lower",extent=[-2,2,-2,2])
gray()
show()