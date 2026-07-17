a={1:20,2:30,3:50,4:60,7:80}
b={1:30,5:80,4:90,6:80,3:40}
c={}
for i in range(0,4):
       if i in a == i in b:
           s=a[i]+b[i]
           n=i
           c[n]=s
print(a)
print(b)
print(c)
