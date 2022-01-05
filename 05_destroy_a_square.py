# Genuary 2022, Jan 5
# Task: Destroy a Square
# Idea: Draw a Square then shuffle all the xy coords

# import python libraries, install with 'pip install ....'
import numpy as np
import pandas as pd
import random as rn

# create a square path using x & y coords
x = list(range(0,24)) + [24]*25 + list(range(24,-1,-1)) + [0]*25
y = [0]*25 + list(range(0,24)) + [24]*25 + list(range(24,-1,-1))
path = list(range(0,len(x)))

# create new positions for the xy coords
new_x = [rn.uniform(0, 24) for p in range(0, len(x))]
new_y = [rn.uniform(0, 24) for p in range(0, len(x))]

# create data frame for square
d = {'x': x, 'y': y,'path': path,'stage':1}
df = pd.DataFrame(data=d)

# create data frame for square after being shuffled
d_new = {'x': new_x, 'y': new_y,'path': path,'stage':2}
df_new = pd.DataFrame(data=d_new)

# combine data frames
df = pd.concat([df,df_new])

# write data to csv
df.to_csv('data\\05_destroy_a_square.csv', encoding='utf-8-sig', index=False)
