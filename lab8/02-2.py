queue = []
while True:
    q = int(input())
    if q < 0: break
    queue.insert(0, q)
print(*queue)