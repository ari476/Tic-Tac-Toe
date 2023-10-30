from game_logic import Player
from typing import List
from game_logic import TicTacToe
import random

IS_FIRST_TURN = True

def is_empty(board: List[List]) -> bool:
    global IS_FIRST_TURN 

    if IS_FIRST_TURN == True: 
        for column in board:
            for row in column:
                if TicTacToe.is_cell_empty((column,row)) == False:
                    return False  
    return True


def is_cell_empty(board: List[List], cell_pos):
    return board[cell_pos[0]][cell_pos[1]] is None


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    """
    Args:
        board (List[List[Player]]): current state of board in the game
        ai_player (Player): X or O enum 

    Returns:
        tuple: cell position for placing the next symbol on the game board
    """
    global IS_FIRST_TURN

    # i've defined if the corner is occupied, and the place of the corners 
    list_corners = [[False, (0,2)], [False, (0,0)], [False, (2,2)], [False, (2,0)]]

    if IS_FIRST_TURN == True:  # if its the first turn 
        IS_FIRST_TURN = False

        if ai_player == Player.X: # if the ai starts
            rnd_list = [(2,0), (0,0), (2,0), (2,2)]
            return random.choice(rnd_list) # put the ai in the corners

        else :
            if is_cell_empty(board, (1,1)) == True:
                return (1,1)
            else:
                for i in range(3):
                    if is_cell_empty(board, list_corners[i][1]) == True:
                        list_corners[i][1] = True

                list_of_options = list(filter(lambda x: x, list_corners[i][0])) # a list of the corners that aren't occupied
                rand_idx = random.randrange(len(list_of_options)) 
                return list_of_options[rand_idx][1]

    else:
        if ai_player == Player.O:
            enemy = Player.X
        else:
            enemy = Player.O

        if is_cell_empty(board, (1,1)) == True:
            return (1,1)
        
        else: 
            #if 2 in a row 
            
            if board[0][0] == enemy and board[0][1] == enemy and is_cell_empty(board, (0, 2)) == True:
                return (0, 2)
            
            elif board[0][1] == enemy and board[0][2] == enemy and is_cell_empty(board, (0, 0)) == True:
                return (0, 0)
            
            elif board[0][2] == enemy and board[1][2] == enemy and is_cell_empty(board, (2, 2)) == True:
                return (2, 2)
            
            elif board[1][2] == enemy and board[2][2] == enemy and is_cell_empty(board, (0, 2)) == True:
                return (0, 2)
            
            elif board[2][1] == enemy and board[2][2] == enemy and is_cell_empty(board, (0, 2)) == True:
                return (0, 2)

            elif board[2][1] == enemy and board[2][0] == enemy and is_cell_empty(board, (2, 2)) == True:
                return (2, 2)
            
            elif board[2][0] == enemy and board[1][0] == enemy and is_cell_empty(board, (0, 0)) == True:
                return (0, 0)
            
            elif board[1][0] == enemy and board[0][0] == enemy and is_cell_empty(board, (2, 0)) == True:
                return (2, 0)
            
            elif board[0][0] == enemy and board[2][1] == enemy and is_cell_empty(board, (2, 0)) == True:
                return (2, 0)
            
            elif board[0][2] == enemy and board[2][1] == enemy and is_cell_empty(board, (2, 2)) == True:
                return (2, 2)
            
            # if 2 in a row thru the center
            
            elif board[1][1] == enemy and board[0][1] == enemy and is_cell_empty(board, (2, 1)) == True:
                return (2, 1)
            
            elif board[1][1] == enemy and board[1][0] == enemy and is_cell_empty(board, (1, 2)) == True: 
                return (1, 2)
            
            elif board[1][1] == enemy and board[1][2] == enemy and is_cell_empty(board, (1, 0)) == True:
                return (1, 0)
            
            elif board[1][1] == enemy and board[2][1] == enemy and is_cell_empty(board, (0, 1)) == True:
                return (0, 1)

            # if 2 in a row in the corners
          
            elif board[2][0] == enemy and board[2][2] == enemy and is_cell_empty(board, (2, 1)) == True:
                return (2, 1)

            elif board[2][0] == enemy and board[0][0] == enemy and is_cell_empty(board, (1, 0)) == True:
                return (1, 0)
            
            elif board[0][2] == enemy and board[0][0] == enemy and is_cell_empty(board, (0, 1)) == True:
                return (0, 1)
            
            elif board[0][2] == enemy and board[2][2] == enemy and is_cell_empty(board, (1, 2)) == True:
                return (1, 2)

            else: # if 2 in diagonal with the center occupied
                if board[1][1] == enemy and board[2][2] == enemy and is_cell_empty(board, (0, 0)) == True:
                    return (0, 0)
                elif board[1][1] == enemy and board[2][0] == enemy and is_cell_empty(board, (1, 0)) == True:
                    return (1, 0)
                elif board[1][1] == enemy and board[0][0] == enemy and is_cell_empty(board, (2, 2)) == True:
                    return (2, 2)
                elif board[1][1] == enemy and board[0][2] == enemy and is_cell_empty(board, (2, 0)) == True:
                    return (2, 0)
                
                # if 2 in diagonal without the center occupied
                elif ((board[0][0] == enemy and board[2][2] == enemy) or (board[0][2] == enemy and board[2][0]== enemy)) and is_cell_empty(board, (1, 1)) == True:
                    return (1, 1)
                
                elif board[0][0] == enemy and board[0][2] == enemy and board[1][1] == ai_player:
                    list_of_not_corners = [(1, 0), (1, 2), (0, 1), (0, 2)]
                    flag = True
                    while flag:
                        choices = random.choice(list_of_not_corners)
                        if is_cell_empty(board, choices) == True:
                            flag = False
                            return choices
                        

                elif board[2][0] == enemy and board[0][2] == enemy and board[1][1] == ai_player:
                    list_of_not_corners = [(1, 0), (1, 2), (0, 1), (2, 1)]

                    for points in list_of_not_corners: # check which is occupied and remove them
                        if is_cell_empty(board, points) == False:
                            list_of_not_corners.remove(points)
                    
                    flag = True
                    while flag:
                        choices = random.choice(list_of_not_corners)
                        flag = False
                        return choices

                else:
                    flag = True
                    while flag:
                        for i in range(len(board)):
                            for j in range(len(board)):
                                if is_cell_empty(board, (i, j)) == True:
                                    flag = False
                                    return (i, j)
                                
                
