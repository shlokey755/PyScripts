#program to create a dataframe using series
import pandas as pd
s1 = pd.Series([11,22,33,44,55])
s2 = pd.Series([1,2,3,4,5])
df1 = pd.DataFrame([s1,s2])
print(df1)
