"""
TESTCASE  เยอะ
"""


n = int(input())

l = []
for i in range(n):
    l.append(input().split())
find = input().split()


final = []

for i in l:
    if set(find).issubset(i):
        final.append(i)


if len(final) == 0:
    print("Not Found")
else:
    for i in sorted(final):
        print(*i)
