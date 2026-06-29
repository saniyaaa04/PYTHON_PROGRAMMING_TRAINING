t=int(input("Enter the tickets: "))
p=int(input("Enter ticket price :"))
a=int(input("category 0 or 1 :"))
amt=t*p
discount=0
if t>=15:
    discount+=20
if a==1:
    discount+=5

if discount>0:
    amt=amt-(amt*discount/100)
    if t>=15 and a==1:
        print("Discount applied both Max ticket and Catagory discount ")
    elif t>=15:
        print("Discount applied Max ticket ")
else :
    print("No discount ") 

print("total amount ",amt)
