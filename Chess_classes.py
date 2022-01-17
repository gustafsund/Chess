class Piece:


    def __init__(self,name,position = None):
        self.name = name
        self.white = (name == name.upper())
        self.captured = False
        self.position = position
    
    def update_position(self,new_position):
        self.position = new_position
    
    # def get_target_squares(self):
    #     squares = []
    #     r = self.position[0]
    #     c = self.position[1]
    #     match self.name.lower():
    #         case 'r':
    #             squares.append([[x,c] for x in range(8) if x != r])
    #             squares.append([[r,x] for x in range(8) if x != r])
            




class Board:

    def __init__(self):
        self.position = ['rnbqkbnr',
                        'pppppppp',
                        '--------',
                        '--------',
                        '--------',
                        '--------',
                        'PPPPPPPP',
                        'RNBQKBNR']
        self.white_to_move = True
        self.pieces = [[None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None]]

        for r in range(8):
            for c in range(8):
                if self.position[r][c] != '-':
                    self.pieces[r][c] = Piece(self.position[r][c],[r,c])
                else:
                    self.pieces[r][c] = None # this else probably reduntant... 
        
        self.translate_file = dict(zip('ABCDEFGH',[0,1,2,3,4,5,6,7]))

    def show(self):
        for line in self.position:
            print(line)

    def update_position(self):
        for r in range(8):
            rebuild_row = ''
            for c in range(8):
                p = self.pieces[r][c]
                if p is None:
                    rebuild_row += '-'
                    
                else:
                    
                    rebuild_row += p.name
            self.position[r] = rebuild_row

    def make_move(self,move): # move as list curr and next pos
        c_now = self.translate_file[move[0][0].upper()]
        r_now = 8-int(move[0][1])
        c_next = self.translate_file[move[1][0].upper()]
        r_next = 8-int(move[1][1])
        if self.pieces[r_next][c_next] is None:
            self.pieces[r_next][c_next] = self.pieces[r_now][c_now]
            self.pieces[r_now][c_now] = None
        else:
            self.pieces[r_now][c_now].captured = True
            self.pieces[r_next][c_next] = self.pieces[r_now][c_now]
            self.pieces[r_now][c_now] = None
        self.white_to_move = not self.white_to_move
        # print(self.pieces)
        self.update_position()
