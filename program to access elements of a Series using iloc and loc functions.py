#program to access elements of a Series using loc and iloc functions
import pandas as pd
s = pd.Series([1,2,3,4,5,6,7,8,9,10], index =[x for x in 'abcdefghij'])
print(s)
print(s.iloc[0:5])
print(s.loc['a':'e'])
