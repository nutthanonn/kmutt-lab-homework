"""
p1 = [(3,6),(2,4),(1,1),(-1,0)]
p2 = [(3,4),(-1,1)]
print(add_poly(p1, p2))
[(3, 6), (5, 4), (-1, 0)] 


p1 = [(3,6),(2,4)]
p2 = [(1,4),(-1,2)]
print(mult_poly(p1, p2))
[(3, 10), (-1, 8), (-2, 6)] 


"""


def add_poly(p1, p2):
    new_dict = dict([(i, j)for j, i in p2])
    print(new_dict)
    for i, j in p1:
        if j in new_dict:
            new_dict[j] += i
        else:
            new_dict[j] = i
    return [(new_dict[i], i) for i in sorted(new_dict)[::-1] if new_dict[i] != 0]


def mult_poly(p1, p2):
    p = {}
    for c1, e1 in p1:
        for c2, e2 in p2:
            e = e1+e2
            c = c1*c2
            if e in p:
                p[e] += c
            else:
                p[e] = c
    return[(p[e], e)for e in sorted(p)[::-1] if p[e] != 0]


for i in range(3):
    exec(input().strip())
