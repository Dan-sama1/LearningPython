class Car:

    def turn_on(self):
        print("You start the engine.")
        return self

    def drive(self):
        print("You drive the car.")
        return self

    def brake(self):
        print("You stepped on breaks.")
        return self

    def turn_off(self):
        print("You turned off the engine.")
        return self

car = Car()

#METHOD CHAINING
car.turn_on().drive()

car.brake().turn_off()

(car.turn_on()
 .drive()
 .brake()
 .turn_off())
