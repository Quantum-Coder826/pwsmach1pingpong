import numpy as np

result = []

# Vars to edit points
xMin = 0
xMax = 3.5
xDelta = 0.25

# constants for math


#* berekende extra constanten
Vmax = np.sqrt((1.01325*10**5)/1.293)
conv = (2.045*10**-3)/(2.293*(1.13*10**-3))

for x in np.arange(xMin, xMax, xDelta):
    #TODO breek consantes uit
    numbers = [x] # voeg de x posietie in
    numbers.append(np.sqrt((2*(1.01325*10**5)*(1.13*10**-3)*x)/(2.045*10**-3))) # bereken het 0ste orde model
    
    numbers.append(Vmax*abs(x/(x+conv)*(1+2*conv/x)**(1/2))) #! bereken het 1ste orde model BORKED
    
    result.append(numbers) 

np.savetxt("data/out.csv", result, delimiter=", ", fmt="% s") # verander de result list in een csv voor importeren.