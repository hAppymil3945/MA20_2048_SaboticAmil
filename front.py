# Auteur : Amil
# nom du programme :2048
# Date : 05.03.26
#version: 0.1

#------------import----------
from tkinter import *
from tkinter.messagebox import showinfo
from back import *
from random import *

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
rand_num = [2,2,2,2,4]

#for the grid
labels = [[None,None,None,None,None],
          [None,None,None,None,None],
          [None,None,None,None,None],
          [None,None,None,None,None],
          [None,None,None,None,None]]
#detect only one time the lose
lose = False

winner = False
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

#spawn a block only if the tot_move is bigger than 0
def new_block_spawn():
    random_block = False
    while not random_block == True:
        line_spawn = randint(0,4)
        col_spawn = randint(0,4)
        if block_in_game[line_spawn][col_spawn] == 0:
            block_in_game[line_spawn][col_spawn] = choice(rand_num)
            random_block = True

#look if detect_full and detect_mo_fusion  is equal to True and if it's true the game is over
def find_lose():
    global lose
    if detect_full() == True and  detect_no_fusion() == True and lose == False:
        showinfo("Perdu!", "good luck next time")
        lose = True


#verify if there is a 2048 block only the first time and display a message "tu as gagné, veux tu continuer"
def find_win():
    global winner
    for line in range(4):
        for col in range(4):
            if block_in_game[line][col] == 2048 and winner==False:
                winner=True
                showinfo("Gagné!", "bien jouer tu veux continuer ?")

#treat the key for the movement
def key_pressed(event):

    tot_move = 0 # if the movement is equal to 0 the game do not spawn block(add for the next sprint)

    keys = event.keysym #collect the symbol of the key
    if keys=="Left" or keys=="a" or keys=="A":
         tot_move = move_left()
    elif keys=="Right" or keys=="d" or keys=="D":
        tot_move =move_right()
    elif keys=="Down" or keys=="s" or keys=="S":
        tot_move =move_down()
    elif keys=="Up" or keys=="w" or keys=="W":
        tot_move =move_up()
    #if there are a movement call the function new_block_spawn
    if tot_move > 0:
        new_block_spawn()

    display()
    find_lose()
    find_win()

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



