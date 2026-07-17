#calculator banayenge

num1=eval(input("num1:"))
num2=eval(input("num2:"))
op=input("operation:")
if op == "+":
    print(num1,"+",num2,"=")
    print(num1+num2)
elif op == "-":
    print(num1,"-",num2,"=")
    print(num1-num2)
elif op == "*":
    print(num1,"x",num2,"=")
    print(num1*num2)
elif op == "/":
    print(num1,"/",num2,"=")
    print(num1/num2)
elif op == "^":
    print(num1,"^",num2,"=")
    print(num1**num2)
else:
    print("error")
    

