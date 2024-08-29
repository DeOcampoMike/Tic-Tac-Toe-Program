from boards import *
import variable
import checkwinner
from boards import TicBoard

def mainMenu():

    global window
    window = tkinter.Tk()
    window.title("Main Menu")

    window.configure(background=color_gray)
    window.resizable(False,False)
    window.update()
    button1 = tkinter.Button(window,text="One Player",font=("Arial,18"),fg="white",width=20,background=color_gray,command=closetoOne)
    button1.pack(padx=10,pady=20)
    button2 = tkinter.Button(window,text="Two Player",font=("Arial,18"),fg="white",width=20,background=color_gray,command=closetoTwo)
    button2.pack(padx=10,pady=20)

    window.update_idletasks()
    width = 250
    height = 250
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.mainloop()


def closetoTwo():
    variable.gamemode = 0          
    variable.turn = 0
    window.destroy()
    checkwinner.game_over = False
    TicBoard()


def closetoOne():   
    variable.gamemode = 1      
    variable.turn = 0
    window.destroy()
    checkwinner.game_over = False
    TicBoard()



