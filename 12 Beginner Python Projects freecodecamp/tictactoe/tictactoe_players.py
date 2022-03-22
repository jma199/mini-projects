'''
This file defines the players that can be used in Tic Tac Toe game.
The Tic Tac Toe players using inheritance implementation was created by
Kylie Ying (YouTuber).
'''

import random
import math

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # check if square is valid by casting it to an integer
            # check if square is available on the board
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Pick another one.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class SmartComputerPlayer(Player):
    '''This player will try to maximize score with the placement of next letter.'''
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, tictactoe_game):
        if len(tictactoe_game.available_moves()) == 9:
            square = random.choice(tictactoe_game.available_moves())
        else:
            square = self.minimax(tictactoe_game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # check if previous move is a winner
