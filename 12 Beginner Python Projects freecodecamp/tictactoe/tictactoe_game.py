'''
This Tic Tac Toe class and tictactoe_game was created by Kylie Ying (YouTube)
'''

import math
import time
from tictactoe_players import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # create a 3 x 3 board
        self.current_winner = None # track winner
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # get which number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        '''Identify the index of spots on board that are empty'''
        return [i for i,x in enumerate(self.board) if x == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        '''Count the number of empty spaces on the board'''
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # a valid move is True
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        '''Winner will have 3 letters in a row. Check all possibilities.'''
        
        # check rows
        # if all the items in the row are equal to letter
        row_idx = math.floor(square / 3)
        row = self.board[row_idx*3 : (row_idx + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check columns
        col_idx = square%3
        column = [self.board[col_idx+i *3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals
        if square % 2 == 0:
            diagonal1 = [0, 4, 8]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [2, 4, 6]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def play(tictactoe_game, x_player, o_player, print_tictactoe_game=True):
    if print_tictactoe_game:
        tictactoe_game.print_board_nums()
    
    letter = 'X' # starting letter

    while tictactoe_game.empty_squares(): # check for empty squares
        # get a move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(tictactoe_game)
        else:
            square = x_player.get_move(tictactoe_game)
        
        # make a move
        if tictactoe_game.make_move(square, letter):
            if print_tictactoe_game:
                print('\n',letter + f" makes a move to square {square}.")
                tictactoe_game.print_board()
                print('') # empty line
            
            # check to see if the last move was the winning move
            if tictactoe_game.current_winner:
                if print_tictactoe_game:
                    print(letter + ' wins!')
                return letter # important to end loop and exit tictactoe_game
            # switch player
            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(0.8)

    if print_tictactoe_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_tictactoe_game=True)