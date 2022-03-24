import numpy as np
k = int(input())
if k % 2 == 0:
    k = int(k//2)
    m = np.array([[1, 0]*k])
    for i in range(1, k*2):
        if i % 2 == 0:
            l = [i+1, 0] * k
        else:
            l = [0, i+1] * k
        m = np.vstack([m, l])
else:
    k = int(k//2)
    m = np.array([[1, 0]*k+[1]])
    for i in range(1, k*2+1):
        if i % 2 == 0:
            l = [i+1, 0] * k + [i+1]
        else:
            l = [0, i+1] * k + [0]
        m = np.vstack([m, l])
print(m)
