"""

6
51234621: A, B, D, E, F
427613829: B, D, G, H, I
38216542: Z, B, D, J
423212822: AA, B1, C3, D
4126548: J, Z3
98871973331: Q, M, N
4126548

38216542


6
51234621: A, B, D, E, F
427613829: B, D, G, H, I
38216542: Z, B, D, J
423212822: AA, B1, C3, D
4126548: J, Z3
98871973331: Q, M, N
423212822

51234621
427613829
38216542 


6
51234621: A, B, D, E, F
427613829: B, D, G, H, I
38216542: Z, B, D, J
423212822: AA, B1, C3, D
4126548: J, Z3
98871973331: Q, M, N
98871973331

Not Found

"""


n = int(input())
temp = {}
for i in range(n):
    keyID, town = input().split(": ")
    temp[keyID] = town.split(", ")


visit = []
search = input()
for i in temp[search]:
    for j in temp:
        if i in temp[j] and j != search:
            visit.append(j)
if len(visit) == 0:
    visit.append("Not Found")
for i in visit:
    print(i)
