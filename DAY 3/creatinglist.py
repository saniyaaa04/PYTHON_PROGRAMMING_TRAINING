num=[]
num2=list((1,2,3))
num3=[10,10.5,"Python",True]
num4=[[1,2],[2,3],[4,5]]
fruits=["Apple","Mango","Grapes"]

num5=[1,2,3,4]


print(num2)

print(num3)
print(num4)
#accessing list
print(fruits[-1])
print(fruits[1])
print(num5[1:4])
#slicing of list
print(num5[0:3])
print(num5[:3]) #from 0 to 3 index
print(num5[2:]) #from 2 to rest of index
print(num5[::-1]) #:: full list -1 means reverse

#list functions
#1. append(): to add elements
nums=[1,2,3]
nums.append(4)
print(nums)

#2. extend():add multiple elements
num7=[1,3]
num7.extend([4,5,6])
print(num7)

#3. Insert at specific index
num7.insert(1,15) #insert 15 at index 1
print(num7)

#4. delete operation
#1. remove()
num7.remove(4)
print(num7)

#2. pop(): removes last element
num7.pop()
print(num7)

#3.clear(): clears all elements
num8=[1,2,3]
num8.clear()
print(num8)

