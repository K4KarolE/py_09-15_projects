import random, time, sys

win = 0
loss = 0
draw = 0

list_of_answers = ('r','p','s')


def delay():
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)



def win_print():
    print('You win!')
    print('Win(' + str(win) + ') Loss(' + str(loss) + ') Draw(' + str(draw) + ')')
    print()

def loss_print():
    print('You lose!')
    print('Win(' + str(win) + ') Loss(' + str(loss) + ') Draw(' + str(draw) + ')')
    print()

def draw_print():
    print('It`s a draw!')
    print('Win(' + str(win) + ') Loss(' + str(loss) + ') Draw(' + str(draw) + ')')
    print()


print()
print()
print('ROCK PAPER SCISSORS')
print('(r)ock, (p)aper, (s)cissors or (q)uit ')
print()
# print('Win(' + str(win) + ') Loss(' + str(loss) + ') Draw(' + str(draw) + ')')


i = 1
while True:
    users_pick = input('What is your ' + str(i) + '.' + ' pick? ')
    i += 1
    my_pick = random.choice(list_of_answers)
    #print(users_pick)
    
    if users_pick == 'q':
        print()
        print('Sorry to see you go, thx for playing.')
        print()
        sys.exit()


#USERS PICK: ROCK    
    elif users_pick == 'r' and my_pick == 'p':
        print('ROCK versus')
        delay()
        print('PAPER')
        loss += 1
        loss_print()

    elif users_pick == 'r' and my_pick == 's':
        print('ROCK versus')
        delay()
        print('SCISSORS')
        win += 1
        win_print()

    elif users_pick == 'r' and my_pick == 'r':
        print('ROCK versus')
        delay()
        print('ROCK')
        draw += 1
        draw_print()


#USERS PICK: PAPER    
    elif users_pick == 'p' and my_pick == 'p':
        print('PAPER versus')
        delay()
        print('PAPER')
        draw += 1
        draw_print()

    elif users_pick == 'p' and my_pick == 's':
        print('PAPER versus')
        delay()
        print('SCISSORS')
        loss += 1
        loss_print()

    elif users_pick == 'p' and my_pick == 'r':
        print('PAPER versus')
        delay()
        print('ROCK')
        win += 1
        win_print()


 #USERS PICK: SCISSORS    
    elif users_pick == 's' and my_pick == 'p':
        print('SCISSORS versus')
        delay()
        print('PAPER')
        win += 1
        win_print()

    elif users_pick == 's' and my_pick == 's':
        print('SCISSORS versus')
        delay()
        print('SCISSORS')
        draw += 1
        draw_print()

    elif users_pick == 's' and my_pick == 'r':
        print('SCISSORS versus')
        delay()
        print('ROCK')
        loss += 1
        loss_print()

#USER`S ANSWER NOT PART OF R/P/S/Q
    elif users_pick not in list_of_answers:
        print()
        time.sleep(0.3)
        print('Bloody alphabet right?')
        loss += 1
        print()