class Animal: #PARENT CLASS

    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")
#TO CREATE A CHILD CLASS ADD A () NEXT TO IT AND PASS THE NAME OF THE PARENT CLASS
class Rabbit(Animal): #CHILD CLASS
    def run(self): #UNIQUE ATTRIBUTES AND METHODS
        print("this animal can run")
class Fish(Animal):
    def swim(self): #UNIQUE ATTRIBUTES AND METHODS
        print("this animal can swim")
class Hawk(Animal):
    def fly(self): #UNIQUE ATTRIBUTES AND METHODS
        print("this animal can fly")

#this children class inherits everything that parent class has
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()