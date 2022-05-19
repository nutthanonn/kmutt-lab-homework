"""
p={100:2, 50:2, 5:2, 1:2};print(total(p)) 
312


p={100:5};take(p,{100:2, 1:3});print(p)
{100: 7, 1: 3}


p={100:5};take(p,{100:0, 1:0});print(p)
{100: 5, 1: 0}


p={10:5, 1:7};print(pay(p, 12));print(p)
{10: 1, 1: 2}
{10: 4, 1: 5}


p={10:5, 1:7};print(pay(p, 18));print(p) 
{}
{10: 5, 1: 7}


p={10:5, 1:7};print(pay(p, 100));print(p)
{}
{10: 5, 1: 7}


p={10:5, 1:7};print(pay(p, 57));print(p)
{10: 5, 1: 7}
{10: 0, 1: 0}

"""


def total(pocket):
    total_p = 0
    for i, j in pocket.items():
        total_p += int(i)*int(j)
    return total_p


def take(pocket, money_in):
    for i in money_in:
        if i not in pocket:
            pocket[i] = money_in[i]
        else:
            pocket[i] += money_in[i]
    return pocket


def pay(pocket, amt):
    if total(pocket) < amt:
        return {}

    temp = {}
    for i in pocket:
        for _ in range(pocket[i]):
            if int(pocket[i]) != 0 and i <= amt:
                amt -= int(i)
                pocket[i] -= 1
                if i not in temp:
                    temp[i] = 1
                else:
                    temp[i] += 1

    if amt != 0:
        for i in temp:
            pocket[i] += temp[i]

    return temp if amt == 0 else {}


exec(input().strip())
