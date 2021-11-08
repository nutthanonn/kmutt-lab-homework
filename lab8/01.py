def arnugrom(x):
    n = x*2
    return [n, n+1, n+2]

def calPi(n):
    pi = 3
    for i in range(1, n+1):
        symbol = "-" if i%2 == 0 else "+"
        suan = arnugrom(i)[0] * arnugrom(i)[1] * arnugrom(i)[2]
        if symbol == "-": pi -= 4 / suan
        else: pi += 4 / suan
    return pi

for i in range(int(input()) + 1):
    print(calPi(i))