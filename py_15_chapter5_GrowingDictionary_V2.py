
# Adding new items to a nested dictionary

favorites = { 'Movies': { 'Horror': ['Aliens', 'Jaws', '28 days later'],
                          'Comedy': ['Dream Team', 'Bio Dome', 'My Cousin Vinny'],
                          'Drama': ['The Road', 'The Big Short', 'The Social Network']},
              'Shows': { 'Horror': ['American Horror Story', 'The Haunting of Hill House'],
                          'Comedy': ['The Office(US)', 'Friends', 'Married... with Children'],
                          'Drama': ['Mindhunter', 'Misfits', 'Chernobyl']},
              'Songs': [ 'Mark Farina: Dream Machine ', 'Mr.Kitty: After Dark', 'Q Lazzarus: Goodbye Horses']}


def listCategories():
    print('Categories:')
    for i in favorites.keys():
        print(' ' * len('Categories:') + i)


print('\n')
print('-' * 22 + ' MY FAVORITES ' + '-' * 22)
print('Type the name of the category to list your favorite bits.')
print()
listCategories()

while True:
    print()
    print('Type \n    "add" for adding to your lists ')
    print('    "list" for display the current categories')
    print('    "q" for quit. ')
    category = input('Next step: ')
    category = category[0].upper() + category[1:]
    print()

    while category not in ['Add', 'Q', 'List'] and category not in favorites.keys():
        category = input('Please add a valid category or type "add", "list" or "q": ')
        category = category[0].upper() + category[1:]
 # Q   
    if category == 'Q':
        print('Thx for dropping by.')
        print()
        break
# List    
    elif category == 'List':
        listCategories()
# New Category with no genre yet  
    elif category in favorites.keys() and favorites[category] == {}:
        print('This category does not have any genre yet.')

# Category(apart from Songs) \ Genre 
    elif category in favorites.keys() and category != 'Songs':
        print('Which genre are you looking for?')
        for i in favorites[category]:
            print(' ' * len('Which genre are you looking for?') + i)
        print()
        choiceGenre = input('Next step: ')
        choiceGenre = choiceGenre[0].upper() + choiceGenre[1:]
           
        while choiceGenre not in favorites[category]:
            choiceGenre = input('Please add a valid genre: ')
            choiceGenre = choiceGenre[0].upper() + choiceGenre[1:]
        if favorites[category][choiceGenre] == []:
                print()
                print('Sorry, this genre does not have any record yet.') 
        
        else:            
            print()
            print(choiceGenre + ':')
            for i in favorites[category][choiceGenre]:
                print( ' ' * (len(choiceGenre) + 1) + i)
            print()
# Songs
    elif category == 'Songs':
        print()
        print('Your selection:')
        for i in favorites[category]:
            print( ' ' * len('Your selection:') + i)
        print()

# Adding new Category / Genre / Record
# Adding Category
    elif category == 'Add':
        newRecord = input('New Category(c), Genre(g) or Record(r)? ').lower()
        if newRecord == 'c':
            print('Current categories: ')
            for i in favorites.keys():
                print(' ' * len('Current categories:') + i)
            print()
            newCat = input('What is the name of your new Category? ')
            newCat = newCat[0].upper() + newCat[1:]
            if newCat not in favorites.keys():
                favorites[newCat] = {}
                print()
                print('New category is added: ')
                for i in favorites.keys():
                    print(' ' * len('New category is added:') + i)
           
            else:
                while newCat in favorites.keys():
                    print()
                    print('Sorry, the category title is already taken. ')
                    newCat = input('Add another Category: ')
                    newCat = newCat[0].upper() + newCat[1:]
                favorites[newCat] = {}
                print()
                print('New category is added: ')
                for i in favorites.keys():
                    print(' ' * len('New category is added:') + i)

# Adding Genre
        elif newRecord == 'g':
            print('Current categories / genres:')
            for i in favorites.keys():
                print(i + ':')
                for k in favorites.get(i):
                    print(' '*len(i) + k)

            print()
            print('Please note: to the "Songs" category only new records are available to add.')
            print()

            category = input('In which category? ')
            category = category[0].upper() + category[1:]
            while category not in favorites.keys():
                category = input('Please add a valid category": ')
                category = category[0].upper() + category[1:]

            if category in favorites.keys():
                choiceName = input('The new title: ')
                choiceName = choiceName[0].upper() + choiceName[1:]
                while choiceName in favorites[category]:
                        print()
                        print('Sorry, the genre title is already taken. ')
                        choiceName = input('Add another Genre: ')
                        choiceName = choiceName[0].upper() + choiceName[1:] 
                favorites[category][choiceName] = []

                print()    
                print('New genre is added:')
                print(category + ':')
                for k in favorites.get(category):
                    print(' '*len(i) + k)

# Adding Record
        elif newRecord == 'r':
            print('Current categories: ')
            for i in favorites.keys():
                print(' ' * len('Current categories:') + i)
            print()
            category = input('In which category? ')
            category = category[0].upper() + category[1:]
            while category not in favorites.keys():
                category = input('Please add a valid category or type "add", "q": ')
                category = category[0].upper() + category[1:]

# Adding Record - No genre yet
            if favorites[category] == {}:
                print()
                print('To be able to add a record, please add a genre to this category first.')
                
# Adding Record - Songs
            elif category == 'Songs':
                print()
                newSong = input('The new track: ')
                while newSong in favorites[category]:
                    print()
                    print('This track already in your list')
                    newSong = input('The new track: ')
                if newSong not in favorites[category]:
                    favorites[category] = favorites[category] + [newSong]
                    print()
                    print('New track added to your selection:')
                    for i in favorites[category]:
                        print( ' ' * len('New track added to your selection:' ) + i)
                print()

# Adding Record - Apart from Songs
            else:
                print()
                print(category + ':')
                for k in favorites.get(category):
                    print(' '*len(category) + k)
                print()
                choiceGenre = input('Add your new record in which genre? ')
                choiceGenre = choiceGenre[0].upper() + choiceGenre[1:] 
                while choiceGenre not in favorites[category]:
                    choiceGenre = input('Please add a valid genre: ')
                    choiceGenre = choiceGenre[0].upper() + choiceGenre[1:] 
                print()
                newRecord = input('Your new record: ')
                favorites[category][choiceGenre] = favorites[category][choiceGenre] + [newRecord]
                print()
                print('New record is added.')
                print(category + ' / ' + choiceGenre + ':' )
                for i in favorites[category][choiceGenre]:
                    print( ' ' * len(category + ' / ' + choiceGenre + ':') + i)
                print()
