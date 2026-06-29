n=int(input("Enter the number"))
sum=0
for i in range(1,len(n)):
    a=n%10
    sum+=a
    n=n//10
    
