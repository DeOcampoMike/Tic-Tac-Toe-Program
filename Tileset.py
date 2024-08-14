import checkwinner
from checkwinner import *
from twoplayer import *
import twoplayer

def set_tile(row,column):
        global currplayer

        if game_over:
                return

        elif board[row][column]["text"] == "" and checkwinner.game_over == False:
                board[row][column]["text"] = currplayer


                if currplayer == player2:
                        currplayer = player1
                else:
                        currplayer = player2

                twoplayer.label2["text"] = currplayer+"'s turn"
                check_winner(board, twoplayer.label2)

                return

        else:
               return