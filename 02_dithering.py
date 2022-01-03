# Genuary 2022, Jan 2
# Task: Dithering.
# Idea: Prompts mention image dithering but prefer the idea of dithering to not reach goals...
# i.e. try to get from A to B but 50% of the time you will go a different directions
# move 2 steps forward, 1 step back (dither) 

# import python libraries, install with 'pip install ....'
import pandas as pd
import numpy as np
import random as rn

# Using pathfinding library:
# https://pypi.org/project/pathfinding/
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# working through pypi tutorial, using 9x9 matrix
matrix = 25*[25*[1]]
grid = Grid(matrix=matrix)

# declare start & end points
start = grid.node(0, 0)
end = grid.node(24, 24)

# set path finder
finder = AStarFinder(diagonal_movement=DiagonalMovement.only_when_no_obstacle)
path, runs = finder.find_path(start, end, grid)

# path finder output
print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
print(path)

# write path data to data frame
regular_df = pd.DataFrame(path, columns=['x', 'y'])
regular_df['stage'] = regular_df.index
regular_df['type'] = 'Not Randomised'

# Do the same as above, except add zeros randomly that block the path
# Loop until a valid path is returned
path_length = 0

while path_length < 1:
    # make long list of 1s & 0s, shuffle and then convert to a matrix
    flat = ([1]*18+[0]*7)*25
    rn.shuffle(flat)
    col = 25
    rand_matrix = [flat[i:i+col] for i in range(0, len(flat), col)]
    rand_grid = Grid(matrix=rand_matrix)

    # declare start & end points (same as before)
    rand_start = rand_grid.node(0, 0)
    rand_end = rand_grid.node(24, 24)

    # set path finder
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    rand_path, rand_runs = finder.find_path(rand_start, rand_end, rand_grid)

    print('operations:', rand_runs, 'path length:', len(rand_path))
    print(rand_grid.grid_str(path=rand_path, start=rand_start, end=rand_end))
    print(rand_path)

    path_length = len(rand_path)

# write random path to dataframe
random_df = pd.DataFrame(rand_path, columns=['x', 'y'])
random_df['stage'] = random_df.index
random_df['type'] = 'Randomised'

# stack data frames together with concat
df = pd.concat([regular_df,random_df])

# write data to csv
df.to_csv('data\\02_dithering.csv', encoding='utf-8-sig', index=False)
