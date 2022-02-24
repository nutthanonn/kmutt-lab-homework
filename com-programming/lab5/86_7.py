"""
TEST CASE
10

"""
n = int(input())
list_c = []
for i in range(2, n):
    x = []
    for j in range(2, n):
        if i*j < n:
            x.append(i*j)
    list_c.append(x)


list_x = [int(y) for x in list_c for y in x]
list_x.sort()
new_list = []
for i in range(len(list_x) - 1):
    if list_x[i] != list_x[i+1]:
        new_list.append(list_x[i])
new_list.append(list_x[-1])
print(new_list)
