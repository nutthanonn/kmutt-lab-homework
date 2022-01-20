import random
import math

name = []
checkVincent = []
count = 0

for i in range(1, 1001):
# while len(checkVincent) != 350:
    if (i  % 100) == 0:
        print("Xingqui : " + str(name.count("Xingqui")))
        print("Raiden : " + str(name.count("Raiden")))
        print("Eula  : " + str(name.count("Eula")))
        print("Riktor : " + str(name.count("Riktor")))
        print("Aleister : " + str(name.count("Aleister")))
        print("Vincent : " + str(name.count("Vincent")))
        print("-----------------------------")
        name.clear()
    
    if len(checkVincent) == 350:
        print("Vincent more than 350")
        break
    
    ra = math.floor(random.random() * 100)

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
        checkVincent.append("Vincent")
    
    count += 1

print(len(checkVincent))
print("--------")
print(count)