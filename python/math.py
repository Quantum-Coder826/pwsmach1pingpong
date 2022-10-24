import numpy as np

# xList = np.array([])
# zeroThOrder = np.array([])
# firstOrder = np.array([])

result = []

for x in np.arange(0, 3.5, 0.25):
    numbers = [x]
    numbers.append(np.sqrt((2*(1.01325*10**5)*(1.12*10**-3)*x)/(2.045*10**-3)))
    numbers.append("test")

    result.append(numbers)

np.savetxt("out.csv", result, delimiter=", ", fmt="% s")