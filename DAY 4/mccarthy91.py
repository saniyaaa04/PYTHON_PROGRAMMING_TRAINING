#if no. >100 -10 
def mccarthy(n):
    if n>100:
        return n-10
    return mccarthy(mccarthy(n+11))

n=int(input("Enter the number:"))
print("Number: ",mccarthy(n))