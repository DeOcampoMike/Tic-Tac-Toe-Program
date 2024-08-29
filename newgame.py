import checkwinner
import boards
from variable import *
import Tileset

def new_game():
        global turn, game_over
        import variable
        variable.turn = 0
        checkwinner.game_over = False
        if variable.gamemode == 1:
              boards.label2.config(text="X 's turn", foreground="white")
        else:
              boards.label2.config(text=Tileset.currplayer+" 's turn", foreground="white")

        for row in range(3):
               for column in range(3):
                      board[row][column].config(text="", foreground=color_blue, background=color_gray)

       