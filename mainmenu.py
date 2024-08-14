from twoplayer import *

def mainMenu():

    global window
    window = tkinter.Tk()
    window.title("Main Menu")

    window.configure(background=color_gray)
    window.resizable(False,False)
    window.update()
    button1 = tkinter.Button(window,text="One Player",font=("Arial,18"),fg="white",width=20,background=color_gray)
    button1.pack(padx=10,pady=20)
    button2 = tkinter.Button(window,text="Two Player",font=("Arial,18"),fg="white",width=20,background=color_gray,command=closetoTwo)
    button2.pack(padx=10,pady=20)
    button3 = tkinter.Button(window,text="Setting",font=("Arial,18"),fg="white",width=20,background=color_gray)
    button3.pack(padx=10,pady=20)

    window.update_idletasks()
    width = 500
    height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.mainloop()


def closetoTwo():
    window.destroy()
    from twoplayer import twoPlayer
    twoPlayer()

mainMenu()

