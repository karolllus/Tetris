import config as cfg
import objects as obj
import random as rnd
import os


VALID_MOVE = "Please make a valid move: "


def starting_position():
    return [0, cfg.BOARD_SHAPE[1] // 2 - 1]


def random_shape():
    return cfg.SHAPES[rnd.choice(cfg.SHAPES_LIST)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    print(*['Starting New Game',
            "a - move piece left",
            "d - move piece right",
            "w - rotate piece counter clockwise",
            "s - rotate piece clockwise"], sep='\n')
    board = obj.Board(cfg.BOARD_SHAPE)
    piece = obj.Piece(random_shape(), starting_position())

    while 1:
        if board.has_moves(piece) == False:
            board.update(piece)
            piece = None

        # check if game is piece is spawned
        if piece == None:
            piece = obj.Piece(random_shape(), starting_position())
        
        # check if game over
        if board.is_valid_move(piece) != True:
            print("Game Over")
            break

        board.show(piece)
        user = ''

        while user not in ['a', 'd', 'w', 's']:
            user = input("Please make a move: ")
            if user == 'a':
                piece.move_left()
            elif user == 'd':
                piece.move_right()
            elif user == 'w':
                piece.rotate_counter_clockwise()
            elif user == 's':
                piece.rotate_clockwise()
            else:
                print(VALID_MOVE)
                continue

            if board.is_valid_move(piece) != True:
                piece.reverse_move()
                print(VALID_MOVE)
                continue



if __name__=='__main__':
    game()