
"""
print(factor(200))
[[2, 3], [5, 2]]


print(factor(3298402)
[[2, 1], [29, 2], [37, 1], [53, 1]]



print(factor(8137740897))
[[3, 4], [11, 2], [13, 2], [17, 3]]


"""


import math


def factor(N):  # N เป็นจำนวนเต็มบวกมากกว่า 1
    temp = []
    for i in range(2, int(math.sqrt(N+1))):
        c = 0
        check = False
        if N % i == 0:
            check = True
            while N % i == 0:
                N = N // i
                c += 1
        if check:
            temp.append([i, c])
    return temp


exec(input().strip())
