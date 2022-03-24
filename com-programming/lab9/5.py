import numpy as np
k = int(input())
if k % 2 == 0:
    k = int(k//2)
    m = np.array([[0, 1] * k, [1, 0] * k]*k)
else:
    k = int(k//2)
    m = np.array([([0, 1] * k)+[0], ([1, 0] * k)+[1]]*k)
    l = [0, 1]*k+[0]
    m = np.vstack([m, l])
print(m)
