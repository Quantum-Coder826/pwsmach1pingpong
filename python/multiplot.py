import numpy as np 
from matplotlib import pyplot as plt

# Vars to edit points/window
xMin = 0
xMax = 3.5
xDelta = 0.125

# wereld constantes
luchtdruk = 1.01325*10**5
dichtheidLucht = 1.293

# vars for math, eerst waarden voor zonder tape; 2de waarden met tape
massaList = [ 18.4*10**-3, 13.41*10**-3 ]
oppervlakList = [ 1.13*10**-3, 1.13*10**-3 ]

# berekende extra constanten
Vmax = np.sqrt((1.01325*10**5)/1.293)

x = np.arange(xMin,xMax + xDelta,xDelta) #maak de lijst van x coordinaden die we willen berekenen, de xMax + XDelta is zodat we wel de xMax halen

# defineer de formules
λ = None
y1 = Vmax*np.absolute(x/(x+λ)*(1+2*λ/x)**(1/2))

# TODO: maak into dubble plots

# alle titels en subplots opstellen
fig, axs = plt.subplots(1,2, sharey=True)
fig.suptitle("pingpongbal")
axs[0].set_title("zonder tape")
axs[1].set_title("met tape")
axs[0].grid(color='gray', linestyle='--', linewidth=1)
axs[1].grid(color='gray', linestyle='--', linewidth=1)


for ax in range(len(axs)):
    massa = massaList[ax]
    oppervlak = oppervlakList[ax]

    # bereken nodige constante
    λ = massa/(dichtheidLucht*oppervlak)

    # plot de lijn
    plt.plot(x, y1, color='b', label='1st order', marker = 'o')

    # extra lijnen voor duidelijkheid
    plt.axhline(343, color='k', linestyle='-', label='geluidssnelheid')
    plt.axhline(Vmax, color='m', linestyle='--', label='Vmax')
    plt.annotate("Vmax = " + str(round(Vmax, 2)), xy=(0,Vmax), textcoords='offset points', xytext=(0,5)) # zet anotation bij de Vmax lijn (-15 voor algemeene plot)

    # print de snelheid na 1 meter uit en invoegen in grafiek
    for i in range(len(x)):
        if x[i] == 1.0:
            print("snelheid na 1,0 meter: " + str(round(y1[i], 8)))
            plt.annotate("v=" + str(round(y1[i], 2)), xy=(x[i],y1[i]), textcoords='offset points', xytext=(30,-15), ha='center',arrowprops=dict(arrowstyle="->"))
            break



#stel legenda op en laat grafiek zien
plt.legend()
plt.show()
