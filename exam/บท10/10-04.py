

"""
9
Shake It Off, Taylor Swift, Pop, 3:39
Rolling In The Deep, Adele, Pop, 3:48
Chandelier, Sia, Pop, 3:36
Roar, Katy Perry, Pop, 3:42
Hotel California, Eagle, Rock, 6:30
We Are the Champions, Queen, Rock, 2:59
Hello Dolly, Louis Armstrong, Jazz, 2:27
Bohemian Rhapsody, Queen, Rock, 5:55
Coward of the County, Kenny Rogers, Country, 4:02


Rock --> 15:24
Pop --> 14:45
Country --> 4:02

"""

n = int(input())
type_time = {}
for i in range(n):
    temp = input().split(", ")
    type_song = temp[2]
    time_song = [int(x) for x in temp[3].split(":")]
    if type_song not in type_time:
        type_time[type_song] = time_song[0]*60 + time_song[1]
    else:
        type_time[type_song] += time_song[0]*60 + time_song[1]
sort_dic = {k: v for k, v in sorted(
    type_time.items(), key=lambda item: item[1], reverse=True)}
c = 0
for i in sort_dic:
    if c == 3:
        break
    m = sort_dic[i] // 60
    s = str(sort_dic[i] - 60*m).zfill(2)
    print(f"{i} --> {m}:{s}")
    c += 1
