#program to enter weight and height of a student and print whether student can take sports or not
height=eval(input("enter height of a student:"))
weight=eval(input("enter weight of a student:"))
if height>5 or weight>50:
    print("can take sports")
else:
    print("cannot take sports")
