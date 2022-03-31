import os
word = [
    "Everything is half here,",
    "like the marble head",
    "of the Roman emperor",
    "and the lean torso",
    "of his favorite.",
    "The way the funnel cloud",
    "which doesn't seem",
    "to touch ground does—",
    "flips a few cars, a semi—",
    "we learn to..."
]

try:
    BASE_PATH = 'aa'
    os.mkdir(BASE_PATH)
except:
    print("You must have \"FileAlreadyExist\" exception handling")
    exit()

path_bb_1_1 = os.path.join(BASE_PATH, 'bb1', 'cc1')
path_bb_1_2 = os.path.join(BASE_PATH, 'bb1', 'cc2')
path_bb_1_3 = os.path.join(BASE_PATH, 'bb1', 'cc3')

path_bb_2_1 = os.path.join(BASE_PATH, 'bb2', 'cc1')
path_bb_2_2 = os.path.join(BASE_PATH, 'bb2', 'cc2')
path_bb_2_3 = os.path.join(BASE_PATH, 'bb2', 'cc3')

path_bb_3_1 = os.path.join(BASE_PATH, 'bb3', 'cc1')
path_bb_3_2 = os.path.join(BASE_PATH, 'bb3', 'cc2')
path_bb_3_3 = os.path.join(BASE_PATH, 'bb3', 'cc3')

lis = [
    path_bb_1_1,
    path_bb_1_2,
    path_bb_1_3,
    path_bb_2_1,
    path_bb_2_2,
    path_bb_2_3,
    path_bb_3_1,
    path_bb_3_2,
    path_bb_3_3
]

for i in lis:
    os.makedirs(i)
for filename in ('dd1.txt', 'dd2.txt', 'dd3.txt'):
    for i in lis:
        with open(os.path.join(i, filename), 'w') as stream:
            stream.write('\n'.join(word))

try:
    word_super = []
    for i in lis:
        path = os.path.abspath(i)
        d1 = "dd1.txt"
        d2 = "dd2.txt"
        d3 = "dd3.txt"

        d_lis = [d1, d2, d3]
        for i in range(3):
            with open(path + "/" + d_lis[i]) as f:
                lines = [line.rstrip() for line in f]
                word_super.append(lines)

    # super_dd
    with open(os.path.join(BASE_PATH, "super_dd.txt"), 'x') as stream:
        for i in word_super:
            stream.write('\n'.join(i))
            stream.write("\n------------------------------------------\n")
except:
    print("You must have \"File not Found\" Exception handling")
