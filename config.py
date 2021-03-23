# Configuration file


# Board parameters
BOARD_SHAPE = (20, 20)


# Game shapes
# To add more shapes SHAPES dictionary needs to include array of the shape and the dictionary key needs to be included in the SHAPES_LIST

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