# Genuary 2022, Jan 1
# Task: Draw 10,000 of something.
# Idea: A grid of 100 x 100 that explodes into random positions

# import python libraries, install with 'pip install ....'
import pandas as pd
import random as rn

# create lists for x and y points and cross join to make 10,000 points, each point forms a grid 100 x 100
x = list(range(100))
y = list(range(100))

x_coords = [a for a in x for b in y]
y_coords = [b for a in x for b in y]

# create 10,000 randomised x and y points
x_rand = [rn.uniform(0, 99) for p in range(0, len(x)*len(y))]
y_rand = [rn.uniform(0, 99) for p in range(0, len(x)*len(y))]

# create an id for all the points
point_id = list(range(len(x)*len(y)))

# create two data frames, one normalised, one randomised, differeniate by column stage = 1 or 2
d = {'stage': 1, 'point_id': point_id,'x':x_coords,'y':y_coords}
d_rand = {'stage': 2, 'point_id': point_id,'x':x_rand,'y':y_rand}
stage_1_df = pd.DataFrame(data=d)
stage_2_df = pd.DataFrame(data=d_rand)

# stack data frames together with concat
df = pd.concat([stage_1_df,stage_2_df])

# write data to csv
df.to_csv('data\\01_draw_10k.csv', encoding='utf-8-sig', index=False)
