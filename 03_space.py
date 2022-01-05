# Genuary 2022, Jan 3
# Task: Space.
# Idea: Space, the last frontier. What is space without aliens, or specifically space invaders.. 
# randomly generate an army of space invaders, size, colour, position
# 4 bands: motherships, space invaders, enemy lasers, human ship

# import python libraries, install with 'pip install ....'
import pandas as pd
import numpy as np
import random as rn

# adding motherships at top band
num_of_motherships = rn.randint(3,9)
size_ms = [rn.randint(1,5) for p in range(0, num_of_motherships)]
x_ms = [rn.uniform(0, 10) for p in range(0, num_of_motherships)]
y_ms = [rn.uniform(9, 10) for p in range(0, num_of_motherships)]
colour_ms = [rn.randint(1,10) for p in range(0, num_of_motherships)]
shape_ms = ['mystery'] * num_of_motherships
ms = {'shape': shape_ms, 'size': size_ms,'colour': colour_ms,'x':x_ms,'y':y_ms}
mothership_df = pd.DataFrame(data=ms)
print(mothership_df)

# create band of enemies
num_of_enemies = rn.randint(70,120)
size_em = [rn.randint(1,5) for p in range(0, num_of_enemies)]
x_em = [rn.uniform(0, 10) for p in range(0, num_of_enemies)]
y_em = [rn.uniform(3, 8) for p in range(0, num_of_enemies)]
colour_em = [rn.randint(1,10) for p in range(0, num_of_enemies)]
shape_em = ['enemy1_1','enemy2_1','enemy3_1','enemy1_2','enemy2_2','enemy3_2'] * num_of_enemies
# randomise enemies
rn.shuffle(shape_em)
shape_em = shape_em[0:num_of_enemies]
em = {'shape': shape_em, 'size': size_em,'colour': colour_em,'x':x_em,'y':y_em}
enemy_df = pd.DataFrame(data=em)
print(enemy_df)

# add band of lasers and explosions
num_of_lasers = rn.randint(10,20)
size_ls = [rn.randint(1,2) for p in range(0, num_of_lasers)]
x_ls = [rn.uniform(2, 8) for p in range(0, num_of_lasers)]
y_ls = [rn.uniform(1, 3) for p in range(0, num_of_lasers)]
colour_ls = [rn.randint(1,10) for p in range(0, num_of_lasers)]
shape_ls = ['enemylaser','explosionblue','explosiongreen','explosionpurple'] * num_of_lasers
rn.shuffle(shape_ls)
shape_ls = shape_ls[0:num_of_lasers]
ls = {'shape': shape_ls, 'size': size_ls,'colour': colour_ls,'x':x_ls,'y':y_ls}
laser_df = pd.DataFrame(data=ls)

# add human ship
num_of_humans = 1
size_hm = [1]
x_hm = [5]
y_hm = [0]
colour_hm = [11]
shape_hm = ['ship']
hm = {'shape': shape_hm, 'size': size_hm,'colour': colour_hm,'x':x_hm,'y':y_hm}
human_df = pd.DataFrame(data=hm)

# combine all data frames
df = pd.concat([mothership_df,enemy_df,laser_df,human_df])

# write data to csv
df.to_csv('data\\03_space.csv', encoding='utf-8-sig', index=False)
