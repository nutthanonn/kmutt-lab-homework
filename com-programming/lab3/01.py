word = input()
longword = input()
i = 0 
while longword.find(word) != -1:
    longword = longword.replace(word, str(), 1)
    i += 1
print(i)
