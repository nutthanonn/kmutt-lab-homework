numAll = []
word = input()
for i in word:
    if 48 <= ord(i) <= 57:
        numAll.append(i)
notInList = []
for i in range(10):
    if str(i) not in numAll:
        notInList.append(i)
if len(notInList) == 0:
    print("None")
else:
    print(*notInList, sep = ",")
        