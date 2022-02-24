"""

(Input)
Being with you I reign in university, the sporty look of mine energize my list. I am going outing in university email
Born in us, the spy of enemy is amoung us

(Output)
[0, 12, 5, 4, 1, 1, 1, 1, 1, 6, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 5, 1, 4, 3, 1, 7, 1, 1, 2, 1, 3, 3, 1, 3, 6, 3, 1, 1, 4, 6]


========================================================================================


(Input)
Being with you I reign in university, the sporty look of mine energize my list. I am going outing in university email
Being in us, the port of energy is out in universe

(Output)
[0, 1, 1, 1, 1, 1, 2, 14, 1, 4, 6, 4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 5, 1, 4, 3, 1, 1, 1, 6, 1, 2, 1, 3, 7, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]

"""

word = input()
newTxt = input()
Outtxt = []

for i in newTxt:
    pos = word.index(i)
    word = word[pos::]
    Outtxt.append(pos)

print(Outtxt)