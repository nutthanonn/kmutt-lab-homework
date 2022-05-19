"""


5
CP 1
ME 2
PE 1
CHE 1
MT 3
6
59301234521 23.6 PE CP MT CHE
59300799921 44.5 ME CP CHE PE
59300081621 37 PE CHE MT CP
59300653521 61.2 PE MT CP ME
59300002121 19.4 CHE CP ME CP
59300048721 7 ME CP CHE MT


"""


n = int(input())
c = {}
final = []
for i in range(n):
    name, total = input().split()
    c[name] = int(total)

m = int(input())
data_class = {}

for i in range(m):
    data = input().split()
    data_class[data[0]] = [float(data[1]), *data[2:]]

sort_dic = {k: v for k, v in sorted(
    data_class.items(), key=lambda item: item[1], reverse=True)}

for i in sort_dic:
    print(sort_dic[i])
    for j in sort_dic[i][1:]:
        if c[j] != 0:
            final.append([i, j])
            c[j] -= 1
            break
print("============")
for i in sorted(final):
    print(*i)
