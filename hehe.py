L1=[]
for i in range(1,11):
    L=eval(input("enter no:"))
    L1.append(L)
L2=L1.copy()
n=L2[:5]
n.reverse()
del L2[:5]
for i in n:
    L2.append(i)
