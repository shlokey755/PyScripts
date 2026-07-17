#function
def func1():
    sum_odd=0
    sum_even=0
    for i in range(1,11):
        num=int(input("enter no:"))
        if num%2==0:
            sum_even=sum_even+num
        else:
            sum_odd=sum_odd+num
    print("sum of odd no.s:",sum_odd)
    print("sum of even no.s:",sum_even)

    
