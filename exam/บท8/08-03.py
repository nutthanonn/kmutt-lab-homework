
"""
AaBbbbbbbCcDddd 

b -> 7
d -> 4
a -> 2
c -> 2

"""


n = input().lower()
temp = {}
for i in n:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1
n = sorted([[-temp[x], x] for x in temp])
for i in n:
    print(f"{i[1]} --> {-i[0]}")
