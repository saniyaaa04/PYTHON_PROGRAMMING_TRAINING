numbers=list(map(int,input("Enter the number :").split()))
k=int(input("Enter the Threshold value k: "))
freq=dict()

for num in numbers:
    freq[num]=freq.get(num,0)+1 # list be 1 2 1 2 3 3 1 2
                #get(key,value) get(1,0 initial value)+1 in freq{1: 2: 3:} like in dictionary u add and count
               #then get(2,0)+1 like key value is 2 u initialize 0 and count it so add 1
               # then get(1,1)+1 already the count is 1 add 1 to it

for num,count in freq.items(): #in freq(1:3,2:3,3:2) freq(num:count)
    if count>k:
        print(f"{num}:{count} times")
       # print(num,":",count,"times") this works tooo if f given u use {name of variable with value if use = it will print the variable  } write in one stretch in""
       


