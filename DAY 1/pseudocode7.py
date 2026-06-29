N=int(input("Enter the number : "))
square=N*N
digits=len(str(N))
right=square%(10**digits)
left=square//(10**digits)

if (left+right==N):
    print("Keprekar Number")

else:
    print("Not a Keprekar Number")
