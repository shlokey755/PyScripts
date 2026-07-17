#program to retrieve values using conditions
import pandas as pd
s = pd.Series([0.123432,1.234223,2.093653,0.986334])
print(s)
print(s[s>1])
print(s[s<2])
