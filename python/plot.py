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

x = np.arange(1,11) 

y1 = np.sqrt((2*luchtdruk*oppervlak*x)/massa)
y2 = Vmax*np.absolute(x/(x+λ)*(1+2*λ/x)**(1/2))

plt.title("Modellen geluidsnelheid") 
plt.xlabel("afstand (m)") 
plt.ylabel("snelheid (m/s)") 
plt.plot(x,y) 
plt.show()