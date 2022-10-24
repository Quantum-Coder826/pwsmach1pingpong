import numpy as np
result = []

# Vars to edit points
xMin = 0
xMax = 3.5
xDelta = 0.25

# constants for math
massa = 2.045*10**-3
luchtdruk = 1.01325*10**5
dichtheidLucht = 1.293
oppervlak = 1.13*10**-3

#* berekende extra constanten
Vmax = np.sqrt((1.01325*10**5)/1.293)
λ = massa/(dichtheidLucht*oppervlak) #! BORKT
print(λ)

for x in np.arange(xMin, xMax, xDelta):
    #TODO breek consantes uit
    numbers = [x] # voeg de x posietie in
    numbers.append(np.sqrt((2*luchtdruk*oppervlak*x)/massa)) # bereken 0ste orde model
    
    numbers.append(Vmax*np.absolute(x/(x+λ)*(1+2*λ/x)**(1/2))) # bereken 1ste orde model
    
    result.append(numbers) 

np.savetxt("data/out.csv", result, delimiter=", ", fmt="% s") # verander de result list in een csv voor importeren.
