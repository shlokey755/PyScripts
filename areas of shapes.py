#program to find area of shapes according to user
shape=input("enter shape:")
if shape=='square':
    side=int(input("enter side:"))
    print("area:",side**2)
elif shape=='circle':
    radius=int(input("enter radius:"))
    print("area:",22/7*radius**2)
elif shape=='rectangle':
    length=int(input("enter length:"))
    breadth=int(input("enter breadth:"))
    print("area:",length*breadth)
elif shape=='triangle':
    base=int(input("enter base:"))
    height=int(input("enter height:"))
    print("area:",1/2*base*height)
else:
    print("shape don't exist in code")
