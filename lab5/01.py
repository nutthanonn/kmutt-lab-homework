def triangle(nline, diff):
    a =  1
    for i in range(nline):
        print("*"*a)
        a += diff

triangle(4, 3)
print("-"*15)
triangle(5, 2)