#program to check whether a no. is prime or not
yes=0
num=int(input("enter no:"))
for i in range(2,num//2):
    if num%i==0:
        yes=1
    else:
        yes=0
if yes==0:
    print("prime")
else:
    print("not prime")
