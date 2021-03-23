import numpy as np


class Piece:
    """
    Piece class with implementation of each piece objects logic
    """

    def __init__(self, arr, position):
        """
        Initialize the piece object

        Parameters:
            - arr - array shape of the piece 
            - position - starting position of the piece
        """
        self.arr = arr
        self.position = position
        

    def rotate_clockwise(self):
        """
        Rotates the piece clocwise and moves one step downwards
        """
        self.arr_old = self.arr.copy()
        self.arr = np.rot90(self.arr, -45)
        self.position[0] += 1


    def rotate_counter_clockwise(self):
        """
        Rotates the piece counter clockwise and moves one step downwards
        """
        self.arr_old = self.arr.copy()
        self.arr = np.rot90(self.arr, 45)
        self.position[0] += 1


    def move_left(self):
        """
        Moves the piece one step left and one step downwards
        """
        self.arr_old = self.arr.copy()
        self.position_old = self.position.copy()
        self.position[0] += 1
        self.position[1] -= 1


    def move_right(self):
        """
        Moves the piece one step right and one step downwards
        """
        self.arr_old = self.arr.copy()
        self.position_old = self.position.copy()
        self.position[0] += 1
        self.position[1] += 1

    
    def reverse_move(self):
        """
        Reverses the move of the piece
        """
        self.arr = self.arr_old.copy()
        self.position = self.position_old.copy()




class Board:
    """
    Board class with implementation of board logic
    """
    
    def __init__(self, shape):
        """
        Initialize the board object

        Parameters:
            - shape - accepts standard numpy array shape in form of tuple with two integers
        """
        self.shape = shape
        self.initialize()


    def initialize(self):
        """
        Initializes the board array
        """
        sy, sx = self.shape[0], self.shape[1]

        # Creating outer rim of the board made out from ones and its inner part made out from zeroes
        outer = np.ones(self.shape, dtype=int)
        inner = np.zeros((sy-1, sx-2), dtype=int)
        x, y = 0, 1
        outer[x:x+inner.shape[0], y:y+inner.shape[1]] = inner

        # Creating outer padding of the board made out from zeroes
        x, y = 0, 2
        uber_outer = np.zeros((sy+2, sx+4), dtype=int)
        uber_outer[x:x+outer.shape[0], y:y+outer.shape[1]] = outer
        self.board = uber_outer


    def update(self, piece):
        """
        Updates the board adding piece array to board array

        Paramenters:
            - piece - object of the piece instance
        """
        x, y = piece.position[0], piece.position[1]
        self.board[x:x+piece.arr.shape[0], y:y+piece.arr.shape[1]] += piece.arr


    def has_moves(self, piece):
        """
        Checks if there are any possible moves for the seleceted piece

        Parameter:
            - piece - object of the piece instance
        """
        
        # loop through all the moves and flag if any is possible
        moves = [piece.move_left, piece.move_right, piece.rotate_clockwise, piece.rotate_counter_clockwise]
        available = []
        for move in moves:
            move()
            available.append(self.is_valid_move(piece))
            piece.reverse_move()

        return any(available) == True


    def is_valid_move(self, piece):
        """
        Checks if the position of the piece is valid

        Parameters:
            - piece - object of the piece isntance
        """
        x, y = piece.position[0], piece.position[1]
        new_board = self.board.copy()

        # check if the current board pieces are overalping
        # else check the board with the piece added
        # 2 == overlaping
        if 2 in new_board:
            return False
        else:
            try:
                new_board[x:x+piece.arr.shape[0], y:y+piece.arr.shape[1]] += piece.arr
            except:
                new_board += new_board
            return 2 not in new_board


    def show(self, piece):
        """
        Displays the board on the screen with the current piece position

        Parameters:
            - piece - object of the piece instance
        """
        x, y = piece.position[0], piece.position[1]
        screen_board = self.board.copy()

        # add the piece to the board array
        screen_board[x:x+piece.arr.shape[0], y:y+piece.arr.shape[1]] += piece.arr

        # prepare string representation of the array
        screen = [''.join(['*' if x == 1 else ' ' for x in y]) for y in screen_board]
        print(*screen, sep='\n')