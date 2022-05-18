import os

BASE_PATH = "aa"
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


def createTxt(path):
    for i in range(1, 11):
        with open(os.path.join((BASE_PATH + "/" + path)[:-1], f"dd{i}.txt"), 'w') as stream:
            stream.write('\n'.join(word))


def makePath(path, curr, m):
    if curr == len(m):
        os.makedirs(os.path.join(BASE_PATH, path))
        createTxt(path)
        return

    for i in range(1, len(m)+1):
        path += f"{m[curr]}{i}/"
        makePath(path, curr+1)
        path = path[:-4]


m = ["bb", "cc", "dd", "ee", "ff"]
makePath("", 0, m)
