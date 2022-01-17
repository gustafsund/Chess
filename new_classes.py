import numpy as np

class Piece:

    def __init__(self,r,c,is_white):
        self.r = r
        self.c = c
        self.is_white = is_white

    def get_pos(self):
        return self.r,self.c
    
    def set_pos(self,r,c):
        self.r = r
        self.c = c
#klar
    def get_king_moves(self,board):
        moves = []
        jumps = [(self.r+1,self.c),(self.r+1,self.c+1),(self.r+1,self.c-1), 
                    (self.r,self.c+1),(self.r,self.c-1),
                    (self.r-1,self.c),(self.r-1,self.c-1),(self.r-1,self.c+1)]
        for r,c in jumps:
            if r in range(8) and c in range(8):
                if board[r,c]:
                    if board[r,c].is_white != self.is_white:
                        moves.append(Move(self.r,self.c,r,c))
                else:
                    moves.append(Move(self.r,self.c,r,c))
        # short castle
        if self.c + 3 in range(8):
            pot_rook = board[self.r,self.c+3]
            if not self.moved and pot_rook and not board[self.r,self.c+1] and not board[self.r,self.c+2]:
                if pot_rook.name.lower() == 'r':
                    if not pot_rook.moved:
                        moves.append(Move(self.r,self.c,self.r,self.c+2,short_castle = True))
        if self.c -4 in range(8):
            pot_rook = board[self.r,self.c-4]
            if not self.moved and pot_rook and not board[self.r,self.c-1] and not board[self.r,self.c-2] and not board[self.r,self.c-3]:
                if pot_rook.name.lower() == 'r':
                    if not pot_rook.moved:
                        moves.append(Move(self.r,self.c,self.r,self.c-2,long_castle = True))


            
        return moves
    #bör vara klar
    def get_diagonal_moves(self,board):
        moves = []
        for i in range(1,8):
            if self.r + i in range(8) and self.c + i in range(8):
                if board[self.r+i,self.c+i]:
                    if board[self.r+i,self.c+i].is_white != self.is_white:
                        moves.append(Move(self.r,self.c,self.r+i,self.c+i))
                    break
                else:
                    moves.append(Move(self.r,self.c,self.r+i,self.c+i))
        for i in range(1,8):
            if self.r + i in range(8) and self.c - i in range(8):
                if board[self.r+i,self.c-i]:
                    if board[self.r+i,self.c-i].is_white != self.is_white:
                        moves.append(Move(self.r,self.c,self.r+i,self.c-i))
                    break
                else:
                    moves.append(Move(self.r,self.c,self.r+i,self.c-i))
        for i in range(1,8):
            if self.r - i in range(8) and self.c - i in range(8):
                if board[self.r-i,self.c-i]:
                    if board[self.r-i,self.c-i].is_white != self.is_white:
                        moves.append(Move(self.r,self.c,self.r-i,self.c-i))
                    break
                else:
                    moves.append(Move(self.r,self.c,self.r-i,self.c-i))
        for i in range(1,8):
            if self.r - i in range(8) and self.c + i in range(8):
                if board[self.r-i,self.c+i]:
                    if board[self.r-i,self.c+i].is_white != self.is_white:
                        moves.append(Move(self.r,self.c,self.r-i,self.c+i))
                    break
                else:
                    moves.append(Move(self.r,self.c,self.r-i,self.c+i))
        return moves
# byta namn på nedanstående kanske... men klar
    def get_horizontal_moves(self,board):
        moves = []
        for row in range(self.r - 1,-1,-1):
            if board[row,self.c]:
                if board[row,self.c].is_white != self.is_white:
                    moves.append(Move(self.r,self.c,row,self.c))
                break
            else:
                moves.append(Move(self.r,self.c,row,self.c))
        for row in range(self.r+1,8):
            if board[row,self.c]:
                if board[row,self.c].is_white != self.is_white:
                    moves.append(Move(self.r,self.c,row,self.c))
                break
            else:
                moves.append(Move(self.r,self.c,row,self.c))
        for col in range(self.c+1,8):
            if board[self.r,col]:
                if board[self.r,col].is_white != self.is_white:
                    moves.append(Move(self.r,self.c,self.r,col))
                break
            else:
                moves.append(Move(self.r,self.c,self.r,col))
        for col in range(self.c-1,-1,-1):
            if board[self.r,col]:
                if board[self.r,col].is_white != self.is_white:
                    moves.append(Move(self.r,self.c,self.r,col))
                break
            else:
                moves.append(Move(self.r,self.c,self.r,col))
        return moves
    #klar
    def get_knight_moves(self,board):
        moves = []
        r = self.r
        c = self.c
        jumps = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
        for row,col in jumps:
            if r +row in range(8) and c + col in range(8):
                if board[r+row,c+col]:
                    if board[r+row,c+col].is_white != self.is_white:
                        moves.append(Move(r,c,r+row,c+col))
                else:
                    moves.append(Move(r,c,r+row,c+col))
        return moves
    #klar förutom en passant
    def get_pawn_moves(self,board):
        moves = []
        mult = -1 if self.is_white else 1
        if self.r+mult in range(8):
            if not board[self.r + mult,self.c]:
                moves.append(Move(self.r,self.c,self.r + mult,self.c))
        if self.can_double and self.r + 2*mult in range(8):
            if not board[self.r + 2*mult,self.c]:
                moves.append(Move(self.r,self.c,self.r + 2*mult,self.c))
        if self.r+mult in range(8) and self.c + 1 in range(8):
            if board[self.r + mult,self.c+1]:
                if board[self.r + mult,self.c+1].is_white != self.is_white:
                    moves.append(Move(self.r,self.c,self.r+mult,self.c+1))
        if self.r+mult in range(8) and self.c - 1 in range(8):
            if board[self.r + mult,self.c-1]:
                if board[self.r + mult,self.c-1].is_white != self.is_white:
                    moves.append(Move(self.r,self.c,self.r+mult,self.c-1))
        return moves



class King(Piece):
    def __init__(self,r,c,is_white):
        super().__init__(r,c,is_white)
        self.name = 'K' if is_white else 'k'
        self.moved = False
        
    def get_moves(self,board):
        return self.get_king_moves(board)    

class Pawn(Piece):
    def __init__(self,r,c,is_white):
        super().__init__(r,c,is_white)
        self.name = 'P' if is_white else 'p'
        self.can_double = True
        self.en_pass_cpos = False
        self.en_pass_cneg = False


    def get_moves(self,board):
        return self.get_pawn_moves(board)

class Queen(Piece):
    def __init__(self,r,c,is_white):
        super().__init__(r,c,is_white)
        self.name = 'Q' if is_white else 'q'

    def get_moves(self,board):
        return self.get_horizontal_moves(board) + self.get_diagonal_moves(board)

class Bishop(Piece):
    def __init__(self,r,c,is_white):
        super().__init__(r,c,is_white)
        self.name = 'B' if is_white else 'b'

    def get_moves(self,board):
        return self.get_diagonal_moves(board)

class Knight(Piece):
    def __init__(self,r,c,is_white):
        super().__init__(r,c,is_white)
        self.name = 'N' if is_white else 'n'

    def get_moves(self,board):
        return self.get_knight_moves(board)

class Rook(Piece):
    def __init__(self,r,c,is_white):
        super().__init__(r,c,is_white)
        self.name = 'R' if is_white else 'r'
        self.moved = False

    def get_moves(self,board):
        return self.get_horizontal_moves(board)        

class Board:
    def __init__(self):
        self.to_string = ['rnbqkbnr',
                        'pppppppp',
                        '--------',
                        '--------',
                        '--------',
                        '--------',
                        'PPPPPPPP',
                        'RNBQKBNR']
        self.white_to_move = True
        self.game_over = False
        self.winner = 0
        pieces = [[None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None]]
        pieces[0][0] = Rook(0,0,False)
        pieces[0][1] = Knight(0,1,False)
        pieces[0][2] = Bishop(0,2,False)
        pieces[0][3] = Queen(0,3,False)
        pieces[0][4] = King(0,4,False)
        pieces[0][5] = Bishop(0,5,False)
        pieces[0][6] = Knight(0,6,False)
        pieces[0][7] = Rook(0,7,False)
        for c in range(8):
            pieces[1][c] = Pawn(1,c,False)
            pieces[6][c] = Pawn(6,c,True)

        pieces[7][0] = Rook(7,0,True)
        pieces[7][1] = Knight(7,1,True)
        pieces[7][2] = Bishop(7,2,True)
        pieces[7][3] = Queen(7,3,True)
        pieces[7][4] = King(7,4,True)
        pieces[7][5] = Bishop(7,5,True)
        pieces[7][6] = Knight(7,6,True)
        pieces[7][7] = Rook(7,7,True)
        self.pieces = pieces
        self.pieces = np.array(pieces)
        self.white_to_move = True
    
    def all_candiadate_moves(self,pos = None,white = 'not specified'):
        if pos is None:
            pos = self.pieces
        
        if white == 'not specified':
            white = self.white_to_move
        moves = []
        for line in pos:
            for piece in line:
                if piece:
                    if piece.is_white == white:
                        moves.extend(piece.get_moves(pos))
        return moves
    
    def in_check(self,pos = None, white = 'not specified'):
        if pos is None:
            pos = self.pieces
        if white == 'not specified':
            white = self.white_to_move
        for r in range(8):
            for c in range(8):
                if pos[r,c]:
                    if pos[r,c].name.lower() == 'k' and pos[r,c].is_white == white:
                        r_king = r
                        c_king = c
                        break
        for move in self.all_candiadate_moves(pos,not white):
            if move.r1 == r_king and move.c1 == c_king:
                return True
        return False

    def get_legal_moves(self,pos = None,white = 'not specified'):
        if pos is None:
            pos = self.pieces
        if white == 'not specified':
            white = self.white_to_move
        candidates = self.all_candiadate_moves(pos,white)
        legal_moves = []
        for cmove in candidates:
            pos = self.make_hyp_move(cmove)
            
            if pos is not None and not self.in_check(pos,white):
                legal_moves.append(cmove)
        return legal_moves

    def is_game_over(self):
        if len(self.get_legal_moves()) == 0:
            if self.in_check():
                self.game_over = True
                self.winner = 1 if not self.white_to_move else -1
            else:
                self.winner = 0

    
    def show(self):
        print(*self.to_string,sep='\n')

    def update_position(self):
        for r in range(8):
            rebuild_row = ''
            for c in range(8):
        
                p = self.pieces[r,c]
                if p is None:
                    rebuild_row += '-'
                    
                else:
                    rebuild_row += p.name
            self.to_string[r] = rebuild_row

    def make_move(self,move):
        legals = self.get_legal_moves()
        if sum(move.equals(m) for m in legals) > 0:
            self.pieces[move.r0,move.c0].set_pos(move.r1,move.c1)
            self.pieces[move.r1,move.c1] = self.pieces[move.r0,move.c0]
            self.pieces[move.r0,move.c0] = None
            if move.short_castle:
                self.pieces[move.r0,move.c0+3].set_pos(move.r1,move.c1-1)
                self.pieces[move.r1,move.c1-1] = self.pieces[move.r0,move.c0+3]
                self.pieces[move.r0,move.c0+3] = None
                self.pieces[move.r1,move.c1-1].moved = True
                self.pieces[move.r1,move.c1].moved = True
            elif move.long_castle:
                self.pieces[move.r0,move.c0-4].set_pos(move.r1,move.c1+1)
                self.pieces[move.r1,move.c1+1] = self.pieces[move.r0,move.c0-4]
                self.pieces[move.r0,move.c0-4] = None
                self.pieces[move.r1,move.c1+1].moved = True
                self.pieces[move.r1,move.c1].moved = True
            elif self.pieces[move.r1,move.c1].name.lower() in ['k','r']:
                self.pieces[move.r1,move.c1].moved = True
            elif self.pieces[move.r1,move.c1].name.lower() == 'p':
                self.pieces[move.r1,move.c1].can_double = False
                if move.c1+1 < 8 and abs(move.r1-move.r0) == 2:
                    if self.pieces[move.r1,move.c1+1] is not None:
                        if self.pieces[move.r1,move.c1+1].is_white != self.white_to_move and self.pieces[move.r1,move.c1+1].name.lower() == 'p':
                            self.pieces[move.r1,move.c1+1].en_pass_cneg = True
                if move.c1-1 >= 0 and abs(move.r1-move.r0) == 2:
                    if self.pieces[move.r1,move.c1-1] is not None:
                        if self.pieces[move.r1,move.c1-1].is_white != self.white_to_move and self.pieces[move.r1,move.c1-1].name.lower() == 'p':
                            self.pieces[move.r1,move.c1-1].en_pass_cpos = True
            self.white_to_move = not self.white_to_move
            self.update_position()
            self.is_game_over()
            return True
        else:
            return False
        

    def make_hyp_move(self,move):
        hyp_pieces = self.pieces.copy()
        if self.pieces[move.r0,move.c0]:
            if self.white_to_move != self.pieces[move.r0,move.c0].is_white:
                return None
            moves = self.pieces[move.r0,move.c0].get_moves(self.pieces)
            if sum(move.equals(m) for m in moves) == 0:
                return None
            else:
                hyp_pieces[move.r1,move.c1] = self.pieces[move.r0,move.c0]
                hyp_pieces[move.r0,move.c0] = None
                return hyp_pieces
        else:
            return None



class Move():
    def __init__(self,r0,c0,r1,c1,short_castle = False,long_castle = False):
        # translate_file = dict(zip('ABCDEFGH',[0,1,2,3,4,5,6,7]))
        # if c0 in 'abcdefgh' or c0 in 'ABCDEFGH':
        #     c0 = translate_file[c0.upper()]
        #     r0 = 8-int(r0)
        # if c1 in 'abcdefgh' or c1 in 'ABCDEFGH':
        #     c1 = translate_file[c1.upper()]
        #     r1 = 8-int(r1)
        ## Gör om.
        self.r0 = r0
        self.c0 = c0
        self.r1 = r1
        self.c1 = c1
        self.short_castle = short_castle
        self.long_castle = long_castle
    def equals(self,other_move):
        return self.r0 == other_move.r0 and self.r1 == other_move.r1 and self.c0 == other_move.c0 and self.c1 == other_move.c1
        

## to-do:
# fixa så den inte kan göra drag som försätter sig själv i schack DONE
# fixa så den vet när en match är över. DONE
# En passant ongoing... 
# rockad -DONE
# Move history... - not really needed..?
