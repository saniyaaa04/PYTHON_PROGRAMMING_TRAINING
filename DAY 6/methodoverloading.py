#method overloading
class Demo:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
obj=Demo()
obj.add(10)
obj.add(10,40)
 #the above is invalid in python

class Demo:
    def add(self,*numbers):
        print(sum(numbers))
obj=Demo()       
obj.add(10)
obj.add(10,40)
obj.add(23,45,67)
#in python this is method overloading
