from game_logic import Player
from typing import List
from game_logic import TicTacToe


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    cells = [(0,0) ,(0,1),(0,2),(1,0) ,(1,1),(1,2) ,(2,0) ,(2,1),(2,2)]
    ############################################################
    # CHECK IF AI_PLAYER CAN WIN
    ############################################################
    for row in range(3):
        result =[board[row][col] for col in range(3) if board[row][col] == ai_player]
        if len(result) ==2:
            print("work")
            if board[row][0] == None:
                return (row,0)
            elif board[row][1] == None:
                return (row,1)
            elif board[row][2] == None:
                return (row,2)

                   
    for col in range(3):
        result = [board[row][col] for row in range(3) if board[row][col] == ai_player]
        if len(result) == 2:
            print("work")
            if board[0][col] == None:
                return (0,col)
            elif board[1][col] == None:
                return (1,col)
            elif board[2][col] == None:
                return (2,col)
            
    if board[0][0] == board[1][1] == ai_player and board[2][2] == None:
        print("work")
        return (2,2)
    if board[0][0] == board[2][2] == ai_player and board[1][1] == None:
        print("work")
        return (1,1)
    if board[2][2] == board[1][1] == ai_player and board[0][0] == None:
        print("work")
        return (0,0)
    if board[0][2] == board[1][1] == ai_player and board[2][0] == None:
        print("work")
        return (2,0)
    if board[0][2] == board[2][0] == ai_player and board[1][1] == None:
        print("work")
        return (1,1)
    if board[2][0] == board[1][1] == ai_player and board[0][2] == None:
        print("work")
        return (0,2)
    
    ############################################################
    # CHECK IF OTHER PLAYER CAN WIN AND BLOCK IT 
    ############################################################
    for row in range(3):
        result =[board[row][col] for col in range(3) if board[row][col] != ai_player and board[row][col] is not None]
        if len(result) ==2:
            print("work")
            if board[row][0] == None:
                return (row,0)
            elif board[row][1] == None:
                return (row,1)
            elif board[row][2] == None:
                return (row,2)

                   
    for col in range(3):
        result = [board[row][col] for row in range(3) if board[row][col] != ai_player and board[row][col] is not None]
        if len(result) == 2:
            print("work")
            if board[0][col] == None:
                return (0,col)
            elif board[1][col] == None:
                return (1,col)
            elif board[2][col]== None:
                return (2,col)
            
    if board[0][0] == board[1][1] and board[0][0] != ai_player and board[2][2] is None and board[0][0] is not None:
        print("work")
        return (2,2)
    if board[0][0] == board[2][2] and board[0][0]!= ai_player and board[1][1] is None and board[0][0] is not None:
        print("work")
        return (1,1)
    if board[2][2] == board[1][1] and board[2][2]!= ai_player and board[0][0] is None and board[2][2] is not None:
        print("work")
        return (0,0)
    if board[0][2] == board[1][1] and board[0][2]!= ai_player and board[2][0] is None and board[0][2] is not None:
        print("work")
        return (2,0)
    if board[0][2] == board[2][0] and board[0][2]!= ai_player and board[1][1] is None and board[0][2] is not None:
        print("work")
        return (1,1)
    if board[2][0] == board[1][1] and board[2][0]!= ai_player and board[0][2] is None and board[2][0] is not None:
        print("work")
        return (0,2)
    
    ############################################################
    # SEARCH WHERE IS THE BEST TO PUT
    ############################################################
    corners = [(0,0),(0,2),(2,0),(2,2)]
    for cell in cells:
        if board[cell[0]][cell[1]] is not None and board[cell[0]][cell[1]] != ai_player:
            if board[1][1] is None:
                return (1,1)
            else:
                if cell[0] == 0 and cell[1] == 1:
                    if board[1][0] != ai_player and board[1][0] is not None:
                        if board[0][0] is None:
                            return (0,0)
                    elif board[1][2] != ai_player and board[1][2] is not None:
                        if board[0][2] is None:
                            return (0,2)
                elif cell[0] == 2 and cell[1] == 1:
                    if board[1][0] != ai_player and board[1][0] is not None:
                        if board[2][0] is None:
                            return (2,0)
                    elif board[1][2] != ai_player and board[1][2] is not None:
                        if board[2][2] is None:
                            return (2,2)
    for corner in corners:
        if board[corner[0]][corner[1]] is None:
            return corner
    
    plus = [(0,1),(1,0),(1,2),(2,1)]
    for p in plus:
        if board[p[0]][p[1]] is None:
            return p