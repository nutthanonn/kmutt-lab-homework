
"""


L=[[50],[90]];first_fit(L,10);print(L)
[[50, 10], [90]]


L=[[50],[90]];best_fit(L,10);print(L)
[[50], [90, 10]]


print(partition_FF([50,90,10,80,50,20]))
[[50, 10, 20], [90], [80], [50]]


print(partition_BF([50,90,10,80,50,20]))
[[50, 50], [90, 10], [80, 20]]


"""


def first_fit(L, e):  # น า e ใสร่ ายการย่อยใน L ด้วยวิธี first fit
    for i in L:
        if sum(i) + e <= 100:
            i.append(e)
            return
    L.append([e])


def best_fit(L, e):  # น า e ใสร่ ายการย่อยใน L ด้วยวิธี best fit
    temp = [100-sum(i)-e if 100-sum(i)-e >= 0 else 100 for i in L]
    min_val = min(temp)
    if min_val == 100:
        L.append([e])
    else:
        L[temp.index(min_val)].append(e)


def partition_FF(D):  # คืนลิสต์ของลิสต์ที่ได้จากการแบ่งข ้อมูลใน D ด้วย first fit
    empty_list = []
    for i in D:
        first_fit(empty_list, i)
    return empty_list


def partition_BF(D):  # คืนลิสต์ของลิสต์ที่ได้จากการแบ่งข ้อมูลใน D ด้วย best fit
    empty_list = [[D[0]]]
    for i in D[1:]:
        best_fit(empty_list, i)
    return empty_list


exec(input().strip())
