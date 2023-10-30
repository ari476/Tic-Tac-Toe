from game_logic import Player
from typing import List
from game_logic import TicTacToe





def is_empty(board: List[List[Player]]) -> bool:
    for row in board:
        for square in row:
            if square != None:
                return False

    return True


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    """
    Args:
        board (List[List[Player]]): current state of board in the game
        ai_player (Player): X or O enum

    Returns:
        tuple: cell position for placing the next symbol on the game board
    """
    if ai_player == Player.X:
        enemy = Player.O
    else:
        enemy = Player.X

    if is_empty(board):
        """
        if the board is empty we pick 
        middle to make sure we tie!
        """
        board[1][1] = ai_player
        print("first")
        return (1, 1)
    

    if board[1][1] == None:
        board[1][1] = ai_player
        return (1, 1)
    
    print(enemy)


    """
    occasion 1:
    Here we check every horizontal line to see 
    if we have 2 in a row or the enemy have 2 in a row.
    """
    enemy_count = 0
    me_count = 0
    for tor in range(len(board)):
        for shura in range(len(board)):
            if board[tor][shura] == enemy:
                enemy_count += 1

            if board[tor][shura] == ai_player:
                me_count += 1

        if enemy_count == 2 or me_count == 2:
            for shura in range(len(board)):
                if board[tor][shura] == None:
                    board[tor][shura] = ai_player
                    return (tor, shura)

        enemy_count = 0
        me_count = 0

    """
    occasion 2:
    Here we check every vertical line to 
    see if we have 2 in a row or the enemy have 2 in a row.
    """
    for shura in range(len(board)):
        for tor in range(len(board)):
            if board[tor][shura] == enemy:
                enemy_count += 1

            if board[tor][shura] == ai_player:
                me_count += 1

        if enemy_count == 2 or me_count == 2:
            for tor in range(len(board)):
                if board[tor][shura] == None:
                    board[tor][shura] = ai_player
                    return (tor, shura)

        enemy_count = 0
        me_count = 0

    """
    occasion 3:
    here we check one type of diagonal 
    to see if there 2 enemy's or ai blocks
    """
    memory = (0, 0)
    enemy_count = 0
    me_count = 0
    for i in range(3):
        if board[i][i] == enemy:
            enemy_count += 1

        if board[i][i] == ai_player:
            me_count += 1

        if board[i][i] == None:
            memory = (i, i)

    if (enemy_count == 2 or me_count == 2) and board[memory[0]][memory[1]] == None:
        board[memory[0]][memory[1]] = ai_player
        return memory

    """
    occasion 5:
    check if the enemy holds both
    corners to reduce vulnerability
    """
    if (board[0][0] == enemy and board[2][2] == enemy) or (board[0][2] == enemy and board[2][0]):
        if board[0][1] == None:
            board[0][1] = enemy
            return (0, 1)

        elif board[2][1] == None:
            board[2][1] = enemy
            return (2, 1)
        
        elif board[1][0] == None:
            board[1][0] = enemy
            return (1, 0)
        
        elif board[1][2] == None:
            board[1][2] = enemy
            return (1, 2)
        

    """
    occasion 4:
    here we check one type of diagonal 
    to see if there 2 enemy's or ai blocks
    """
    enemy_count = 0
    me_count = 0
    for i in range(3):
        if board[i][2 - i] == enemy:
            enemy_count += 1

        if board[i][2 - i] == ai_player:
            me_count += 1

        if board[i][2 - i] == None:
            memory = (i, 2 - i)

    if (enemy_count == 2 or me_count == 2) and board[memory[0]][memory[1]] == None:
        board[memory[0]][memory[1]] = ai_player
        return memory
    

    if board[0][0] == enemy and board[2][1] == enemy and board[2][0] == None:
        board[2][0] = ai_player
        return(2,0)

        
    """
    if non of the occasions 
    is activated we pick a random block
    """
    for tor in range(len(board)):
        for shura in range(len(board)):
            if board[tor][shura] == None:
                board[tor][shura] = ai_player
                return (tor, shura)
