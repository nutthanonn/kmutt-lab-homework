word = input()
l = []
for i in word:
    if  48 <= ord(i) <= 57 and i in l:
        print(i)
        exit()
    l.append(i)
print("none")