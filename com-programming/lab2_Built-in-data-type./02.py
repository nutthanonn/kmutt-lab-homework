a = input().split()
f = input()
j = 1
for i in range(len(a)):
    if a[i] == f:
        a[i] = str(j)
        j += 1
print(*a)


"""

เทสเคส ปรากฏช่องว่าง "  " เเต่ในขณะที่ Output ช่องว่างถูกตัดไปเหลือ " "

"""

word = input()
f = input()
i = 1
while word.find(f) != -1:
    word = word.replace(f, str(i), 1)
    i += 1
print(word)
