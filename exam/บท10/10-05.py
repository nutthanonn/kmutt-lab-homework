"""
Ted, bear
Pongo, dog
Fozzie, bear
Winnie-the-Pooh, bear
Nana, dog
Hello Kitty, cat
Scooby Doo, dog
Garfield, cat
Yogi, bear
Tom, cat
Sylvester, cat
Pluto, dog
Goofy, dog
q

"""

n = input()
temp = {}
while n != "q":
    name, type_animal = n.split(", ")
    if type_animal not in temp:
        temp[type_animal] = [name]
    else:
        temp[type_animal].append(name)
    n = input()
print(temp)
