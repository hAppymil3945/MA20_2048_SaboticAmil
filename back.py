# Auteur : Amil
# nom du programe :2048
# Date :08.02.25
#version: 0.0

"""
#grid for example of all the color
block_in_game= [[0,2,4,8,16],
                [32,64,128,256,512],
                [1024,2048,4096,8192,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
"""
#the real grid
block_in_game= [[0,0,0,0,0],
                [0,0,0,0,0],
                [2,2,2,2,2],
                [0,0,0,0,0],
                [0,0,0,0,0]]

#it's for all the color for each number
color = {0: "#C38858",
         2: "#93F9EA",
         4 : "#6DB6AC",
         8 : "#997CD2",
         16 : "#7963AA",
         32 : "#B16871",
         64 :"#93565E",
         128: "#90A763",
         256 : "#5D6C41",
         512 : "#4E865F",
         1024: "#467754",
         2048: "#AA9F64",
         4096: "#67623D",
         8192: "#345070"}

#function for packing the number
def pack5(a,b,c,d,e):
    nmove = 0
    if d == 0:
        d,e = e,0
        nmove += 1
    if c == 0:
        c,d,e = d,e,0
        nmove += 1
    if b==0:
        b,c,d,e=c,d,e,0
        nmove += 1
    if a==0:
        a,b,c,d,e = b,c,d,e,0
        nmove += 1
    if a==b:
        a,b,c,d,e=2*a,c,d,e,0
        nmove += 1
    if b==c:
        b,c,d,e=2*b,d,e,0
        nmove += 1
    if c==d:
        c,d,e=2*c,e,0
        nmove += 1
    if d==e:
        d,e=2*d,0
        e=0
        nmove += 1
    return a,b,c,d,e,nmove

#pack the grid to the left
def move_left():
    tot_move = 0 #count the number of movement to the left

    for line in range(5):
        [block_in_game[line][0],block_in_game[line][1],block_in_game[line][2],block_in_game[line][3],block_in_game[line][4],nmove] = (
            pack5(block_in_game[line][0],block_in_game[line][1],block_in_game[line][2],block_in_game[line][3], block_in_game[line][4]))

        tot_move+=nmove
    return tot_move

#pack the grid to the right
def move_right():
    tot_move = 0 #count the number of movement to the right

    for line in range(5):
        [block_in_game[line][4],block_in_game[line][3],block_in_game[line][2],block_in_game[line][1],block_in_game[line][0],nmove] = (
            pack5(block_in_game[line][4],block_in_game[line][3],block_in_game[line][2],block_in_game[line][1],block_in_game[line][0]))

        tot_move += nmove
    return tot_move

#pack the grid to the down
def move_down():
    tot_move = 0 #count the number of movement to the down
    for col in range(5):
        [block_in_game[4][col],block_in_game[3][col],block_in_game[2][col],block_in_game[1][col],block_in_game[0][col],nmove] = (
            pack5(block_in_game[4][col],block_in_game[3][col],block_in_game[2][col],block_in_game[1][col],block_in_game[0][col]))

        tot_move += nmove
    return tot_move

#pack the grid to the up
def move_up():
    tot_move = 0 #count the number of movement to the up
    for col in range(5):
        [block_in_game[0][col],block_in_game[1][col],block_in_game[2][col],block_in_game[3][col],block_in_game[4][col],nmove] = (
            pack5(block_in_game[0][col],block_in_game[1][col],block_in_game[2][col],block_in_game[3][col],block_in_game[4][col]))

        tot_move += nmove
    return tot_move