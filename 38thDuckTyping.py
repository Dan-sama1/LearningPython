class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This Chicken is walking")

    def talk(self):
        print("This Chicken is clucking")

class Person:
    #Class type will not be checked if the minimum methods or attributes is present(in this case the walk and the talk).
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
human = Person()
human.catch(chicken)