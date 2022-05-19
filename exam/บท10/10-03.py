"""
courses.txt
teachers.txt
database.txt

2110101,Sukree
2110101,Somchai
2100111,Sukree
2110200,Nattee
2110327,Nattee


courses.txt
teachers.txt
database2.txt

record error
2100111,Somchai
2110200,Nattee
record error


"""


courses = {}
teacher = {}
database = []

with open(input(), 'r') as file:
    for line in file:
        s = line.strip().split(',')
        courses[s[0]] = s[1]

with open(input(), 'r') as file:
    for line in file:
        s = line.strip().split(',')
        teacher[s[0]] = s[1]

with open(input(), 'r') as file:
    for line in file:
        s = line.strip().split(',')
        database.append({s[0]: s[1]})


print(courses)
print(teacher)
print(database)
l = []
for i in database:
    for j in i:
        if i[j] in teacher and j in courses:
            l.append(f"{courses[j]}, {teacher[i[j]]}")
        else:
            l.append("record error")
for i in l:
    print(i)
