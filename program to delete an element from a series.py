#program to delete elements from a series
import pandas as pd
s = pd.Series([11,22,33,44,55])
print(s)
s2 = s.drop(4)
print(s2)
