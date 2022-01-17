from new_classes import *
b = Board()
print(b.get_legal_moves())
# print(b.make_hyp_move(Move(6,4,4,4)))
# print(b.make_move(Move(6,4,4,4)))

#Verify castling:
# short castling for white:
# b.show()
# b.make_move(Move(6,4,4,4))
# b.show()
# b.make_move(Move(1,0,2,0))
# b.show()
# b.make_move(Move(7,5,6,4))
# b.show()
# b.make_move(Move(1,2,3,2))
# b.show()
# b.make_move(Move(7,6,5,5))
# b.show()
# b.make_move(Move(1,4,2,4))
# b.show()
# b.make_move(Move(7,4,7,6,short_castle = True))
# b.show()

# for i in range(20):
#     print('---------------------------------------')
#     print()
#     b.show()
#     print()
#     print()
#     moves = b.all_candiadate_moves()
#     move = np.random.choice(moves)
#     b.make_move(move)
    

# Try playing with annoying input
# while True:
#     print()
#     b.show()
#     print()
#     if b.white_to_move:
#         print('Vits tur!')
#     else:
#         print('Svarts tur!')
#     r0 = int(input('från rad: '))
#     c0 = int(input ('från kolumn: '))
#     r1 = int(input('till rad: '))
#     c1 = int(input('till kolumn: '))
#     while not b.make_move(Move(r0,c0,r1,c1)):
#         print('Tyvärr olagligt drag. Prova igen')
#         r0 = int(input('från rad: '))
#         c0 = int(input ('från kolumn: '))
#         r1 = int(input('till rad: '))
#         c1 = int(input('till kolumn: '))

    
