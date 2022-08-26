"""

64090500431 ณัฐนนท์ ทองเจริญ

"""

import numpy as np


def f(M, L, m, r): return 12*M/r * (1-(1+r/12)**(-12*m)) - L


def BisectionInterest(M, L, m):
    a = 0.0000001
    b = 100.0
    epsilon = 1e-6
    c = (a+b)/2

    if np.sign(f(M, L, m, a)) == np.sign(f(M, L, m, b)):
        return "Error"

    while np.abs(f(M, L, m, c)) >= epsilon:
        if np.sign(f(M, L, m, a)) == np.sign(f(M, L, m, c)):
            a = c
        else:
            b = c
        c = (a+b)/2

    return c


M = 600
L = 150000
m = 30
eps = 1e-4
print(BisectionInterest(M, L, m))
