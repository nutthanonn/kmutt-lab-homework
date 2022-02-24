"""
TEST CASE
[[1,2,3],[4,5,6],[7,8,9]]

"""

m = input()[1:-1]
symbol = []
subNumber = []
txt_list = ""
for i in m:
    if i == "[":
        symbol.append(i)
    if len(symbol) > 0 and i != "[" and i != "]":
        txt_list += i
    if i == "]":
        symbol.pop()
        subNumber.append(txt_list.split(","))
        txt_list = ""
symbol.clear()
for i in subNumber:
    symbol += i
print(symbol)
