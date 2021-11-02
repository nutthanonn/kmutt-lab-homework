import uuid 
l = []
UNIQUE_ID = uuid.uuid4() #generate uuidV4 ถ้าจารไม่ให้ใช้เปลี่ยนเป็น -> UNIQUE_ID = list()
def check(paramiter = UNIQUE_ID):
    if paramiter == UNIQUE_ID:
       return "Invalid Number"
    for i in paramiter:
        if  48 <= ord(i) <= 57 and i in l:  # ord เป็นการเปลี่ยน ตัวอักษรให้อยู่ในเลข ASCII Table โดย รหัส Ascii 0-9 คือ ช่วงของ 48-57
            return i
        l.append(i)

print(check('ab138g579b'))
print(check('h54325b1'))
print(check())
