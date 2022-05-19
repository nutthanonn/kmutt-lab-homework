"""
print(is_coprime(2,3,6),is_coprime(2,4,8))
True False


print(primitive_Pythagorean_triples(10))
[[3, 4, 5]]


print(primitive_Pythagorean_triples(20))
[[3, 4, 5], [5, 12, 13], [8, 15, 17]]

"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    return gcd(a, b) == 1 or gcd(a, c) == 1 or gcd(c, b) == 1


def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(3, max_len+1):
        for a in range(3, c):
            for b in range(a, c+1):
                if a**2 + b**2 == c**2 and is_coprime(a, b, c):
                    triple.append([a, b, c])
    return triple


exec(input().strip())
