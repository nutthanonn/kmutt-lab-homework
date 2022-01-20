def sum_is_even(a, b):
   for i in range(a, b):
        check = sum([int(x) for x in list(str(i))])
        if check%2 == 0:
            print(i, end=",")

sum_is_even(5, 20)
print()
sum_is_even(95, 110)
print()
sum_is_even(990, 1010)