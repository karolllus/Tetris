import numpy as np


class Piece:

    def __init__(self, shape, position):
        self.shape = shape
        self.shape_old = self.shape
        self.position = shape[1]
        self.position_old = self.position
        

    def rotate_clockwise(self):
        self.shape_old = self.shape
        self.shape = np.rot90(self.shape, -45)


    def rotate_counter_clockwise(self):
        self.shape_old = self.shape
        self.shape = np.rot90(self.shape, 45)


    def move_left(self):
        self.position_old = self.position
        self.position[0] -= 1
        self.position[1] += 1


    def move_right(self):
        self.position_old = self.position
        self.position[0] += 1
        self.position[1] += 1


    def show_shape(self):
        print(self.shape)
