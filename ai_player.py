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
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while board[x][y] != None: 
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    return (x,y)