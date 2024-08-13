from Color import *


turn = 0
game_over = False                     

def check_winner(board, label):
    global turn, game_over
    turn += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] !=  ""):
            label.config(text=board[row][0]["text"] + " is the winner!",foreground = color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_ligthgray)
            game_over = True
            print(game_over)
            turn = 0
            
            return

    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] !=  ""):
            label.config(text=board[0][column]["text"] + " is the winner!",foreground = color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow,background=color_ligthgray)
            game_over = True
            turn = 0
            return

        
        if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
                and board[0][0]["text"] != ""):
                label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
                for i in range(3):
                        board[i][i].config(foreground=color_yellow, background=color_ligthgray)
                game_over = True
                turn = 0
                return


        if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
                and board[0][2]["text"] != ""):
                label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
                board[0][2].config(foreground=color_yellow, background=color_ligthgray)
                board[1][1].config(foreground=color_yellow, background=color_ligthgray)
                board[2][0].config(foreground=color_yellow, background=color_ligthgray)
                game_over = True
                turn = 0
                return
        
        if (turn == 9):
            game_over = True
            turn = 0
            label.config(text="Tie!", foreground=color_yellow)
            return