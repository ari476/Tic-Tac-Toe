from tkinter import messagebox, Tk, Canvas
from game_logic import TicTacToe, Player
from ai_player import make_decision
import numpy as np
import copy
import random

size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 30
symbol_X_color = '#EE4035'              
symbol_O_color = '#0492CF'
Green_color = '#7BC043'


class TicTacToeGUI(TicTacToe):
    def __init__(self):
        self.window = Tk()              
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(
            self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()

        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)
        self.initialize_game()

    def mainloop(self):
        self.window.mainloop()

    def initialize_game(self):
        super().__init__()
        self.reset_board = False 
        is_ai_start = random.choice([True, False])  
        self.make_ai_move() if is_ai_start else None   

        for i in range(2):
            self.canvas.create_line(
                (i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

        for i in range(2):
            self.canvas.create_line(
                0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    def draw_O(self, cell_pos):
        # cell_pos = grid value on the board
        # pixel_pos = actual pixel values of the center of the grid
        cell_pos = np.array(cell_pos)
        pixel_pos = self.convert_cell_pos_to_pixel_pos(cell_pos)
        self.canvas.create_oval(pixel_pos[0] - symbol_size, pixel_pos[1] - symbol_size,
                                pixel_pos[0] + symbol_size, pixel_pos[1] + symbol_size, width=symbol_thickness,
                                outline=symbol_O_color)

    def draw_X(self, cell_pos):
        pixel_pos = self.convert_cell_pos_to_pixel_pos(cell_pos)
        self.canvas.create_line(pixel_pos[0] - symbol_size, pixel_pos[1] - symbol_size,
                                pixel_pos[0] + symbol_size, pixel_pos[1] + symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)
        self.canvas.create_line(pixel_pos[0] - symbol_size, pixel_pos[1] + symbol_size,
                                pixel_pos[0] + symbol_size, pixel_pos[1] - symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)

    def display_game_over(self, result_game):
        text_map = {Player.X: 'Winner: Player 1 (X)',
                    Player.O: 'Winner: Player 2 (O)',
                    'Tie': 'Its a tie'}

        color_map = {Player.X: symbol_X_color,
                     Player.O: symbol_O_color,
                     'Tie': Green_color}

        self.canvas.create_text(size_of_board / 2, size_of_board / 3,
                                font="cmr 40 bold", fill=color_map[result_game], text=text_map[result_game])

    def convert_cell_pos_to_pixel_pos(self, cell_pos):
        cell_pos = np.array(cell_pos, dtype=int)
        return (size_of_board / 3) * cell_pos + size_of_board / 6

    def convert_pixel_pos_to_cell_pos(self, pixel_pos):
        pixel_pos = np.array(pixel_pos)
        return np.array(pixel_pos // (size_of_board / 3), dtype=int)

    def click(self, event):
        pixel_pos = [event.x, event.y]
        cell_pos = self.convert_pixel_pos_to_cell_pos(pixel_pos)
        if self.make_move(cell_pos):
            self.make_ai_move()

    def make_ai_move(self):
        try:
            cell_pos = make_decision(copy.deepcopy(
                self.board), self.current_player)
        except Exception as e:
            self.exit_game('AI Error!', f'AI Error! {e}')

        if not check_legal_value(cell_pos):
            self.exit_game('AI Error!', f'Invalid value {cell_pos}')

        if not self.is_cell_empty(cell_pos):
            self.exit_game("AI Error - Invalid Move!",
                           f"Cell {cell_pos} already occupied!")

        self.make_move(cell_pos)

    def make_move(self, cell_pos):
        if not self.reset_board:
            if self.is_cell_empty(cell_pos):
                self.board[cell_pos[0]
                           ][cell_pos[1]] = self.current_player

                if self.current_player == Player.X:
                    self.draw_X(cell_pos)
                else:
                    self.draw_O(cell_pos)

                if result_game := self.is_game_over():
                    self.reset_board = True
                    self.display_game_over(result_game)
                    return False

                self.current_player = Player.X if self.current_player is Player.O else Player.O
                return True
        # is play again
        else:
            self.canvas.delete('all')
            self.initialize_game()
            return False

    def exit_game(self, title, body_text):
        messagebox.showinfo(title, body_text)
        self.window.destroy()


def check_legal_value(cell_pos):
    return isinstance(cell_pos, (list, tuple)) and len(cell_pos) == 2 and all(
        isinstance(elem, int) for elem in cell_pos)


if __name__ == "__main__":
    game_instance = TicTacToeGUI()
    game_instance.mainloop()
