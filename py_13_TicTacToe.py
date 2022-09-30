import time, sys


first_row = ['[ ]', '[ ]', '[ ]']
second_row = ['[ ]', '[ ]', '[ ]']
third_row = ['[ ]', '[ ]', '[ ]']

symbol_firsp = ['X', '0']
symbol_secondp = ['X', '0']

def help():
    print('   A ', '  B ', '  C')
    print('1: A1 | B1 | C1')
    print('2: A2 | B2 | C2')
    print('3: A3 | B3 | C3')


def current_table():
    print('  ', ' A ', ' B ', ' C')
    print('1: ' + first_row[0] + ' ' + first_row[1] + ' ' + first_row[2])
    print('2: ' + second_row[0] + ' ' + second_row[1] + ' ' + second_row[2])
    print('3: ' + third_row[0] + ' ' + third_row[1] + ' ' + third_row[2])



print('\n')
print('---TIC TAC TOE---')
print('Guide:')
help()
print()



selected_symbol = input('First Player which symbol do you want to play with?(X or 0) ').upper()
while selected_symbol not in symbol_firsp:
    selected_symbol = input('Come on buddy, you can make it. X or 0? ').upper()
    
if selected_symbol == 'X':
    print()
    print('Second Player, your`s will be: 0')
elif selected_symbol == '0':
    print()
    print('Second Player, your`s will be: X')

playchar = ' ' + selected_symbol + ' ' #make sure the step graphicly align in the 3x3 matrix

symbol_secondp.remove(selected_symbol)    
second_playchar =  ' ' + symbol_secondp[0] + ' '  #the second player`s symbol


time.sleep(1)
print()
current_table()


def first_user_moves():
    if move[1] == '1':
        if move[0] == 'A':
            first_row[0] = playchar
        elif move[0] == 'B':
            first_row[1] = playchar
        elif move[0] == 'C':
            first_row[2] = playchar
           
    if move[1] == '2':
        if move[0] == 'A':
            second_row[0] = playchar
        elif move[0] == 'B':
            second_row[1] = playchar
        elif move[0] == 'C':
            second_row[2] = playchar
  
    if move[1] == '3':
        if move[0] == 'A':
            third_row[0] = playchar
        elif move[0] == 'B':
            third_row[1] = playchar
        elif move[0] == 'C':
            third_row[2] = playchar


def second_user_moves():
    if move[1] == '1':
        if move[0] == 'A':
            first_row[0] = second_playchar
        elif move[0] == 'B':
            first_row[1] = second_playchar
        elif move[0] == 'C':
            first_row[2] = second_playchar
           
    if move[1] == '2':
        if move[0] == 'A':
            second_row[0] = second_playchar
        elif move[0] == 'B':
            second_row[1] = second_playchar
        elif move[0] == 'C':
            second_row[2] = second_playchar
  
    if move[1] == '3':
        if move[0] == 'A':
            third_row[0] = second_playchar
        elif move[0] == 'B':
            third_row[1] = second_playchar
        elif move[0] == 'C':
            third_row[2] = second_playchar


def win():
    #ROWS
    if first_row[0] in [playchar, second_playchar] and first_row[0] == first_row[1] == first_row[2] or \
        second_row[0] in [playchar, second_playchar] and second_row[0] == second_row[1] == second_row[2] or \
        third_row[0] in [playchar, second_playchar] and third_row[0] == third_row[1] == third_row[2]:
        print()
        current_table()
        print()
        print('Congraulations ' + player[i] + '! What a bloody legend!')
        print()
        sys.exit()
    #COLUMS
    elif first_row[0] in [playchar, second_playchar] and first_row[0] == second_row[0] == third_row[0] or \
        first_row[1] in [playchar, second_playchar] and first_row[1] == second_row[1] == third_row[1] or \
        first_row[2] in [playchar, second_playchar] and first_row[2] == second_row[2] == third_row[2]:
        print()
        current_table()
        print()
        print('Congraulations ' + player[i] + '! What a bloody legend!')
        print()
        sys.exit()
    #DIAGONALS
    elif first_row[0] in [playchar, second_playchar] and first_row[0] == second_row[1] == third_row[2] or \
        first_row[2] in [playchar, second_playchar] and first_row[2] == second_row[1] == third_row[0]:
        print()
        current_table()
        print()
        print('Congraulations ' + player[i] + '! What a bloody legend!')
        print()
        sys.exit()
        


player = ['First Player', 'Second Player']


user_move_list = []
i=0


while len(user_move_list) < 9:                             
            move = input('Make your move ' + player[i] + ': ').upper()
            
            if len(move) == 2 and move not in user_move_list and move[0] in ['A', 'B', 'C'] and move[1] in ['1', '2', '3']:
                user_move_list = user_move_list + [move]   #for validation, make sure the user not moving to an already allocated position
                if i == 0:
                    first_user_moves()
                    if win():
                        print()
                else:
                    second_user_moves()
                    if win():
                        print()
                
                print()   
                current_table()
                print()
                i = (i + 1)%2
            else:
                print()
                print('Wrong step buddy, try again.')


if len(user_move_list) == 9:
        print('It`s a draw!')
        print()