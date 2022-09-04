'''A Sudoku Solver
Solve any Sudoku puzzle, with user input to add starting numbers to the board
This code is based on a version created by Kylie Ying.
'''

import os

def input_num(prompt: str, min_value: int = 1, max_value: int = 9) -> int:
    """User input to add a number to the Sudoku board"""

    while True:
        line = input(prompt)
        try:
            value = int(line)
            if value < min_value:
                print(f"The minimum value is {min_value}. Try again.")
            elif value > max_value:
                print(f"The maximum value is {max_value}. Try again.")
            else:
                return value
        except ValueError:
            print(f"Invalid guess. Select an integer between {min_value} and {max_value}.")


class SudokuBoard:
    '''Puzzle board is a list of lists'''
    def __init__(self):
        # Create board object
        self.board = self.create_empty_board()
        # self.board = self.create_example_board()

        # Keep track of spaces where number was added to board
        self.game_numbers = set()
    
    def create_empty_board(self):
        '''Create a new sudoku board'''
        return [[-1 for _ in range(9)] for _ in range(9)]
    
    # def create_example_board(self):
    #     return [[3, 9, -1, -1, 5, -1, -1, -1, -1], [-1, -1, -1, 2, -1, -1, -1, -1, 5], [-1, -1, -1, 7, 1, 9, -1, 8, -1], [-1, 5, -1, -1, 6, 8, -1, -1, -1], [2, -1, 6, -1, -1, 3, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, 4], [5, -1, -1, -1, -1, -1, -1, -1, -1], [6, 7, -1, 1, -1, 5, -1, 4, -1], [1, -1, 9, -1, -1, -1, 2, -1, -1]]
    
    def find_next_empty(self):
        '''Find place on board that's not filled yet.
        :place on board: row, col
        :empty space: -1
        '''
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == -1:
                    return row, col
        
        return None, None # no empty spaces

    def is_valid(self, guess: int, row: int, col: int) -> bool:
        '''Determine whether a guess is valid'''
        row_vals = self.board[row]
        if guess in row_vals:
            return False
        col_vals = [self.board[row][col] for row in range(9)]
        if guess in col_vals:
            return False
        # check the 3x3 square
        row_start = (row // 3) * 3 # which square is the guess in?
        col_start = (col // 3) * 3
        for row in range (row_start, row_start +3):
            for col in range(col_start, col_start +3):
                if self.board[row][col] == guess:
                    return False
        
        return True
    
    def add_start_nums(self):
        '''Add number to sudoku board'''
        number_value, start_num_row, start_num_col = get_start_nums()
        self.board[start_num_row][start_num_col] = number_value
        self.game_numbers.add((start_num_row, start_num_col))
    
    def to_string(self):
        rows_str = [" ".join(str(row)) for row in self.board]
        return "\n".join(rows_str)

    
def get_start_nums():
    '''Get a number to add to sudoku board from user input'''
    number_value = input_num("What number do you want to add to the board? ")
    
    start_num_row = input_num("What row should the number be placed at? ") -1
    start_num_col = input_num("What column should the number be placed at? ") -1
    
    return number_value, start_num_row, start_num_col


def sudoku_solver(board:SudokuBoard):
     # solve the board
    row, col = board.find_next_empty()
    if row is None:
        return True
    
     # if there is an empty space, make a guess
    for guess in range (1, 10):
        if board.is_valid(guess, row, col):
            board.board[row][col] = guess
            # recursively call function
            if sudoku_solver(board):
                return True
        
        # reset value because it didn't contribute to the solving of the board
        board.board[row][col] = -1

    # if no numbers work, then the board is unsolvable
    return False

def main():
    os.system("clear")
    print("\nSudoku Solver!\n")
    puzzle = SudokuBoard()
    
    # add numbers to board
    play = True
    while play:
        line = input("\nDo you have a number to add to the board (y/n)? ")
        if line == 'y':
            puzzle.add_start_nums()
        elif line == 'n':
            print(f"You have added {len(puzzle.game_numbers)} numbers to the sudoku board.")
            play = False
        else:
            print("Invalid entry. Try again\n")

    print('\n* * * * * * * * * * * * * * *\n')
    sudoku_solver(puzzle)
    print("Your puzzle is now solved!\n")
    print(puzzle.to_string())
   
if __name__ == "__main__":
    main()
