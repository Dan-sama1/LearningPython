class Car:
    wheels = 4

    def __init__(self,make,model,year,color):
        self.make = make #INSTANCE VARIABLE
        self.model = model #INSTANCE VARIABLE
        self.year = year #INSTANCE VARIABLE
        self.color = color #INSTANCE VARIABLE

    def drive(self): #in self we do not need to pass anything in function
        print("This " + self.model+ " is driving")

    def stop(self):
        print("This " + self.model +" is stopped")