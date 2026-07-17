d1={}
n=int(input("enter the number of students:"))
i=1
while i<=n:
    Admno=input("enter admission number:")
    rollno=int(input("enter rollno:"))
    name=input("enter name of student:")
    subject=input("enter your subject:")
    d1[Admno]=(rollno,name,subject)
    i=i+1
print('student details')
for j in d1:
    print('admission no:',j,'Student details:',d1[j])
