#program to create a dataframe using dictionary of lists
import pandas as pd
list1 = [1,2,3,4]
list2 = ['Arunabh','Kanak','Shlok','Lokesh']
list3 = [17,20,18,19]
df1 = pd.DataFrame({'rollno':list1,'name':list2,'rating':list3})
print(df1)
