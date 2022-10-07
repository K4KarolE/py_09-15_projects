# problem - adding genre to a new category

# Adding new items to a nested dictionary with different key-value types

favorites = { 'Movies': { 'Horror': ['Aliens', 'Jaws', '28 days later'],
                          'Comedy': ['Dream Team', 'Bio Dome', 'My Cousin Vinny'],
                          'Drama': ['The Road', 'The Big Short', 'The Social Network']},
              'Shows': { 'Horror': ['American Horror Story', 'The Haunting of Hill House'],
                          'Comedy': ['The Office(US)', 'Friends', 'Married... with Children'],
                          'Drama': ['Mindhunter', 'Misfits', 'Chernobyl']},
              'Songs': [ 'Mark Farina: Dream Machine ', 'Mr.Kitty: After Dark', 'Q Lazzarus: Goodbye Horses']}

newGenList = { 'Movies': [], 'Shows': [] }  #collecting the newly added genres separately for Movies, Shows

newCatList = []    #collecting the newly added categories

print()
while True:
    print()
    print('Type "Movies", "Shows" or "Songs" to list your favorite bits.')
    print('Or the name of the previously added category: ' + str(newCatList))
    category = input('Or type "add" for adding to your list or "q" for quit. ')
    category = category[0].upper() + category[1:]
    print()

    while category not in ['Movies', 'Shows', 'Songs', 'Add', 'Q'] and category not in newCatList:
        category = input('Please add a valid category or type "add", "q": ')
        category = category[0].upper() + category[1:]
    
    
    if category == 'Q':
        print('Thx for dropping by.')
        print()
        break
#Print out Movies or Shows (already existing categories)
    elif category in ['Movies', 'Shows']:
        print('Which genre are you looking for? Horror, Comedy or Drama?')
        choiceGenre = input('Or in the previously added genre(s): ' + str(newGenList[category]) + ' ')
        choiceGenre = choiceGenre[0].upper() + choiceGenre[1:]   
        while choiceGenre not in ['Horror', 'Comedy', 'Drama'] and choiceGenre not in newGenList[category]:
            choiceGenre = input('Please add a valid genre: ')
            choiceGenre = choiceGenre[0].upper() + choiceGenre[1:] 
        
        print()
        print(choiceGenre + ':')
        for i in favorites[category][choiceGenre]:
            print( ' ' * (len(choiceGenre) + 1) + i)
        print()

 #Print out Newly added Category \ genre?
    elif category in newCatList:
        if favorites[category] == {}:
            print('Sorry, this category does not have any genre and/or record yet.')
        else:
            print()
            print( category + ':')
            for i in favorites[category]:
                print( ' ' * (len(category) + 1) + i)
            print()

            choiceGenre = input('Which genre are you looking for? ')
            choiceGenre = choiceGenre[0].upper() + choiceGenre[1:]   
            while choiceGenre not in newGenList[category]:
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
            if newCat not in ['Movies', 'Shows', 'Songs'] and newCat not in newCatList:
                newCatList = newCatList + [newCat]
                favorites[newCat] = {}
                print()
                print('New category is added: ')
                for i in favorites.keys():
                    print(' ' * len('New category is added:') + i)

                
            else:
                while newCat in ['Movies', 'Shows', 'Songs'] or newCat in newCatList:
                    print('Sorry, the category title is already taken. ')
                    newCat = input('Add another Category: ')
                    newCat = newCat[0].upper() + newCat[1:]
                newCatList = newCatList + [newCat]
                favorites[newCat] = {}
                print()
                print('New category is added: ')
                for i in favorites.keys():
                    print(' ' * len('New category is added:') + i)

# Adding Genre
# Selection
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
            while category not in ['Movies', 'Shows'] and category not in newCatList:
                category = input('Please add a valid category": ')
                category = category[0].upper() + category[1:]

# Adding Genre
# Where to add the new Genre: Movies, Shows + newly added category
            if category in ['Movies', 'Shows'] or category in newCatList:
                choiceName = input('The new title: ')
                choiceName = choiceName[0].upper() + choiceName[1:]

                if category in ['Movies', 'Shows']:
                    if choiceName not in ['Horror', 'Comedy', 'Drama'] and choiceName not in newGenList[category]:
                        newGenList[category] = newGenList[category] + [choiceName]   
                        favorites[category][choiceName] = []
                        print()
                        print('New genre is added:')
                        print(category + ':')
                        for k in favorites.get(category):
                            print(' '*len(i) + k)
                        print()
                    else:
                        while choiceName in ['Horror', 'Comedy', 'Drama'] or choiceName in newGenList[category]:
                            print()
                            print('Sorry, the genre title is already taken. ')
                            choiceName = input('Add another Genre: ')
                            choiceName = choiceName[0].upper() + choiceName[1:]
                        newGenList[category] = newGenList[category] + [choiceName]   
                        favorites[category][choiceName] = []
                    
                    print('New genre is added:')
                    print(category + ':')
                    for k in favorites.get(category):
                        print(' '*len(i) + k)
                    print()
                
                
                elif category in newCatList:
                    if choiceName not in newGenList[category]:
                        newGenList[category] = newGenList[category] + [choiceName]   
                        favorites[category][choiceName] = []
                        print()
                        print('New genre is added:')
                        print(category + ':')
                        for k in favorites.get(category):
                            print(' '*len(i) + k)
                        print()
                    else:
                        while choiceName in newGenList[category]:
                            print('Sorry, the genre title is already taken. ')
                            choiceName = input('Add another Genre: ')
                            choiceName = choiceName[0].upper() + choiceName[1:]
                        newGenList[category] = newGenList[category] + [choiceName]   
                        favorites[category][choiceName] = []
                    
                    print('New genre is added:')
                    print(category + ':')
                    for k in favorites.get(category):
                        print(' '*len(i) + k)
                    print()



# Adding Record
        elif newRecord == 'r':
            print('Current categories: ')
            for i in favorites.keys():
                print(' ' * len('Current categories:') + i)
            print()
            category = input('In which category? ')
            category = category[0].upper() + category[1:]
            while category not in ['Movies', 'Shows', 'Songs'] and category not in newCatList:
                category = input('Please add a valid category or type "add", "q": ')
                category = category[0].upper() + category[1:]

# Adding Record - Songs
            if category == 'Songs':
                print()
                newSong = input('The new track: ')
                favorites[category] = favorites[category] + [newSong]
                print()
                print('New track added to your selection:')
                for i in favorites[category]:
                    print( ' ' * len('New track added to your selection:' ) + i)
                print()

# Adding Record - Apart from Songs
            elif category in ['Movies', 'Shows'] or category in newCatList:
                print('Which genre are you looking for? Horror, Comedy or Drama?')
                choiceGenre = input('Or in the previously added genre(s): ' + str(newGenList[category]) + ' ')
                choiceGenre = choiceGenre[0].upper() + choiceGenre[1:]   
                while choiceGenre not in ['Horror', 'Comedy', 'Drama'] and choiceGenre not in newGenList[category]:
                    choiceGenre = input('Please add a valid genre: ')
                    choiceGenre = choiceGenre[0].upper() + choiceGenre[1:] 
                print()
                newRecord = input('Your new ' + category[:-1] + ': ')
                favorites[category][choiceGenre] = favorites[category][choiceGenre] + [newRecord]
                print()
                print('New record is added.')
                print(category + ' / ' + choiceGenre + ':' )
                for i in favorites[category][choiceGenre]:
                    print( ' ' * len(category + ' / ' + choiceGenre + ':') + i)
                print()

    
    if category == 'Q':
        print('Thx for dropping by.')
        print()
        break
