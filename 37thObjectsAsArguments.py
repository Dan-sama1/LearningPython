#We can pass objects as arguments to a function much like what we've been doing with variables however the type of objects that we pass in may be limited on the required attributes and methods that given class or objects might have.
class Car:

    color = None
class Motorcycle:

    color = None
def change_color(car, color):

    car.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "yellow")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)


