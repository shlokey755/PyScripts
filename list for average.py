#program to calculate average by entering marks at runtime
list1 = []
print("enter no. of students:")
n=int(input())
for i in range(0,n):
    print("enter marks of students:")
    marks=int(input())
    list1.append(marks)
    total = 0
    for marks in list1:
        total=total+marks
        
average = total / n
print("average:",average)
print(list1)
