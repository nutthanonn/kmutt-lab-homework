"""
TESTCASE!!!!

sunny 50 t         play
cloudy 88 f        play
sunny 80 t         not play
rainy 66 true      not play 
rainy 66 false     play

"""


outlook, humidity, rainy = [x for x in input("outlook (sunny or cloudy or rainy), humidity (integer), and rainy (true or t or false or f): ").split(" ")]

checkOutlook = ['sunny', 'cloudy', 'rainy']


if outlook not in checkOutlook:
    print("Invalid outlook. Please try again.")
    exit()

if outlook == checkOutlook[0]:
    if int(humidity) > 75:
        print("not Play")
    else:
        print("Play")

elif outlook  == checkOutlook[1]:
    print("Play")

elif outlook == checkOutlook[2]:
    if rainy == "t" or rainy == 'true':
        print("not play")
    else:
        print("play")
