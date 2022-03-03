"""

book

"""


x = input()
dic = {word: x.count(word) for word in set(x)}
print(dic)
