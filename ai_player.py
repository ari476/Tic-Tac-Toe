from game_logic import Player
from typing import List
from game_logic import TicTacToe
import random

TURN = 1
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

def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    """
    Args:
        board (List[List[Player]]): current state of board in the game
        ai_player (Player): X or O enum 

    Returns:
        tuple: cell position for placing the next symbol on the game board
        (y, x)
    """

    global TURN
    global CORNERS
    global MIDDLE

    if is_board_empty(board):  #checks if computer is first
        corner = CORNERS[random.randrange(0,4)]
        TURN = TURN + 2
        return corner
    
    elif TURN == 1:  #if computer is second
        if is_empty((1,1), board):
            return (1,1)
        else:
            for corner in CORNERS:
                if is_empty(corner, board):
                    TURN = 4
                    return corner
                
    elif TURN >= 3:  #not first or second turn
        for row in range(3):  #checks for two in a row (in row)
            if board[row][0] == board[row][1]:
                TURN = TURN + 2
                if is_empty((row, 2), board):
                    return (row, 2)
            
            elif board[row][1] == board[row][2]:
                TURN = TURN + 2
                if is_empty((row, 0), board):
                    return (row, 0)
            
            elif board[row][2] == board[row][0]: #checks for two in corners of row
                TURN = TURN + 2
                if is_empty((row, 1), board):
                    return (row, 1)


        for column in range(3): #checks for two in a row (in column)
            if column == 0:
                if board[0][column] == board[0][column + 1]:
                    TURN = TURN + 2
                    if is_empty((0, column + 2), board):
                        return (0, column + 2)
                
            elif column == 1:
                if board[0][column] == board[0][column + 1]:
                    TURN = TURN + 2
                    if is_empty((0, column - 1), board):
                        return (0, column - 1)
                
            else:
                if board[0][column] == board[0][column - 2]: #checks for two in corners of column
                    TURN = TURN + 2
                    if is_empty((0, column - 1), board):
                        return (0, column - 1)
                
        for row in range(3):  #checks for two in a row (in diagonal) 
            if row == 0:
                if board[row][0] == board[row + 1][1]:
                    TURN = TURN + 2
                    if is_empty((row + 2, 2), board):
                        return (row + 2, 2)

                elif board[row][2] == board[row + 1][1]:
                    TURN = TURN + 2
                    if is_empty((row + 2, 0), board):
                        return (row + 2, 0)


            elif row == 1:
                if board[row][1] == board[row + 1][2]:
                    TURN = TURN + 2
                    if is_empty((row - 1, 0), board):
                        return (row - 1, 0)

                elif board[row][1] == board[row + 1][0]:
                    TURN = TURN + 2
                    if is_empty((row - 1, 2), board):
                        return (row - 1, 2)

            else: #checks for two in corners of diagonal
                if board[row][2] == board[row - 2][0]:
                    TURN = TURN + 2
                    if is_empty((row - 1, 1), board):
                        return (row - 1, 1)

                elif board[row][0] == board[row - 2][2]:
                    TURN = TURN + 2
                    if is_empty((row - 1, 1), board):
                        return (row - 1, 1)
                
    else:
        for corner in CORNERS: #checks for cell next to my cell
            row = corner[0]
            column = corner[1]
            if column == 0:
                if board[row, column + 1] == board[row, column]:
                    if is_empty(corner, board):
                        TURN = TURN + 2
                        return corner
            elif column == 2:
                if board[row, column - 1] == board[row, column]:
                    if is_empty(corner, board):
                        TURN = TURN + 2
                        return corner
            
            if row == 0:
                if board[row + 1, column] == board[row, column]:
                    if is_empty(corner, board):
                        TURN = TURN + 2
                        return corner
            elif row == 2:
                if board[row - 1, column] == board[row, column]:
                    if is_empty(corner, board):
                        TURN = TURN + 2
                        return corner
            
        for corner in CORNERS:
            if is_empty(corner, board):
                TURN = TURN + 2
                return corner
            
        for middle in MIDDLE: #checks for cell next to my cell
            row = middle[0]
            column = middle[1]
            if row == 0 or row == 2:
                if board[row, column + 1] == board[row, column] or board[row, column - 1] == board[row, column]:
                    if is_empty(middle, board):
                        TURN = TURN + 2
                        return middle
                    
            elif row == 1:
                if board[1, 1] == board[row, column] or board[row + 1, column] == board[row, column] or board[row -1, column] == board[row, column]:
                    if is_empty(middle, board):
                        TURN = TURN + 2
                        return middle

        for middle in MIDDLE:
            if is_empty(middle, board):
                TURN = TURN + 2
                return middle
            
        
