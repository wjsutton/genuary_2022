# Genuary 2022, Jan 6
# Task: Trade Styles with a Friend
# Idea: I'd consider anyone who made a library or package a friendy person, 
# so after a quick Google I've found the "samila" library on Github and will modify the tutorial to flow into Tableau
# https://github.com/sepandhaghighi/samila

# import python libraries, install with 'pip install ....'
import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from samila import GenerativeImage
from samila import Projection

# tutorial define maths functions and randomisation for data points
def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result

def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

# generate plot as polar, circles are super nice :)
g = GenerativeImage(f1,f2)
g.generate()
g.plot(projection=Projection.POLAR)
print(g.seed)
x = g.data2
y = g.data1

# convert polar to x and y for Tableau plot
x_polar = np.array(g.data2) * np.cos(np.array(g.data1))
y_polar = np.array(g.data2) * np.sin(np.array(g.data1))

# add data to dataframe 
d = {'x':x_polar,'y':y_polar,'seed':g.seed}
df = pd.DataFrame(data=d)

# write data to csv
df.to_csv('data\\06_trade_styles.csv', encoding='utf-8-sig', index=False)

# show image of plot
plt.show()