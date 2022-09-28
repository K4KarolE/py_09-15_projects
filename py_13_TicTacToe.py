import time

valid_list = ['A', 'B', 'C', 1, 2, 3]
# colomn = ['A', 'B', 'C']
# row = [1, 2, 3]

first_row = ['[ ]', '[ ]', '[ ]']
second_row = ['[ ]', '[ ]', '[ ]']
third_row = ['[ ]', '[ ]', '[ ]']

symbol_list = ['X', '0']
symbol_list_PC = ['X', '0']

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
print('TIC TAC TOE')


playcharORI = input('Which symbol do you want to play with?(X or 0) ').upper()
while playcharORI not in symbol_list:
    playcharORI = input('Come on buddy, you can make it. X or 0? ').upper()

playchar = ' ' + playcharORI + ' ' #make sure the step graphicly align in the 3x3 matrix

symbol_list_PC.remove(playcharORI)    
PC_char = symbol_list_PC[0]   #the symbol the PC will use

print()
current_table()
print('Type "help" for guidance.')
move = input('Make your move: ').upper()
user_move_list = [] + [move]   #for validation, make sure the user not moving to an already allocated position


def validation():
    if move not in user_move_list:
        validation = True
    if move[0] in valid_list[0:2]:
        validation = True
    if move[1] in valid_list[3:5]:
        validation = True
    else:
        validation = False


def user_moves():
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

user_moves()

print()   
current_table()
print()
# print(user_move_list)



    



        


