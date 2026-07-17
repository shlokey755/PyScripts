#program to print any no. backwards
num=int(input("enter no:"))
x=num
while num > 0:
    n=num//10
    r=num%10
    num=n
    print(r,end="")

