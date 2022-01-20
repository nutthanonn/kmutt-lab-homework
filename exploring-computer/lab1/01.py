import math

x = float(input())
if x <= 0:
    print("Error")
else:
    f = math.pi*x - 3/x + 7*(x**5) - math.log(x, 10) - math.e**(-x)
    print(f)
