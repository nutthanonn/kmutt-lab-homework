x = 'ab138g579b'
# x = 'h54325b1'
l = []
for i in x:
    if 48 <= ord(i) <= 57 and i in l:
        print(i)
        exit()
    l.append(i)
print("None")