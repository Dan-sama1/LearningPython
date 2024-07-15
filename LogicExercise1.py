'''
import random
#PRINT ALL THE PRIME NUMBER FROM 1 TO 100
print("PRIME NUMBERS FROM 1 TO 100")
for num in range(2, 101):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

#PRINT THE 2O NUMBERS IN FIBONACCI SEQUENCE
print("FIRST 20 NUMBERS IN FIBONACCI SEQUENCE")
loop = 0
a = 0
b = 1

for num in range(1, 21):
    print(a)
    a, b = b, a+b

#MOVE THE VALUE OF THE LIST
inputlist = [1, 2, 3, 4, 5]
print(inputlist)
print("MOVE THE VALUE OF THE LIST")
rotation = int(input('Rotation count: '))
for rotate in range(rotation):
    list1 = inputlist.pop(0)
    inputlist.append(list1)
print(inputlist)

#GUESS THE RANDOM NUMBER FROM 1 TO 100
print("GUESSING GAME")
life = 5
num = random.randint(1, 100)
print("Current life: ", life)
while life > 0:
    user = int(input("Guess the number[0 - 100]: "))

    if user == num:
        print("YOU WIN!")
        break
    elif user > 100 or user < 0:
        print("You've reached the limit! Please guess again!")
    elif abs(user - num) <= 10:
        if user > num:
            print("Ooooh close(lower)")
        else:
            print("AW so close!(higher)")
        life -= 1
    elif user > num:
        print("too high")
        life -= 1
    elif user < num:
        print("too low")
        life -= 1
    print("life: ", life)
else:
    print("LMAO you lose!!")

#REVERSE THE ORDER OF THE WORDS IN THE SENTENCE
sent = input('Enter a sentence: ')
sentence = sent.split()[::-1]
print(' '.join(sentence))

#EASY: ADD ALL EVEN NUMBERS IN 0 TO 50
total = 0
for n in range(2, 51, 2):
    total += n
print(total)

#COUNT THE VOWELS IN A SENTENCE
vowels = 'aeiou'
string = input("Enter a sentence: ").lower()
count = 0
for letters in string:
    if letters in vowels:
        count += 1
print('Number of vowels: ', count)

#MULTIPLICATION TABLE OF A GIVEN NUMBER
num = int(input('Enter a number: '))
for prod in range(1, 11):
    multi = num * prod
    print(f"{num} * {prod} = {multi}")

#SOLVE THE FACTORIAL OF THE GIVEN NUMBER
num = int(input("Enter a number: "))
a = 1
while num >= 1:
    a = num * a
    num -= 1
print(a)

#REVERSE A STRING WITHOUT USING ANY REVERSE FUNCTION
string = input('Enter a sentence: ')
rev = ''
for reverse in range(len(string)-1, -1, -1):
    rev += string[reverse]
print(rev)

#Check IF THE TWO WORDS ARE ANAGRAM
word1 = input("Enter first word: ")
word2 = input("Enter a second word: ")
count1 = {}
count2 = {}

for words1 in word1:
    count1[words1] = count1.get(words1, 0)+1
for words2 in word1:
    count2[words2] = count2.get(words2, 0)+1
if count1 == count2:
    print("The words are anagram")
else:
    print("The words are not an anagram")

#LIST PRACTICE
data = {'f', 'b', 'c', 'd'}
data2 = {'a', 'e', 'i', 'o', 'u'}
enter = input("Enter a letter: ")

if enter in data:
    print("This data is doubled: ", data.intersection(enter))
elif enter in data2:
    print("This data is doubled: ", data2.intersection(enter))
else:
    print("New data created!\nAll data added!")
    data3 = data.union(data2)
    print("New data: ", data3)

#LIST MORE PRACTICE
stack_data = {'a', 'b', 'c', 'd'}
print("HI! Do you want to [add] new data or to [view] the data?", end=" ")
select = input().lower()
if select == "add":
    enter = int(input("Enter the number of data that you want to add: "))
    new_data = set()
    while enter > 0:
        add_data = input("Add data: ")
        if add_data in stack_data:
            print("data is already existing!")
        else:
            new_data.add(add_data)
            enter -= 1
    updated_data = stack_data.union(new_data)
    print(f"""
Data Added:
{new_data}
All Data:
{updated_data}""")
elif select == "view":
    print(f""""View Data
{stack_data}""")
else:
        print("try again")

basket = ('apple', 'banana', 'orange', 'grape')
basket1 = basket[:2]
basket2 = basket[3:]

#CREATE ACCOUNT, CHECKS THE EMAIL IF IT EXISTS AND IF IT EXISTS MATCH IF THE ENTERED PASSWORD MATCHED THE ASSIGNED
#PASSWORD IN THE EMAIL
print("create account")
dic = {}
enter = input("Enter username: ")
pw = input("Enter password: ")
pw2 = input("Confirm password: ")
if pw == pw2:
    dic[enter] = pw
    print("Account Created! Please log in.")
    em = input("Enter username: ")
    pwrd = input("Enter password: ")
    for key, value in dic.items():
        if em in key and pwrd == dic.get(em):
            print("Login successful")
        else:
            print("Wrong credentials")
            break
else:
    print("Try again")

#Write a program that takes a user's full name as input and prints the initials in uppercase.
name = input("Enter your fullname: ").upper().split()
initials = ""
for index in name:
    initials += index[0]
print(initials)

#Create a list of five favorite fruits. Add one more fruit to the list, remove the third fruit, and print the final list.
fav = ['apple', 'banana', 'mango', 'strawberry', 'orange']
fav.append('watermelon')
fav.remove('mango')
print(fav)

#Create a dictionary with three key-value pairs: name, age, and city. Update the city value and print the updated dictionary.
dic = {'name': 'john',
       'age': 18,
       'city': 'Washington DC'}
dic.update({'city': 'Los Angeles'})
print(dic)

#Write a program that takes a list of numbers and prints whether each number is even or odd.
enter = int(input('How many times you want to enter a number? '))
while enter > 0:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even number")
    else:
        print(f"{num} is Odd number")
print("Done")

#Create a tuple with seven elements. Unpack the first three elements into individual variables and the remaining
#elements into another tuple. Print all variables.
letters = ('b','c','d','a','e','i','o')
l1, l2, l3, *vowel = letters
print(f"""
{l1}
{l2}
{l3}
{vowel}""")

#Create two sets of numbers. Find and print the union, intersection, and difference of these sets.
a = {'paper', 'pen', 'wallet'}
b = {'bag', 'notebook', 'pen'}
c = a.union(b)
print(c)
print("Both a and b has: ", a.intersection(b))
print("a has: ", a.difference(b))
print("b has: ", b.difference(a))

#Write a program that takes a sentence as input and prints each word in reverse order.
enter = input("Enter a sentence: ").split()
rev = ""
for a in enter:
    reverse = a[::-1]
    rev += reverse + " "
print(rev.strip())

#Create a function that takes a list of numbers and returns a new list with each number squared.
# Use the math library to find the square root of each squared number and print
import math
nums = int(input("How many time do you want to input a number? "))
listnum = []
while nums > 0:
    enter = int(input("Enter a number: "))
    listnum .append(enter)
    nums -=1
for n in listnum:
    print("the square root of ", n, "is: ", math.sqrt(n))

#Write a program that takes a list of words and counts the frequency of each word using a dictionary.
# Print the word frequencies.

enter = input("Enter a repeating words: ").split()
dic = {}
for a in enter:
    #if yung word is nasa dictionary na mag a add nalang
    if a in dic:
        dic[a] += 1
    #if yung word is wala pa sa dictionary ia add sa enter as a key sa dictionary and yung key nya is 1
    else:
        dic[a] = 1
print("word frequencies:")
for txt,num in dic.items():
    print(f"{txt}: {num}")
#output: Word frequencies:
#        hello: 3
#        world: 2

#Write a function called greet that takes a name as an argument and prints "Hello, [name]!"
def greet(name):
    print("Hello, " + name + "!")
greet("dan")

#Write a function called add that takes two numbers as arguments, adds them together, and returns the result.
def add(n1, n2):
    return n1 + n2
print(add(7, 2))

#Write a function called introduce that takes three arguments: first name, middle name, and last name.
# Use keyword arguments to pass the values and print the full name.
def introduce(first_name, middle_name, last_name):
    print("My name is " + first_name + " " + middle_name + ". " + last_name)
introduce(first_name="Dan", middle_name="D", last_name="Coder")

#Write a function called calculate_area that takes the radius of a circle as an argument and returns the area.
#Use the formula πr^2 and import the math library to get the value of π.
import math
def calculate_area(radius):
    return math.pi * (radius ** 2)
print(calculate_area(6))

#Area Calculator: Create a function calculate_area(length, width) that calculates the area of a rectangle and
#returns the result. Call the function with some values for length and width, and then print the area.
def calculateArea(l, w):
    return l * w
print("the area is: ",calculateArea(6, 9))

#Define a function is_even(number) that checks if a given number is even.
# It should return True if the number is even, and False otherwise.
# Use the function to check if several numbers (positive, negative, and zero) are even.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(32))
print(is_even(-98))
print(is_even(0))

#Write a function convert_temperature(celsius, scale) that converts a temperature value from Celsius to another scale
# (Fahrenheit or Kelvin) based on the specified scale argument. The function should return the converted temperature.
# Call the function with different Celsius values and scales, and print the results.

def convert_temperature(enter, con):
    if con == "F":
        Fahrenheit = (enter * 9/5) + 32
        return Fahrenheit
    elif con == "K":
        Kelvin = enter + 273.15
        return Kelvin
    else:
        return "Please enter 'F' for fahrenheit and 'K' for Kelvin"
enter = float(input("Enter temperature in celsius: "))
con = input("Convert to Fahrenheit[F] or Kelvin [K]: ").upper()
temp = convert_temperature(enter, con)
if isinstance(temp, str):
    print(temp)
else:
    print(f"°{enter} to {con} is: °{temp:.2f}{con}")

#Create a function calculate_list_stats(numbers) that takes a list of numbers and calculates the sum, average, minimum,
#and maximum values. The function should return a dictionary containing these statistics.
# Use the function with a sample list of numbers and print the dictionary containing the statistics.
def cal_list_stats(number):
    add = sum(num_list)
    ave = sum(num_list) / len(num_list)
    mini = min(num_list)
    maxi = max(num_list)
    dic = {'Sum': add,
           'Average': ave,
           'Minimum': mini,
           'Maximum': maxi}
    return dic
num_list = [5, 8, 14, 32, -4, 7]
list_stat = cal_list_stats(num_list)
print(list_stat)

#Define a function is_prime(number) that efficiently determines if a number is prime (divisible only by 1 and itself).
#The function should return True if the number is prime, and False otherwise.
#Use the function to check if several numbers (including negative numbers, 1, and large numbers) are prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
print(is_prime(num))

#Develop a function-based guessing game where the computer generates a random number within a specified range.
# he function should take the range and the number of guess attempts allowed as arguments.
#It should guide the user through guessing the number and provide feedback on their attempts.
#If the user guesses correctly within the allowed attempts, print a success message. Otherwise, print the correct answer
import random
def guessing_game(life):

    num_guess = random.randint(1, 100)
    print("Remaining life: ", life)
    while life > 0:
        try:
            guess = int(input("Guess the number: "))
            if guess == num_guess:
                print("You win!")
                return
            elif guess < 1 or guess > 100:
                print("You've passed the limit! Please guess again.")
            elif abs(guess - num_guess) <= 10:
                life -= 1
                if guess > num_guess:
                    print("So close... Lower!")
                else:
                    print("So close... Higher!")
            elif guess > num_guess:
                life -= 1
                print("Too high!")
            elif guess < num_guess:
                life -= 1
                print("Too low!")
            print("Remaining life: ", life)
        except ValueError:
            print("Invalid guess! Please enter a number.")
    return print("You lose! The number is: ", num_guess)
num = 5
guessing_game(num)

#Create a function analyze_text(text) that takes a string as input and returns a dictionary containing information
#about the text. Analyze the number of characters, words, uppercase letters, lowercase letters, digits,
#and punctuation marks. Use the function with a sample text and print the analysis dictionary.
import string
def analyze_text(txt):
    dic = {"Number of characters": len(txt),
           "Number of words": len(txt.split()),
           "Number of uppercase letters": sum(1 for char in txt if char.isupper()),
           "Number of lowercase letters": sum(1 for char in txt if char.islower()),
           "Number of digits": sum(1 for char in txt if char.isdigit()),
           "Number of punctutation marks": sum(1 for char in txt if char in string.punctuation)
    }
    return dic
text = input("Enter a sentece: ")
print(analyze_text(text))

#Word Frequency Counter: Define a function count_word_frequency(text) that analyzes a piece of text
#(provided as a string) and returns a dictionary where keys are unique words and values are the corresponding word
#frequencies. Use the function with a longer text and print the dictionary containing word frequencies
#(sorted by frequency in descending order).
def count_word_frequency(text):
    words = {}
    for word in text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words
enter = input("Enter a sentence: ").split()
for word, count in count_word_frequency(enter).items():
    print(f"{word}: {count}")

#Write a function called calculate_area that takes the radius of a circle as an argument and returns the area.
#Use the formula πr^2 and import the math library to get the value of π.
import math
def calculate_area(area):
    a = math.pi * (area ** 2)
    return a
circle = int(input("Enter a number: "))
print(calculate_area(circle))

#Write a function called format_name that takes first and last names and returns them formatted as "Last, First".
def format_name(first, last):
    return "Hi! I am " + first + " " + last
fn = input("Enter your first name: ")
ln = input("Enter your last name: ")
print(format_name(fn, ln))

#Write a function called max_of_three that takes three numbers and returns the largest one.
#Use nested function calls to achieve this.
def max_of_three(n1, n2, n3):
    return max(max(n1, n2), n3)
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
print("Max: ", max_of_three(num1, num2, num3))

#Write a function called compound_interest that calculates the compound interest.
#The function should take the principal amount, the rate of interest, and the number of years,
#and return the amount after interest. Use the formula: A = P(1 + R/100)^Y
def compound_interest(principal, rate, years):
    amount = principal * (1 + rate/100) ** years
    return amount
p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate: "))
y = int(input("Enter the years of payment: "))
print(compound_interest(p, r, y))

#Write a function called palindrome that takes a string as an argument and returns True if the string is a palindrome,
#and False otherwise. Use nested function calls to remove spaces and convert the string to lowercase before checking.
def palindrome(pal):
    cleaned = pal.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
sentence = input("Enter a sentence: ")
print(palindrome(sentence))

#Write a function called fibonacci that returns the nth Fibonacci number. Use recursion to solve this.
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for f in range(2, n+1):
       a, b = b , a+b
    return b
num = int(input("Input a number to solve it's fibonacci value:  "))
print(fib(num))

#Create a program that asks the user for the radius of a sphere and then calculates and prints the volume and surface
#Area of the sphere using nested function calls.
import math
def volume(radius):
    #FORMULA: (4/3) * π*r^3
    return (4/3) * math.pi * radius**3
def surface(radius):
    return 4 * math.pi * radius**2
def sphere():
    r = float(input("Enter the radius: "))
    v = volume(r)
    a = surface(r)
    return v, a
v, a = sphere()
print(f"""
The volume of the sphere is: {v}
The surface area of the sphere is: {a}""")

#Create two functions. The first function sum_numbers should take a list of numbers and return their sum.
#The second function average should take a list of numbers, call sum_numbers to get the sum, and return the average.
def sum_nums(list):
    sum = 0
    for n in list:
        sum += n
    return sum
def average(list):
    count = len(list)
    add = sum_nums(list)
    ave = add / count
    return ave
def total():
    s = sum_nums(l)
    a = average(l)
    return s, a

l = [1, 2, 3, 4, 5]
s, a = total()
print(f"""
Numbers: {l}
Sum of numbers: {s}
Average of numbers: {a}""")

#Create a function process_string that takes a string and two keyword arguments: case (which can be "upper" or "lower")
#and remove_spaces (a boolean). The function should first convert the string to upper or lower case based on the case
#argument and then remove spaces if remove_spaces is True.
def process_string(word, space, case):
    if space == "y":
        word = word.replace(" ", "")
    if case == "lower":
        return word.lower()
    else:
        return word.upper()

enter = input("Enter 2 word: ")
sp = input("Remove spaces[Y or N]? ").lower()
c = input("Choose [upper] or [lower]: ").lower()
result = process_string(enter, sp, c)
print(result)
#Create a function that checks if two strings are anagrams. An anagram is a word or phrase formed by rearranging the
#letters of a different word or phrase, typically using all the original letters exactly once.
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
string1 = input("Enter the First word: ")
string2 = input("Enter the Second word: ")
anagram = is_anagram(string1, string2)
print(anagram)

#Create a function that checks if a number is an Armstrong number. An Armstrong number (or narcissistic number) for a
#given number of digits is an integer such that the sum of its digits each raised to the power of the number of digits
#is equal to the number itself. Ex: 153 is armstrong number
def is_armstrongnum(num):
    n = len(str(num))
    temp = num
    add = 0
    while temp > 0:
        digit = temp % 10
        add += digit ** n
        temp //= 10
    return add == num
enter = int(input("Enter a  number: "))
print(is_armstrongnum(enter))
'''


