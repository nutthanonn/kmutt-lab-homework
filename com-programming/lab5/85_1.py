"""
TEST CASE

['abba','babana','ann']
a

"""


seq = input()[1:-1].split(",")
c = input()
d = [i.count(c) for i in seq]
print(d)
