from math import sin, cos, sqrt, atan

x, y = [float(x) for x in input().split()]
r = sqrt(x**2 + y**2)
theta = atan(y/x)

print(r,theta)