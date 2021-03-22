import numpy as np


class Board:
    
    def __init__(self, shape):
        self.shape = shape
        self.initialize()


    def initialize(self):
        outer = np.ones(self.shape, dtype=int)
        inner = np.zeros((self.shape[0]-1, self.shape[1]-2), dtype=int)
        x = 0
        y = 1
        outer[x:x+inner.shape[0], y:y+inner.shape[1]] = inner
        self.board = outer


    def show(self):
        board = []
        for y in self.board:
            board.append(''.join(['*' if x == 1 else ' ' for x in y]))
        print(*board, sep='\n')


    def update(self):
        pass
        

board = Board((20, 20))
board.show()