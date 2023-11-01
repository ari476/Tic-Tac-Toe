
from game_logic import Player
from typing import List
from game_logic import TicTacToe

def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    def is_winner(board, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(board):
    # The game is a draw if there are no empty cells
     return all(all(cell is not None for cell in row) for row in board)

    def available_moves(board):
        # Return a list of available (empty) positions on the board
        moves = []
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    moves.append((row, col))
        return moves

    def minimax(board, depth, is_maximizing, player):
        if is_winner(board, ai_player):
            return 1
        if is_winner(board, opponent):
            return -1
        if is_draw(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in available_moves(board):
                board[move[0]][move[1]] = ai_player
                if is_winner(board, ai_player):
                    score = 1
                else:
                    score = minimax(board, depth + 1, False, player)
                board[move[0]][move[1]] = None
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in available_moves(board):
                board[move[0]][move[1]] = opponent
                if is_winner(board, opponent):
                    score = -1
                else:
                    score = minimax(board, depth + 1, True, player)
                board[move[0]][move[1]] = None
                best_score = min(score, best_score)
            return best_score

    opponent = Player.X if ai_player == Player.O else Player.O
    best_move = None
    best_score = -float('inf')

    for move in available_moves(board):
        board[move[0]][move[1]] = ai_player
        if is_winner(board, ai_player):
            return move  # Win if possible
        score = minimax(board, 0, False, ai_player)
        board[move[0]][move[1]] = None

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
