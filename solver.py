
import numpy as np
import math

items = 5
weights = np.array([1, 2, 4, 8, 16])
values = np.array([10, 40, 30, 20, 25])
backpack = 25
vmax = items*np.max(values)
dpTable = np.zeros((items, vmax))

# dpTable[i,j] is the minimal weight of a bag that has items from 1,..,i that their total value is j
# initialize first row
for j in range(1, vmax+1):
    dpTable[0, j-1] = math.inf
    for m, k in enumerate(values):
        if k == j:
            dpTable[0, j-1] = weights[m]


# dynamic programing
for i in range(1, items):
    for j in range(0, vmax):
        dpTable[i, j] = min(dpTable[i-1, j], dpTable[i-1, j-values[i]] + weights[i])



# get best
result=0
for j in range(1, vmax + 1):
    if (dpTable[items-1, vmax-j] <= backpack) and (result < dpTable[items-1, vmax-j]):
        result = dpTable[items-1, vmax-j]

#print(dpTable)
print("the total weight of your backpack that yields maximum profit is: {}".format(result))