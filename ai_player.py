from game_logic import Player
from game_logic import TicTacToe
from typing import List


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    """
    Args:
        board (List[List[Player]]): current state of the game board
        ai_player (Player): X or O enum 

    Returns:
        tuple: cell position for placing the next symbol on the game board
    """
    def is_winner(player):
        """
        Unlike is_winner in the logic file, this function checks whether a specific player has one
        """
    # Check rows and columns
        for row in range(3):
            if all(board[row][column] == player for column in range(3)) or all(board[column][row] == player for column in range(3)):
                return True 
    # Check diagonals
        if all(board[row][row] == player for row in range(3)) or all(board[row][2 - row] == player for row in range(3)):
            return True
        return False
    
    def minimax(board, recursion_number, maximizing):
        #AI won
        if is_winner(ai_player):
            return 1
        #Opponent won
        if is_winner(Player.X if ai_player == Player.O else Player.O):
            return -1
        #Tie game
        if all(all(cell is not None for cell in row) for row in board):
            return 0
        #If the game is still going
        #The AI is trying to win/draw
        if maximizing:
            #Iterate over all possible moves and check which leads to a win
            winning_move = -float('inf')
            for row in range(3):
                for column in range(3):
                    if board[row][column] is None:
                        board[row][column] = ai_player
                        # Recursion call
                        next_move = minimax(board, recursion_number + 1, False)
                        board[row][column] = None
                        # Compares moves and find the one of the higher score
                        winning_move = max(winning_move, next_move)
            return winning_move
        #The AI is blocking the opponent's move
        else:
            blocking_move = float('inf')
            for row in range(3):
                for column in range(3):
                    if board[row][column] is None:
                        board[row][column] = Player.X if ai_player == Player.O else Player.O
                        # Recursion call
                        next_move = minimax(board, recursion_number + 1, True)
                        board[row][column] = None
                        # Compares moves nd find the one of the lower score
                        blocking_move = min(blocking_move, next_move)
            return blocking_move       
    #The actual function call and usage
    final_move = None
    best_evaluation = -float('inf')
    for row in range(3):
        for column in range(3):
            if board[row][column] is None:
                board[row][column] = ai_player
                next_move = minimax(board, 0, False)
                board[row][column] = None
                if next_move > best_evaluation:
                    best_evaluation = next_move
                    final_move = (row, column)
    return final_move