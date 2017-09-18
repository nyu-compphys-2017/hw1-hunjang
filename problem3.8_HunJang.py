# -*- coding: utf-8 -*-
from math import *
from pylab import *
from numpy import *

#3.8-(1) solution
data = loadtxt("/Users/janghun/Desktop/NYU1stY/Comphy/hw1-hunjang/millikan.txt",float) # loading data  

print data

title("Millikan Data")
xlabel("Frequency f in Hertz")
ylabel("Voltages V in volts")

scatter(data[:,0],data[:,1])
show()

#3.8-(2) solution

E_x = sum(data[:,0])/len(data[:,0])
E_y = sum(data[:,1])/len(data[:,1])
E_xx = sum(data[:,0]**2)/len(data[:,0])
E_xy = sum(data[:,0]*data[:,1])/len(data[:,0])
m = ((E_xy - E_x*E_y)/(E_xx-E_x**2))
c = ((E_xx*E_y-E_x*E_xy)/(E_xx-E_x**2))

print "m is",m,"and c is",c

#3.8-(3) solution

calculatedY = [m*x_i+c for x_i in data[:,0]] # the fitting line

plot(data[:,0],calculatedY,"r-")
grid()
show()

#3.8-(4) solution
e_charge = 1.602e-19 #Coulomb unit.
workfunction = c

PlanckConst_exp = m*e_charge
PlanckConst_ac = 6.62607004e-34

Difference = (PlanckConst_exp-PlanckConst_ac)/PlanckConst_ac*100 # the difference rate of h_exp to h_ac
print "Planck constant 'h_exp' calculated from Millikan experiment is", PlanckConst_exp,". On the contrary, the accepted constant 'h_ac' is", PlanckConst_ac
print "The difference rate is", Difference,"%, which means that the h_exp is smaller than h_ac only by",Difference,"% of the h_ac."