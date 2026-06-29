r=int(input("Enter the rainfall in mm :"))
if r>=0 and r<1:
    print("No Rain")
elif r>=1 and r<5:
    print("Light Rainfall")
elif r>=5 and r<10:
    print("Moderate rainfall")
else:
    print("Heavy rain")
