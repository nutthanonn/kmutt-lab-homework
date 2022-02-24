"""
TEST CASE

[[1,2,3],[4,5,6]]

"""


seq = input()[1:-1]
symbol = []
subNumber = []
txt_list = ""
for i in seq:
    if i == "[":
        symbol.append(i)

    elif len(symbol) > 0 and i != "[" and i != "]":
        txt_list += i

    elif i == "]":
        symbol.pop()
        subNumber.append([int(x) for x in txt_list.split(",")])
        txt_list = ""

sumAll = 0
for i in subNumber:
    sumAll += sum(i)
print(sumAll)
