# Create NumPy Arrays

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1)
print(type(arr1))



# Create Different Types of Arrays


import numpy as np

print(np.zeros(5))

print(np.ones(5))

print(np.arange(1, 11))

print(np.linspace(0, 100, 5))



# Mathematical Operations

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)

print(arr - 2)

print(arr * 5)

print(arr / 2)

print(arr ** 2)




# Array Calculations

import numpy as np

arr = np.array([5, 10, 15, 20, 25])

print("Sum =", np.sum(arr))

print("Mean =", np.mean(arr))

print("Maximum =", np.max(arr))

print("Minimum =", np.min(arr))

print("Standard Deviation =", np.std(arr))



# Practice with Two Arrays

import numpy as np

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

print("Addition:", a + b)

print("Subtraction:", b - a)

print("Multiplication:", a * b)

print("Division:", b / a)