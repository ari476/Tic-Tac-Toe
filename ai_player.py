from game_logic import Player
from typing import List
from game_logic import TicTacToe


def make_decision(board: List[List[Player]], ai_player: Player) -> tuple:
    """
    Args:
        board (List[List[Player]]): current state of board in the game
        ai_player (Player): X or O enum 

    Returns:
        tuple: cell position for placing the next symbol on the game board
    """
    for column in board:
        #to not defeat
        if column.count(Player.X) == 2:
            for i in range(len(column)):
                if column[i] != Player.X:
                    column[i] = ai_player.O
    pass