import pandas as pd
data = [[240,25,123,94],
           [76,68,98,57],
           [164,114,95,125],
           [375,180,95,115]]
SALES = pd.DataFrame(data,index=['jammu','reasi','udhampur','srinagar'],columns=['apples','grapes','banana','guava'])
print(SALES)
