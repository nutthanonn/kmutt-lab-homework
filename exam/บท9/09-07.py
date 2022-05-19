"""
print(pattern1(3,4)) [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(pattern2(3,4)) [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
print(pattern3(4)) [[1, 2, 3, 4], [0, 5, 6, 7], [0, 0, 8, 9], [0, 0, 0, 10]]
print(pattern4(4)) [[1, 3, 6, 10], [0, 2, 5, 9], [0, 0, 4, 8], [0, 0, 0, 7]]
print(pattern5(4)) [[1, 5, 8, 10], [0, 2, 6, 9], [0, 0, 3, 7], [0, 0, 0, 4]]
print(pattern6(4)) [[1, 7, 8, 10], [0, 2, 6, 9], [0, 0, 3, 5], [0, 0, 0, 4]]




"""


def pattern1(nrows, ncols):
    c = 1
    l = []
    for _ in range(nrows):
        t_l = []
        for _ in range(ncols):
            t_l.append(c)
            c += 1
        l.append(t_l)
    return l


def pattern2(nrows, ncols):
    l = []
    for i in range(nrows):
        c = i+1
        t_l = []
        for _ in range(ncols):
            t_l.append(c)
            c += 3
        l.append(t_l)
    return l


def pattern3(N):
    m = [[0]*N for _ in range(N)]
    c = 1
    for i in range(N):
        for j in range(i, N):
            m[i][j] = c
            c += 1
    return m


def pattern4(N):
    m = [[0]*N for _ in range(N)]
    c = 1
    for i in range(N):
        for j in reversed(range(i+1)):
            m[j][i] = c
            c += 1
    return m


def pattern5(N):
    m = [[0]*N for _ in range(N)]
    c = 1
    for i in range(N):
        for j in range(N-i):
            count_1 = i+j
            m[j][count_1] = c
            c += 1
    return m


def pattern6(N):
    m = [[0]*N for _ in range(N)]
    c = 1
    for i in range(N):
        if i % 2 == 0:
            for j in range(N-i):
                count_1 = i+j
                m[j][count_1] = c
                c += 1
        else:
            for j in reversed(range(N-i)):
                count_1 = i+j
                m[j][count_1] = c
                c += 1
    return m


exec(input().strip())
