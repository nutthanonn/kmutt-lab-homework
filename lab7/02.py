l = []
def check(paramiter = "none"):
    if(paramiter == "none"):
       return "Invalid Number"
    for i in paramiter:
        if  48 <= ord(i) <= 57 and i in l:
            return i
        l.append(i)
        
print(check('ab138g579b'))
print(check('h54325b1'))
print(check())
