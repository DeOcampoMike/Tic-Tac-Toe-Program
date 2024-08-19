import checkwinner
from checkwinner import *
import twoplayer
from minimax import best_move
from variable import *

def set_tile(row, column):
    import variable
    global currplayer, game_over  # Declare both as global
    print("2")

    if variable.gamemode == 0:  # Two-player mode
        if game_over:
            return

        elif board[row][column]["text"] == "" and not checkwinner.game_over:
                board[row][column]["text"] = currplayer

            # Check for a winner after the move
                if currplayer == player2:
                        currplayer = player1
                else:
                        currplayer = player2

                twoplayer.label2["text"] = currplayer+"'s turn"
                check_winner(board, twoplayer.label2)

                return

        else:
               return

    else:  # Single-player mode
        if game_over:
            return

        if board[row][column]["text"] == "" and currplayer == "X":
            board[row][column]["text"] = currplayer
            twoplayer.label2["text"] = f"{currplayer}'s turn"

            # Check for a winner after the player's move
            check_winner(board, twoplayer.label2)
            currplayer = "O"
            move = best_move()
            print(f"Best move determined by AI: {move}")  # Debugging output
            if move:
                board[move[0]][move[1]]["text"] = currplayer
                check_winner(board, twoplayer.label2)
                currplayer = "X"
                twoplayer.label2["text"] = f"{currplayer}'s turn"
        return
