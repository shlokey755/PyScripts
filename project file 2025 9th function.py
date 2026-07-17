#9
import pandas as pd
import matplotlib.pyplot as plt
'''data = [[1,2,3,4],[4,3,2,1],[3,3,2,2],[2,2,3,3]]
df = pd.DataFrame(data, index = ["nitin",'hitesh','shashank','shlok'], columns = ['rin','barou','nagi','bachira'])
print(df)
'''
#1st rows filtering
'''n = int(input("Enter the starting no:"))
n1 = int(input("Enter the tarting no:"))
n1 = n1 + 1
e = df.iloc[n:n1]
print(e)

#2nd rows filtering
n2 = input("enter starting: ")
n3 = input("enter tarting: ")
d = df.loc[n2:n3]
print(d)

#1st columns filtering
c = int(input("enter starting: "))
c1 = int(input("enter tarting: "))
c1 = c1+1
d = df.iloc[:,c:c1]
print(d)

#2nd columns filtering
v = input("enter starting: ")
v1 = input("enter tarting: ")

d = df.loc[:,v:v1]
print(d)

#1st rows and column filtering
bb = int(input("enter starting:"))
bb1 = int(input("enter tarting:"))
b3 = int(input("enter starting:"))
b4 = int(input("enter startin:"))
bb1 = bb1 + 1
b4 = b4 + 1
d = df.iloc[bb:bb1,b3:b4]
print(d)

#2nd rows and column filtering
bb = input("enter starting:")
bb1 = input("enter tarting:")
b3 = input("enter starting:")
b4 = input("enter startin:")

d = df.loc[bb:bb1,b3:b4]
print(d)
'''


'''
24 acc
28 ip
3 eco'''

dataset = pd.read_csv("C:\\Users\\Keerti\\Downloads\\sleep_health_data.csv")
_main_dataframe_ = pd.DataFrame(dataset)

print("Choice: Display the dataset with specific columns.")
print(_main_dataframe_)
'''
i = int(input("Enter the number of columns you want"))
colmns = [ ]
for i in range(0,i):
    _col_name_ = input("Enter column name:")
    colmns.append(_col_name_)
_df_specific_columns_ = pd.read_csv("C:\\Users\\Keerti\\Downloads\\sleep_health_data.csv",usecols = colmns)
print(_df_specific_columns_)'''

'''plt.plot(Age, SleepQuality)
plt.show()
'''

'''plt.plot(df['Column1'], df['Column2'])
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.title('Plot of Column1 vs Column2')
plt.show()
'''
'col = _main_dataframe_[Age]'
'''
plt.bar(_main_dataframe_["Occupation"], _main_dataframe_["BMICategory"])
plt.plot(_main_dataframe_["PhysicalActivityLevel"], _main_dataframe_["BMICategory"])

plt.xlabel("Age")
plt.ylabel("s")
'''
'''
plt.plot(_main_dataframe_["PersonID"],_main_dataframe_['SleepDuration'])
plt.plot(_main_dataframe_["PersonID"],_main_dataframe_["QualityofSleep"])
plt.xlabel("Person ID")
plt.ylabel("Duration of Sleep & Quality of Sleep")
plt.xticks([10,20,30,40,50])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
plt.title("Sleep Chart")
plt.show()

plt.plot(_main_dataframe_["PersonID"],_main_dataframe_["PhysicalActivityLevel"])
plt.xlabel("Person ID")
plt.ylabel("Physical Activity Level (10 -120)")
plt.yticks([0,30,60,90,120])
plt.xticks([10,20,30,40,50])
plt.title("Physical Activity Chart")
plt.show()

plt.plot(_main_dataframe_["PersonID"],_main_dataframe_["StressLevel"], 'c')
plt.xlabel("Person ID")
plt.ylabel("Stress Level (1 - 10)")
plt.title("Stress Chart")
plt.show()

plt.plot(_main_dataframe_["PersonID"],_main_dataframe_["Age"], 'r','--')
plt.xlabel("Person ID")
plt.ylabel("Age")
plt.show()'''

plt.plot(_main_dataframe_["QualityofSleep"],_main_dataframe_["PersonID"])
plt.show()
