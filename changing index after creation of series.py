#program to change index of series after creation
import pandas as pd
s = pd.Series([11,2,3,4,3,33,69])
print(s)
print("after changing index")
s.index(1,2,3,4,5,6,7)
print(s)
