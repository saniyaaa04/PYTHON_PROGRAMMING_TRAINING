class Dog:
    def sound():
        print("BOW BOW")
    def eat(self):
        print("Dog is eating")
class Cat(Dog):
    def sound():
        print("MEOW MEOW")
#instances
d=Cat()
d.eat()

#ex2
class father:
    def eat(self):
        print("Eating")
class Son:
    pass

son=Son()
son.eat()