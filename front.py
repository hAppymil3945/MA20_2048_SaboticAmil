# Auteur : Amil
# nom du programe :2048
# Date :06.02.26
#version: 0.0

#------------import----------
from tkinter import *
from back import *





# ----------Game window-------
window = Tk()
window.geometry("700x850")
window.resizable(False, False)
window.title("2048")
window.config(bg="#B5739D")


#----------Label----------

#title of the program
lbl_title = Label(window,text="2048",font=("Verdana 25 bold"),bg="#B5739D")
lbl_title.pack()

#-----------Frame------------------
all_frm = Frame(window,bg="#B5739D")
all_frm.pack()
frm_btn = Frame(all_frm,bg="#B5739D")
frm_btn.pack(side="bottom",fill="x",pady=(10,0))

#------------Variable---------------


#for the grid
labels = [[None,None,None,None,None],
          [None,None,None,None,None],
          [None,None,None,None,None],
          [None,None,None,None,None],
          [None,None,None,None,None]]




#----------Fonction--------

def mainloop():

    # call the function display
    display()
    window.mainloop()

#display the grid
def display():

        for line in range((len(block_in_game))):
            for col in range(len(block_in_game[line])):
                bg_color = color[block_in_game[line][col]]
                if block_in_game[line][col] > 0:
                    labels[line][col].config(text= block_in_game[line][col], bg=bg_color)
                else:
                    labels[line][col].config(text="", bg=bg_color)

#place  the lines in the grid
for line in range((len(block_in_game))):
    frm =Frame(all_frm,bg="#B5739D")
    frm.pack(pady=5)

    #place  the columns in the grid
    for col in range(len(block_in_game[line])):
        labels[line][col] = Label(frm, width=6, height=3, borderwidth=1,relief="solid",font=("Arial", 20))
        labels[line][col].pack(side=LEFT,padx=10,pady=10)


#-------------------Button-----------------
#bouton pour recommencer
btn_restart = Button(frm_btn,text="Recommencer",width=12,font=("Comfortaa 15 bold"),command="restart")
btn_restart.pack(padx=(0,5),side="left")

#bouton pour quitter
btn_quit = Button(frm_btn,text="Quitter",width=12,font=("Comfortaa 15 bold"),command=quit)
btn_quit.pack(side="right")



