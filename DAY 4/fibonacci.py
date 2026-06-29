n=int(input("Enter the steps"))
def climbStairs( n):
        if n==1 or n==0:
            return 1
        s=climbStairs(n-1)+climbStairs(n-2)
        return s

p=climbStairs(n)
print(p)