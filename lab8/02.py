from random import randint

number = []
while len(number) != 10:
    n = randint(0, 9)
    if n not in number: number.append(n)
print(*number)

while True:
    queue = int(input())
    if queue < 0: break
    number.pop(number.index(queue))
    number.insert(0, queue)
    print(*number)
    