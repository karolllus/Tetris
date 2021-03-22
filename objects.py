import numpy as np


class Piece:

    def __init__(self, arr, position):
        self.arr = arr
        self.position = position
        

    def rotate_clockwise(self):
        self.arr_old = self.arr.copy()
        self.arr = np.rot90(self.arr, -45)
        self.position[0] += 1


    def rotate_counter_clockwise(self):
        self.arr_old = self.arr.copy()
        self.arr = np.rot90(self.arr, 45)
        self.position[0] += 1


    def move_left(self):
        self.arr_old = self.arr.copy()
        self.position_old = self.position.copy()
        self.position[0] += 1
        self.position[1] -= 1


    def move_right(self):
        self.arr_old = self.arr.copy()
        self.position_old = self.position.copy()
        self.position[0] += 1
        self.position[1] += 1

    
    def reverse_move(self):
        self.arr = self.arr_old.copy()
        self.position = self.position_old.copy()
        


    def show_shape(self):
        print(self.arr)




class Board:
    
    def __init__(self, shape):
        self.shape = shape
        self.initialize()


    def initialize(self):
        outer = np.ones(self.shape, dtype=int)
        inner = np.zeros((self.shape[0]-1, self.shape[1]-2), dtype=int)
        x, y = 0, 1
        outer[x:x+inner.shape[0], y:y+inner.shape[1]] = inner
        self.board = outer


    def update(self, piece):
        x, y = piece.position[0], piece.position[1]
        self.board[x:x+piece.arr.shape[0], y:y+piece.arr.shape[1]] += piece.arr


    def has_moves(self, piece):
        moves = [piece.move_left, piece.move_right, piece.rotate_clockwise, piece.rotate_counter_clockwise]
        available = []
        for move in moves:
            move()
            available.append(self.is_valid_move(piece))
            piece.reverse_move()

        return any(available) == True


    def is_valid_move(self, piece):
        x, y = piece.position[0], piece.position[1]
        new_board = self.board.copy()
        if 2 in new_board:
            return False
        else:
            try:
                new_board[x:x+piece.arr.shape[0], y:y+piece.arr.shape[1]] += piece.arr
            except:
                new_board += new_board
            return 2 not in new_board


    def show(self, piece):
        x, y = piece.position[0], piece.position[1]
        screen_board = self.board.copy()
        screen_board[x:x+piece.arr.shape[0], y:y+piece.arr.shape[1]] += piece.arr
        screen = [''.join(['*' if x == 1 else ' ' for x in y]) for y in screen_board]
        print(*screen, sep='\n')