import pandas as pd
l1 = [['mps',80,10,70],['sfc',88,12,76],['jps',25,4,21],['aps',45,6,39],['rlps',90,15,75],['dps',60,6,54]]
l2 = ['so1','so2','so3','so4','so5','so6']
l3 = ['school','computers','non-working','working']
df = pd.DataFrame(l1, index = l2, columns = l3)
print(df)
print(df.shape)
