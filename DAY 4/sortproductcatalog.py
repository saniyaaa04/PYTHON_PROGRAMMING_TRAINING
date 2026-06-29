products=eval(input("Enter the list of product and price :"))
choice=input("KEY/PRICE :").upper()
def get_value(item):
    return item[1]

if choice=="KEY":
    sorted_dic=dict(sorted(products.items()))
    print("Sorted dictionary :",sorted_dic)
elif choice=="PRICE":
    sorted_dic=dict(sorted(products.items(),key=get_value))
    print(sorted_dic)
else:
    print("INVALID CHOICE")





