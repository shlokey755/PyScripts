#program to print list
d={}
l_name = []
l_pass = []
n=int(input("enter no. of names:"))
for i in range(0,n):
    nme=input("enter name:")
    pss=input("enter pass:")
    l_name.append(nme)
    l_pass.append(pss)
    d[nme]=(pss)
print("")
print(d)
print(l_name)
print(l_pass)

    
