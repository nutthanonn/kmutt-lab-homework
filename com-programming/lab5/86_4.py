"""
TEST CASE

1 1 1 1
1 1 1 1

"""

x = [int(j) for j in input().split()]
y = [int(j) for j in input().split()]
z = [int(x[i]+y[i]) for i in range(len(x))]
print(z)
