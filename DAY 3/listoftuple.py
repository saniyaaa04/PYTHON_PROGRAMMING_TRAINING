list=eval(input("enter "))
k=int(input("Enter :"))
product=1
for i in list:
    product=product*i[k]
print(f"Product of value:{k}: {product}")
