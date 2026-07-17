#dataframe to test slicing
import pandas as pd
import numpy as np
data = {'name':['shlok','veeraj','krish','hoshank','aditya','arunabh','kanak','jha'],
              'class':[12,12,12,12,12,12,12,12],
              'position':['CDM','CB','LWF','CAM','RWF',np.NAN,np.NAN,'GK']}
df = pd.DataFrame(data)
print(df)
