

import sys


number = input('Give me a number and I will "Collatz collapse" it for you. ')

def collatz(number):
    if number % 2 == 0:
        number //=2
        print(number)
        return number 
    elif number % 1 == 1:
        number = number * 3 + 1
        print(number)
        return number

try:
    while True:
        if type(number) == int:
            collatz(number)
        
        elif type(number) != int:
            number = input('Give me a number and I will "Collatz collapse" it for you. ')
        
except KeyboardInterrupt:
    sys.exit()


x = type(333)
print(x)