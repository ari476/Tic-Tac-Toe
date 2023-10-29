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
            if not TicTacToe.is_cell_empty((row, column)):
                return False
    return True

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
        if TicTacToe.is_cell_empty((1,1)):
            return (1,1)
        else:
            for corner in CORNERS:
                if TicTacToe.is_cell_empty(corner):
                    TURN = 4
                    return corner
                
    elif TURN >= 3:  #not first or second turn
        for row in range(3):  #checks for two in a row (in row)
            if board[row][0] == board[row][1]:
                TURN = TURN + 2
                return (row, 2)
            
            elif board[row][1] == board[row][2]:
                TURN = TURN + 2
                return (row, 0)
            
            elif board[row][2] == board[row][0]: #checks for two in corners of row
                TURN = TURN + 2
                return (row, 1)


        for column in range(3): #checks for two in a row (in column)
            if column == 0:
                if board[0][column] == board[0][column + 1]:
                    TURN = TURN + 2
                    return (0, column + 2)
                
            elif column == 1:
                if board[0][column] == board[0][column + 1]:
                    TURN = TURN + 2
                    return (0, column - 1)
                
            else:
                if board[0][column] == board[0][column - 2]: #checks for two in corners of column
                    TURN = TURN + 2
                    return (0, column - 1)
                
        for row in range(3):  #checks for two in a row (in diagonal) 
            if row == 0:
                if board[row][0] == board[row + 1][1]:
                    TURN = TURN + 2
                    return (row + 2, 2)

                elif board[row][2] == board[row + 1][1]:
                    TURN = TURN + 2
                    return (row + 2, 0)


            elif row == 1:
                if board[row][1] == board[row + 1][2]:
                    TURN = TURN + 2
                    return (row - 1, 0)

                elif board[row][1] == board[row + 1][0]:
                    TURN = TURN + 2
                    return (row - 1, 2)

            else: #checks for two in corners of diagonal
                if board[row][2] == board[row - 2][0]:
                    TURN = TURN + 2
                    return (row - 1, 1)

                elif board[row][0] == board[row - 2][2]:
                    TURN = TURN + 2
                    return (row - 1, 1)
                
    else:
        for corner in CORNERS:
            #add if cell next to it is my cell
            if TicTacToe.is_cell_empty(corner):
                TURN = TURN + 2
                return corner
            
        for middle in MIDDLE:
            #add if cell next to it is my cell
            if TicTacToe.is_cell_empty(middle):
                TURN = TURN + 2
                return middle
            
        
