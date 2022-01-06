# Genuary 2022, Jan 4
# Task: The next next Fidenza.
# Idea: Having trouble with fidenza free flow algo so improvising
# There is a town in Italy called Fidenza so:
#  - Find the city roads for Fidenza here: https://anvaka.github.io/city-roads/?q=fidenza&areaId=3600043602
#  - Download the svg, then warp the svg twice using: https://pavellaptev.github.io/warp-svg/
#  - Take the 3 svgs and get the xy coords using: https://spotify.github.io/coordinator/

# import python libraries, install with 'pip install ....'
import numpy as np
import pandas as pd

# Read in the coordinator csvs
df1 = pd.read_csv('fidenza_svgs\\Fidenza xy.csv')
df2 = pd.read_csv('fidenza_svgs\\Fidenza xy warp1.csv')
df3 = pd.read_csv('fidenza_svgs\\Fidenza xy warp2.csv')

# add a path that is a row count
df1['path'] = df1.index
df2['path'] = df2.index
df3['path'] = df3.index

# label the different datasets
df1['stage'] = 1
df2['stage'] = 2
df3['stage'] = 3

# concat all data frames together
df = pd.concat([df1,df2,df3])

# write data to csv
df.to_csv('data\\04_fidenza.csv', encoding='utf-8-sig', index=False)
