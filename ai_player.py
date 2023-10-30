from game_logic import Player
from typing import List
from game_logic import TicTacToe
import random

CORNERS = [(0, 0), (0, 2), (2, 0), (2, 2)]
MIDDLE = [(0, 1), (1, 2), (2, 1), (1, 0)]

def is_board_empty(board: List[List[Player]]):
    for row in range(3):
        for column in range(3):
            if not is_empty((row, column), board):
                return False
    return True

def is_empty(cell_pos: tuple, board: List[List[Player]]):
    return board[cell_pos[0]][cell_pos[1]] is None

def cell_not_empty(board: List[List[Player]]):
    counter = 0
    for row in range(3):
        for column in range(3):
            if not is_empty((row, column), board):
                counter += 1


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    """
    Args:
        board (List[List[Player]]): current state of board in the game
        ai_player (Player): X or O enum 

    Returns:
        tuple: cell position for placing the next symbol on the game board
        (y, x)
    """

    global CORNERS
    global MIDDLE
    
    if ai_player == Player.X:
        enemy = Player.O
    else:
        enemy = Player.X
    
    if ai_player == Player.X:  #checks if computer is first
        corner = CORNERS[random.randrange(0,4)]
        return corner
    
    else:  #if computer is second
        if is_empty((1,1), board):
            return (1,1)
        else:
            for corner in CORNERS:
                if is_empty(corner, board):
                    return corner
                
    if ai_player == Player.O:  #not first or second turn 
        for row in range(3):  #checks for two in a row (in row)
            if board[row][0] == board[row][1] and (board[row][0] == enemy and board[row][1] == enemy):
                if is_empty((row, 2), board):
                    return (row, 2)
            
            elif board[row][1] == board[row][2] and (board[row][1] == enemy and board[row][2] == enemy):
                if is_empty((row, 0), board):
                    return (row, 0)

            elif board[row][2] == board[row][0] and (board[row][2] == enemy and board[row][0] == enemy): #checks for two in corners of row
                if is_empty((row, 1), board):
                    return (row, 1)


        for column in range(3): #checks for two in a row (in column)
            if column == 0:
                if (board[0][column] == board[0][column + 1]) and (board[0][column] == enemy and board[0][column + 1] == enemy):
                    if is_empty((0, column + 2), board):
                        return (0, column + 2)
                
            elif column == 1:
                if board[0][column] == board[0][column + 1] and (board[0][column] == enemy and board[0][column + 1] == enemy):
                    if is_empty((0, column - 1), board):
                        return (0, column - 1)
                
            else:
                if board[0][column] == board[0][column - 2] and (board[0][column] == enemy and board[0][column - 2] == enemy): #checks for two in corners of column
                    if is_empty((0, column - 1), board):
                        return (0, column - 1)
                
        for row in range(3):  #checks for two in a row (in diagonal) 
            if row == 0:
                if board[row][0] == board[row + 1][1] and (board[row][0] == enemy and board[row + 1][1] == enemy):
                    if is_empty((row + 2, 2), board):
                        return (row + 2, 2)

                elif board[row][2] == board[row + 1][1] and (board[row][2] == enemy and board[row + 1][1] == enemy):
                    if is_empty((row + 2, 0), board):
                        return (row + 2, 0)


            elif row == 1:
                if board[row][1] == board[row + 1][2] and (board[row][1] == enemy and board[row + 1][2] == enemy):
                    if is_empty((row - 1, 0), board):
                        return (row - 1, 0)

                elif board[row][1] == board[row + 1][0] and (board[row][1] == enemy and board[row + 1][0] == enemy):
                    if is_empty((row - 1, 2), board):
                        return (row - 1, 2)

            else: #checks for two in corners of diagonal
                if board[row][2] == board[row - 2][0] and (board[row][2] == enemy and board[row - 2][0] == enemy):
                    if is_empty((row - 1, 1), board):
                        return (row - 1, 1)

                elif board[row][0] == board[row - 2][2] and (board[row][0] == enemy and board[row - 2][2] == enemy):
                    if is_empty((row - 1, 1), board):
                        return (row - 1, 1)
                    
            for row in range(3):  #checks for two in a row (in row)
                if board[row][0] == board[row][1] and (board[row][0] == enemy and board[row][1] == enemy):
                    if is_empty((row, 2), board):
                        return (row, 2)
                
                elif board[row][1] == board[row][2] and (board[row][1] == enemy and board[row][2] == enemy):
                    if is_empty((row, 0), board):
                        return (row, 0)

                elif board[row][2] == board[row][0] and (board[row][2] == enemy and board[row][0] == enemy): #checks for two in corners of row
                    if is_empty((row, 1), board):
                        return (row, 1)

        #check for win
        for column in range(3): #checks for two in a row (in column)
            if column == 0:
                if (board[0][column] == board[0][column + 1]) and (board[0][column] == ai_player and board[0][column + 1] == ai_player):
                    if is_empty((0, column + 2), board):
                        return (0, column + 2)
                
            elif column == 1:
                if board[0][column] == board[0][column + 1] and (board[0][column] == ai_player and board[0][column + 1] == ai_player):
                    if is_empty((0, column - 1), board):
                        return (0, column - 1)
                
            else:
                if board[0][column] == board[0][column - 2] and (board[0][column] == ai_player and board[0][column - 2] == ai_player): #checks for two in corners of column
                    if is_empty((0, column - 1), board):
                        return (0, column - 1)
                
        for row in range(3):  #checks for two in a row (in diagonal) 
            if row == 0:
                if board[row][0] == board[row + 1][1] and (board[row][0] == ai_player and board[row + 1][1] == ai_player):
                    if is_empty((row + 2, 2), board):
                        return (row + 2, 2)

                elif board[row][2] == board[row + 1][1] and (board[row][2] == ai_player and board[row + 1][1] == ai_player):
                    if is_empty((row + 2, 0), board):
                        return (row + 2, 0)


            elif row == 1:
                if board[row][1] == board[row + 1][2] and (board[row][1] == ai_player and board[row + 1][2] == ai_player):
                    if is_empty((row - 1, 0), board):
                        return (row - 1, 0)

                elif board[row][1] == board[row + 1][0] and (board[row][1] == ai_player and board[row + 1][0] == ai_player):
                    if is_empty((row - 1, 2), board):
                        return (row - 1, 2)

            else: #checks for two in corners of diagonal
                if board[row][2] == board[row - 2][0] and (board[row][2] == ai_player and board[row - 2][0] == ai_player):
                    if is_empty((row - 1, 1), board):
                        return (row - 1, 1)

                elif board[row][0] == board[row - 2][2] and (board[row][0] == ai_player and board[row - 2][2] == ai_player):
                    if is_empty((row - 1, 1), board):
                        return (row - 1, 1)
                
    for corner in CORNERS: #checks for cell next to my cell
        row = corner[0]
        column = corner[1]
        if column == 0:
            if board[row][column + 1] == board[row][column] and (board[row][column + 1] == ai_player and board[row][column] == ai_player):
                if is_empty(corner, board):
                    return corner
        elif column == 2:
            if board[row][column - 1] == board[row][column] and (board[row][column - 1] == ai_player and board[row][column] == ai_player):
                if is_empty(corner, board):
                    return corner
        
        if row == 0:
            if board[row + 1][column] == board[row][column] and (board[row + 1][column] == ai_player and board[row][column] == ai_player):
                if is_empty(corner, board):
                    return corner
        elif row == 2:
            if board[row - 1][column] == board[row][column] and (board[row - 1][column] == ai_player and board[row][column] == ai_player):
                if is_empty(corner, board):
                    return corner
    else:    
        for corner in CORNERS:
            if is_empty(corner, board):
                return corner
            
        for middle in MIDDLE: #checks for cell next to my cell
            row = middle[0]
            column = middle[1]
            if row == 0 or row == 2:
                if board[row][column + 1] == board[row][column] or board[row][column - 1] == board[row][column] and ((board[row][column + 1] == ai_player or board[row][column] == ai_player) and (board[row][column - 1] == ai_player and board[row][column] == ai_player)):
                    if is_empty(middle, board):
                        return middle
                    
            elif row == 1:
                if board[1][1] == board[row][column] or board[row + 1][column] == board[row][column] or board[row -1][column] == board[row][column] and ((board[1][1] == ai_player or board[row][column] == ai_player) or (board[row + 1][column] == ai_player or board[row][column] == ai_player) or (board[row -1][column] == ai_player or board[row][column] == ai_player)):
                    if is_empty(middle, board):
                        return middle

        for middle in MIDDLE:
            if is_empty(middle, board):
                return middle
            
        for row in range(3):
            for column in range(3):
                if is_empty((row, column), board):
                    return (row, column)
