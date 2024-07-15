from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2023, "red")

print(Car.wheels) #displays the value of the class variable

car_1.wheels = 2 #Change the class variable for car1 only
print(car_1)

Car.wheels = 2 #Change the class variable using other class, this also change the value of the class variable