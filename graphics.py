import pygame as p
from pygame.constants import MOUSEBUTTONDOWN 
from new_classes import *
WIDTH = HEIGHT = 800
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15 
IMAGES = {}

def load_images():
    pieces = 'rbnqkpRBNQKP'
    for piece in pieces:
        IMAGES[piece] = p.image.load(f'images/{piece}.png')

def draw_board(screen):
    colors = [p.Color('white'),p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def draw_pieces(screen,gs):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = gs[r,c]
            if piece is not None:
                screen.blit(IMAGES[piece.name],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


def draw_game_state(screen,gs):
    draw_board(screen)
    draw_pieces(screen,gs)



def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    b = Board()
    load_images()
    sq_selected = ()
    player_clicks = []
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sq_selected == (row,col):
                    sq_selected = ()
                    player_clicks = []

                else:
                    sq_selected = (row,col)
                    player_clicks.append(sq_selected)
                if len(player_clicks) == 2:
                    r0 = player_clicks[0][0]
                    c0 = player_clicks[0][1]
                    r1 = player_clicks[1][0]
                    c1 = player_clicks[1][1]
                    if b.pieces[r0,c0]:
                        if b.pieces[r0,c0].name.lower() == 'k' and c1-c0==3:
                            b.make_move(Move(r0,c0,r1,c0+2,short_castle=True))
                            sq_selected = ()
                            player_clicks = []
                        elif b.pieces[r0,c0].name.lower() == 'k' and c1-c0==-4:
                            b.make_move(Move(r0,c0,r0,c0-2,long_castle=True))
                            sq_selected = ()
                            player_clicks = []
                            
                    b.make_move(Move(r0,c0,r1,c1))
                    sq_selected = ()
                    player_clicks = []
                elif len(player_clicks) > 2:
                    sq_selected = ()
                    player_clicks = []

                    

        draw_game_state(screen,b.pieces)
        p.display.flip()

    
    if b.winner == 1:
        print('white won')
    elif b.winner == -1:
        print('black won')
    elif b.winner == 0:
        print('draw')

if __name__ == '__main__':
    main()