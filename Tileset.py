
from checkwinner import check_winner
from minimax import best_move
from variable import *


def set_tile(row, column):
    import variable
    import boards
    import checkwinner
    global currplayer, game_over  

    if variable.gamemode == 0:  # Two-player mode
        if game_over:
            return

        elif board[row][column]["text"] == "" and not checkwinner.game_over:
                board[row][column]["text"] = currplayer

                if currplayer == player2:
                        currplayer = player1
                else:
                        currplayer = player2

                boards.label2["text"] = currplayer+"'s turn"
                check_winner(board, boards.label2)
            

                return

        else:
               return

    else:   #One Player
    
        if game_over:
            return

        if board[row][column]["text"] == "" and (currplayer == variable.player1 or currplayer == variable.player2) and not checkwinner.game_over:
            if currplayer == "O":
                 currplayer = "X"
            board[row][column]["text"] = currplayer
            check_winner(board, boards.label2)
            currplayer = "O"
            move = best_move()
            if move and not checkwinner.game_over:
                board[move[0]][move[1]]["text"] = currplayer
                boards.label2["text"] = "Player vs AI"
                check_winner(board, boards.label2)
                currplayer = "X"



                
        return
