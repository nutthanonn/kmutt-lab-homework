"""
TEST CASE

1 1 2 -3 -2 -2 -1 -2

"""

seq = input().split()
result = filter(lambda x: int(x) > 0, seq)
print(abs(len(seq) - len(list(result))))
