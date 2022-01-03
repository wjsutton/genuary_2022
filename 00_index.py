# Genuary 2022, Index
# Task: Create index page
# Idea: Radial, order by days of Jan, random radius, colour, size

# import python libraries, install with 'pip install ....'
import pandas as pd
import random as rn

df = pd.read_csv('data\\index.csv')

size = [rn.randint(1,5) for p in range(0, len(df))]
colour = [rn.randint(1,9) for p in range(0, len(df))]
radius = [rn.randint(1,5) for p in range(0, len(df))]

df['size'] = size
df['colour'] = colour
df['radius'] = radius

# write data to csv
df.to_csv('data\\00_index.csv', encoding='utf-8-sig', index=False)
