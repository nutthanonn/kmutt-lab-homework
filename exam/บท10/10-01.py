
"""
3
1 2 1 2 3 1 2 1 2 1
2 3
2 5 4 3




"""


n = int(input())

l = []

for i in range(n):
    l.append(set(input().split()))


u = l[0]
ins = l[0]
for i in range(1, n):
    u = u.union(l[i])
    ins = ins.intersection(l[i])
print(len(u))
print(len(ins))
