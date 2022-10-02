import random
import time
import sys

win = 0
loss = 0
draw = 0

list_of_answers = ('r', 'p', 's')


print()
print()
print('ROCK PAPER SCISSORS')
print('(r)ock, (p)aper, (s)scissors or (q)uit ')
print()

i = 1

while True:
    users_pick = input('What is your ' + str(i) + '.' + ' pick? ')
    i += 1
    my_pick = random.choice(list_of_answers)

    if users_pick == 'q':
        print()
        print('Sorry to see you go, thx for playing.')
        print()
        sys.exit()

# USERS PICK: ROCK
    elif users_pick == 'r' and my_pick == 'p':
        print('ROCK versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('PAPER')
        loss += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

    elif users_pick == 'r' and my_pick == 's':
        print('ROCK versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('SCISSORS')
        win += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

    elif users_pick == 'r' and my_pick == 'r':
        print('ROCK versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('ROCK')
        draw += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

# USERS PICK: PAPER
    elif users_pick == 'p' and my_pick == 'p':
        print('PAPER versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('PAPER')
        draw += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

    elif users_pick == 'p' and my_pick == 's':
        print('PAPER versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('SCISSORS')
        loss += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

    elif users_pick == 'p' and my_pick == 'r':
        print('PAPER versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('ROCK')
        win += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

 # USERS PICK: SCISSORS
    elif users_pick == 's' and my_pick == 'p':
        print('SCISSORS versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('PAPER')
        win += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

    elif users_pick == 's' and my_pick == 's':
        print('SCISSORS versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('SCISSORS')
        draw += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()

    elif users_pick == 's' and my_pick == 'r':
        print('SCISSORS versus')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('ROCK')
        loss += 1
        print('Win(' + str(win) + ') Loss(' +
              str(loss) + ') Draw(' + str(draw) + ')')
        print()


# USER`S ANSWER IS NOT PART OF R/P/S/Q
    elif users_pick not in list_of_answers:
        print()
        time.sleep(0.3)
        print('Bloody alphabet right?')
        loss += 1
        print()
