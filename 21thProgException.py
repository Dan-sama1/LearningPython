#Exception
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e) #displays exception that occurs
    print("you cannot divide by zero, lmao")
except ValueError as e:
    print(e)
    print("Please enter a number")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("Finished! :)")