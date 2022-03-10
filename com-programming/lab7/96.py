
x = input().lower().strip()
d = []
for i in set(x):
    d.append([-x.count(i), i])
d.sort()
for i in d:
    print(f"{i[1]} -> {-i[0]}")
