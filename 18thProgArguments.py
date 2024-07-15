#ARGUMENTS
def add(*xD):
    sum = 0
    for i in xD:
        sum+= i
    return sum
print(add(1,2,3))

#KWARGS
def hello(**names):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in names.items():
        print(value, end=" ")
hello(title= "Mr.", first="Dan")