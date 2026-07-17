#program to convert digital time into analog time
d_time=int(input("enter digital time:",))
if d_time <=12:
    print("digital time:",d_time,"am")
    print("analog time:",d_time,"am")
else:
    print("digital time:",d_time,"pm")
    print("analog time:",d_time-12,"pm")
