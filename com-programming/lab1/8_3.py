from math import sqrt
x1, y1, x2, y2 = [float(x) for x in input().split()]

min_distance = sqrt((x2-x1)**2 + (y2-y1)**2)
print(min_distance)