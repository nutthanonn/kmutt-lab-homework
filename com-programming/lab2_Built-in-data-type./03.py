number = []
for i in range(6):
    num = tuple(int(x) for x in input().split())
    if num not in number:
        number.append(num)
print(number)