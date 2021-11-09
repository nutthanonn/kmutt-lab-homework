def mypi(n):
    y = 2
    summarry = 3    
    for i in range(1,n+1):
        if i%2 == 0:
            x = -(4 / (y*(y+1)*(y+2)))
            y += 2
            summarry += x
            i += 1
        else:
            x = 4 / (y*(y+1)*(y+2))
            y += 2
            summarry += x
            i += 1
    return [i,summarry]

for i in range(1, 31):
    pi = mypi(i)
    print(pi[0], pi[1])