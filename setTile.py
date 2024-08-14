from checkwinner import *
from Color import *

def set_tile():
    global turn, game_over
    if game_over:
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = currplayer

    if currplayer == player2:
        currplayer = player1
    else:
        currplayer = player2

    label["text"] = currplayer + "'s turn"

    check_winner(board, label)

        
