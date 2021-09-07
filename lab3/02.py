import random
import math

name = []

ra = math.floor(random.random() * 100)
print(ra)

if 0 <= ra <= 10:
    name.append("Xingqui")

elif 10 < ra <= 35:
    check = ['Eula', 'Raiden']
    r = math.floor(random.random() * 2)
    name.append(check[r])

elif 35 < ra <= 65:
    check = ['Aleister', 'Riktor']
    r = math.floor(random.random() * 2)
    name.append(check[r])

elif 65 < ra <= 100:
    name.append("Vincent")

print(name[0])