#program to create a series using a list
import pandas as pd
s = pd.Series([1,2,3,4,5], index = [x for x in 'abcde'])
print(s)
