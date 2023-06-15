from numpy import random
import numpy as np
x = random.choice(['R','B'], size=(1))
y = random.randint(36, size=(1))

a = random.randint(0, 36, size=(36))
b = random.choice(['R', 'B'], size=(36))

# arr = np.concatenate((a,b))
arr = np.stack((a, b), axis=1)
print(arr)