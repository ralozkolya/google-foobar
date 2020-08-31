from math import floor

BOARD_SIZE = 8

POSSIBLE_MOVES = [
    [ 1, 2, 1, 2, -1, -2, -1, -2 ],
    [ 2, 1, -2, -1, 2, 1, -2, -1 ]
]

def get_xy(src):
    x = src % BOARD_SIZE
    y = int(floor(src / BOARD_SIZE))
    return [ x, y ]

def get_dest(xy):
    return BOARD_SIZE * xy[1] + xy[0]

def in_grid(index):
    return 0 <= index <= BOARD_SIZE - 1

def possible_moves(src):
    x, y = get_xy(src)
    moves = []
    for i in range(8):
        px = x + POSSIBLE_MOVES[0][i]
        py = y + POSSIBLE_MOVES[1][i]
        if in_grid(px) and in_grid(py):
            moves.append(get_dest([px, py]))

    return moves
        

def solution(src, dst):
    queue = [{ 'position': src, 'distance': 0 }]

    for cell in queue:

        if (cell['position'] == dst):
            return cell['distance']
        
        queue.extend(
            [{ 'position': m, 'distance': cell['distance'] + 1 } for m in possible_moves(cell['position'])]
        )
