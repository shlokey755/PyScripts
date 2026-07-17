#program to calculate the factorial of a no.
fact=1
num=int(input("enter no:"))
for i in range(1,num+1):
    fact=fact*i
print("factorial of",num,"is",fact)
