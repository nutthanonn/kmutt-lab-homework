li = [0.2, -1000, 1000, 33.21, -101.12, 0.01, 212, 0.4, -0.3, -100]

# b1
# arr = list(map(lambda n: n+10000 if -0.5 < n < 0.5 else n, li))
# print(arr)

# b2
# arr = [x+10000 if -0.5 < x < 0.5 else x for x in li]
# print(arr)


# b3
arr = list(filter(lambda n: n > 0.5 or n < -0.5, li))
# print(arr)

# b4
arr = [x for x in li if x > 0.5 or x < -0.5]
# print(arr)

################################################################################################################################

# b5
global animals
animals = ['dogs', 'cats', 'birds', 'insects', 'rats']
inbox1 = ['cars', 'keys', 'computers']
inbox2 = ['chairs', 'cats', 'water']


def check_animals(box):
    for i in box:
        if i in animals:
            return "'" + i + "'"
    return "'not found'"


# kk = check_animals(inbox2)
# print(kk)
# kk = check_animals(inbox1)
# print(kk)

################################################################################################################################


# c1
testcase = "100111001"
stack = []
count = 0
for i in str(testcase):
    if len(stack) == 0:
        stack.append(i)

    if int(i) == 0 and int(stack[len(stack)-1]) == 1:
        count += 1
        stack.pop()

    elif int(i) == 1 and int(stack[len(stack)-1]) == 0:
        count += 1
        stack.pop()

print(count)

################################################################################################################################


# c2
def func_count(d):
    count = []
    for j in d:
        stack = []
        c = 0

        for i in str(d[j]):
            if len(stack) == 0:
                stack.append(i)

            if int(i) == 0 and int(stack[len(stack)-1]) == 1:
                c += 1
                stack.pop()

            elif int(i) == 1 and int(stack[len(stack)-1]) == 0:
                c += 1
                stack.pop()
        count.append(c)
    return {x: y for x, y in zip(d, count)}


temp = {'t1': 1010101, 't2': 1100110110}


temp_count = func_count(temp)
print(temp_count)


# finish time 10: 10

################################################################################################################################


a = [['k', [1, 2, 3]], ['j', [-1, -2, -3, -4]], ['m', []]]
new_a = {i[0]: i[1] for i in a if len(i[1]) != 0}
print(new_a)
