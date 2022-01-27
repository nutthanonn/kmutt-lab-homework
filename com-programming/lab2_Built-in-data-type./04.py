a = {}
for i in range(3):
    data = input().split()
    a[data[0]] = data[1]
serch = input()
print(a[serch])