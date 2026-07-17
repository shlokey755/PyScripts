#program to convert height of a student in inches convert these inches into feet and remaining inches
height=int(input("height of a student in total inches:"))
feet=height//12 # // is used to divide but not to enter the remainder
inches=height%12 # % modulus operater is used to store the operater
print("total feet=",feet)
print("total inches=",inches)
