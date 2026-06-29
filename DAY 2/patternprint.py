n=int(input("Enter the number"))
for i in range(1,n+1):
   print("*"*i)

#inverted
for i in range(n,0,-1):
   print("*"*i)


#arrow
for i in range(1,n+1):
   print(" "*(n)+"*"*i)

print("*"*(2*n+1))

#inverted
for i in range(n,0,-1):
   print(" "*(n)+"*"*i)