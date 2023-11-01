from game_logic import Player
from typing import List
from game_logic import TicTacToe
import random

def is_moves_left(board) :  #checks if there are moves left to do

    for row in range(3) : 
        for col in range(3) : 
            if (board[row][col] == None) : 
                return True 
    return False
 
def evaluate_move(board, player, opponent) :  
    
    for row in range(3) :     #checks victory in row (x or o)
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :         
            if (board[row][0] == player) : 
                return 10
            elif (board[row][0] == opponent) : 
                return -10

    for col in range(3) : #checks victory in column (x or o)
    
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) : 
        
            if (board[0][col] == player) :  
                return 10
            elif (board[0][col] == opponent) : 
                return -10

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) : #checks victory in diagonal (x or o)
    
        if (board[0][0] == player) : 
            return 10
        elif (board[0][0] == opponent) : 
            return -10

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) : 
    
        if (board[0][2] == player) : 
            return 10
        elif (board[0][2] == opponent) : 
            return -10


    return 0 # returns 0 if there are no wins

def minimax(board, depth, is_max, player, opponent) :  #minimax function (checks all ways the game could go) returns 10 for win for ai, -10 for lose and 0 for tie
    score = evaluate_move(board, player, opponent) 

    if (score == 10) :  
        return score 

    elif (score == -10) : 
        return score 

    elif (is_moves_left(board) == False) : 
        return 0

    if (is_max) :      #when it is the ai move
        best = -1000 

        for row in range(3) :          
            for col in range(3) : 
            
                if (board[row][col] == None) : 
                    board[row][col] = player  #tries the move
                    best = max( best, minimax(board, depth + 1, not is_max, player, opponent) ) #checks if this move is the best
                    board[row][col] = None  #delete the move
        return best 

    else :        #when it is the enemy move
        best = 1000 

        for row in range(3) :          
            for col in range(3) : 
            
                if (board[row][col] == None) : 
                    board[row][col] = opponent  
                    best = min(best, minimax(board, depth + 1, not is_max, player, opponent)) 
                    board[row][col] = None
        return best 

def make_decision(board: List[List[Player]], ai_player: Player) -> tuple: #returns best move for ai
    """
    Args:
        board (List[List[Player]]): current state of board in the game
        ai_player (Player): X or O enum 

    Returns:
        tuple: cell position for placing the next symbol on the game board
        (y, x)
    """  
    if ai_player == Player.X:
        player = Player.X
        opponent = Player.O
    else:
        opponent = Player.X
        player = Player.O

    best_val = -1000 
    best_move = (-1, -1)  

    for row in range(3) :      
        for col in range(3) : 

            if (board[row][col] == None) :  
                board[row][col] = player 
                move_val = minimax(board, 0, False, player, opponent)  
                board[row][col] = None

                if (move_val > best_val) :                 
                    best_move = (row, col) 
                    best_val = move_val 

    return best_move 