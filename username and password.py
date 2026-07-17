#program to enter and display name and functions
username=input("enter username:")
password=input("enter password:")
if username == "admin" and password == "root":
    print("you are admin")
elif username == "user" and password == "root":
    print("you are user")
elif username == "guest" and password == "root":
    print("you are guest")
else:
    print("invalid user")
