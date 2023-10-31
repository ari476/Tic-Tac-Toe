from game_logic import Player
from typing import List
from game_logic import TicTacToe
import random


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    """
    Args:
        board (List[List[Player]]): current state of board in the game
        ai_player (Player): X or O enum 

    Returns:
        tuple: cell position for placing the next symbol on the game board
    """
    o_counter = count_x_and_o(board)[1]
    if ai_player == Player.X: #if ai_player starts
        user_player = Player.O
    else: 
        user_player = Player.X

    if o_counter == 0:
        if ai_player == Player.X:
            return (1,1)
        else:
            if not [1, 1] in get_positions(board, user_player):
                return (1, 1) 
            elif board[0][1] == user_player:
                return (0,2)
            elif board[1][0] == user_player:
                return (1,2)
            elif board[2][1] == user_player:
                return (0,1)
            elif board[1][2] == user_player:
                return (1,0)
            else:
                return (0, 0)
    if o_counter == 1: #if ai_player and user made both one move
        block_diagonal_cell = last_cell_diagonal(board, user_player)
        if block_diagonal_cell[0] != -1 and not block_diagonal_cell in get_positions(board, ai_player):
            return block_diagonal_cell
        block_row_cell = last_cell_rows(board, user_player)
        if block_row_cell[1] != -1 and not block_row_cell in get_positions(board, ai_player):
            return block_row_cell
        block_column_cell = last_cell_column(board, user_player)
        if block_column_cell[0] != -1 and not block_column_cell in get_positions(board, ai_player):
            return block_column_cell
        if board[0][0] == user_player or board[2][2] == user_player:
            if board[1][1] == ai_player:
                return random.choice([(1,0), (2,1)])
        if board[0][2] == user_player or board[2][0] == user_player:
            if board[1][1] == ai_player:
                return random.choice([(0,1), (2,1)])
        block_small_diagonal = check_small_diagonal(board, user_player)
        if block_small_diagonal[0] != -1 and not block_small_diagonal in get_positions(board, ai_player):
            return block_small_diagonal
        pos_one_in_row = one_in_row(board, ai_player)
        if pos_one_in_row[0] != -1 and not pos_one_in_row in get_positions(board, user_player):
            return pos_one_in_row
        pos_one_in_column = one_in_column(board, ai_player)
        if pos_one_in_column[0] != -1 and not pos_one_in_column:
                return pos_one_in_column
    else: #if ai_player and user made more than one move each
        diagonal_cell = last_cell_diagonal(board, ai_player)
        if diagonal_cell[0] != -1 and not diagonal_cell in get_positions(board, user_player):
            return diagonal_cell
        position_rows = last_cell_rows(board, ai_player)
        if position_rows[1] != -1 and not position_rows in get_positions(board, user_player):
            return position_rows
        position_column = last_cell_column(board, ai_player)
        if position_column[0] != -1 and not position_column in get_positions(board, user_player):
            return position_column
        block_diagonal_cell = last_cell_diagonal(board, user_player)
        if block_diagonal_cell[0] != -1 and not block_diagonal_cell in get_positions(board, ai_player):
            return block_diagonal_cell
        block_row_cell = last_cell_rows(board, user_player)
        if block_row_cell[1] != -1 and not block_row_cell in get_positions(board, ai_player):
            return block_row_cell
        block_column_cell = last_cell_column(board, user_player)
        if block_column_cell[0] != -1 and not block_column_cell in get_positions(board, ai_player):
            return block_column_cell
        block_small_diagonal = check_small_diagonal(board, user_player)
        if block_small_diagonal[0] != -1 and not block_small_diagonal in get_positions(board, ai_player):
            return block_small_diagonal
        pos_one_in_row = one_in_row(board, ai_player)
        if pos_one_in_row[0] != -1 and not pos_one_in_row in get_positions(board, user_player):
            return pos_one_in_row
        pos_one_in_column = one_in_column(board, ai_player)
        if pos_one_in_column[0] != -1 and not pos_one_in_column in get_positions(board, user_player):
                return pos_one_in_column
    for row in range(3):
        for cell in range(3):
            if board[row][cell] is None:
                return (row, cell)

def count_x_and_o(board: List[List[Player]]) -> list:
    """
    a function that returns the number of Xs and Os in the game
    """
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == Player.X:
                count_x = count_x + 1
            if cell == Player.O:
                count_o = count_o + 1
    return [count_x, count_o]
    
def get_positions(board: List[List[Player]], player) -> list:
    get_positions = []
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == player:
                get_positions.append([row, cell])
    return get_positions

def last_cell_rows(board: List[List[Player]], player) -> tuple:
    for row in range(len(board)):
        cells_counter = 0
        empty_cell = -1
        for cell in range(len(board[row])):
            if board[row][cell] == player:
                cells_counter += 1
            elif board[row][cell] == None:
                empty_cell = cell                
        if cells_counter == 2 and empty_cell != -1:
             return (row, empty_cell)
    return (-1, -1)


def last_cell_column(board: List[List[Player]], player) -> tuple[int, int]:
    for i in range(3):  
        if board[0][i] == player and board[1][i] == player and board[2][i] is None:
            return (2, i)
        if board[0][i] == player and board[2][i] == player and board[1][i] is None:
            return (1, i)
        if board[1][i] == player and board[2][i] == player and board[0][i] is None:
            return (0, i)
    return (-1, -1) 
    

def last_cell_diagonal(board: List[List[Player]], player) -> tuple:
    if board[0][0] == player and board[1][1] == player and board[2][2] is None:
        return (2,2)
    elif board[1][1] == player and board[0][2] == player and board[2][0] is None:
        return (2,0)
    elif board[1][1] == player and board[2][0] == player and board[0][2] is None:
        return (0,2)
    elif board[2][0] == player and board[0][2] == player and board[1][1] is None:
        return (1,1)
    elif board[2][2] is player and board[1][1] == player and board[0][0] is None:
        return (0,0)
    else: 
        return (-1, -1)
    
def one_in_column(board: List[List[Player]], player) -> tuple:
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] is None and board[i][2] is None:
            return (2, i)
        if board[i][0] is None and board[i][1] == player and board[i][2] is None:
            return (i, 0)
        if board[i][0] is None and board[i][1] is None and board[i][2] == player:
            return (i, 1)
    return (-1,-1)

def one_in_row(board: List[List[Player]], player) -> tuple:
    for i in range(len(board)):
        if board[0][i] == player and board[1][i] is None and board[2][i] is None:
            return (i, 2)
        if board[0][i] is None and board[1][i] == player and board[2][i] is None:
            return (i, 0)
        if board[0][i] is None and board[1][i] is None and board[2][i] == player:
            return (1, i)
    return (-1,-1)

def check_small_diagonal(board: List[List[Player]], player) -> tuple:
    if board[0][1] == player and board[1][0] == player and board[0][0] is None:
        return (0,0)
    elif board[0][1] == player and board[1][2] == player and board[0][2] is None:
        return (0,2)
    elif board[1][2] == player and board[2][1] == player and board[2][2] is None:
        return (2,2)
    elif board[2][1] == player and board[1][0] == player and board[0][2] is None:
        return (2,0)
    else:
        return (-1,-1)