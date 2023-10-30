from game_logic import Player
from typing import List ,Optional, Tuple
from game_logic import TicTacToe


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:

    opponent = Player.X if ai_player == Player.O else Player.O

    if all(all(cell is None for cell in row) for row in board):
        if board[1][1] is None:
            return (1, 1)
        else:
            # If the center is taken, choose a corner
            return (0, 0)

    # Check rows for the opponent's potential win and block it
    for row in board:
        if row.count(opponent) == 2 and row.count(None) == 1:
            col = row.index(None)
            return (board.index(row), col)

    # Check columns for the opponent's potential win and block it
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        if column.count(opponent) == 2 and column.count(None) == 1:
            row = column.index(None)
            return (row, col)

    # Check main diagonal for the opponent's potential win and block it
    main_diag = [board[i][i] for i in range(3)]
    if main_diag.count(opponent) == 2 and main_diag.count(None) == 1:
        index = main_diag.index(None)
        return (index, index)

    # Check the other diagonal for the opponent's potential win and block it
    other_diag = [board[i][2 - i] for i in range(3)]
    if other_diag.count(opponent) == 2 and other_diag.count(None) == 1:
        index = other_diag.index(None)
        return (index, 2 - index)

    # If there are no immediate threats, proceed with a default strategy

    if board[1][1] is None:
        return (1, 1)

    # If no immediate threats and the center is taken, choose a corner
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in corners:
        if board[corner[0]][corner[1]] is None:
            return corner

    # Choose any available edge
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for edge in edges:
        if board[edge[0]][edge[1]] is None:
            return edge

    # Fallback if the board is full (the game should already be over by this point)
    return (-1, -1)