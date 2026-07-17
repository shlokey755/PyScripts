#program to create a dataframe using ndarray
import pandas as pd
import numpy as np
arr1 = np.array([1,'Arunabh',17])
arr2 = np.array([2,'Kanak',20])
arr3 = np.array([3,'Shlok',18])
arr4 = np.array([4,'Lokesh',19])
df1 = pd.DataFrame([arr1,arr2,arr3,arr4], columns = ['rollno','name','ratings'])
print(df1)
