import numpy as np 
from matplotlib import pyplot as plt 

# Vars to edit points/window
xMin = 0
xMax = 3.5
xDelta = 0.125

# wereld constantes
luchtdruk = 1.01325*10**5
dichtheidLucht = 1.293

# vars for math
massa = 2.045*10**-3 # pingpongbal
oppervlak = 1.13*10**-3 # pingpongbal

# berekende extra constanten
Vmax = np.sqrt((1.01325*10**5)/1.293)
λ = massa/(dichtheidLucht*oppervlak)

x = np.arange(xMin,xMax + xDelta,xDelta) #maak de lijst van x coordinaden die we willen berekenen, de xMax + XDelta is zodat we wel de xMax halen

# defineer de formules
y1 = np.sqrt((2*luchtdruk*oppervlak*x)/massa)
y2 = Vmax*np.absolute(x/(x+λ)*(1+2*λ/x)**(1/2))

# plot de formules
plt.plot(x, y1, color='r', label='0th order', marker = 'o')
plt.plot(x, y2, color='b', label='1st order', marker = 'o')

# extra lijnen voor duidelijkheid
plt.axhline(343, color='k', linestyle='-', label='geluidssnelheid')
#plt.axhline(Vmax, color='m', linestyle='--', label='Vmax: ' + str(round(Vmax, 2)))

# code om bij elk punt x en y waarde te zetten
#for i in range(len(x)): # add values to points
#    plt.annotate( "(" + str(x[i]) + ";" + str(round(y2[i],2)) + ")", xy=(x[i], y2[i]), textcoords='offset points', xytext=(0,5), ha='center')

# zet namen op grafiek en assen + doe gridlines invoegen

# print de snelheid na 1 meter uit
for i in range(len(x)):
    if x[i] == 1.0:
        print("snelheid na 1,0 meter: " + str(round(y2[i], 8)))

plt.title("Model snelheid pingpongbal") 
plt.xlabel("loop lengte (m)") 
plt.ylabel("mondings snelheid (m/s)") 
plt.grid(color='gray', linestyle='--', linewidth=1)

#stel legenda op en laat grafiek zien
plt.legend()
plt.show()
