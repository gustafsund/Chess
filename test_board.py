from Chess_classes import Piece, Board


def main():
    # p = Piece('K')
    # print(p.white)
    # print(p.captured)
    # b = Board()
    # print()
    # print()
    # b.make_move('E4')
    # b.make_move('E5')

    print('Play game, White to move: ')
    b = Board()
    going = True

    b.show()
    while going:
        print()
        print()
        print('To quit game, make from square = to square!')
        from_square = input('From what square:\n')
        to_square = input('To what square: \n')
        going = from_square != to_square
        b.make_move([from_square, to_square])
        print()
        b.show()

if __name__ == '__main__':
    main()