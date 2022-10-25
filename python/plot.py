import numpy as np 
from matplotlib import pyplot as plt 

# Vars to edit points/window
xMin = 0
xMax = 3.5
xDelta = 0.125

# constants for math
massa = 2.045*10**-3
luchtdruk = 1.01325*10**5
dichtheidLucht = 1.293
oppervlak = 1.13*10**-3

# berekende extra constanten
Vmax = np.sqrt((1.01325*10**5)/1.293)
λ = massa/(dichtheidLucht*oppervlak) 

x = np.arange(xMin,xMax,xDelta) 

y1 = np.sqrt((2*luchtdruk*oppervlak*x)/massa)
y2 = Vmax*np.absolute(x/(x+λ)*(1+2*λ/x)**(1/2))

plt.plot(x, y1, color='b', label='0th order')
plt.plot(x, y2, color='r', label='1st order')
plt.axhline(343, color='k', linestyle='-', label='geluidssnelheid')

# stel as namen op
plt.title("Modellen geluidsnelheid") 
plt.xlabel("afstand (m)") 
plt.ylabel("snelheid (m/s)") 

#stel legenda op en laat grafiek zien
plt.legend()
plt.show()