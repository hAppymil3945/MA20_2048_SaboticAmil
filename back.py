# Auteur : Amil
# nom du programme :2048
# Date : 05.03.26
#version: 0.1

"""
#grid for example of all the color
block_in_game= [[4,2,4,8,16],
                [32,64,128,256,512],
                [1024,2048,4096,8192,0],
                [2,4,8,16,32],
                [8192,32,1024,2,4]]
"""
#the real grid for the game
block_in_game= [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
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

# Function to compact and merge numbers for 2048 5x5 grid
def pack5(a, b, c, d, e):
    nmove = 0  # Counter for number of operations performed
    # === PHASE 1: Compact zeros to the right ===
    # If d is zero, shift e left into d, set e to 0
    # != 0 check: Only move if e has a tile (non-zero value)
    if d == 0 and e != 0:
        d, e = e, 0
        nmove += 1
    # If c is zero, shift c,d,e left, set e to 0
    # != 0 check: Only move if d has a tile (non-zero value)
    if c == 0 and d != 0:
        c, d, e = d, e, 0
        nmove += 1
    # If b is zero, shift b,c,d,e left, set e to 0
    # != 0 check: Only move if c has a tile (non-zero value)
    if b == 0 and c != 0:
        b, c, d, e = c, d, e, 0
        nmove += 1
    # If a is zero, shift a,b,c,d,e left, set e to 0
    # != 0 check: Only move if b has a tile (non-zero value)
    if a == 0 and b != 0:
        a, b, c, d, e = b, c, d, e, 0
        nmove += 1
    # === PHASE 2: Merge adjacent identical numbers ===
    # If a == b, merge them (double a), shift others left, set e to 0
    # != 0 check: Only merge if the tiles are not empty (prevents merging zeros)
    if a == b and a != 0:
        a, b, c, d, e = 2 * a, c, d, e, 0
        nmove += 1
    # If b == c, merge them (double b), shift others left, set e to 0
    # != 0 check: Only merge if the tiles are not empty (prevents merging zeros)
    if b == c and b != 0:
        b, c, d, e = 2 * b, d, e, 0
        nmove += 1
    # If c == d, merge them (double c), shift others left, set e to 0
    # != 0 check: Only merge if the tiles are not empty (prevents merging zeros)
    if c == d and c != 0:
        c, d, e = 2 * c, e, 0
        nmove += 1
    # If d == e, merge them (double d), set e to 0
    # != 0 check: Only merge if the tiles are not empty (prevents merging zeros)
    if d == e and d != 0:
        d, e = 2 * d, 0
        nmove += 1

    # Return final state and operation count
    return a, b, c, d, e, nmove

#pack the grid to the left
def move_left():
    tot_move = 0 # Track total number of movements across all rows

    # Process each row in the 5x5 grid
    for line in range(5):
        # Call pack5() to shift tiles left and merge matching values in this row
        # pack5() returns the 5 packed values plus the number of moves made
        [block_in_game[line][0],block_in_game[line][1],block_in_game[line][2],block_in_game[line][3],block_in_game[line][4],nmove] = (
            pack5(block_in_game[line][0],block_in_game[line][1],block_in_game[line][2],block_in_game[line][3], block_in_game[line][4]))

        tot_move += nmove  # Add this row's movements to the total count
    return tot_move  # Return total movements (0 if no tiles moved)

#pack the grid to the right
def move_right():
    tot_move = 0 # Track total number of movements across all rows

    # Process each row in the 5x5 grid
    for line in range(5):
        # Call pack5() to shift tiles right and merge matching values in this row
        # pack5() returns the 5 packed values plus the number of moves made
        [block_in_game[line][4],block_in_game[line][3],block_in_game[line][2],block_in_game[line][1],block_in_game[line][0],nmove] = (
            pack5(block_in_game[line][4],block_in_game[line][3],block_in_game[line][2],block_in_game[line][1],block_in_game[line][0]))

        tot_move += nmove # Add this row's movements to the total count
    return tot_move # Return total movements (0 if no tiles moved)

#pack the grid to the down
def move_down():
    tot_move = 0 # Track total number of movements across all rows

    # Process each row in the 5x5 grid
    for col in range(5):
        # Call pack5() to shift tiles downward and merge matching values in this row
        # pack5() returns the 5 packed values plus the number of moves made
        [block_in_game[4][col],block_in_game[3][col],block_in_game[2][col],block_in_game[1][col],block_in_game[0][col],nmove] = (
            pack5(block_in_game[4][col],block_in_game[3][col],block_in_game[2][col],block_in_game[1][col],block_in_game[0][col]))

        tot_move += nmove  # Add this row's movements to the total count
    return tot_move  # Return total movements (0 if no tiles moved)

#pack the grid to the up
def move_up():
    tot_move = 0 # Track total number of movements across all rows

    # Process each row in the 5x5 grid
    for col in range(5):
        # Call pack5() to shift tiles upward and merge matching values in this row
        # pack5() returns the 5 packed values plus the number of moves made
        [block_in_game[0][col],block_in_game[1][col],block_in_game[2][col],block_in_game[3][col],block_in_game[4][col],nmove] = (
            pack5(block_in_game[0][col],block_in_game[1][col],block_in_game[2][col],block_in_game[3][col],block_in_game[4][col]))

        tot_move += nmove  # Add this row's movements to the total count
    return tot_move  # Return total movements (0 if no tiles moved)

def detect_no_fusion():
    # Check horizontal merges
    for line in range(5):
        for col in range(4):
            if block_in_game[line] [col] == block_in_game[line] [col + 1]:
                return False  # Merge possible → return False
    # Check vertical merges
    for line in range(4):
        for col in range(5):
            if block_in_game[line] [col] == block_in_game[line + 1] [col]:
                return False  # Merge possible → return False
    return True  # No merges found → return True

def detect_full():
    # Check if grid is full (no empty cells)
    for line in range(5):
        for col in range(5):
            if block_in_game[line] [col] == 0:
                return False  # Empty cell found → not full
    return True  # All cells filled

