import numpy as np
#import gstools as gs
import pandas as pd

# the grid
x = np.arange(100* np.pi())
#x = list(range(0,100)) * np.pi()/100.0
#y = list(range(0,100))

x = x/1.0
x = float(x) * np.pi()
print(x)