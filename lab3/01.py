max = 8
n = 6
check = max
# 8, 6



for i in range(1, max + 1):
    print("Multiplication table of " + str(i))
    if i == n:
        check = n
    for j in range(1, check + 1):
       print(i * j, end=" ")
    print()