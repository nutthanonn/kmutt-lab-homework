"""
TEST CASE

[1,2,3,-1,-2,-3]

"""


seq = input()[1:-1].split(",")
result = filter(lambda x: int(x) > 0, seq)
print(list(result))
