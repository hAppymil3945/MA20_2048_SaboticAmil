# menu.py

from tkinter import *
from tkinter.messagebox import showinfo
import subprocess

# --- Variables globales ---
config_grid = 0  # 0 = 4x4, 1 = 5x5

# --- Fonctions ---
def launch_game():
    subprocess.call(["python", "main.py"])

def toggle_grid_size():
    global config_grid
    if config_grid == 0:
        btn_grid.config(text="4x4")
        config_grid = 1
    else:
        btn_grid.config(text="5x5")
        config_grid = 0

def handle_name_input(event):
    keys = event.keysym
    title = ent_name.get()
    if len(title) >= 10:
        showinfo(title="Trop long", message="Ton texte est trop long")
        ent_name.delete(0, END)
    if keys == "Return":
        lbl_title.config(text=f"Bienvenue {title} !", font="Comfortaa 32 bold")



menu = Tk()
menu.geometry("500x500")
menu.resizable(False, False)
menu.title("2048")
menu.config(bg="#B5739D")

# --- Nom ---
frm_name = Frame(menu, bg="#B5739D")
frm_name.pack(anchor="nw", expand=True, pady=10)
lbl_name = Label(frm_name, text="Nom :", font="Comfortaa 15 bold", bg="#B5739D")
lbl_name.pack(side="left")
ent_name = Entry(frm_name, font="Comfortaa 15 bold", width=8)
ent_name.pack(side="right")

# --- Titre ---
lbl_title = Label(menu, bg="#B5739D", text="Bienvenue !", font="Comfortaa 32 bold")
lbl_title.pack()

# --- Boutons ---
frm_btn = Frame(menu, bg="#B5739D")
frm_btn.pack(pady=(150, 0))
btn_launch = Button(frm_btn, text="Jouer", relief="raised", font="Comfortaa 15 bold", width=15, command=launch_game)
btn_launch.pack(pady=30)
btn_grid = Button(frm_btn, text="5x5", font="Comfortaa 15 bold", width=15, command=toggle_grid_size)
btn_grid.pack()
btn_quit = Button(menu, text="Quitter", relief="raised", font="Comfortaa 15 bold", width=15, command=menu.quit)
btn_quit.pack(pady=30)

menu.bind('<Key>', handle_name_input)
menu.mainloop()

