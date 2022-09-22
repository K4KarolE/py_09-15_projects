
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('')
print('Give me an english couple`s first names and I will tranform them into baby names.')


firstname = input('Husband`s First Name: ')
firstname = firstname.lower()
while True:
    for i in firstname:
        if i not in alphabet:
            print()
            print('Please add a proper english first name, no special characters, no numbers.')
            firstname = input('Husband`s First Name: ')
            break
    else:
        break


secondname = input('Wife`s First Name: ')
secondname = secondname.lower()
while True:
    for i in secondname:         
        if i not in alphabet:
            print()
            print('Please add a proper english second name, no special characters, no numbers.')
            secondname = input('Wife`s First Name: ')
            break
    else:
        break

fn_value = 0
for i in firstname:
    n = alphabet.index(i) + 1   #looking for the position of the first name`s letters in alphabet
    fn_value = fn_value + n     #sum of the position/index of the letters

# print(fn_value)


sn_value = 0
for i in firstname:
    n = alphabet.index(i) + 1
    sn_value = sn_value + n

# print(sn_value)


first_letter_number = fn_value*sn_value

# print(first_letter_number)

first_letter_number = fn_value*sn_value%26


first_letter = alphabet[first_letter_number-1]

# print(first_letter_number)

print()

print(first_letter)
