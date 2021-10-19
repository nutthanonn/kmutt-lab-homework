import math

def trigonometry(x):
    number = []
    a = 0
    for i in range(17):
        print(str(a) + "     " + str(math.sin(math.pi/180 * a)))
        print(" "*(len(str(a)) + 5) + str(math.cos(math.pi/180 * a)))
        a += 22.5
        print("--------------------------------")

trigonometry(0)
