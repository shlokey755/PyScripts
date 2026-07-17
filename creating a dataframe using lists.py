#program to create a dataframe using lists
import pandas as pd
list1 = [1,'A','Arunabh']
list2 = [2,'K','Kanak']
list3 = [3,'S','Shlok']
list4 = [4,'L','Lokesh']
list5 = [list1,list2,list3,list4]
df1 = pd.DataFrame(list5, columns=['No.','Initials','Name'])
print(df1)
