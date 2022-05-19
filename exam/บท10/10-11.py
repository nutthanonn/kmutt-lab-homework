"""
Siam ChitLom
ChitLom PhloenChit
PhloenChit Nana
Siam NationalStadium
Ratchadamri Siam
Siam PhayaThai
Ratchadamri SalaDaeng
ThongLo Ekkamai
Ekkamai ThongLo
Siam


"""


station = {}

while True:
    n = input().split()
    if len(n) == 1:
        break
    way1, way2 = n
    if way1 not in station:
        station[way1] = set()
    if way2 not in station:
        station[way2] = set()

    station[way1].add(way2)
    station[way2].add(way1)

current = n[0]
res = station[current]
for i in station[current]:
    res = res.union(station[i])
for i in sorted(res):
    print(i)
