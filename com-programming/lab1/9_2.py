a, b, c = input().split()
txt = a + b + c
txt += txt[0:2] * int(c)
print(txt)