def triangle(nline, diff):
    a =  1
    for i in range(nline):
        print("*"*a)
        a += diff
triangle(4, 3)