
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('Give me two english names and I will tranform them into one for you.')
firstname = input('First Name: ')
firstname = firstname.lower()
namelenght = len(firstname) - 1


n = 0
while n <= namelenght and firstname[n] in alphabet:
      n += 1
else:
    print('Please use english characters only.')

# print(n)
# print(firstname[n])
# print(namelenght)



# letter = firstname[:1]





# print(letter)
# print(len(firstname))
# print(alphabet[25])
# secondname = input('Second Name: ')