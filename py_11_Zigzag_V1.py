

#NO INPUT VALIDATION

import time

print()
print('ZIGZAG - Started as a normal zigzag. Now, if you wait enough it looks like an acid trip labirynth. It`s alive. It`s beautiful.')
paint =input('I will draw you a zigzag. Which characters should I use it for? ')
wide = input('How many characters wide should it be? ')

k=4
while True:
    
    for i in range(int(len(paint)+k)):
        print(' ' * i, paint * int(wide), ' ' * i, paint * int(wide), ' ' * i, paint * int(wide))
        time.sleep(0.1)

    for p in range(int(len(paint)+k),0,-1):
        print(' ' * p, paint * int(wide), ' ' * p, paint * int(wide), ' ' * p, paint * int(wide))
        time.sleep(0.1)

    k += 6

#DAMN BOY, WHERE IS THE EXIT?