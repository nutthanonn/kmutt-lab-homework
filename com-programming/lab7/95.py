"""
INPUT


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

----------------
OUTPUT

Jack
James
Not found
Deborah


"""


dict_name = {}
list_find = []
N = int(input())
for i in range(N):
    k, v = input().split()
    dict_name.update({k: v})
M = int(input())
for i in range(M):
    check = True
    word = input()
    for k, v in dict_name.items():
        if k == word:
            list_find.append(v)
            check = False
        elif v == word:
            list_find.append(k)
            check = False
    if check:
        list_find.append("Not found")
print("---------------")
for i in list_find:
    print(i)
