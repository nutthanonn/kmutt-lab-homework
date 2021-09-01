"""

TESTCASE!!!
775  307
1256 4E8


"""



concat = int(input())
string = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
remainderList = []
out = ""

# integerpart

quotien = 1


while concat != 0:
    quotien = concat // 16
    remainder =  concat % 16
    remainderList.append(remainder)
    concat = quotien

for i in reversed(remainderList):
    check = True
    for j in string:
        if i == j:
            out += string[j]
            check = False
    if check:
        out += str(i)
print(out)