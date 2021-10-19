#python3 02.py 

import math


def trigonometry(x):
    s = "%.15f" % math.sin(math.radians(x))
    c = "%.15f" % math.cos(math.radians(x))
    return [s, c]

a = 0
for i in range(int(360/22.5)+1):
    print()
    print(str(a), "     sin ->", trigonometry(a)[0], "    cos ->", trigonometry(a)[1])
    a += 22.5
    print()
    print("<------------------------------------------------------------------------->")
