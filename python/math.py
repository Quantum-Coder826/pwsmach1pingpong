import numpy as np

result = []
xMax = 3.5
xDelta = 0.25

#* berekende variabelen voor constanten
Vmax = None
conv = None

for x in np.arange(0, xMax, xDelta):
    numbers = [x] # voeg de x posietie in
    numbers.append(np.sqrt((2*(1.01325*10**5)*(1.12*10**-3)*x)/(2.045*10**-3))) # bereken het 0ste orde model
    numbers.append("test") # bereken het 1ste orde model

    result.append(numbers) 

np.savetxt("out.csv", result, delimiter=", ", fmt="% s") # verander de result list in een csv voor importeren.