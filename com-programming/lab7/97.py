N = int(input())
total_sales = 0
shop = {}
top_sell = {}
for i in range(N):
    k, v = input().split()
    shop.update({k: v})

M = int(input())
for i in range(M):
    km, vm = input().split()
    if km in shop:
        total_sales += int(shop[km])*int(vm)
        if km not in top_sell:
            top_sell.update({km: int(shop[km])*int(vm)})
        else:
            top_sell[km] += int(shop[km])*int(vm)


max_val = top_sell[max(top_sell)]


if total_sales == 0:
    print("No ice cream sales")
else:
    print(f"Total ice cream sales: {round(total_sales,1)}")

print("Top sales: ", end="")
for i in top_sell:
    if top_sell[i] == max_val:
        print(i, end=" ")


# เขียนแบบเพิ่งนอนได้ 2 ชม ค่ตเบลอ