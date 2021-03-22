import numpy as np


# Board
BOARD_SHAPE = (20, 20)


SHAPES_LIST = ['I', 'L', 'J', 'S', 'O']
SHAPES = {
    'I':np.array([[0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]]),

    'L':np.array([[0, 1, 0],
                [0, 1, 0],
                [0, 1, 1]], dtype=int),

    'J':np.array([[0, 1, 0],
                [0, 1, 0],
                [1, 1, 0]]),

    'S':np.array([[0, 1, 0],
                [1, 1, 0],
                [1, 0, 0]]),

    'O':np.array([[1, 1],
                [1, 1]]),
}