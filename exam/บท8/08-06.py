"""
print(text2keys("I am busy.")) 
444 0 2 6 0 22 88 7777 999


print(keys2text("444 0 2 6 0 22 88 7777 999"))
i am busy



"""


temp = {
    " ": 0,
    "abc": 2,
    "def": 3,
    "ghi": 4,
    "jkl": 5,
    "mno": 6,
    "pqrs": 7,
    "tuv": 8,
    "wxyz": 9,
}


def text2keys(text):
    txt = []
    for i in text.lower():
        for j in temp:
            if i in j:
                index_of = j.index(i) + 1
                txt.append(index_of*str(temp[j]))
    return txt


def keys2text(keys):
    global temp
    const = keys.split()
    txt = ""
    for i in const:
        keys_list = list(temp)
        if i == "0":
            txt += " "
        else:
            txt += keys_list[int(i[0])-1][len(i)-1]
    return txt


exec(input().strip())
