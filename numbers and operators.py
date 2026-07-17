#program to enter numbers and operators at runtime
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
optr=input("enter operator")
if optr=='+':
    print(num1+num2)
elif optr=='-':
    print(num1-num2)
elif optr=='*':
    print(num1*num2)
elif optr=='/':
    print(num1/num2)
elif optr=='**':
    print(num1**num2)
else:
    print("invalid operator")
