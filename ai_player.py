from game_logic import Player
from typing import List
from game_logic import TicTacToe


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
# -----------------------------                     play              -------------------------------------------
    # check for possible winning in rows
    for row in range(3):
        match = [board[row][col] for col in range(3) if board[row][col] == ai_player]
        if len(match) == 2:
            if board[row][0] == None:
                return (row,0)
            elif board[row][1] == None:
                return (row,1)
            elif board[row][2] == None:
                return (row,2)
            
    # check for possible winning in colum
    for col in range(3):
        match = [board[row][col] for row in range(3) if board[row][col] == ai_player]
        if len(match) == 2:
            if board[0][col] == None:
                return (0, col)
            elif board[1][col] == None:
                return (1, col)
            elif board[2][col] == None:
                return (2, col)
            
    # check for possible winning in diagonals
    if board[0][0] == board[1][1] == ai_player and board[2][2] == None:
        return (2,2)
    if board[0][0] == board[2][2] == ai_player and board[1][1] == None:
        return (1,1)
    if board[2][2] == board[1][1] == ai_player and board[0][0] == None:
        return (0,0)
    if board[0][2] == board[1][1] == ai_player and board[2][0] == None:
        return (2,0)
    if board[0][2] == board[2][0] == ai_player and board[1][1] == None:
        return (1,1)
    if board[2][0] == board[1][1] == ai_player and board[0][2] == None:
        return (0,2)

#   -----------------------------                   defense             -------------------------------------------
    # check for enemy's possible winning in rows
    for row in range(3):
        not_match = [board[row][col] for col in range(3) if board[row][col] != ai_player and board[row][col] is not None]
        if len(not_match) == 2:
            if board[row][0] == None:
                return (row, 0)
            elif board[row][1] == None:
                return (row, 1)
            elif board[row][2] == None:
                return (row, 2)
            
    # check for enemy's possible winning in colum
    for col in range(3):
        not_match = [board[row][col] for row in range(3) if board[row][col] != ai_player and board[row][col] is not None]
        if len(not_match) == 2:
            if board[0][col] == None:
                return (0, col)
            elif board[1][col] == None:
                return (1, col)
            elif board[2][col] == None:
                return (2, col)
            
    # check for enemy's possible winning in diagonals
    if board[0][0] == board[1][1] != ai_player and board[2][2] is None and board[0][0] is not None:
        return (2, 2)
    if board[0][0] == board[2][2] != ai_player and board[1][1] is None and board[0][0] is not None:
        return (1, 1)
    if board[2][2] == board[1][1] != ai_player and board[0][0] is None and board[2][2] is not None:
        return (0, 0)
    if board[0][2] == board[1][1] != ai_player and board[2][0] is None and board[0][2] is not None:
        return (2, 0)
    if board[0][2] == board[2][0] != ai_player and board[1][1] is None and board[0][2] is not None:
        return (1, 1)
    if board[2][0] == board[1][1] != ai_player and board[0][2] is None and board[2][0] is not None:
        return (0, 2)

# ----------------------------------------------------------        moves     ------------------------------------------
    all_cells = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    for cell in all_cells:
         # check if the border is empty. if is not, check if is fill with the ai value.
         if board[cell[0]][cell[1]] is not None and board[cell[0]][cell[1]] != ai_player: 
            # if the middle cell is empty - the best move is to put there.
            if board[1][1] is None:
                return (1,1) 
              
    # in the following conditions we going to block threats from pluses((0,1), (2,1), (1,0), (1,2)), and avoid from double threats.     
    if board[0][1] != ai_player and board[0][1] is not None:
        if (board[1][0] != ai_player and board[1][0] is not None) or (board[2][0] != ai_player and board[2][0] is not None):
            if board[0][0] is None:
                return (0,0)
        elif board[1][2] != ai_player and board[1][2] is not None:
            if board[0][2] is None:
                return (0,2)
        elif board[2][2] != ai_player and board[2][2] is not None:
            if board[0][2] is None:
                return (0,2)
            
    elif board[2][1] != ai_player and board[2][1] is not None:
        if board[1][0] != ai_player and board[1][0] is not None:
            if board[2][0] is None:
                return (2,0)
        elif board[0][0] != ai_player and board[0][0] is not None:
            if board[2][0] is None:
                return (2,0)
        elif board[1][2] != ai_player and board[1][2] is not None:
            if board[2][2] is None:
                return (2,2)
        elif board[0][2] != ai_player and board[0][2] is not None:
            if board[2][2] is None:
                return (2,2)
            
    elif board[1][0] != ai_player and board[1][0] is not None: 
        if board[0][2] != ai_player and board[0][2] is not None:
            if board[0][0] is None:
                return (0,0)  
        elif board[2][2] != ai_player and board[2][2] is not None:
            if board[2][0] is None:
                return (2,0) 
            
    elif board[1][2] != ai_player and board[1][2] is not None:
        if board[0][0] != ai_player and board[0][0] is not None:
            if board[0][2] is None:
                return (0,2) 
        elif board[2][0] != ai_player and board[2][0] is not None:
            if board[2][2] is None:
                return (2,2) 

    all_corners = [(0,0), (0,2), (2,0), (2,2)] 
    pluses = [(0,1), (1,0), (1,2), (2,1)]
# if the enemy put in two corners you block him in one of the pluses and dont go to the middle like always.
    for one_corner in all_corners:
        if board[one_corner[0]][one_corner[1]] != ai_player and board[one_corner[0]][one_corner[1]] != None:
            for plus in pluses:
                if board[plus[0]][plus[1]] is None:
                    return plus
            
# after we check all and we cant win and we cant lose do this   
    for one_corner in all_corners:
        if board[one_corner[0]][one_corner[1]] is None:
            return one_corner                   
  
    for plus in pluses:
        if board[plus[0]][plus[1]] is None:
            return plus
