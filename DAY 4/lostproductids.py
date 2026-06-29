products=input("Enter list of products").split()
all_ids=set(products)
duplicates=set()

#find duplicates
for id in products:
    if products.count(id)>1:
        duplicates.add(id)

lost_ids=all_ids-duplicates
print("Lost product IDs :",lost_ids)