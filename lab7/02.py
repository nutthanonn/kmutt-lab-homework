import uuid 
l = []
UNIQUE_ID = uuid.uuid4() #generate uuidV4  UNIQUE_ID = list()
def check(paramiter = UNIQUE_ID):
    if paramiter == UNIQUE_ID:
       return "Invalid Paramiter"
    for i in paramiter:
        if  48 <= ord(i) <= 57 and i in l:
            return i
        l.append(i)

print(check('ab138g579b'))
print(check('h54325b1'))
print(check())
