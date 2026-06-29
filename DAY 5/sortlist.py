#numbers=list(input("Enter"))
students=[("Dinix",23),("Susanne",25),("Saniya",19),("Nandana",20)]
a=sorted(students, key=lambda x:x[1] )
b=list(min(students, key=lambda x:x[1] )) #make it list of tuple
c=max(students, key=lambda x:x[1] )
print(a)
print(b)
print(c)