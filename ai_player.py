from typing import List
from game_logic import Player


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    bestMove = findBestMove(board, ai_player)
    return bestMove


def isMovesLeft(board):
    if all(board[row][col] is not None for row in range(3) for col in range(3)):
        return False
    return True

# checks for wins and will grade them.
def evaluate(board, player, opponent):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == player:
                return 10
            elif board[row][0] == opponent:
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10
            elif board[0][col] == opponent:
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10
    return 0

# minimax function with alpha beta pruning.
def minimax(board, depth, isMax, player, alpha, beta):
    opponent = Player.X if player == Player.O else Player.O
    score = evaluate(board, player, opponent)

    if score == 10:
        return score - depth # - depth to give preference to faster wins
    if score == -10:
        return score + depth # + depth to prolong loosing.

    if isMovesLeft(board) == False:
        return 0

    # ai turn
    if isMax: 
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = player
                    best = max(
                        best, minimax(board, depth + 1, False, player, alpha, beta)
                    )
                    alpha = max(alpha, best)
                    board[i][j] = None

                    # alpha beta pruning
                    if beta <= alpha:
                        break
        return best
    # player turn
    else: 
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = opponent
                    best = min(
                        best, minimax(board, depth + 1, True, player, alpha, beta)
                    )
                    beta = min(beta, best)
                    board[i][j] = None

                    if beta <= alpha:
                        break
        return best


def findBestMove(board, ai_player):
    bestVal = -1000
    alpha = float("-inf")
    beta = float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                board[i][j] = ai_player
                moveVal = minimax(board, 0, False, ai_player, alpha, beta)
                board[i][j] = None
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove
