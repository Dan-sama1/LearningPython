started = False
while True:
    user = input('Enter: ').upper()
    if user == "HELP":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif user == "START":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif user == "STOP":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif user == "QUIT":
        break
    else:
        print("I don't understand that")
