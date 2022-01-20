data = []
p = 4
n = 10
count = 0
print('Period', end="   ")
for i in range(1, n+1):
    print(str(i) + "%", end="         ")
print()

for i in range(1, n+1):
    txt = 1 + (i * 0.010)
    data.append("%.3f" % txt)
    for j in range(2, p+1):
        a  = float(txt)**j
        data.append("%.3f" % a)

for i in range(p):
    p = 0
    print(i+1 ,end="     ")
    for j in range(n):
        print("|" +data[i+p]+"|", end="    ")
        p += 4
    print()