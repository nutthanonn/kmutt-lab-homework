"""
print(row_number([[0,8,7],[6,5,4],[3,2,1]], 0)) 
0


print(flatten([[0,8,7],[6,5,4],[3,2,1]])) 
[8, 7, 6, 5, 4, 3, 2, 1]


print(inversions([8,7,6,5,4,3,2,1])) 
28


print(solvable([[0,8,7],[6,5,4],[3,2,1]])) 
True

print(solvable([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,15,14,0]]))
False


print(solvable([[1,7,2,3], [6,0,8,4], [5,9,10,11], [13,14,15,12]]))
False

"""


def row_number(t, e):  # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        if e in t[i]:
            return i


def flatten(t):  # return a list of ints converted from list of lists of ints t
    return [y for x in t for y in x if y != 0]


def inversions(x):  # return the number of inversions of list x
    return int(len(x)*(len(x)-1)/2)


def solvable(t):  # return True if tiling t (list of lists of ints) is solvable
    if len(t) % 2 == 1:
        if inversions(flatten(t)) % 2 == 0:
            return True
    else:
        if inversions(flatten(t)) % 2 == 0:
            for i in range(len(t)):
                if 0 in t[i] and i % 2 == 1:
                    return True
        else:
            for i in range(len(t)):
                if 0 in t[i] and i % 2 == 0:
                    return True
    return False


exec(input().strip())  # do not remove this line
