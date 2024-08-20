
from checkwinner import check_winner
from minimax import best_move
from variable import *


def set_tile(row, column):
    import variable
    import board
    import checkwinner
    global currplayer, game_over  # Declare both as global

    if variable.gamemode == 0:  # Two-player mode
        if game_over:
            return

        elif board[row][column]["text"] == "" and not checkwinner.game_over:
                board[row][column]["text"] = currplayer

                if currplayer == player2:
                        currplayer = player1
                else:
                        currplayer = player2

                board.label2["text"] = currplayer+"'s turn"
                check_winner(board, board.label2)
            

                return

        else:
               return

    else: 
    
        if game_over:
            return

        if board[row][column]["text"] == "" and (currplayer == "X" or currplayer == "O") and not checkwinner.game_over:
            if currplayer == "O":
                 currplayer = "X"
            board[row][column]["text"] = currplayer
            check_winner(board, board.label2)
            currplayer = "O"
            move = best_move()
            if move and not checkwinner.game_over:
                board[move[0]][move[1]]["text"] = currplayer
                board.label2["text"] = "1 Player"
                check_winner(board, board.label2)
                currplayer = "X"



                
        return
