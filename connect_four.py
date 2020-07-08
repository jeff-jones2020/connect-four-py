grid = {'count': 0}
blank = '\u2298'
circle = '\u2B24'
square = '\u2B1B'
turn = circle

GRID_BOUND = 11
grid['max'] = (GRID_BOUND - 1) * (GRID_BOUND - 1)

CARDINALS = {
        'WE': (1, 0),
        'NS': (0, 1),
        'NW_SE': (1, 1),
        'SW_NE': (1, -1)
    }

CARDINAL_DIRS = CARDINALS.values()

def reset_board(char):
    grid['count'] = 0
    blank = char
    for y in range(1, GRID_BOUND):
        for x in range(1, GRID_BOUND):
            grid[(x, y)] = blank


def print_board():
    for row in range(1, GRID_BOUND):
        row_str = ''
        for col in range(1, GRID_BOUND):
            row_str += grid[row,col] + ' '
        print(row_str)

def check_directions(coords, turn):
    counter = 0
    has_won = False
    for DIR in CARDINAL_DIRS:
        counter = 0
        for index in range(-3, 4):
            check_coords = (coords[0] + index * DIR[0], coords[1] + index * DIR[1])
            
            if check_coords not in grid:
                continue
            # print( 'checking coordinates: ', str(check_coords) , ' Cardinal: ', str(DIR))
            if grid[check_coords] == turn:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                has_won = True
                print('has won')
                break
        if has_won:
            break

    return has_won

def check_win(coords, turn):
    # print('check_win called')
    
    has_won = check_directions(coords, turn)
    print_board()
    print('\n')
    
    if has_won:
        print(turn + ' won!')


# Places a marker on the grid.
# If the input is invalid, returns -1. If valid, returns 0. If valid and is a winning move, returns 1.
def drop_piece(col, turn):
    for row in range(GRID_BOUND - 1, 0, -1):
        if col < 1 or col >= GRID_BOUND:
            return -1
        if grid[(row, col)] != blank:
            continue
        
        grid[(row, col)] = turn
        grid['count'] += 1
        has_won = check_win((row, col), turn)
        if has_won:
            return 1
        else:
            return 0

    return -1
reset_board(blank)

print('Valid inputs are from 1 and ' + str(GRID_BOUND - 1))

while grid['count'] < grid['max']:
    input_row = input('Enter a column, ' + turn + ':  ')
    print('---------------------------------------------------------')
    is_valid = drop_piece(int(input_row), turn)
    if(is_valid == -1):
        print(input_row + ' is not a valid input.')
        continue
    if(turn == circle):
        turn = square
    else:
        turn = circle
