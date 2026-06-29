#2nd largest of the following
a=int(input("enter "))
b=int(input("enter "))
c=int(input("enter "))
if (a<=b and a>=c) or (a<=c and a>=b):
    print("b is 2nd largest")
elif (b<=a and b>=c) or (b<=c and b>=a):
        
    print("a is 2nd largest")
else:
    print("c is 2nd largest")