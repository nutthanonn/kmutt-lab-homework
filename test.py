import math

def trigonometry(x):
    number = []
    a = 0
    for i in range(17):
        s = "%.6f" %math.sin(math.radians(a))
        c = "%.6f" %math.cos(math.radians(a))
        print(str(a) + "     " + "sin ==> "+ str(s))
        print(" "*(len(str(a)) + 5) + "cos ==> " + str(c))
        a += 22.5
        print("<---------------------------------------------->")

trigonometry(0)
