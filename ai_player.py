import math
from game_logic import Player
from typing import List

def moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return True
    return False

def evaluate(board, player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == player:
                return 10
            elif board[row][0] != None:
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10
            elif board[0][col] != None:
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        elif board[0][0] != None:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        elif board[0][2] != None:
            return -10

    return 0

def minimax(board, isMax, player):
    
    score = evaluate(board,player) 
    if score != 0:
        return score
    if not moves_left(board):
        return 0
    # print(Player.O if player == Player.X else Player.X, player)
    if isMax:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = player
                    best = max(best, minimax(board, not isMax, player))
                    board[i][j] = None
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = Player.O if player == Player.X else Player.X
                    best = min(best, minimax(board, not isMax, player))
                    board[i][j] = None
        print(best)
        return best

def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    bestVal = -math.inf
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                board[i][j] = ai_player
                moveVal = minimax(board, False, ai_player)
                board[i][j] = None
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove
