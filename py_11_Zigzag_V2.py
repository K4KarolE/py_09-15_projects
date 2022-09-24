
import time, sys

charlenght = 4
chartype = '$'
push = 0
pushincreasing = True

try:
    while True:
        print(' ' * push, end = '')
        print(chartype * charlenght)
        time.sleep(0.2)

        if pushincreasing:
            push += 1
            if push == 20:
                pushincreasing = False

        else:
            push -=1
            if push == 0:
                pushincreasing = True        
        

except KeyboardInterrupt:
    sys.exit()

