import math

r = float(input("Input the radius of the circle: "))

if r < 0:
    print("Error")
else:
    area = math.pi * (r**2)
    print("The area of the circle with radius " + str(r) + ' is ' + str('%.5f' % area))