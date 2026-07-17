#program to give indexing to a series using for loop
import pandas as pd
s = pd.Series(range(1,15,3), index=[x for x in 'abcde'])
print(s)
