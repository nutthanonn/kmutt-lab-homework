import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
k = int(input())
for i in range(len(x)):  # col
    for j in range(len(x[i])):  # row
        if (i+1) % k == 0 and (j+1) % k == 0:
            x[i][j] = 2*x[i][j]
print(x)
