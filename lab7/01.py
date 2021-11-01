l = []
def check(x):
    for i in x:
        if  48 <= ord(i) <= 57 and i in l:
            return i
        l.append(i)
print(check('ab138g579b'))
print(check('h54325b1'))
