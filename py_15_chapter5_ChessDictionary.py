# ***Chess***
# We are going to print out the Color Types / Piece Types / Pieces` amount
# with valid location and uppercase first letter

chessDic = {'white': {'pawn': {'a2': 1, 'b2': 1, 'c2': 1, 'd2': 1, 'e2': 1, 'f2': 1, 'g2': 1, 'h2': 1},
                      'rook': {'a1': 1, 'h1': 1},
                      'knight': {'b1': 1, 'g1': 1},
                      'bishop': {'c1': 1, 'f1': 1},
                      'queen': {'d1': 1},
                      'king': {'e1': 1}},

            'black': {'pawn': {'a7': 1, 'b7': 1, 'c7': 1, 'd7': 1, 'e7': 1, 'f7': 1, 'g7': 1, 'h7': 1},
                      'rook': {'a8': 1, 'h8': 1},
                      'knight': {'b8': 1, 'g8': 1},
                      'bishop': {'c8': 1, 'f8': 1},
                      'queen': {'d8': 1},
                      'king': {'e8': 1}}}


valid_pos = ('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
             'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
             'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
             'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
             'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
             'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
             'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8')

pieces = ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king')

color = ('white', 'black')


def countAllPieces():
    count = 0
    for p in color:
        for i in valid_pos:
            for k in pieces:
                count = count + chessDic.get(p, {}).get(k, {}).get(i, 0)
    


print()
piecesUpper = []
p=0

for i in chessDic.keys():
    printColor = i[0].upper() + i[1:] + ':'
    print(printColor)
    printPieces = list(chessDic[i].keys())

    for k in range(6):
        count = 0
        for p in valid_pos:
            count = count + chessDic.get(i, {}).get(printPieces[k], {}).get(p, 0)
        piecesUpper = piecesUpper + [printPieces[k][0].upper() + printPieces[k][1:] + ':']
        print(piecesUpper[k].rjust(8) + ' ' + str(count))
  
    
    print()
