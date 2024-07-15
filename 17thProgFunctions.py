#FUNCTIONS
'''
def hello(age, last):
    print("Your name is " + last + " and you are ", age, " years old.")
hello(18, "Dan")

#RETURN STATEMENT
def multiply(num1, num2):
    result = num1 * num2
    return result
print(multiply(6, 8))

def multiply(num1, num2):
    return num1 * num2
ans = multiply(6, 8)
print("Value: ", ans)


#Keyword arguments
def names(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)
names(first="dan",middle="xD",last="lamaw")
'''
print(round(abs(float(input("Enter a whole positive number: ")))))