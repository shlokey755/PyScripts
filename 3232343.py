program=input('''Welcome to this very special program of python code-learning for those who can't
understand its working properly. Given below is the list of all the python programs included
in this specially built program for the beginners:
1. Area
    Areaofsquare
    Areaoftriangle
    Areaofrectangle
    Areaofcircle
2. Conversion
    Conversionoftemperature
    Conversionofdigitaltime
    Conversionoftotalminutes
    Conversionoftotalinches
3. Looping codes
    3.1 For Loop-
          forloop1to100
          forloop1000to1
          forlooptables
          forloopfibonacciseries
    3.2 While Loop-
          whileloop1to100
          whileloop1000to1
          whilelooptables
          whileloopfibonacciseries



Now please enter the program name:''')

if program=="Areaofsquare":
    print('''s=eval(input("side:"))
area=s**2
print("area is:",area)''')
elif program=="Areaoftriangle":
    print('''base=int(input("enter base:"))
    height=int(input("enter height:"))
    print("area:",1/2*base*height)''')
elif program=="Areaofrectangle":
    print('''length=int(input("enter length:"))
    breadth=int(input("enter breadth:"))
    print("area:",length*breadth)''')
elif program=="Areaofcircle":
    print('''radius=int(input("enter radius:"))
    print("area:",22/7*radius**2)''')
elif program=="Conversionoftemperature":
    print('''temperature_in_fahrenheit=eval(input("enter the temperature in fahrenheit:"))
temperature_in_celsius=(temperature_in_fahrenheit-32)*5/9
print("temperature in fahrenheit:",temperature_in_fahrenheit)
print("temperature in celsius:",temperature_in_celsius)''')
elif program=="Conversionofdigitaltime":
    print('''d_time=int(input("enter digital time:",))
if d_time <=12:
    print("digital time:",d_time,"am")
    print("analog time:",d_time,"am")
else:
    print("digital time:",d_time,"pm")
    print("analog time:",d_time-12,"pm")''')
elif program=="Conversionoftotalminutes":
    print('''time=int(input("enter the time in minutes:"))
hours=time//60
mins=time%60

print("hours are:",hours)
print("minsutes are:",mins)''')
elif program=="Conversionoftotalinches":
    print('''height=int(input("height of a student in total inches:"))
feet=height//12 
inches=height%12 
print("total feet=",feet)
print("total inches=",inches)''')
elif program=="forloop1to100":
    print('''for i in range(1,101):
    print(i)      ''')
elif program=="forloop1000to1":
    print('''for i in range(1000,0,-1):
    print(i)''')
elif program=="forlooptables":
    print('''num=int(input("enter no:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)''')
elif program=="forloopfibonacciseries":
    print('''rows=int(input("enter:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="  ")
    print("")''')
elif program=="whileloop1to100":
    print('''i=1
while i<=100:
    print(i)
    i=i+1''')
elif program=="whileloop1000to1":
    print('''i=1000
while i>=1:
    print(i)
    i=i-1''')
elif program=="whilelooptables":
    print('''num=int(input("enter no:"))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1''')
elif program=="whileloopfibonacciseries":
    print('''n = int(input("Enter number of terms: "))
n1, n2 = 0, 1 
i = 0  

if n <= 0:
  print("Please enter a positive integer")
elif n == 1:
  print("Fibonacci sequence upto",n,":")
  print(n1)
else:
  print("Fibonacci sequence:")
  for i in range(n):  
      print(n1)
      sum = n1 + n2 
      n1 = n2
      n2 = sum
      i += 1''')
else:
    print("Invalid Request. Please try again!")








