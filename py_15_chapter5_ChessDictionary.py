

chessDic = { 'white': {'pawn': { 'a2': 1, 'b2': 1, 'c2': 1, 'd2': 1, 'e2': 1, 'f2': 1, 'g2': 1, 'h2': 1}, 
                        'rook': {'a1': 1, 'h1': 1},
                        'knight': {'b1':1, 'g1': 1},
                        'bishop': {'c1':1, 'f1': 1},
                        'queen': {'d1': 1},
                        'king': {'e1':1} },
             
             'black': { 'pawn': { 'a7': 1, 'b7': 1, 'c7': 1, 'd7': 1, 'e7': 1, 'f7': 1, 'g7': 1, 'h7': 1}, 
                        'rook': {'a8': 1, 'h8': 1},
                        'knight': {'b8':1, 'g8': 1},
                        'bishop': {'c8':1, 'f8': 1},
                        'queen': {'d8': 1},
                        'king': {'e8':1} } }


print(chessDic.get('white',{}).get('pawn',{}).get('a2',0))




