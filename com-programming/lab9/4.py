import math
import numpy as np
X = np.array([[3, 4], [5, 12], [24, 7]])

y = []
for i in range(len(X)):
    y.append(math.hypot(X[i][0], X[i][1]))
print(np.array(y))
