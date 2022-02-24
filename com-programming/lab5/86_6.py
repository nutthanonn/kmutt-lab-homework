
"""
TEST CASE
1 1 1 1 1 1 1 1 1 1 2 3 4 4 4 5 5 6 6 7 7 7 7 8 8 8 9 9 9 9 9 

"""

list_x = [int(x) for x in input().split()]
list_x.sort()
new_list = []
for i in range(len(list_x) - 1):
    if list_x[i] != list_x[i+1]:
        new_list.append(list_x[i])
new_list.append(list_x[-1])
print(new_list)
