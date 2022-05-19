
"""
5
Magnum 50
Cornetto 25
PaddlePop 15
AsianDelight 20
Calippo 15
3
Cookie 20
MamaTomYum 3
MangoSheet 10

No ice cream sales




5
Magnum 50
Cornetto 25
PaddlePop 15
AsianDelight 20
Calippo 15
6
Magnum 5
Magnum 5
Cookie 20
MamaTomYum 3
Cornetto 20
AsianDelight 1

Total ice cream sales: 1020.0
Top sales: Cornetto, Magnum


"""


n = int(input())

icream = {}

for i in range(n):
    name, price = input().split()
    icream[name] = int(price)


total_order = int(input())
name_order = {}


for i in range(total_order):
    name_o, total = input().split()
    if name_o not in name_order:
        name_order[name_o] = int(total)
    else:
        name_order[name_o] += int(total)

total_price = {}


for i in name_order:
    for j in icream:
        if i == j:
            total_price[i] = icream[j]*name_order[i]
Total_sale = sum([total_price[x] for x in total_price])
sort_order = sorted([i for i in total_price if total_price[i]
                    == total_price[max(total_price)]])

if Total_sale == 0:
    print("No ice cream sales")
else:
    print(f"Total ice cream sales: {Total_sale}")
    print(f"Top sales: ", end="")
    print(*sort_order)
