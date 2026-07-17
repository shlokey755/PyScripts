#program to create a dataframe using a dictionary of series
import pandas as pd
s1 = pd.Series([1,2,3,4])
s2 = pd.Series(['Arunabh','Kanak','Shlok','Lokesh'])
s3 = pd.Series([17,20,18,19])
d = {'rollno': s1,'name': s2,'ratings': s3}
df1 = pd.DataFrame(d)
print(df1)
