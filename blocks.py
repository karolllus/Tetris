import numpy as np

class Piece:

    def __init__(self, shape):
        self.shape = shape
        # self.position = position
    

    def rotate_clockwise(self):
        self.shape = np.rot90(self.shape)


    def rotate_counter(self):
        pass


    def move_left(self):
        pass


    def move_right(self):
        pass

    def show_shape(self):
        print(self.shape)


shape = np.array([  [1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]])
shape = np.rot90(shape)

# print(''.join([''.join(item) for item in shape.astype(str)]).replace('1','*').replace('0',' '), sep='\n')

# block = Piece(shapeA)
# block.show_shape()