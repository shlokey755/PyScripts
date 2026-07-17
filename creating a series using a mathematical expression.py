#program to create a series using a mathematical expression
import pandas as pd
import numpy as np
a = np.array([1,2,3,4,5])
s = pd.Series(a, index = a**2)
print(s)
