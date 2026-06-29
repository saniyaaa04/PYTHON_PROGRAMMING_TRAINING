numbers=list(map(int,input("Enter the number :").split()))

s=set(numbers)
if len(numbers)==len(s):
    print(False)
else:
    print(True)
