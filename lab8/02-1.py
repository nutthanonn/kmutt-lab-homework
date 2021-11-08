from random import randint
number = []
while len(number) != 10:
    n = randint(0, 9)
    if n not in number: number.append(n)
print(*number)