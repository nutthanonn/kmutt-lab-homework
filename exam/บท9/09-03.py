"""

A=read_matrix();print(mult_c(0.5,A))
3
1 2
2 3
3 2

[[0.5, 1.0], [1.0, 1.5], [1.5, 1.0]]





A=read_matrix();B=read_matrix();print(mult(A,B))
3
1 2 3
1 1 1
2 2 2
3
1 2
2 3
3 2

[[14.0, 14.0], [6.0, 7.0], [12.0, 14.0]]

"""


def read_matrix():
    m = []
    nrows = int(input())
    for _ in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    new_matrix = []
    for i in A:
        temp = []
        for j in i:
            temp.append(j*c)
        new_matrix.append(temp)
    return new_matrix


def mult(A, B):
    new_matrix = []
    for i in A:
        temp = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(i)):
                s += B[k][j] * i[k]
            temp.append(s)
        new_matrix.append(temp)
    return new_matrix


exec(input().strip())
