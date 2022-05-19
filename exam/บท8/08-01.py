"""

print(reverse({3:"A", 2:"B"}) == {"A":3, "B":2})    True
print(keys({3:33, 4:33, 5:55, 2:33}, 33))           [3, 4, 2]
print(keys({3:33, 4:33, 5:55, 2:33}, 9999))         []

"""


def reverse(d):
    return {d[x]: x for x in d}


def keys(d, v):
    return [x for x in d if d[x] == v]


exec(input().strip())
