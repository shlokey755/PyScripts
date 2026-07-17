#program to access elements from a series
import pandas as pd
s = pd.Series({'A':'Arunabh','K':'Kanak','S':'Shlok','L':'Lokesh'})
print(s)
print(s[['S','L']])
print(s[['A','K']])
