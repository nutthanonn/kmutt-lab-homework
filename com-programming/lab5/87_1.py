
"""
TEST CASE
10

"""

n = int(input())
xx = [int(i) for i in range(1, (n//2)+1)
      if n % i == 0]
nn = [int(x) for x in range(2, n-1)
      if x not in xx]

print(xx)
print(nn)
