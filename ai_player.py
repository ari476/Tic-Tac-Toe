from game_logic import Player
from typing import List
from game_logic import TicTacToe
import random

# This function returns true if there are moves  
# remaining on the board. It returns false if  
# there are no moves left to play.  
def is_moves_left(board) :  

    for row in range(3) : 
        for col in range(3) : 
            if (board[row][col] == None) : 
                return True 
    return False

# This is the evaluation function as discussed  
# in the previous article ( http://goo.gl/sJgv68 )  
def evaluate(board) :  
    
    # Checking for Rows for X or O victory.  
    for row in range(3) :      
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :         
            if (board[row][0] == player) : 
                return 10
            elif (board[row][0] == opponent) : 
                return -10

    # Checking for Columns for X or O victory.  
    for col in range(3) : 
    
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) : 
        
            if (board[0][col] == player) :  
                return 10
            elif (board[0][col] == opponent) : 
                return -10

    # Checking for Diagonals for X or O victory.  
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) : 
    
        if (board[0][0] == player) : 
            return 10
        elif (board[0][0] == opponent) : 
            return -10

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) : 
    
        if (board[0][2] == player) : 
            return 10
        elif (board[0][2] == opponent) : 
            return -10

    # Else if none of them have won then return 0  
    return 0

# This is the minimax function. It considers all  
# the possible ways the game can go and returns  
# the value of the board  
def minimax(board, depth, isMax) :  
    score = evaluate(board) 

    # If Maximizer has won the game return his/her  
    # evaluated score  
    if (score == 10) :  
        return score 

    # If Minimizer has won the game return his/her  
    # evaluated score  
    if (score == -10) : 
        return score 

    # If there are no more moves and no winner then  
    # it is a tie  
    if (is_moves_left(board) == False) : 
        return 0

    # If this maximizer's move  
    if (isMax) :      
        best = -1000 

        # Traverse all cells  
        for i in range(3) :          
            for j in range(3) : 
            
                # Check if cell is empty  
                if (board[i][j]=='_') : 
                
                    # Make the move  
                    board[i][j] = player  

                    # Call minimax recursively and choose  
                    # the maximum value  
                    best = max( best, minimax(board, 
                                            depth + 1, 
                                            not isMax) ) 

                    # Undo the move  
                    board[i][j] = '_'
        return best 

    # If this minimizer's move  
    else : 
        best = 1000 

        # Traverse all cells  
        for i in range(3) :          
            for j in range(3) : 
            
                # Check if cell is empty  
                if (board[i][j] == '_') : 
                
                    # Make the move  
                    board[i][j] = opponent  

                    # Call minimax recursively and choose  
                    # the minimum value  
                    best = min(best, minimax(board, depth + 1, not isMax)) 

                    # Undo the move  
                    board[i][j] = '_'
        return best 

# This will return the best possible move for the player  
def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
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
    bestVal = -1000 
    bestMove = (-1, -1)  

    # Traverse all cells, evaluate minimax function for  
    # all empty cells. And return the cell with optimal  
    # value.  
    for row in range(3) :      
        for col in range(3) : 
        
            # Check if cell is empty  
            if (board[row][col] == None) :  
            
                # Make the move  
                board[row][col] = player 

                # compute evaluation function for this  
                # move.  
                moveVal = minimax(board, 0, False)  

                # Undo the move  
                board[row][col] = None

                # If the value of the current move is  
                # more than the best value, then update  
                # best/  
                if (moveVal > bestVal) :                 
                    bestMove = (row, col) 
                    bestVal = moveVal 
    return bestMove 