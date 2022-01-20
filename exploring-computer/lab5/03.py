#python3 03.py 

def rectangle(width=5, height=5):
    for i in range(height):
        print("*"*width)

rectangle(3, 2)
print('-'*10)
rectangle(6)
print('-'*10)
rectangle(width=4)
print('-'*10)
rectangle(height=4)
print('-'*10)
rectangle()