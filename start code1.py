'''#program to calculate average marks of n students
list1 = [ ]
n = int(input("How many students you want to enter:"))
for i in range(0,n):
    print("Enter marks of",(i+1),"student:")
    marks = int(input())
    list1.append(marks)
    total = 0
    for marks in list1:
        total = total + marks
average = total/n
print("Average marks of",n,"students:",average)'''

'''#program to add only even no. to a list
def main():
    L = [ ]
    n = int(input("Total no. of values in list:"))
    i = 1
    while i <= n:
        a = int(input("Enter element:"))
        if a%2 == 0:
            L.append(a)
            i=i+1
    print(L)'''

'''#program to check whether an element is in the list or not
list1 = [ ]
maximum = int(input("Enter the no. of elements in the list:"))
for i in range(0,maximum):
    n = int(input())
    list1.append(n)
num = int(input("Enter the no. to be searched:"))
pos = -1
for i in range(0,len(list1)):
    if list1[i] == num:
        pos = i
if pos == -1:
    print("not present")
else:
    print("present at",pos+1,"position")'''

'''#program to enter and count occurrences of an element
list1 = [10,20,30,40,10,50,10]
n = eval(input("Enter a no:"))
count = 0
for i in list1:
    if n == i:
        count = count + 1
print(n,"is present",count,"number of times")'''

'''#program to show products and their prices
d = {}
n = int(input("Enter no. of products:"))
for i in range(0,n):
    prod_name = input("Enter product name:")
    prod_price = int(input("Enter product price:"))
    d[prod_name] = prod_price
print(d)
srch = input("Enter product name here:")
for j in d:
    if srch == j:
        print(j,":",d[j])
        break
    else:
        print("No products found")'''

'''#program to perform linear search
d = {1:"one",2:"two",3:"three"}
print(d)
n = eval(input("Enter element to be searched:"))
for i in d:
    if i == n:
        print(i,":",d[i])
    break
else:
    print("No element found")'''

'''#program to find value
d = {1:10,2:12,3:14,4:14,5:14}
print(d)
n = int(input("enter value to be searched:"))
count = 0
for i in d:
    if n == d[i]:
        count = count + 1
if count != 0:
    print(n,"is present",count,"times")
else:
    print("No",n,"value found")'''

        

