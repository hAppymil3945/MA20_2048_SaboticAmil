# Author: Amil
# Program name: 2048
# Date: 05.03.26
# Version: 0.1

# ---- Import ----
from tkinter import *
from tkinter.messagebox import showinfo
from back import *  # Game logic (move, detect_full, etc.)
from random import *
from winsound import *
# ---- Variables ----
# 80% chance to spawn 2, 20% chance to spawn 4
rand_num = [2, 2, 2, 2, 4]
second = 0
minute = 0

# Grid labels (UI elements)
labels = [[None, None, None, None, None],
          [None, None, None, None, None],
          [None, None, None, None, None],
          [None, None, None, None, None],
          [None, None, None, None, None]]

# Game state flags
lose = False
winner = False

# UI elements (global for access in functions)
window = None
lbl_title = None
all_frm = None
frm_btn = None
btn_restart = None
lbl_timer = None
btn_quit = None


# ---- Functions ----

def display():
    """Update UI based on current game grid state"""
    for line in range(len(block_in_game)):
        for col in range(len(block_in_game[line])):
            bg_color = color[block_in_game[line][col]]
            if block_in_game[line][col] > 0:
                labels[line][col].config(text=block_in_game[line][col], bg=bg_color)
            else:
                labels[line][col].config(text="", bg=bg_color)


def new_block_spawn():
    """Spawn a new tile (2 or 4) in a random empty cell"""
    random_block = False
    while random_block == False:
        line_spawn = randint(0, 4)
        col_spawn = randint(0, 4)
        if block_in_game[line_spawn][col_spawn] == 0:
            block_in_game[line_spawn][col_spawn] = choice(rand_num)
            random_block = True


def find_lose():
    """Check if game is lost (grid full + no possible moves)"""
    global lose
    if detect_full() == True and detect_no_fusion() == True and lose == False:
        showinfo("Perdu!", "good luck next time")
        lose = True


def find_win():
    """Check if player reached 2048 (only once)"""
    global winner
    for line in range(5):
        for col in range(5):
            if block_in_game[line][col] == 2048 and winner == False:
                winner = True
                showinfo("Gagné!", "bien jouer tu veux continuer ?")


def key_pressed(event):
    """Handle keyboard input for tile movement"""
    global lose, winner

    tot_move = 0
    keys = event.keysym

    if keys == "Left" or keys == "a" or keys == "A":
        tot_move = move_left()
    elif keys == "Right" or keys == "d" or keys == "D":
        tot_move = move_right()
    elif keys == "Down" or keys == "s" or keys == "S":
        tot_move = move_down()
    elif keys == "Up" or keys == "w" or keys == "W":
        tot_move = move_up()

    # Only spawn new tile if a move was made
    if tot_move > 0:
        new_block_spawn()

    display()
    find_lose()
    find_win()


def timer():
    """Update game timer every second"""
    global second, minute, lose, winner

    if lose or winner:
        return  # Stop timer if game over

    second += 1
    if second == 60:
        minute += 1
        second = 0

    lbl_timer.config(text=f"{minute} min et {second} sec")
    lbl_timer.after(1000, timer)  # Call again after 1 second


def restart():
    """Reset game to initial state"""
    global block_in_game, lose, winner, second, minute

    second = 0
    minute = 0

    # Clear grid
    for col in range(5):
        for row in range(5):
            block_in_game[row][col] = 0

    lose = False
    winner = False
    new_block_spawn()
    new_block_spawn()
    display()
    timer()


def initialize_game_interface():
    """Create all UI elements for the game window"""
    global window, lbl_title, all_frm, frm_btn, labels, btn_restart, lbl_timer, btn_quit

    # Title label
    lbl_title = Label(window, text="2048", font=("Verdana 25 bold"), bg="#B5739D")
    lbl_title.pack()

    # Main frame
    all_frm = Frame(window, bg="#B5739D")
    all_frm.pack()
    frm_btn = Frame(all_frm, bg="#B5739D")
    frm_btn.pack(side="bottom", fill="x", pady=(10, 0))

    # Create 5x5 grid of labels
    for line in range(5):
        frm = Frame(all_frm, bg="#B5739D")
        frm.pack(pady=5)
        for col in range(5):
            labels[line][col] = Label(frm, width=6, height=3, borderwidth=1, relief="solid", font=("Comfortaa 15", 20))
            labels[line][col].pack(side=LEFT, padx=10, pady=10)

    # Bind keyboard events
    window.bind('<Key>', key_pressed)

    # Buttons and timer display
    btn_restart = Button(frm_btn, text="Recommencer", width=12, font=("Comfortaa 15 bold"), command=restart)
    btn_restart.pack(padx=(0, 5), side="left")

    lbl_timer = Label(frm_btn, font=("Arial 15 bold"), bg="#B5739D")
    lbl_timer.pack(padx=(70, 0), side="left")

    btn_quit = Button(frm_btn, text="Quitter", width=12, font=("Comfortaa 15 bold"), command=quit)
    btn_quit.pack(side="right")


def launch_game():
    """Initialize and start the game"""
    global window, lose, winner, second, minute, menu

    # Create game window
    window = Tk()
    window.geometry("700x850")
    window.resizable(False, False)
    window.title("2048")
    window.config(bg="#B5739D")

    PlaySound('Menu_music.wav', SND_FILENAME | SND_ASYNC)

    # Reset game state
    lose = False
    winner = False
    second = 0
    minute = 0

    # Clear grid
    for col in range(5):
        for line in range(5):
            block_in_game[col][line] = 0

    # Close menu
    menu.destroy()

    # Build game UI
    initialize_game_interface()

    # Spawn first two tiles
    new_block_spawn()
    new_block_spawn()
    display()
    timer()
    window.mainloop()


def createmenu():
    """Create main menu with name input and play/quit buttons"""
    global ent_name, menu

    menu = Tk()
    menu.geometry("500x500")
    menu.resizable(False, False)
    menu.title("2048")
    menu.config(bg="#B5739D")

    # Name input field
    frm_name = Frame(menu, bg="#B5739D")
    frm_name.pack(anchor="nw", expand=True, pady=10)
    lbl_name = Label(frm_name, text="Nom :", font="Comfortaa 15 bold", bg="#B5739D")
    lbl_name.pack(side="left")
    ent_name = Entry(frm_name, font="Comfortaa 15 bold", width=8)
    ent_name.pack(side="right")

    # Welcome title
    lbl_menu_title = Label(menu, bg="#B5739D", text="Bienvenue !", font="Comfortaa 32 bold")
    lbl_menu_title.pack()

    # Buttons
    frm_btn = Frame(menu, bg="#B5739D")
    frm_btn.pack(pady=(150, 0))
    btn_launch = Button(frm_btn, text="Jouer", relief="raised", font="Comfortaa 15 bold", width=15, command=launch_game)
    btn_launch.pack(pady=30)
    btn_quit = Button(menu, text="Quitter", relief="raised", font="Comfortaa 15 bold", width=15, command=menu.quit)
    btn_quit.pack(pady=30)

    # Handle Enter key for name input
    def handle_name_input(event):
        keys = event.keysym
        title = ent_name.get()
        if len(title) >= 10:
            showinfo(title="Trop long", message="Ton texte est trop long")
            ent_name.delete(0, END)
        if keys == "Return":
            lbl_menu_title.config(text=f"Bienvenue {title} !", font="Comfortaa 32 bold")

    menu.bind('<Key>', handle_name_input)
    menu.mainloop()




# Start the program
if __name__ == "__main__":
    createmenu()