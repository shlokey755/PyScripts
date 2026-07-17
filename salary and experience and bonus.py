#program to enter salary and experience and calculate bonus
sal=int(input("enter salary:"))
exp=int(input("enter experience:"))
if sal>50000:
    if exp == 0:
        print("salary:",sal)
        print("bonus:",sal*3/100)
    elif exp > 10:
        print("salary:",sal)
        print("bonus:",sal*10/100)
    else:
        if exp < 10:
            print("salary:",sal)
            print("bonus:",sal*8/100)
else:
    if sal < 50000 and exp < 10:
        print("salary",sal)
        print("bonus:",sal*5/100)
        
