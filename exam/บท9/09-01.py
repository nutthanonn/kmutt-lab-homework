"""

7
n = int(input("n = "))
for k in range(2,n):
....if n%k == 0:
........print("composite..")
........break
else:
....print("prime.")


"""


n = int(input())
w = []
for i in range(n):
    stack = []
    word = input()
    for j in word:
        if j == ".":
            stack.append(".")

        if j != ".":
            break
    stack = stack[:len(stack)//2]
    if len(stack) != 0:
        w.append(word[len(stack)::])
    else:
        w.append(word)
for i in w:
    print(f"{i}")
