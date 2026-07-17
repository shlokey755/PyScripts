import pandas as pd
import matplotlib.pyplot as plt
list1 = [[1,2,3],[4,5,6],[6,5,4],[4,5,6],[6,5,4],[4,5,6],[6,5,4],[5,5,5]]
df = pd.DataFrame(list1)
df.plot(kind = 'line')
plt.xticks()
plt.yticks()
plt.show()
