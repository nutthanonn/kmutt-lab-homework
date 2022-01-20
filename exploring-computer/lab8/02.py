from random import randint

queue = []
while len(queue) != 10:
    n = randint(0, 9)
    if n not in queue: queue.append(n)
print(*queue)
 
while True:
    number = int(input())
    if number < 0: break
    queue.remove(number)
    queue.insert(0, number)
    print(*queue)
    