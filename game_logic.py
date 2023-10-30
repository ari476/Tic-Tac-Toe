from enum import Enum
import copy

class Player(Enum):
    X = 'X'
    O = 'O'

class TicTacToe:
    def __init__(self, current_player = None, board = None):     
        self.current_player = current_player or Player.X 
        self.board = copy.deepcopy(board) or [[None for _ in range(3)] for _ in range(3)] 

    def is_cell_empty(self, cell_pos):
        return self.board[cell_pos[0]][cell_pos[1]] is None    

    def is_winners(self):
        """
        check if self.current_player win: 
        """

        # Check rows
        for row in self.board:
            if row.count(self.current_player) == 3:
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True

        return False

    def is_cells_occupied(self):  
        return all(self.board[row][col] is not None for row in range(3) for col in range(3))

    def is_game_over(self):
        """
        if one from the player won return him.
        if the result game is tie return 'Tie'.
        in any other case return False.
        """
        if self.is_winners():
            return self.current_player

        if self.is_cells_occupied():
            return 'Tie'

        return False
