
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('')
print('Give me two english names and I will tranform them into one for you.')


firstname = input('First Name: ')
firstname = firstname.lower()
while True:
    for i in firstname:
        if i not in alphabet:
            print()
            print('Please add a proper english first name, no special characters, no numbers.')
            firstname = input('First Name: ')
            break
    else:
        break


secondname = input('Second Name: ')
secondname = secondname.lower()
while True:
    for i in secondname:
        if i not in alphabet:
            print()
            print('Please add a proper english second name, no special characters, no numbers.')
            secondname = input('Second Name: ')
            break
    else:
        break

fn_value = 0
for i in firstname:
    n = alphabet.index(i) + 1
    fn_value = fn_value + n


sn_value = 0
for i in firstname:
    n = alphabet.index(i) + 1
    sn_value = sn_value + n


first_letter_number = fn_value*sn_value
first_letter_number = fn_value*sn_value%26


first_letter = alphabet[first_letter_number-1]
print(first_letter)
