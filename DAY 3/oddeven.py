s=list(map(int,input("Enter the value :").split()))
even=0
odd=0
for i in s:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Odd: ",odd,"\nEven :",even)