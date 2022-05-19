"""
10
Robert Dick
William Bill
James Jim
John Jack
Margaret Peggy
Edward Ed
Sarah Sally
Andrew Andy
Anthony Tony
Deborah Debbie
4
John
Jim
Don
Debbie


Jack
James
Not found
Deborah



"""


n = int(input())
name_nickname = []

for i in range(10):
    name_nickname.append(input().split())

f = int(input())
find_name = []
for i in range(f):
    find_name.append(input())

for i in find_name:
    not_f = True
    for j in name_nickname:
        if i == j[0]:
            print(j[1])
            not_f = False
            continue
        elif i == j[1]:
            print(j[0])
            not_f = False
            continue
    if not_f:
        print("Not found")
