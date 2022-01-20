from math import sin, cos, radians
r, theta = [float(x) for x in input().split()]
x = r*cos(radians(theta))
y = r*sin(radians(theta))

print(x,y)
