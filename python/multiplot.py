import numpy as np 
from matplotlib import pyplot as plt

# Vars to edit points/window
xMin = 0
xMax = 3.5
xDelta = 0.125

# wereld constantes
luchtdruk = 1.01325*10**5
dichtheidLucht = 1.293

# waarden lijsten voor de plots
massaList = [45.49*10**-3, 
            48.4*10**-3]
oppList = [1.13*10**-3, 1.13*10**-3]

# vasr maken omdat het moet
massa = 0
oppervlak = 0

x = np.arange(xMin,xMax + xDelta,xDelta) #maak de lijst van x coordinaden die we willen berekenen, de xMax + XDelta is zodat we wel de xMax halen

# TODO: maak into dubble plots\
plt.suptitle("golfbal")

for i in range(1,3):
    plt.subplot(1,2,i)
    if i == 1:
        plt.title("zonder tape")
    else:
        plt.title("met tape")

    # waarden opstellen
    massa = massaList[i - 1]
    oppervlak = oppList[i - 1]

    # bereken de zooi voor het plotten
    Vmax = np.sqrt((1.01325*10**5)/1.293)
    λ = massa/(dichtheidLucht*oppervlak)
    y = Vmax*np.absolute(x/(x+λ)*(1+2*λ/x)**(1/2))

    plt.plot(x, y, color='b', label='1st order', marker = 'o')

    plt.axhline(Vmax, color='m', linestyle='--', label='Vmax')
    plt.annotate("Vmax = " + str(round(Vmax, 2)), xy=(0,Vmax), textcoords='offset points', xytext=(0,2)) # zet anotation bij de Vmax lijn (-15 voor algemeene plot)

    for i in range(len(x)):
        if x[i] == 1.0:
            print("snelheid na 1,0 meter: " + str(round(y[i], 8)))
            plt.annotate("v=" + str(round(y[i], 2)), xy=(x[i],y[i]), textcoords='offset points', xytext=(30,-15), ha='center',arrowprops=dict(arrowstyle="->"))

    plt.legend(loc=6)
    plt.grid(color='gray', linestyle='--', linewidth=1)

#stel legenda op en laat grafiek zien
plt.savefig("fig1.png")
plt.show()
