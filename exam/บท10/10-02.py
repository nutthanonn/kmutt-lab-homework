"""
5
Chelsea Liverpool
ManU Liverpool
Liverpool ManU
Chelsea Arsenal
Everton ManCity
['Chelsea', 'Everton']


1
Liverpool WestHam
['Liverpool']


4
Arsenal ManCity
Arsenal Everton
Arsenal Tottenham
ManCity Arsenal
[]

"""


n = int(input())

score = {}
winner = []

for i in range(n):
    w, l = input().split()
    if w not in score:
        score[w] = 1

    if l not in score:
        score[l] = 1

    if l in score:
        score[l] = -1

for i in score:
    if score[i] == 1:
        winner.append(i)

print(sorted(winner))
