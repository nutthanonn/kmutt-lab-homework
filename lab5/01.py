def triangle(nline, diff):
    a =  1
    for i in range(nline):
        print("*"*a)
        a += diff
nline = int(input())
diff = int(input())
triangle(nline, diff)