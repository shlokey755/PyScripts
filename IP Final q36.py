import pandas as pd
data = {"DID":[101,102,103,104,105],
        "NAME":["j",'s','j','n','v'],
        "Department":["ent",'uro','ortho','ent','ortho'],
        "fee":[1500,1600,1550,1200,1700]}
df = pd.DataFrame(data)
print(df)
