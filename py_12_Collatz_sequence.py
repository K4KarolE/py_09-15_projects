
import sys
import time


def collatz():
    while True:
        number = input(
            'Add a positive, int number and I will "Collatz collapse" it for you. ')
        if number.isdigit():
            number = int(number)
            if number == 1:
                print()
                print('Come on bro, give me a bigger one. (That what she said.)')
            else:
                break
        else:
            print()
            print('Sorry buddy, it has to be a positive number.')
    return number


print()
dumber = collatz()
try:
    print()
    while True:
        if dumber % 2 == 0:
            dumber //= 2
            print(dumber)
            time.sleep(0.2)

        elif dumber == 1:
            break

        elif dumber % 2 == 1:
            dumber = dumber * 3 + 1
            print(dumber)
            time.sleep(0.2)


except KeyboardInterrupt:
    sys.exit()

print()
