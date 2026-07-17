#practice3
principal=eval(input("enter the value of principle:"))
rate=eval(input("enter the rate of interest:"))
time=eval(input("enter the time:"))
simple_interest=(principal*rate*time)/100
amount=principal+simple_interest
print("simple interest:",simple_interest)
print("amount:",amount)
