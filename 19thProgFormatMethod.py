#FORMAT METHOD
first = "dan"
last = "xD"
animal = "cow"
item = "moon"
#print("Hi my first name is {}, and my last name is {}".format(first, last))
#print("Hi my first name is {1}, and my last name is {0}".format(first, last)) #positional argument
#print("Hi my first name is {first}, and my last name is {first}".format(first="dan", last="xD")) #keyword argument

text = "The {} jump over the {}"
#print(text.format(animal, item))

#ADD A PATHING
name = "lamaw"
#I can add a number to precede using a colon
print("HI {:25}, nice to meet you!".format(name))

print("HI {:<25}, nice to meet you!".format(name)) #Align to left

print("HI {:>25}, nice to meet you!".format(name)) #Align to right

print("HI {:2^5}, nice to meet you!".format(name)) #Align to center

#Number variables

pi = 3.14159
number = 1000
print("The number pi is {:.2f}".format(pi))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number)) #Convert to binary
print("The number pi is {:o}".format(number)) #Convert to Octal
print("The number pi is {:X}".format(number)) #Convert to hexadecimal (Upper case X if you want upper case. Use 'x' if lower case)
print("The number pi is {:E}".format(number)) #Convert to Scientific notation (Uppercase E if you want upper case, use lower case 'e' if you want lowercase)