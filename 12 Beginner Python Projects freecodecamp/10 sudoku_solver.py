'''
A Sudoku solver that using recursion to solve the puzzle.
This is an original implementation by K. Ying (Github User @kying18)
'''
from pprint import pprint

def find_next_empty(puzzle):
    '''Find place on board that's not filled yet.

    :place on board: row, col
    :empty space: -1
    '''
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    
    return None, None # no empty spaces

def is_valid(puzzle, guess, row, col):
    '''Determine whether a guess is valid'''
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[row][col] for row in range(9)]
    if guess in col_vals:
        return False
    
    # check the 3x3 square
    row_start = (row // 3) * 3 # which square is the guess in?
    col_start = (col // 3) * 3 

    for row in range (row_start, row_start +3):
        for col in range(col_start, col_start +3):
            if puzzle[row][col] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    '''Main puzzle solving function'''
    # choose a place to make a guess on the board
    row, col = find_next_empty(puzzle)
    # You solved the puzzle
    if row is None:
        return True
    
    # if there is an empty space, make a guess
    for guess in range (1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # recursively call function
            if solve_sudoku(puzzle):
                return True
        
        # reset value because it didn't contribute to the solving of the puzzle
        puzzle[row][col] = -1

    # if no numbers work, then the puzzle is unsolvable
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
