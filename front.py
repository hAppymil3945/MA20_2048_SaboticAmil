# Auteur: Amil
# nom du programe :2048
# Date :06.02.26
#version: 0.0

#------------import----------
import random
import time
from tkinter import *
from back import *
from winsound import *


#----------Principal window-------
window = Tk()
window.geometry("700x850")
window.resizable(False,False)
window.title("2048")

#----------Label----------

#title of the program
lbl_title = Label(window,text="2048",font=("Verdana 25 bold"))
lbl_title.pack()

#-----------Frame------------------
all_frm = Frame(window)
all_frm.pack()
frm_btn = Frame(all_frm)
frm_btn.pack(side="bottom",fill="x",pady=(10,0))

#Label for the timer
lbl_timer = Label(frm_btn,font=("Arial 15 bold"))
lbl_timer.pack(pady=10)
#------------Variable---------------
#variable for the second in the function timer
second = 0
#variable for the minute in the function timer
minute = 0



#for the grid
labels = [[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None]]

#list for the random number 2 = 80% and 4 = 20% chance of spawning
rand_num = [2,2,2,2,4]



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
    frm =Frame(all_frm)
    frm.pack(pady=5)

    #place  the columns in the grid
    for col in range(len(block_in_game[line])):
        labels[line][col] = Label(frm, width=6, height=3, borderwidth=1,relief="solid",font=("Arial", 20))
        labels[line][col].pack(side=LEFT,padx=10,pady=10)


#Function for spawning random blocks in the grid
def new_block_spawn():
    random_block = 1
    while not random_block == 0:
        line_spawn = random.randint(0,3)
        col_spawn = random.randint(0,3)
        random_block = block_in_game[line_spawn][col_spawn]
        if random_block == 0:
            block_in_game[line_spawn][col_spawn] = random.choice(rand_num)
#-------------------Button-----------------
#bouton pour reccomencer
btn_restart = Button(frm_btn,text="Recommencer",width=12,font=("Arial 15 bold"),command="restart")
btn_restart.pack(padx=(0,5),side=LEFT)
#bouton pour quitter
btn_quit = Button(frm_btn,text="Quitter",width=12,font=("Arial 15 bold"),command=quit)
btn_quit.pack(side=RIGHT)
#bouton pour couper le son du jeux
btn_mute = Button(frm_btn,text="Couper le son",width=12,font=("Arial 15 bold"),command="mute")
btn_mute.pack()