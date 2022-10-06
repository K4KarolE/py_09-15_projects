# 4 tomorrow newly added category is not choosable

# Adding new items to a nested dictionary, pls note the Songs category value is a list

favorites = { 'Movies': { 'Horror': ['Aliens', 'Jaws', '28 days later'],
                          'Comedy': ['Dream Team', 'Bio Dome', 'My Cousin Vinny'],
                          'Drama': ['The Road', 'The Big Short', 'The Social Network']},
              'Shows': { 'Horror': ['American Horror Story', 'The Haunting of Hill House'],
                          'Comedy': ['The Office(US)', 'Friends', 'Married... with Children'],
                          'Drama': ['Mindhunter', 'Misfits', 'Chernobyl']},
              'Songs': [ 'Mark Farina: Dream Machine ', 'Mr.Kitty: After Dark', 'Q Lazzarus: Goodbye Horses']}


newCatList = []
print()
while True:
    print()
    print('Which of your favorite categories are you interested in?')
    print('Movies, Shows or Songs?')
    print('Or in the previously added category:' + str(newCatList))
    category = input('Or type "add" for adding to your list or "q" for quit. ').lower()
    print()

    while category not in ['movies', 'shows', 'songs', 'add', 'q'] and category not in newCatList:
        category = input('Please add a valid category or type "add", "q": ').lower()
    
    category = category[0].upper() + category[1:]

    if category in ['Movies', 'Shows'] or category in newCatList:
        choiceMovies = input('Which genre are you looking for? Horror, Comedy or Drama? ').lower()   
        while choiceMovies not in ['horror', 'comedy', 'drama']:
            choiceMovies = input('Please add a valid genre: ').lower()
        choiceMovies = choiceMovies[0].upper() + choiceMovies[1:]
        print()
        print(choiceMovies + ':')
        for i in favorites[category][choiceMovies]:
            print( ' ' * (len(choiceMovies) + 1) + i.ljust(len(i)))
        print()

    elif category == 'Songs':
        for i in favorites['Songs']:
            print( ' ' * len('Songs:') + i.ljust(len(i)))
        print()

# Adding new category / genre / record
# Category
    elif category == 'Add':
        newRecord = input('New Category(c), Genre(g) or Record(r)? ').lower()
        if newRecord == 'c':
            print('Current categories: ')
            for i in favorites.keys():
                print(' ' * len('Current categories:') + i)
            print()
            newCat = input('What is the name of your new Category? ')
            newCatList = newCatList + [newCat]
            favorites[newCat] = {}
            print()
            print('New category is added: ')
            for i in favorites.keys():
                print(' ' * len('New category is added:') + i)
# Genre
        elif newRecord == 'g':
            print('Current categories / genres:')
            for i in favorites.keys():
                print(i + ':')
                for k in favorites.get(i):
                    print(' '*len(i) + k)
            print()
            print('As you can see the "Songs" category do not have any genre yet.')
            print()

            choiceCat = input('In which category? ')
            while choiceCat not in ['Movies', 'Shows', 'Songs'] and choiceCat not in newCatList:
                choiceCat = input('Please add a valid category": ')
# Genre in Movies, Shows + newly added category
            if choiceCat in ['Movies', 'Shows'] or choiceCat in newCatList:
                choiceName = input('The new title: ')
                favorites[choiceCat][choiceName] = {}
                print('Updated genres:')
                print(choiceCat + ':')
                for k in favorites.get(choiceCat):
                    print(' '*len(i) + k)
                print()
            


    
    
    elif category == 'Q':
        print('Thx for dropping by.')
        print()
        break


    