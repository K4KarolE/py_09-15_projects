

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('')
print('Give me two english names and I will tranform them into one for you.')
firstname = input('First Name: ')
firstname = firstname.lower()
namelenght = len(firstname) - 1


n = 0
while n <= namelenght:
        while firstname[n] not in alphabet:
            firstname = input('Please add a proper english First Name: ')
            n = 0
        while firstname[n] in alphabet:    
            testN = firstname[n]
            n += 1
            print(testN)
        if n > namelenght:
            break


    

    

    

# print(n)
# print(firstname[n])
# print(namelenght)



# letter = firstname[:1]





# print(letter)
# print(len(firstname))
# print(alphabet[25])
# secondname = input('Second Name: ')