# Auteur: Amil
# nom du programe :2048
# Date :06.02.26

from tkinter import *
import subprocess
from tkinter.messagebox import showinfo

#----------Menu window-------
menu = Tk()
menu.geometry("500x500")
menu.resizable(False,False)
menu.title("2048")
menu.config(bg="#B5739D")


#-----------------Variable---------------

config_grid = 0
#---------------Function----------------------
#launch the main.py file
def launch():
    subprocess.call(["python","main.py"])

#if I click on the grid button I will change my grid to 4x4
def size():
    global config_grid
    if config_grid == 0:
        btn_grid.config(text="4x4")
        config_grid +=1
    elif config_grid == 1:
        btn_grid.config(text="5x5")
        config_grid -=1


#take the name entry and take it for the title(it caps at 10)
def hello(event):
    keys = event.keysym
    title = ent_name.get()

    if len(title) >= 10:
        showinfo(title="Trop long",message="Ton texte est trop long")
        ent_name.delete(0, END)
    if keys=="Return":
        lbl_title.config(text=f"Bienvenue {title} !",font="Comfortaa 32 bold")


menu.bind('<Key>', hello) #treat the keys




#-----------------Name---------------
frm_name = Frame(menu,bg="#B5739D")
frm_name.pack(anchor="nw",expand=True,pady=10)

lbl_name = Label(frm_name,text="Nom :",font="Comfortaa 15 bold",bg="#B5739D")
lbl_name.pack(side="left")

ent_name = Entry(frm_name,font="Comfortaa 15 bold",width=8)
ent_name.pack(side="right")
#-----------------Title---------------
lbl_title = Label(menu,bg="#B5739D",text="Bienvenue !",font="Comfortaa 32 bold")
lbl_title.pack()
#-----------------Button---------------
frm_btn = Frame(menu,bg="#B5739D")
frm_btn.pack(pady=(150,0))

btn_launch = Button(frm_btn,text="Jouer",relief="raised",font="Comfortaa 15 bold",width=15,command=launch)
btn_launch.pack(pady=30)

btn_grid = Button(frm_btn,text="5x5",font="Comfortaa 15 bold",width=15,command=size)
btn_grid.pack()

btn_quit = Button(menu,text="Quitter",relief="raised",font="Comfortaa 15 bold",width=15,command=menu.quit)
btn_quit.pack(pady=30)

#-----------------Mainloop---------------
menu.mainloop()

