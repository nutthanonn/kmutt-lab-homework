"""

Dear Amanda I haven't knew how joyous life could be until I saw your face. My heart leaps like a hummingbird in flight every time I see your face. This is something I have never felt before, and it is you that inspires it.

"""

letter = "Dear Amanda I haven't knew how joyous life could be until I saw your face. My heart leaps like a hummingbird in flight every time I see your face. This is something I have never felt before, and it is you that inspires it."
letter = letter.replace(".", " ")
letterArr = letter.split()


code = {
    '.':' ',
    'in':'very',
    'Amanda' : 'Doctor',
    'haven\'t' : 'am',
    'knew' : 'now',
    'how' : 'in',
    'joyous' : 'great',
    'could' : 'threatening',
    'be' : 'danger,',
    'until' : 'please',
    'saw' : 'need',
    'face': 'help',
    'leaps' : 'beats',
    'hummingbird' : 'machine ',
    'flight' : 'alarmingly',
    'time' : 'hour,',
    'see' : 'need',
    'you' : 'the drug',
    'inspires' : 'causes',
}

newTxt = ""

for i in range(len(letterArr)):
    if i == 2:
        newTxt += "\n"
        
    if letterArr[i] in code:
        newTxt += code[letterArr[i]] + " "

    else:
        newTxt += letterArr[i] + " "

# for i in code:
#     if newTxt.find(i) != -1:
#         newTxt = newTxt.replace(i, code[i])


print(newTxt)