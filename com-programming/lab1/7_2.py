from math import log10

x = float(input())
y = 2 - x + 3/(7*x**2) - 5/(11*x**3) + log10(x)
print(y)