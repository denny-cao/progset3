import numpy as np

A = np.array([1, 2, 3])
B = A

B[0] = 100
print(A)  # [100 2 3]
