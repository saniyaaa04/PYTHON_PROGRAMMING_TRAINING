n=int(input("Enter the number"))
for i in range(1,n+1):
   print("*"*i+" "*(2*(n-i))+"*"*i)

#inverted
for i in range(n-1,0,-1):
   print("*"*i+" "*(2*(n-i))+"*"*i)