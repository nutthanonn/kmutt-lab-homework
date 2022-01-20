def calc(x):
    group = x.split() #['number-1', 'symbol', 'number-2' ,'symbol' , 'number-3']
    symbol = group[1::2]
    number = group[::2]
    if len(group) == 1: 
        return group[0]
    score = float(number[0])
    for i in range(len(symbol)): 
        if symbol[i] == "+": 
            score += float(number[i+1])
        elif symbol[i] == "-": 
            score -= float(number[i+1])
        elif symbol[i] == "*": 
            score *= float(number[i+1])
        else: 
            score /= float(number[i+1])
    return '%.2f'% score

print(calc('1 + 2 + 3 + 4 + 5 + 6'))
print(calc('1.11 + 1.11 * 2'))
print(calc("1023.5 + 4 - 17"))
print(calc("12.34"))