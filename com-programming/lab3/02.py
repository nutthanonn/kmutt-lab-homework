number = []
while True:
    num = input()
    if(num == 'q'):
        break
    else:
        number.append(float(num))

if len(number) == 0:
    print("No Data")
else:
    avg = sum(number) / len(number)
    print(f'{avg:.1f}') if avg.is_integer() else print(f'{avg:.2f}')