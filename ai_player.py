from game_logic import Player
from typing import List
from game_logic import TicTacToe


def is_moves_left(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                return True
    return False


def eval(board, ai_player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == ai_player:
                return 1
            elif board[row][0] is not None:
                return -1

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == ai_player:
                return 1
            elif board[0][col] is not None:
                return -1

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == ai_player:
            return 1
        elif board[0][0] is not None:
            return -1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == ai_player:
            return 1
        elif board[0][2] is not None:
            return -1

    return 0


def mini_max(board, is_max, ai_player):
    opponent = Player.O if ai_player == Player.X else Player.X
    score = eval(board, ai_player)

    if score == 1:
        return score

    if score == -1:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000

        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = ai_player
                    best = max(best, mini_max(board, not is_max, ai_player))
                    board[row][col] = None
        return best
    else:
        best = 1000

        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = opponent
                    best = min(best, mini_max(board, not is_max, ai_player))
                    board[row][col] = None
        return best


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    best_val = -1000
    best_move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = ai_player
                move_val = mini_max(board, False, ai_player)
                board[row][col] = None
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val

    return best_move
