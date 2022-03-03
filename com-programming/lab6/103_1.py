"""
TESTCASE

5
Tom Engineering
Pam Arts
Jim Engineering
Tom Arts
Jenny Science
Engineering Arts


"""

n = int(input())
name_position = []
name = set()
for i in range(n):
    name_position.append(input().split())
word_name = [x for x in input().strip()]
for i in name_position:
    if i[1] in word_name:
        name.add(i[0])
print(*name)
