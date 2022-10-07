

# new genre separate list for movies and shows


# Adding new items to a nested dictionary, list

favorites = { 'Movies': { 'Horror': ['Aliens', 'Jaws', '28 days later'],
                          'Comedy': ['Dream Team', 'Bio Dome', 'My Cousin Vinny'],
                          'Drama': ['The Road', 'The Big Short', 'The Social Network']},
              'Shows': { 'Horror': ['American Horror Story', 'The Haunting of Hill House'],
                          'Comedy': ['The Office(US)', 'Friends', 'Married... with Children'],
                          'Drama': ['Mindhunter', 'Misfits', 'Chernobyl']},
              'Songs': [ 'Mark Farina: Dream Machine ', 'Mr.Kitty: After Dark', 'Q Lazzarus: Goodbye Horses']}


newCatList = [] # collecting the newly added categories in this list
newGenList = [] # collecting the newly added genres in this list
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
        choiceMovies = input('Or in the previously added genre(s): ' + str(newGenList) + ' ')
        choiceMovies = choiceMovies[0].upper() + choiceMovies[1:]   
        while choiceMovies not in ['Horror', 'Comedy', 'Drama'] and choiceMovies not in newGenList:
            choiceMovies = input('Please add a valid genre: ').lower()
        
        print()
        print(choiceMovies + ':')
        for i in favorites[category][choiceMovies]:
            print( ' ' * (len(choiceMovies) + 1) + i.ljust(len(i)))
        print()

 #Print out Newly added Category \ genre?
    elif category in newCatList:
        if favorites[category] == {}:
            print('Sorry, this category does not have any genre and/or record yet.')
        else:
            print()
            print( category + ':')
            for i in favorites[category]:
                print( ' ' * (len(category) + 1) + i.ljust(len(i)))
            print()

            choiceMovies = input('Which genre are you looking for? ')
            choiceMovies = choiceMovies[0].upper() + choiceMovies[1:]   
            while choiceMovies not in newGenList:
                choiceMovies = input('Please add a valid genre: ')
                choiceMovies = choiceMovies[0].upper() + choiceMovies[1:]
            if favorites[category][choiceMovies] == {}:
                print()
                print('Sorry, this genre does not have any record yet.')
            else:            
                print()
                print(choiceMovies + ':')
                for i in favorites[category][choiceMovies]:
                    print( ' ' * (len(choiceMovies) + 1) + i.ljust(len(i)))
                print()


    elif category == 'Songs':
        print()
        print('Your selection:')
        for i in favorites[category]:
            print( ' ' * len('Your selection:') + i.ljust(len(i)))
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

            choiceCat = input('In which category? ')
            choiceCat = choiceCat[0].upper() + choiceCat[1:]
            while choiceCat not in ['Movies', 'Shows'] and choiceCat not in newCatList:
                choiceCat = input('Please add a valid category": ')
                choiceCat = choiceCat[0].upper() + choiceCat[1:]

# Adding Genre
# Where to add the new Genre: Movies, Shows + newly added category
            if choiceCat in ['Movies', 'Shows'] or choiceCat in newCatList:
                choiceName = input('The new title: ')
                choiceName = choiceName[0].upper() + choiceName[1:]
                if choiceName not in ['Horror', 'Comedy', 'Drama'] and choiceName not in newGenList:
                    newGenList = newGenList + [choiceName]   #able to add the same new genre to all categories
                    favorites[choiceCat][choiceName] = {}
                    print()
                    print('New genre is added:')
                    print(choiceCat + ':')
                    for k in favorites.get(choiceCat):
                        print(' '*len(i) + k)
                    print()
                else:
                    while choiceName in ['Horror', 'Comedy', 'Drama'] or choiceName in newGenList:
                        print('Sorry, the genre title is already taken. ')
                        choiceName = input('Add another Genre: ')
                        choiceName = choiceName[0].upper() + choiceName[1:]
                    newGenList = newGenList + [choiceName]   
                    favorites[choiceCat][choiceName] = {}

                    print('New genre is added:')
                    print(choiceCat + ':')
                    for k in favorites.get(choiceCat):
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
            elif category == 'Movies':
                



    
    
    if category == 'Q':
        print('Thx for dropping by.')
        print()
        break


            
            


    
    
    # elif category == 'Q':
    #     print('Thx for dropping by.')
    #     print()
    #     break


    