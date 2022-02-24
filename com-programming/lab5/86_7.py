
"""
TEST CASE
10

"""

n = int(input())
list_x = []
for i in range(2, n-1):
    for j in range(2, n//2-1):
        list_x.append(i*j)

list_x.sort()
new_list = []
for i in range(len(list_x) - 1):
    if list_x[i] != list_x[i+1]:
        new_list.append(list_x[i])
new_list.append(list_x[-1])

print(new_list)
