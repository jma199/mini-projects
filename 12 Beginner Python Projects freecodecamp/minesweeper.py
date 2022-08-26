"""Implementation of a command line minesweeper game

This code is based on a version created by Kylie Ying.
Kylie's Github Code for her version: https://github.com/kying18/minesweeper/blob/main/minesweeper.py
Code refactoring inspired a code roast of a battleship game by AryanCodes.
AryanCode's Github Code for his code roast: https://github.com/ArjanCodes/2022-coderoast-battleship/blob/main/after.py

Thanks for stopping by!
"""


import random
import os

DIM_SIZE = 10
NUM_BOMBS = 10

def user_input(prompt: str, min_value: int = 0, max_value: int = 9) -> int:
    """Read an integer between min and max values."""
    
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


class MinesweeperBoard:
    def __init__(self, dim_size: int, num_bombs: int):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create board object
        self.board = self.make_new_board()
        self.place_bombs()
        self.assign_values_to_board()

        # keep track of uncovered locations
        self.already_dug = set()
    
    def make_new_board(self):
        '''Create a board'''
        return [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

    def place_bombs(self):
        '''Add bombs to board'''
        bombs_planted = 0
        
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size  # number of times dim_size goes into loc (row)
            col = loc % self.dim_size  # remainder tells us what index in that row (i.e. column)

            if self.board[row][col] == '*': # if bomb is already there
                continue
            
            self.board[row][col] = '*' # plant bomb
            bombs_planted += 1
        
    def assign_values_to_board(self):
        '''Assign a number (0-8) to represents the number of neighbouring bombs there are.'''
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)
    
    def get_num_neighbouring_bombs(self, row, col):
        '''Iterate through neighbouring positions and sum the number of bombs.
        Make sure to stay in bounds.'''
        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
        
        return num_neighbouring_bombs
    
    def is_dig_safe(self, row:int, col:int) -> bool:
        """Determine whether digging at (row,col) is safe (True) or uncovers a bomb (False)."""

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # if self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.already_dug:
                    continue # don't dig where you've already dug
                self.already_dug.add((r,c))
                self.is_dig_safe(r, c)
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.already_dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))
        
        indices = list(range(self.dim_size))
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            cell_format = f'%-{str(widths[idx])}s'
            cells.append(cell_format % col)
        indices_row = '   ' + '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                cell_format = f'%-{str(widths[idx])}s'
                cells.append(cell_format % col)
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'
        
        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len
        
        return string_rep


def read_guess(already_dug):
    """Read a valid guess from player"""

    while True:
        # read the row and column
        guess_row = user_input("Which row would you like to dig at? ")
        guess_col = user_input("Which column would you like to dig at? ")

        if guess_row < 0 or guess_row >= DIM_SIZE or guess_col < 0 or guess_col >= DIM_SIZE:
            print("Invalid guess. Try again.\n")

        if (guess_row, guess_col) not in already_dug:
            return guess_row, guess_col
        
        print("You guessed that already. Try again\n")

def turn(board: MinesweeperBoard) -> bool:
    "Handle each turn a player gets"
    print(board)

    # let the player guess
    guess_row, guess_col = read_guess(board.already_dug)
    
    # add guess to list of places already dug
    board.already_dug.add((guess_row, guess_col))
    
    # is the guess safe or not?
    return board.is_dig_safe(guess_row, guess_col)

def play_game(board: MinesweeperBoard) -> None:
    """Play a game of Minesweeper"""
    os.system("clear")

    print("    M I N E S W E E P E R\n")

    safe = True

    while len(board.already_dug) < board.dim_size**2 - board.num_bombs:
        if turn(board):
            print("Still safe. Keep digging!\n")
        else:
            safe = False
            print("\nSorry, you lost. GAME OVER :'(\n")
            # reveal entire board
            board.already_dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
            print(board)
            break
    
    if safe:
        print("CONGRATULATIONS! You won!")
    

def main() -> None:
    os.system("clear")
    board = MinesweeperBoard(DIM_SIZE, NUM_BOMBS)
    play_game(board)

if __name__ == '__main__':
    main()
