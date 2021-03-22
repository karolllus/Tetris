import numpy as np

class Board:
    
    def __init__(self, shape):
        self.shape = shape
        self.initialize()


    # def initialize(self):
    #     x_axis = [0]*self.width
    #     x_axis[0] = 1
    #     x_axis[-1] = 1
    #     x_bottom = [1]*self.width
    #     self.board = [x_bottom if y+1 == self.height else x_axis for y in range(self.height)]

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