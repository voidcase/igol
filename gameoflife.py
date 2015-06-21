import os
import time

def print_grid(grid):
    for i in grid:
        for j in i:
            if j == 1:
                print ("#",end=" ")
            if j == 0:
                print (".",end=" ")
        print ("")
    print ("")

def update_grid(grid):
    newgrid = [a[:] for a in grid]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            h = len(grid)
            w = len(grid[row])
            adj = []
            for i in range(-1,2):
                for j in range(-1,2):
                    adj.append(grid[(row+i)%h][(col+j)%w])
            adjsum = sum(adj)-grid[row][col]
            if adjsum == 3:
                newgrid[row][col] = 1
            elif adjsum > 3 or adjsum < 2:
                newgrid[row][col] = 0
    print_grid(newgrid)
    return newgrid
infile = open(argv[0], "r")
lines = infile.read().split("\n")
infile.close()

ingrid = []
toplength = 0
for l in lines:
    inline = []
    for i in l:
        if i in "#qwertyasdfghzxcvbn":
            inline.append(1)
        else:
            inline.append(0)
    toplength = max(toplength, len(inline))
    ingrid.append(inline)
for l in ingrid:
    for i in range(toplength-len(l)):
        l.append(0)

time_delta = 0.0
last_frame_time = time.time()
current_frame_time = 0.0

while True:
    timebefore = time.time()
    os.system("clear")
    ingrid = update_grid(ingrid)
    timeafter = time.time()
    time_delta = timeafter - timebefore
    time.sleep(0.1-time_delta)
