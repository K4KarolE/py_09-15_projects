

spam = ['apples', 'bananas', 'tofu', 'cats']
# spam=[]

def printer():
    print()
    if len(spam) == 0:
        print('Sorry, your list is empty.')
    for i in range(len(spam)):
        if i + 1 < len(spam):
            print(spam[i] + ', ', end='')
        else:
           print('and ' + spam[i]) 
            
printer()


def lister():
    new_list = []
    print()
    if len(spam) == 0:
        print('Sorry, your list is empty.')
    else:
        for i in range(len(spam)):
            if i + 1 < len(spam):
                new_list.append(spam[i] + ', ')
            else:
                new_list.append('and ' + spam[i])
        print(new_list)

lister()        
