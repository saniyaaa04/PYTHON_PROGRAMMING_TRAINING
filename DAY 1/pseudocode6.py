N=75
if(N<=100 and N>0):
    result=N*1.5
elif(N<=200):
    result=((N-100)*2.5)+(100*1.5)
else:
    result=100*1.5+100*2.5+((N-200)*4)
print("The bill is :",result)