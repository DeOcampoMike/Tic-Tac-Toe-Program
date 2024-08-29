from boards import *
import variable
import boards

def check_winner(board, label2):
    global turn, game_over

    variable.turn += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] !=  ""):
            label2.config(text=board[row][0]["text"] + " is the winner!",foreground = color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_lightgray)
            game_over = True
            variable.turn = 0
            
            return

    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] !=  ""):
            label2.config(text=board[0][column]["text"] + " is the winner!",foreground = color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow,background=color_lightgray)
            game_over = True
            variable.turn = 0
            return

        
        if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
                and board[0][0]["text"] != ""):
                label2.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
                for i in range(3):
                        board[i][i].config(foreground=color_yellow, background=color_lightgray)
                game_over = True
                variable.turn = 0
                return


        if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
                and board[0][2]["text"] != ""):
                label2.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
                board[0][2].config(foreground=color_yellow, background=color_lightgray)
                board[1][1].config(foreground=color_yellow, background=color_lightgray)
                board[2][0].config(foreground=color_yellow, background=color_lightgray)
                game_over = True
                variable.turn = 0
                return
        
        if (variable.turn == 9):
            game_over = True
            variable.turn = 0
            boards.label2.config(text="Tie!", foreground=color_yellow)
            return