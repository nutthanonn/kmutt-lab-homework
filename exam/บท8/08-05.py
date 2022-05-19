
"""
5
Anthony Stark 086-111-1111
Henry Pym 087-222-2222
Robert Banner 088-333-3333
Steven Rogers 089-444-4444
Natasha Romanoff 091-555-5555
4
087-222-2222
Steven Rogers
Monica Rambeau
911


087-222-2222 --> Henry Pym
Steven Rogers --> 089-444-4444
Monica Rambeau --> Not found
911 --> Not found


"""


n = int(input())
name_tel = {}

for i in range(n):
    n, t = input().rsplit(" ", 1)
    name_tel[n] = t


nn = int(input())
order = []
for i in range(nn):
    order.append(input())

for i in order:
    check = True
    for j in name_tel:
        if i == j:
            print(f"{i} --> {name_tel[j]}")
            check = False
        elif name_tel[j] == i:
            print(f"{i} --> {name_tel[j]}")
            check = False
    if check:
        print(f"{i} --> Not found")
