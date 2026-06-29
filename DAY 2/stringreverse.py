name=input("Enter the string :")
mid=len(name)//2

firstpart=name[:mid]
secondpart=name[mid:]
reversefirstpart=firstpart[::-1]
reversesecondpart=secondpart[::-1]
result=reversefirstpart+reversesecondpart
print(result)

