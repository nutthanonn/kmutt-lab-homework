# checkNumber = input()

# n12 = (11 - ((13*int(checkNumber[0]) +  12*int(checkNumber[1]) + 11*int(checkNumber[2]) + 10*int(checkNumber[3])
#                 + 9*int(checkNumber[4]) + 8*int(checkNumber[5]) + 7*int(checkNumber[6]) + 6*int(checkNumber[7])
#                 + 5*int(checkNumber[8]) + 4*int(checkNumber[9]) + 3*int(checkNumber[10]) + 2*int(checkNumber[11])) % 11)) % 10

# #123456789012
# #310030011214
# print(checkNumber[0], checkNumber[1:5], checkNumber[5:10], checkNumber[10:13], n12)







"""

number = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

numberInput = int(input())
for i in number: 
    if numberInput == i:
        print(str(numberInput) + " --> " + number[i])

"""






"""
import datetime

d, m, y = [a for a in input().split("/")]
x = datetime.datetime(2020, int(m), 1)
print(x.strftime("%B"), d + ", " + y)

"""







"""

print(str(input()).zfill(int(input())))

""" 




"""

print(sum([int(x) for x in input().split()]))

"""




"""

# [1, 3, 3, 4, 2]
# [1, 3, 3, 4, 2]
u = input()[1:-1].split(", ")
v = input()[1:-1].split(", ")

txt = '['
for i in u: txt += str(float(i)) + ", "
txt = txt[:-2:]
txt += '] + ['
for i in v: txt += str(float(i)) + ", "
txt = txt[:-2:]
txt += '] = ['

for i in range(len(u)): txt += str(float(int(u[i]) + int(v[i]))) + ", "
txt = txt[:-2:]
txt += "]"
print(txt)


"""

# print(f'{tax:,}')


