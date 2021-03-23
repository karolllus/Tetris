import config as cfg
import objects as obj
import random as rnd
import os


# static variables
VALID_MOVE = "Please make a valid move: "


def starting_position():
    """
    Calculates starting position for the piece object
    """
    return [0, cfg.BOARD_SHAPE[1] // 2 - 1]


def random_shape():
    """
    Chooses random shape from the config shapes
    """
    return cfg.SHAPES[rnd.choice(cfg.SHAPES_LIST)]


def clear_screen():
    """
    Clears the display screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    """
    Main game logic
    """

    # Initiating board and piece
    board = obj.Board(cfg.BOARD_SHAPE)
    piece = obj.Piece(random_shape(), starting_position())

    while 1:

        # check if the piece has any moves left
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

        # display new state of the game
        clear_screen()
        print(*["a - move piece left",
            "d - move piece right",
            "w - rotate piece counter clockwise",
            "s - rotate piece clockwise"], sep='\n')
        board.show(piece)

        # get input and decide the next move for the piece
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

            # checking if the move is valid
            if board.is_valid_move(piece) != True:
                piece.reverse_move()
                print(VALID_MOVE)
                continue



if __name__=='__main__':
    game()