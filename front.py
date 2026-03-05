# Auteur : Amil
# nom du programme :2048
# Date : 05.03.26
#version: 0.1

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
    display()
    window.mainloop()

#update the display based on the logic grid
def display():
        for line in range((len(block_in_game))):
            for col in range(len(block_in_game[line])):
                bg_color = color[block_in_game[line][col]]
                if block_in_game[line][col] > 0:
                    labels[line][col].config(text= block_in_game[line][col], bg=bg_color)
                else:
                    labels[line][col].config(text="", bg=bg_color)

#treat the key for the movement
def key_pressed(event):
    tot_move = 0 # if the movement is equal to 0 the game do not spawn block(add for the next sprint)

    keys = event.keysym #collect the symbol of the key
    if keys=="Left" or keys=="a" or keys=="A":
         tot_move = move_left()
    if keys=="Right" or keys=="d" or keys=="D":
        tot_move =move_right()
    if keys=="Down" or keys=="s" or keys=="S":
        tot_move =move_down()
    if keys=="Up" or keys=="w" or keys=="W":
        tot_move =move_up()
    display()




#place  the lines in the grid
for line in range((len(block_in_game))):
    frm =Frame(all_frm,bg="#B5739D")
    frm.pack(pady=5)
    #place  the columns in the grid
    for col in range(len(block_in_game[line])):
        labels[line][col] = Label(frm, width=6, height=3, borderwidth=1,relief="solid",font=("Comfoorta 15 ", 20))
        labels[line][col].pack(side=LEFT,padx=10,pady=10)

window.bind('<Key>', key_pressed) #treat the keys
#-------------------Button-----------------
#bouton for restart
btn_restart = Button(frm_btn,text="Recommencer",width=12,font=("Comfortaa 15 bold"),command="restart")
btn_restart.pack(padx=(0,5),side="left")

#bouton for quitting
btn_quit = Button(frm_btn,text="Quitter",width=12,font=("Comfortaa 15 bold"),command=quit)
btn_quit.pack(side="right")



