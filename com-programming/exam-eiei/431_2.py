"""

(Input)
Being with you I reign in university, the sporty look of mine energize my list. I am going outing in university email
[0,12,5,4,1,1,1,1,1,6,4,1,1,1,1,1,1,1,4,1,6,1,1,6,1,1,7,1,1,2,1,3,3,1,8,1,3,1,1,4,6]

(Output)
Born in us, the spy of enemy is amoung us

========================================================================================


(Input)
Being with you I reign in university, the sporty look of mine energize my list. I am going outing in university email
[0,1,1,1,1,1,18,1,1,1,6,4,1,1,1,1,1,2,1,1,1,2,6,1,1,6,1,1,1,1,6,1,2,1,3,12,1,1,4,1,1,1,1,1,1,1,1,1,1,5]

(Output)
Being in us, the port of energy is out in universe

"""


word = input()
txt = ""
position = 0
num = input()

#create list
if num.find(" ") == -1:
    lis = num[1:-1:].split(",")
else:
    lis = num[1:-1:].split(", ")


#main function
for i in lis:
    position += int(i)
    txt += word[position]
print(txt)

