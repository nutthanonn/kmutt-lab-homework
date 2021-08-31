import math

a, b, c = [float(x) for x in input().split()]

inSqrt = b**2 - 4*a*c

if inSqrt < 0:
    print("No Solution in real number.")
else:
    ans = math.sqrt(inSqrt)
    PositiveNumber = (-b + ans) / (2*a)
    NegativeNumber = (-b - ans) / (2*a)

    if PositiveNumber == NegativeNumber:
        print(PositiveNumber)
        
    else:
        print(str(PositiveNumber) + ", " + str(NegativeNumber))