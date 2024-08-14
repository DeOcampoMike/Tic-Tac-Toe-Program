from variable import *
import tkinter
from newgame import new_game
from Tileset import set_tile

def twoPlayer():
        global label2, window2
        window2 = tkinter.Tk()
        window2.title("TickTackToe")
        window2.resizable(False,False)

        frame2 = tkinter.Frame(window2)
        label2 = tkinter.Label(frame2,text = "turn",font=("Consolas",20,"bold"),
                                                background=color_gray,foreground="white",width=4,height= 1)

        label2.grid(row=0, column=0, columnspan=3, sticky="we")

        for row in range(3):
                for column in range(3):
                        board[row][column] = tkinter.Button(frame2, text="",font=("Consolas",50,"bold"),background=color_gray,foreground=color_blue, width=4, height=1,command=lambda row=row, column=column:set_tile(row,column))

                        board[row][column].grid(row = row + 1,column=column)

        button = tkinter.Button(frame2, text="restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)
        button.grid(row=4, column=0, columnspan=1, sticky="we")

        button2 = tkinter.Button(frame2, text="Main Menu", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=twotoMain)
        button2.grid(row=4, column=1, columnspan=2, sticky="we")

        frame2.pack()



        window2.update()
        window2_width = window2.winfo_width()
        window2_height = window2.winfo_height()
        screen_width = window2.winfo_screenwidth()
        screen_height = window2.winfo_screenheight()
        window2_x = int((screen_width/2) - (window2_width/2))
        window2_y = int((screen_height/2) - (window2_height/2))
        window2.geometry(f"{window2_width}x{window2_height}+{window2_x}+{window2_y}")


def twotoMain():
        window2.destroy()
        from mainmenu import mainMenu
        mainMenu()
        
