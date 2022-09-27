

def help():
    print('   A ', '  B ', '  C')
    print('1: A1 | B1 | C1')
    print('2: A2 | B2 | C2')
    print('3: A3 | B3 | C3')


validation = ['A', 'B', 'C', 1, 2, 3]

first_row = ['_', '_', '_']
second_row = ['_', '_', '_']
third_row = ['_', '_', '_']

print()
print('TIC TAC TOE\n')
print('   A ', ' B ', ' C')
print('1: _ | _ | _')
print('2: _ | _ | _')
print('3: _ | _ | _')

print()
print('Type "help" for guidence.')
move = input('Make your move: ').upper()


# validation with 2 ranges from the list
