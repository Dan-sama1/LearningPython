# Classes and Instance Variables
#Create a Person class with instance variables for name and age.
#Create two instances of the class and print their attributes.
#Add a method to the Person class to print a greeting that includes the person's name.
'''
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_name(self):
        print("Your name is " + self.name)
        return self

    def display_age(self):
        print("You are "+ str(self.age) + " years old")
        return self

    def greet(self):
        print("Hello, " +self.name + "!")
        return self


person1 = Person("Dan", 19)
person2 = Person("Smith", 19)

person1.display_name().display_age().greet()
person2.display_name().display_age().greet()
#Define a Book class with instance variables title and author. Instantiate three books and print their titles.
#Extend the Book class to include a method that prints a summary of the book's details.
class Book:

    def __init__(self,title,author,summary):
        self.title = title
        self.author = author
        self.summary = summary

    def book_title(self):
        print("Book title: " + self.title)
        return self

    def book_author(self):
        print("Author: " + self.author)
        return self

    def book_summary(self):
        print("Summary: " + self.summary)
        return self


book1 = Book("The Perils of Pursuing a Prince by Julia London", "Julia London", "LAMAW READ IT XD")
book2 = Book("Where dreams begin", "Lisa Kleypas", "READ IT PLZ")
book3 = Book("Romeo and Juliet", "William Shakespear", "U KNOW THAT IT'S ABOUT FORBIDDEN LOVE)")

book1.book_title().book_author().book_summary()
book2.book_title().book_author().book_summary()
book3.book_title().book_author().book_summary()


#Write a Dog class with instance variables breed and size. Create two instances and print their sizes.
#Modify the Dog class to include a method that simulates the dog barking by printing "Woof!" followed by the breed of the dog.
class Dog:

    def __init__(self,breed,size,bark):
        self.breed = breed
        self.size = size
        self.bark = bark

    def dog_breed(self):
        print("This dog is a " + self.breed)
        return self

    def dog_size(self):
        print("This dog size is " + str(self.size) + " inches")
        return self

    def dog_bark(self):
        print(str(self.bark) + " " + str(self.breed))
        return self


dog1 = Dog("German Shepherd", 24, "Woof!")
dog2 = Dog("Siberian Husky", 23.5, "Barf!")

dog1.dog_size().dog_bark()
dog2.dog_size().dog_bark()


#Create a BankAccount class with methods for depositing and withdrawing money,
#and an instance variable for the balance. Add error handling for overdrafts.
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Amount: {amount:.2f}")
        else:
            print("Invalid Amount, please try again.")
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Amount.")
            print(f"Current Balance: {self.balance}")
        elif amount <= 0:
            print("Invalid Amount, please try again.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount:.2f}")
        return self

    def display_balance(self):
        print(f"Current Balance: {self.balance}")
        return self

def main():
    print("Enter Account Balance:")
    try:
        bal = float(input(">> "))
        account1 = BankAccount(bal)
        print("[W] - Withdraw")
        print("[D] - Deposit")
        choice = input(">> ").upper()
        if choice == 'D':
            try:
                print("DEPOSIT")
                print("Enter Amount: ")
                amount = float(input(">> "))
                account1.deposit(amount)
            except ValueError as e:
                print(e)
                print("Invalid input, Please try again")
        elif choice == 'W':
            try:
                print("WITHDRAW")
                print("Enter Amount: ")
                amount = float(input(">> "))
                account1.withdraw(amount)
            except ValueError as e:
                print(e)
                print("Invalid input, Please try again")
        else:
            print("Invalid input, Please try again")
        account1.display_balance()
    except ValueError:
        print("Invalid input, Please try again")

if __name__ == "__main__":
    main()


#Write a Student class that tracks a list of courses the student is enrolled in.
#Include methods to add and remove courses.
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Course {course} successfully added.")
        else:
            print(f"Course {course} already exists, please try again.")

    def remove_course(self, course):
        if course not in self.courses:
            print(f"Course {course} not existing, please try again.")
        else:
            self.courses.remove(course)
            print(f"Course {course} removed successfully.")

    def display_courses(self):
        if self.courses:
            print(f"{self.name} is enrolled in the following courses:")
            for course in self.courses:
                print(f"- {course}")
        else:
            print(f"{self.name} is NOT ENROLLED in any courses.")

def main():
    print("Enter student name:")
    student_name = input(">> ")
    student = Student(student_name)
    while True:
        print("[A] - Add Course")
        print("[D] - Remove Course")
        print("[V] - View my Courses")
        print("[X] - EXIT")
        choice = input(">> ").upper()

        if choice == 'A':
            while True:
                print("AVAILABLE COURSES: MATH, SCIENCE, LITERATURE, PROGRAMMING, PHYSICS")
                print("Enter courses [X to EXIT]:")
                course = input(">> ").upper()
                if course == 'X':
                    break
                elif course in ["MATH", "SCIENCE", "LITERATURE", "PROGRAMMING", "PHYSICS"]:
                    student.add_course(course)
                else:
                    print("Invalid input, Please try again.\n")
        elif choice == "D":
            student.display_courses()
            print("\nENTER COURSE THAT YOU WANT TO REMOVE:")
            course = input(">> ").upper()
            student.remove_course(course)
        elif choice == "V":
            student.display_courses()
        elif choice == "X":
            input("Press any key to continue...")
            break
        else:
            print("Invalid input, Please try again.\n")

if __name__ == "__main__":
    main()


#Define a Library class that contains a list of Book objects. Include methods to add and remove books,
#and a method to print all book titles in the library.

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = (title, author)
        if book not in self.books:
            self.books.append(book)
            print(f"Book '{title}' by {author} successfully added.")
        else:
            print(f"Book '{title}' by {author} already exists in the library.")

    def remove_book(self, title, author):
        book = (title, author)
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{title}' by {author} removed successfully.")
        else:
            print(f"Book '{title}' by {author} not found in the library.")

    def display_books(self):
        if self.books:
            print("Books in the Library: ")
            for title, author in self.books:
                print(f"- {title} by {author}")
        else:
            print("The library has no Books.")

def main():
    library = Library()
    while True:
        print("[A] - Add Book")
        print("[D] - Remove Book")
        print("[V] - View Books")
        print("[X] - EXIT")
        choice = input(">> ").upper()

        if choice == 'A':
            title = input("Book title: ")
            author = input("Author: ")
            library.add_book(title, author)

        elif choice == 'D':
            title = input("Book title: ")
            author = input("Author: ")
            library.remove_book(title, author)

        elif choice == 'V':
            library.display_books()

        elif choice == 'X':
            break

        else:
            print("Invalid input, please try again.")

if __name__ == '__main__':
    main()
'''


