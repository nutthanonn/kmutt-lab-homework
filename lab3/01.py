tos = 18
if tos >= 500:
        price = tos // 500
elif 500 > tos >= 100:
        price = tos // 100
elif 100 > tos >= 20:
        price = tos // 20
elif 20 > tos >= 5:
        price = tos // 5
elif 5 > tos >= 1:
        price = tos // 1

print(price)