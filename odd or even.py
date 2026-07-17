#program to check whether the no is odd or even
num=int(input("enter the no."))
rem=num%2 #modulus operator... isko lagane ke baad sirf decimal value dikhti hai
if rem==0: #if argument use horhi hai kyuki 2 outcomes hai... == aur = alag alag hai.. == use hota hai check krne ke liye
    print("it is an even no.") #agar x/2 mein koi decimal nhi hai toh ye print hoga
else:
        print("it is an odd no.") #agar x/2 mein hai decimal toh ye print hoga
