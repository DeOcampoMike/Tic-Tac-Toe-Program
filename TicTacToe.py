import tkinter
import checkwinner
from checkwinner import *
from Color import *


player1 = "X"
player2 = "O"
currplayer = player1
board = [[0,0,0],
         [0,0,0],
         [0,0,0],]


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

                label["text"] = currplayer+"'s turn"
                check_winner(board, label)

                return

        else:
               return





def new_game():
        global turn, game_over
        turn = 0
        checkwinner.game_over = False

        label.config(text=currplayer+"s turn", foreground="white")

        for row in range(3):
               for column in range(3):
                      board[row][column].config(text="", foreground=color_blue, background=color_gray)




window = tkinter.Tk()
window.title("TickTackToe")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame,text = "turn",font=("Consolas",20,"bold"),
                                                background=color_gray,foreground="white",width=4,height= 1)

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="",font=("Consolas",50,"bold"),background=color_gray,foreground=color_blue, width=4, height=1,command=lambda row=row, column=column:set_tile(row,column))

        board[row][column].grid(row = row + 1,column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()



window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")



window.mainloop()