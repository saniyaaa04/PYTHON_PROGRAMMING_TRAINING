num=input()
increasing=True
decreasing=True
for i in range (len(num)-1):
    if int(num[i+1])!=int(num[i])+1:
        increasing=False
    elif int(num[i+1])!=int(num[i])-1:
        decreasing=False
if increasing:
    print("Increasing Fancy Number")
elif decreasing:
    print("Decreasing Fancy Number")
else:
    print("Not a fancy number")
