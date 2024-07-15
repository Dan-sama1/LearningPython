from abc import ABC, abstractmethod #ABC MEANS ABSTRACT BASE CLASSES


class Vehicle(ABC):

    @abstractmethod #PREVENTS USER FROM CREATING AN OBJECT OF THIS CLASS.
    #if this abstract method is not override in the children class the children class is not accessable
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive a car")
        return self

    def stop(self):
        print("Car is stopped")
        return self


class Motorcycle(Vehicle):

    def go(self):
        print("You drive a motorcycle.")
        return self

    def stop(self):
        print("Motorcycle is stopped")
        return self


car = Car()
motorcycle = Motorcycle()

car.go().stop()
motorcycle.go().stop()