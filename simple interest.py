principle=eval(input("Enter the value of Principle:"))
rate=eval(input("Enter the Rate of Interest:"))
time=1.3

simple_int=principle*rate*time/100
amount=principle+simple_int

print("simple interest=",simple_int)
print("amount=",amount)
