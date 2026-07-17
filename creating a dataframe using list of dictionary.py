#program to create a dataframe using list of dictionary
import pandas as pd
d1 = {'rollno':1,'name':'Arunabh','rating':17}
d2 = {'rollno':2,'name':'Kanak','rating':20}
d3 = {'rollno':3,'name':'Shlok','rating':18}
d4 = {'rollno':4,'name':'Lokesh','rating':19}
l=[d1,d2,d3,d4]
df1 = pd.DataFrame(l)
print(df1)
